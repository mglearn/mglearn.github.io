# TCEA 2027 · MG Learn conference companion

Published at https://mglearn.github.io/tcea27/ from `mglearn/mglearn.github.io`, main branch root. The first workshop is **High-Impact Teaching Math Tools Without the Price Tag**. Its stable path remains `sessions/math-without-price-tag/`.

## Maintain the site

Canonical session, resource, strategy, experience, download and lesson records live in `data/*.json`. Static pages are generated so navigation and explanations also work without JavaScript. `site-data.js` is a generated local snapshot, allowing extracted `file://` use without fetch or a web server. No frameworks, runtime packages, trackers, cookies, browser persistence or external fonts are used.

- Edit JSON, `assets/css/`, `assets/js/`, or the page compositions in `scripts/build.py`.
- Run `python3 tcea27/scripts/build-downloads.py` from the repository root (requires Python ReportLab only for PDF authoring). It regenerates static pages, PDFs, HTML companions, datasets, QR code, and the offline ZIP.
- Run `python3 tcea27/scripts/verify.py` to check paths, data, downloads, and research provenance. Browser checks live in `tests/`; see `tests/README.md`.
- Serve the repository root with `python3 -m http.server 4227`; visit `/tcea27/`.
- Review changes, commit and push main; verify GitHub Pages and the live site.

## Add a workshop

1. Add a unique `id` and `slug` in `data/sessions.json`, initially with `status: "draft"`. Follow the existing record's fields, including audience, presenters, learning objectives, tool/strategy IDs, activities, resources, and completed downloads.
2. Create `sessions/<slug>/index.html` and any workshop-specific activities and presenter materials. Keep references relative to `/tcea27/`. Use shared styles and components. The first session's build functions illustrate the structure; avoid copying private facilitation notes.
3. Add resource and strategy records and their related session IDs. Research values must be verified from a primary source, with date and interpretation notes; use null for values that cannot be verified. The card component supports missing values without inventing a number.
4. Create and check every linked download. Keep incomplete sessions out of navigation by leaving them draft.
5. Mark the session published, run the build and checks, then commit/push. The home card grid grows from the published session records without a layout redesign. The first math session has a dedicated illustrated card; future subjects can customize its visual treatment in `session_card`.

## Evidence and availability

Seven MetaX influence records were reviewed October 27, 2026, version 1.4 (February 2026). The reported statistic is **Weighted mean effect size**, which can differ from the record's meta-analysis table average. Corrective feedback maps to the broader Feedback influence. Retrieval practice maps to Practice testing. These values describe research on strategies, not these tools. The `strategies.json` records include URLs, domains, definitions, examples and limitations.

TEKS correlations are paraphrased from TEA's current Chapter 111 elementary, middle-school and high-school PDFs (links in `lessons.json`). Kindergarten joining/separating, Grade 3 categorical graphs, Grade 6 distributions and Algebra I data relationships were checked. This does not certify a complete curriculum alignment. Digital Math Tools' five grade-band collections and the GraphSplat/Quiz tool pages were verified as published.

The public presenter guide contains only nonconfidential facilitation notes. Attendee answer explanations start collapsed. Timers are optional, text-only and do not flash or play sound. No leaderboard or learning-gain claim is made.

## Offline and accessible formats

Download/extract the packet and open `tcea27/index.html`. Local graphs, native explanation disclosures, interactions, reflection copying (with fallback), presenter controls and PDFs work without internet. External tools/research need connectivity. Print styles expose answer keys and all presenter segments. The five PDFs have selectable text and complete semantic HTML alternatives; they are not claimed to be tagged PDF/UA. Reflections remain in memory, clearing on reload; copy or print to preserve them.

Original teaching materials may be reused and adapted with attribution to Miguel Guhlin / MG Learn. Third-party research, standards and linked resources retain their respective rights. The visual design draws inspiration from the convention site's hierarchy and the requested navy/blue/gold palette; it includes original graphics and no copied TCEA artwork or logo.
