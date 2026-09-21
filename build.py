"""Build a portable static website from site.json and Markdown posts."""
from pathlib import Path
from datetime import date
import argparse, html, json, re, shutil
import markdown, yaml
from math_markdown import MathJaxExtension

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dist'
DATA = json.loads((ROOT / 'content/site.json').read_text())
VISIBLE_PAPERS = [p for p in DATA['papers'] if not p.get('hidden', False)]
TOPIC_LABELS = DATA.get('topic_labels', {})
E = html.escape
SITE_URL = 'https://hongruzhao.github.io'
page_routes = []
args = argparse.ArgumentParser()
args.add_argument('--include-drafts', action='store_true')
preview = args.parse_args().include_drafts
# Preserve the original site's public documents and images when migrating to GitHub Pages.
for legacy_name in ('files', 'images'):
    legacy_path = ROOT / legacy_name
    if legacy_path.is_dir():
        shutil.copytree(legacy_path, OUT / legacy_name, dirs_exist_ok=True)
# Remove generated article pages so previously previewed drafts cannot survive a public build.
for old_article in (OUT / 'blog').glob('*/index.html'):
    old_article.unlink()

def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def load_posts():
    posts = []
    for path in sorted((ROOT / 'content/posts').glob('*.md'), reverse=True):
        raw = path.read_text()
        _, front, body = raw.split('---', 2)
        p = yaml.safe_load(front)
        if p.get('draft', False) and not (preview or p.get('publish', False)):
            continue
        p['slug'] = path.stem
        p['body'] = markdown.markdown(body, extensions=['fenced_code', 'tables', 'toc', 'sane_lists', MathJaxExtension()])
        p['date'] = date.fromisoformat(str(p['date'])).isoformat()
        if p.get('updated'):
            p['updated'] = date.fromisoformat(str(p['updated'])).isoformat()
            if p['updated'] < p['date']:
                raise ValueError(f'{path.name}: updated must not precede date')
        p['minutes'] = max(1, round(len(body.split()) / 220))
        posts.append(p)
    return sorted(posts, key=lambda p:(p.get('sequence', 9999), -date.fromisoformat(p['date']).toordinal()))

POSTS = load_posts()
NAV = [('Home',''), ('Teaching','teaching/'), ('Talks','talks/'), ('CV','cv/'), ('Blog','blog/')]

def post_time(value):
    day = date.fromisoformat(value)
    label = f'{day:%B} {day.day}, {day.year}'
    return f'<time datetime="{value}">{label}</time>'

def page(title, route, content, description='', classes='', filename=None):
    prefix = '/' if filename else ('../' * len([x for x in route.split('/') if x]) or './')
    def link(label, path):
        current = (path == route) or (path == 'blog/' and route.startswith('blog/'))
        return f'<a href="{prefix}{path}"'+(' aria-current="page"' if current else '')+f'>{label}</a>'
    research_active = route.startswith('research/')
    menu = link(*NAV[0])
    menu += f'''<details class="nav-dropdown"><summary{' class="is-current"' if research_active else ''}>Research</summary><div class="dropdown-panel research-menu">{link('Publications','research/publications/')}{link('Research by Topic','research/topics/')}</div></details>'''
    menu += ''.join(link(*n) for n in NAV[1:])
    mobile_menu = link(*NAV[0])
    mobile_menu += f'<div class="mobile-research"><span class="mobile-group-label">Research</span>{link("Publications", "research/publications/")}{link("Research by Topic", "research/topics/")}</div>'
    mobile_menu += ''.join(link(*n) for n in NAV[1:])
    title_text = f'{title} · Hongru Zhao' if title != 'Home' else 'Hongru Zhao · Statistics and Quantum Information Science'
    body = f'''<!doctype html>
<html lang="en" data-background="{E(DATA['background'])}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title_text)}</title><meta name="description" content="{E(description or 'Hongru Zhao. Research in statistics, quantum information science, and foundations of machine learning.')}">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23245da8'/%3E%3Ctext x='32' y='42' text-anchor='middle' font-family='Georgia' font-size='30' fill='white'%3EHZ%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="{prefix}assets/style.css"><script src="{prefix}assets/appearance.js"></script>
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}}}};</script><script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js"></script>
</head><body><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="nav-wrap"><a class="wordmark" href="{prefix}">Hongru <strong>Zhao</strong></a><nav class="desktop-navigation" aria-label="Main navigation">{menu}</nav>
<details class="mobile-navigation nav-dropdown"><summary aria-label="Navigation menu"><span aria-hidden="true">⋯</span></summary><nav class="dropdown-panel mobile-menu" aria-label="Mobile navigation">{mobile_menu}</nav></details>
<details class="appearance nav-dropdown"><summary aria-label="Appearance settings"><span aria-hidden="true">◐</span><span class="appearance-label">Appearance</span></summary><div class="dropdown-panel appearance-panel"><div class="control-label">Appearance</div><div class="mode-buttons"><button data-mode="light" type="button">Light</button><button data-mode="dark" type="button">Dark</button><button data-mode="system" type="button">Auto</button></div><label for="background-select">Background</label><select id="background-select"><option value="plain">Plain</option><option value="mist">Soft gradient</option><option value="grid">Graph paper</option><option value="ink">Ink gradient</option></select></div></details></div></header>
<main id="main" class="site-main {classes}">{content}</main>
<footer class="site-footer"><span>© {date.today().year} Hongru Zhao</span><span>Statistics · University of Minnesota</span><a href="mailto:{DATA['email']}">Email</a></footer>
<script src="{prefix}assets/site.js" defer></script></body></html>'''
    dest = OUT / filename if filename else OUT / route / 'index.html'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(body)
    if not filename:
        page_routes.append(route)

