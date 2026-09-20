"""Check the built static site before publishing it to GitHub Pages."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dist'
BASE = 'https://hongruzhao.github.io/'


class Document(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.ids = []
        self.links = []
        self.redirect = None
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.append(a['id'])
        if a.get('href'):
            self.links.append(a['href'])
        if a.get('src'):
            self.links.append(a['src'])
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh':
            self.redirect = a.get('content', '').split('url=', 1)[-1]
            self.links.append(self.redirect)


documents = {p: Document(p.read_text()) for p in OUT.rglob('*.html')}
errors = []
checked = 0
for path, doc in documents.items():
    duplicates = [i for i, count in Counter(doc.ids).items() if count > 1]
    if duplicates:
        errors.append(f'{path.relative_to(OUT)}: duplicate IDs {duplicates}')
    relative = path.relative_to(OUT).as_posix()
    current = urljoin(BASE, relative[:-10] if relative.endswith('index.html') else relative)
    for link in doc.links:
        parsed = urlsplit(urljoin(current, link))
        if parsed.scheme not in ('http', 'https') or parsed.hostname != 'hongruzhao.github.io':
            continue
        target = OUT / unquote(parsed.path).lstrip('/')
        if target.is_dir():
            target /= 'index.html'
        checked += 1
        if not target.is_file():
            errors.append(f'{relative}: missing target {link}')
        elif parsed.fragment and target in documents:
            fragment = unquote(parsed.fragment)
            if fragment not in documents[target].ids and not fragment.startswith(':~:text='):
                errors.append(f'{relative}: missing anchor {link}')

for old, target in json.loads((ROOT / 'content/legacy_redirects.json').read_text()).items():
    path = OUT / old.lstrip('/')
    if not old.endswith('.html'):
        path /= 'index.html'
    if not path.is_file() or Document(path.read_text()).redirect != target:
        errors.append(f'Missing or incorrect legacy redirect: {old}')

expected_posts = {p.stem for p in (ROOT / 'content/posts').glob('*.md')}
actual_posts = {p.parent.name for p in (OUT / 'blog').glob('*/index.html')}
if not expected_posts.issubset(actual_posts):
    # Unpublished future drafts are allowed; current explicitly public posts are not.
    import yaml
    for slug in expected_posts - actual_posts:
        raw = (ROOT / f'content/posts/{slug}.md').read_text()
        meta = yaml.safe_load(raw.split('---', 2)[1])
        if not meta.get('draft', False) or meta.get('publish', False):
            errors.append(f'Published post missing: {slug}')

for name in ['404.html', 'robots.txt', 'sitemap.xml', '.nojekyll']:
    if not (OUT / name).is_file():
        errors.append(f'Missing publishing file: {name}')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(documents)} HTML pages, {checked} internal references, '
      f'{len(actual_posts)} blog posts, and all legacy redirects.')
