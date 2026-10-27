# Verification

The website has no package dependencies. Browser QA uses external development tools:

```bash
npm install --prefix /tmp/tcea27-qa --no-save --ignore-scripts playwright@1.60.0 axe-core@4.10.3 jsqr@1.4.0
NODE_PATH=/tmp/tcea27-qa/node_modules node tcea27/tests/browser.cjs
```

Install the matching Playwright Chromium browser if needed. Serve the repository root at `http://127.0.0.1:4227` before running. Set `TCEA_BASE_URL` to the deployed `/tcea27/` URL for live verification. Results go to `/tmp/tcea27-qa-results` by default; `TCEA_QA_OUTPUT` can change that folder.

The suite covers all 17 pages, axe WCAG 2 A/AA and 2.1/2.2 AA rules, 390px and 320px reflow, keyboard radio selection, mobile navigation, hidden answer keys, reset and retrieval restart, actual clipboard copying, reflection privacy and clearing, discussion timer, presenter timing/navigation, resource filters, QR decoding, print output, no-JavaScript reading and screenshots. Automated accessibility results are not a full WCAG certification.

`python3 tcea27/scripts/verify.py` checks internal references, fragments, unique IDs, required metadata, agenda duration, source provenance, selectable PDF text and ZIP integrity. PDF verification requires `pypdf`. Build PDFs with `reportlab`; neither library is used by the published site.

Additional release checks: extract the ZIP and open `index.html` under `file://` with networking disabled; use all core controls; inspect printed activity/presenter PDF text; test a draft and published second workshop in an isolated copy; review desktop/mobile screenshots and primary research/TEKS references.