def cards(prefix, limit=None, heading_level=3, reverse=False):
    if not POSTS:
        return '<p class="empty-state">Research notes and new posts will appear here.</p>'
    selected = (list(reversed(POSTS)) if reverse else POSTS)[:limit]
    grid_class = 'post-grid post-grid-four' if len(selected) == 4 else 'post-grid'
    result = f'<div class="{grid_class}">'
    for p in selected:
        status = E(p.get('draft_label', 'Draft preview')) if p.get('draft') else post_time(p['date'])
        updated = f'<span>Updated {post_time(p["updated"])}</span>' if p.get('updated') else ''
        number = f'Post {p["sequence"]:02d} · ' if p.get('sequence') else ''
        cover = f'<a class="post-image" href="{prefix}blog/{p["slug"]}/"><img src="{prefix}{E(p["image"])}" width="{p.get("image_width",960)}" height="{p.get("image_height",600)}" alt="{E(p["image_alt"])}" loading="lazy"></a>' if p.get('image') else ''
        text_class = '' if cover else ' post-card-text'
        reading = '' if p.get('awaiting_text') else f'<span>{p["minutes"]} min read</span>'
        result += f'''<article class="post-card{text_class}">{cover}<div class="post-copy"><div class="post-category">{number}{E(p['category'])}</div><h{heading_level}><a href="{prefix}blog/{p['slug']}/">{E(p['title'])}</a></h{heading_level}><p>{E(p['description'])}</p><div class="post-meta"><span>{status}</span>{reading}{updated}</div></div></article>'''
    return result + '</div>'

gbs_post = next((p for p in POSTS if p['slug'] == '2026-09-12-gaussian-boson-sampling'), None)
gbs_news = f'''<div class="news-row"><time datetime="2026-09-12">Sep 12, 2026</time><p>My recent work on uniform hiding and local hafnian anticoncentration represents a significant breakthrough toward establishing quantum advantage in Gaussian boson sampling. <a href="./blog/{gbs_post['slug']}/">Read the explanation</a>.</p></div>''' if gbs_post else ''

