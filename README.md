# Hongru Zhao’s personal website

The public website is **https://hongruzhao.github.io/**. It includes research by topic, publications, teaching, talks, a CV, and five research blog posts.

## Edit the website

- Update publications, research categories, courses, and talks in `content/site.json`.
- Set a paper's `hidden` field to `true` to temporarily remove it from the website while preserving its details for restoration.
- Update the homepage introduction and CV summary in `build.py`.
- Edit a blog post in `content/posts/`. Keep its filename to preserve its web address, and update its `updated` date when making a substantive revision.
- Upload images and the current CV PDF to `dist/assets/`.
- Keep the existing `files/` and `images/` directories: these preserve previously published paper, slide, CV, and image links.

Committing to `main` rebuilds, checks, and publishes the website through GitHub Actions.

## Blog publication

Start a new post from `content/templates/post.md`. The `sequence` field sets the reading order; the homepage and blog index show the highest sequence first.

- `draft: true` keeps a new draft out of the public build.
- `draft: false` publishes a finished post.
- `draft: true` together with `publish: true` publishes an evolving draft while retaining its visible draft label. The four evolving posts imported with the redesign use this explicit setting.

All five posts present in the September 20, 2026 redesign are included in the public build. Future drafts remain unpublished unless explicitly enabled.

## Build and check locally

```sh
python -m pip install -r requirements.txt
python build.py
python verify_site.py
python -m http.server --directory dist 8000
```

The site is generated into `dist/`. Generated pages are not committed; the saved assets under `dist/assets/` are committed. `math_markdown.py` preserves LaTeX for MathJax. The optional figure-generation dependencies are in `requirements-figures.txt` and are not needed for ordinary builds.

`verify_site.py` checks internal links, local assets, anchor targets, duplicate HTML IDs, redirects, and publication of the five current posts. The deployment workflow runs the same checks before publishing.

## Address continuity and recovery

`content/legacy_redirects.json` maps old research, publication, talk, and teaching addresses to the new site. The original document and image files remain available at their existing paths. The builder also creates a sitemap, robots.txt, and a custom 404 page.

The pre-redesign main revision was `1f10d14e393688db8e3d08af5dd6b51d7d65ae7e`. A complete source ZIP and verified Git history bundle were downloaded before replacement. The redesign is a normal commit, so the earlier site remains recoverable from repository history.

The retained `LICENSE` records the license of the previous Academic Pages / Minimal Mistakes material, including preserved legacy assets.