about = f'''<section class="about-top"><div class="about-copy"><header class="about-heading"><h1>Hongru Zhao</h1><p class="role">IRSA Faragher Distinguished Postdoctoral Fellow</p><p class="affiliation">School of Statistics, University of Minnesota–Twin Cities</p></header><section class="about-bio" aria-labelledby="about-me"><h2 id="about-me">About Me</h2><p>I am a postdoctoral fellow in the <a href="https://cla.umn.edu/statistics">School of Statistics</a> at the University of Minnesota–Twin Cities (2025–2027). I received my Ph.D. in Statistics from the University of Minnesota in 2025, advised by <a href="https://users.stat.umn.edu/~arothman/">Adam J. Rothman</a>. My research spans three connected areas:</p><p><strong>Statistics for science.</strong> My current research focuses on <a href="https://hongruzhao.github.io/research/topics/#quantum-information-science">quantum information science</a>, particularly <a href="https://hongruzhao.github.io/research/topics/#quantum-tomography">quantum state estimation</a> and the foundations of <a href="https://hongruzhao.github.io/research/topics/#gaussian-boson-sampling">quantum computational advantage</a>. I also work on <a href="https://hongruzhao.github.io/research/topics/#astrostatistics">astrostatistics</a>, including modeling and inference for the stochastic gravitational-wave background.</p><p><strong>Foundations of AI.</strong> I study the <a href="https://hongruzhao.github.io/research/topics/#generative-ai-and-reinforcement-learning">theoretical foundations of machine learning</a>, including training dynamics and generative modeling with human feedback.</p><p><strong>Statistical theory and methods.</strong> My research spans <a href="https://hongruzhao.github.io/research/topics/#high-dimensional-statistics">high-dimensional statistics</a>, <a href="https://hongruzhao.github.io/research/topics/#statistical-inference-and-experimental-design">adaptive experimental design</a>, and <a href="https://hongruzhao.github.io/research/topics/#random-matrix-theory">random matrix theory</a>.</p></section></div><aside class="profile"><img src="./assets/profile.png" alt="Hongru Zhao" width="634" height="788"><div class="profile-caption"><strong>School of Statistics</strong><span>University of Minnesota–Twin Cities</span><span>355 Ford Hall · Minneapolis, MN</span><a href="mailto:{DATA['email']}">{DATA['email']}</a><a href="https://scholar.google.com/citations?user=Gu0Z3BkAAAAJ">Google Scholar</a></div></aside></section>
<section class="news-section"><div class="section-heading"><h2>News</h2><a href="./talks/">All Talks <span aria-hidden="true">↗</span></a></div>{gbs_news}<div class="news-row"><time datetime="2026-07-13">Jul 13, 2026</time><p>Invited talk on gravitational-wave inference at Sun Yat-sen University. <a href="https://hongruzhao.github.io/files/SGWB.pdf">Slides</a></p></div><div class="news-row"><time datetime="2026-07-09">Jul 09, 2026</time><p>Invited talk on adaptive design for quantum state tomography at Tianjin University. <a href="https://hongruzhao.github.io/files/quantum_tomography_Tianjin.pdf">Slides</a></p></div><div class="news-row"><time datetime="2025">2025</time><p>Began the IRSA Faragher Distinguished Postdoctoral Fellowship at the University of Minnesota.</p></div></section>
<section class="latest-section"><div class="section-heading"><h2>Latest Posts</h2><a href="./blog/">All Posts <span aria-hidden="true">↗</span></a></div>{cards('./',4,reverse=True)}</section>'''
page('Home','',about,classes='about-page')
page('Blog','blog/',f'<div class="page-heading"><h1>Blog</h1><p>Research notes, visual explanations, and ideas in progress.</p></div>{cards("../", heading_level=2, reverse=True)}',classes='blog-page')

def paper_item(p, heading_level=3):
    authors = E(p['authors']).replace('Hongru Zhao','<span class="author-me">Hongru Zhao</span>')
    title = E(p['title'])
    paperlink = f'<a class="paper-link" href="{E(p["url"])}">{E(p.get("link_label", "Paper"))} <span aria-hidden="true">↗</span></a>' if p['url'] else ''
    leanlink = f'<a class="paper-link lean-link" href="{E(p["lean_url"])}" title="{E(p.get("lean_scope", "Lean proof repository"))}">Lean verified <span aria-hidden="true">↗</span></a>' if p.get('lean_url') else ''
    links = f'<div class="publication-links">{paperlink}{leanlink}</div>' if paperlink or leanlink else ''
    tags = []
    for tag_id in p['tags']:
        tag = DATA['paper_tag_definitions'][tag_id]
        tags.append(f'<span class="paper-tag" data-tag-kind="{E(tag["kind"])}" data-topic-color="{E(tag["color"])}">{E(tag["label"])}</span>')
    metadata = f'<div class="publication-details"><span class="publication-venue">{E(p["venue"])} · {p["year"]}</span>{"".join(tags)}</div>'
    return f'<article class="publication" id="{p["id"]}"><h{heading_level}>{title}</h{heading_level}><p class="authors">{authors}</p><div class="publication-meta">{metadata}{links}</div></article>'

pubs='<div class="page-heading"><h1>Publications</h1><p><a href="../topics/">Explore Research by Topic</a></p></div>'
published = sorted(
    [p for p in VISIBLE_PAPERS if not p['preprint']
     and (p.get('include_in_publications', False)
          or not re.search(r'\b(forthcoming|accepted|in press|preprint)\b', p['venue'], re.I))],
    key=lambda p: p['year'], reverse=True)
for year in sorted({p['year'] for p in published}, reverse=True):
    pubs += f'<section class="publication-section" aria-labelledby="publications-{year}"><h2 id="publications-{year}">{year}</h2>'
    pubs += ''.join(paper_item(p) for p in published if p['year'] == year) + '</section>'
page('Publications','research/publications/',pubs,classes='research-page')
research_areas = [
    ('statistics-and-foundations-of-machine-learning',
     'Statistics and Foundations of Machine Learning',
     [t for t in DATA['topics'] if t not in ['Quantum Information Science', 'Astrostatistics', 'Other applications']]),
    ('statistics-for-science', 'Statistics for Science', ['Quantum Information Science', 'Astrostatistics', 'Other applications'])
]
topics = '<div class="page-heading"><h1>Research by Topic</h1></div>'
topics += '<nav class="research-areas" aria-label="Research areas">'
for area_id, label, area_topics in research_areas:
    topics += f'<a class="research-area-choice" id="choose-{area_id}" href="#{area_id}" data-research-area="{area_id}"><span>{E(label)}</span></a>'
topics += '</nav>'
for area_id, label, area_topics in research_areas:
    topics += f'<section class="research-area-panel" id="{area_id}" aria-labelledby="choose-{area_id}">'
    if len(area_topics) > 1:
        topics += '<nav class="topic-jump" aria-label="Topics in this research area">' + ''.join(f'<a href="#{slug(t)}" data-topic-color="{E(DATA["topic_colors"][t])}">{E(TOPIC_LABELS.get(t, t))}</a>' for t in area_topics) + '</nav>'
    for topic in area_topics:
        papers = [p for p in VISIBLE_PAPERS if topic in p['topics']
                  and (area_id == 'statistics-for-science' or 'Quantum Information Science' not in p['topics'])]
        aliases = ''.join(f'<span class="topic-alias" id="{E(anchor)}" aria-hidden="true"></span>' for anchor in DATA.get('topic_aliases', {}).get(topic, []))
        topics += f'<section class="topic-section" id="{slug(topic)}" data-topic-color="{E(DATA["topic_colors"][topic])}">{aliases}<h2>{E(TOPIC_LABELS.get(topic, topic))}</h2>'
        if topic == 'Quantum Information Science':
            groups = DATA['quantum_subgroups']
            topics += '<nav class="topic-jump quantum-jump" aria-label="Quantum research subgroups">' + ''.join(f'<a href="#{g["id"]}" data-topic-color="{E(g["color"])}">{E(g["title"])}</a>' for g in groups) + '</nav>'
            for group in groups:
                topics += f'<section class="quantum-subgroup" id="{group["id"]}" data-topic-color="{E(group["color"])}"><h3>{E(group["title"])}</h3>'
                group_content = ''.join(paper_item(p, 4) for p in papers if p['id'] in group['paper_ids'])
                topics += (group_content or '<p>Coming soon.</p>') + '</section>'
        else:
            topics += ''.join(paper_item(p) for p in papers)
        topics += '</section>'
    topics += '</section>'
page('Research by Topic','research/topics/',topics,classes='research-page')

teaching='<div class="page-heading"><h1>Teaching</h1><p>School of Statistics, University of Minnesota–Twin Cities</p></div><div class="course-list">'
previous_role = None
for c in DATA['teaching']:
    if c['role'] != previous_role:
        teaching += f'<h2 class="teaching-role">{E(c["role"])}</h2>'
        previous_role = c['role']
    code,name=c['course'].split(':',1)
    teaching+=f'<article class="course-row"><p class="course-term">{E(c["term"])}</p><div><span class="course-code">{E(code)}</span><h3>{E(name.strip())}</h3></div></article>'
page('Teaching','teaching/',teaching+'</div>')
talks='<div class="page-heading"><h1>Talks</h1></div>'
for t in DATA['talks']:
    slides=f'<a class="paper-link" href="{E(t["url"])}">Slides ↗</a>' if t['url'] else ''
    talks+=f'<article class="talk-row"><p class="talk-date">{E(t["date"])}</p><h2>{E(t["title"])}</h2><p>{E(t["place"])}</p>{slides}</article>'
page('Talks','talks/',talks)
cv='''<div class="page-heading"><h1>Curriculum Vitae</h1><p><a class="solid-link" href="../assets/cv.pdf">Open CV (PDF) ↗</a><span class="cv-date">Updated September 2026</span></p></div><section class="cv-section"><h2>Academic Appointment</h2><div class="cv-row"><span>2025–2027</span><div><h3>IRSA Faragher Distinguished Postdoctoral Fellow</h3><p>School of Statistics, University of Minnesota–Twin Cities</p></div></div></section><section class="cv-section"><h2>Education</h2><div class="cv-row"><span>2025</span><div><h3>Ph.D. in Statistics</h3><p>University of Minnesota · Adviser: Adam J. Rothman</p></div></div><div class="cv-row"><span>2020</span><div><h3>M.S. in Mathematical Sciences</h3><p>University of Minnesota</p></div></div><div class="cv-row"><span>2018</span><div><h3>B.S. in Statistics</h3><p>Jilin University, China</p></div></div></section><section class="cv-section"><h2>Research and Teaching</h2><p><a href="../research/publications/">Publications</a> · <a href="../teaching/">Courses taught</a> · <a href="../talks/">Talks and presentations</a></p></section>'''
cv += '<section class="cv-section"><h2>Mentoring</h2><div class="cv-row"><span>2025–2026</span><div><h3>Huiqian Feng</h3><p>Undergraduate research mentee in high-dimensional statistics, University of Minnesota.</p></div></div></section>'
cv += '<section class="cv-section"><h2>Professional Service</h2><h3>Departmental Service and Outreach</h3><p>Seminar Coordinator, UMN School of Statistics Seminar Series (Fall 2025). IRSA sponsor representative at the WiADS Conference.</p><h3>Reviewer Service</h3><p>Journal of Machine Learning Research (2026); Journal of the American Statistical Association (2026); IEEE Transactions on Information Theory (2025); Electronic Journal of Statistics (2025); Annals of Applied Probability (2022); Transactions on Machine Learning Research (2024–2025).</p></section>'
page('CV','cv/',cv)
for post_index, p in enumerate(POSTS):
    status = E(p.get('draft_label', 'Draft preview')) + ' · ' if p.get('draft') else ''
    number = f'Post {p["sequence"]:02d} · ' if p.get('sequence') else ''
    reading = '' if p.get('awaiting_text') else f' · {p["minutes"]} min read'
    date_label = 'Started' if p.get('draft') else 'Published'
    dates = f'<span>{date_label} {post_time(p["date"])}</span>'
    if p.get('updated'):
        dates += f'<span>Last updated {post_time(p["updated"])}</span>'
    evolving = '<p class="article-update-note">This is an evolving article. I will add explanations, examples, and research updates here over time.</p>' if p.get('living') else ''
    cover = f'<figure class="article-cover"><a href="../../{E(p["image"])}"><img src="../../{E(p["image"])}" alt="{E(p["image_alt"])}" width="{p.get("image_width",960)}" height="{p.get("image_height",600)}"></a><figcaption>{E(p["caption"])}</figcaption></figure>' if p.get('image') else ''
    neighbors = []
    for offset, label in [(-1, 'Previous post'), (1, 'Next post')]:
        index = post_index + offset
        if 0 <= index < len(POSTS):
            neighbor = POSTS[index]
            direction = 'previous' if offset < 0 else 'next'
            neighbors.append(f'<a class="post-{direction}" href="../{neighbor["slug"]}/"><span>{label}</span>{E(neighbor["title"])}</a>')
    pagination = '<nav class="post-pagination" aria-label="Post navigation">' + ''.join(neighbors) + '</nav>' if neighbors else ''
    article=f'''<a class="back-link" href="../">← All Posts</a><header class="article-header"><p class="eyebrow">{number}{E(p['category'])}</p><h1>{E(p['title'])}</h1><p class="article-description">{E(p['description'])}</p><div class="post-meta">{status}{E(p.get('author', 'Hongru Zhao'))}{reading}</div><div class="post-meta article-dates">{dates}</div>{evolving}</header>{cover}<div class="article-body">{p['body']}</div>{pagination}'''
    page(p['title'],'blog/'+p['slug']+'/',article,p['description'],'article-page')
# Retain published entry points while the new layout becomes the main website.
for old, new in json.loads((ROOT / 'content/legacy_redirects.json').read_text()).items():
    old_path = old.lstrip('/')
    dest = OUT / old_path if old_path.endswith('.html') else OUT / old_path / 'index.html'
    dest.parent.mkdir(parents=True, exist_ok=True)
    title = 'Continue to Hongru Zhao’s website'
    dest.write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="refresh" content="0; url={E(new)}"><link rel="canonical" href="{SITE_URL}{E(new)}"><title>{title}</title></head><body><p><a href="{E(new)}">{title}</a></p></body></html>')
page('Page not found', '404/', '<div class="page-heading"><h1>Page not found</h1><p>This address may have changed. Visit the <a href="/">homepage</a>, browse <a href="/research/topics/">research by topic</a>, or read the <a href="/blog/">blog</a>.</p></div>', filename='404.html')
(OUT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE_URL}/{E(route)}</loc></url>\n' for route in page_routes) + '</urlset>\n')
(OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n')
(OUT/'.nojekyll').write_text('')
print(f'Built {len(list(OUT.rglob("index.html")))} pages; {len(POSTS)} posts; include_drafts={preview}')
