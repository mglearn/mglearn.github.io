# Verification

The website has no package dependencies. Browser QA uses external development tools:

```bash
npm install --prefix /tmp/tcea27-qa --no-save --ignore-scripts playwright@1.60.0 axe-core@4.10.3 jsqr@1.4.0
NODE_PATH=/tmp/tcea27-qa/node_modules node tcea27/tests/browser.cjs
```

Install the matching Playwright Chromium browser if needed. Serve the repository root at `http://127.0.0.1:4227` before running. Set `TCEA_BASE_URL` to the deployed `/tcea27/` URL for live verification. Results go to `/tmp/tcea27-qa-results` by default; `TCEA_QA_OUTPUT` can change that folder.

The suite covers 26 public and protected pages, axe WCAG 2 A/AA and 2.1/2.2 AA rules, 390px and 320px reflow, keyboard radio selection, mobile navigation, hidden answer keys, reset and retrieval restart, actual clipboard copying, reflection privacy and clearing, discussion timer, presenter timing/navigation, resource filters, QR decoding, print output, no-JavaScript reading and screenshots. Automated accessibility results are not a full WCAG certification.

`python3 tcea27/scripts/verify.py` checks internal references, fragments, unique IDs, required metadata, agenda duration, source provenance, selectable PDF text and ZIP integrity. PDF verification requires `pypdf`. Build PDFs with `reportlab`; neither library is used by the published site.

Additional release checks: extract the ZIP and open `index.html` under `file://` with networking disabled; use all core controls; inspect printed activity/presenter PDF text; test a draft and published second workshop in an isolated copy; review desktop/mobile screenshots and primary research/TEKS references.

Presenter checks require `TCEA_PASSWORD_FILE` pointing to the private password file outside the repository. Run `tests/presenter.cjs` with the same NODE_PATH setup to check encryption, wrong-password behavior, reload locking, slide geometry and timing, two-window synchronization, speaker-notes resizing, PDF output, and mobile reflow. Do not publish decrypted screenshots or slide PDFs with speaker notes.

Set `TCEA_DECK_URL=https://mguhlin.github.io/webdecks/tcea27/math-tools.html` when running `presenter.cjs` to exercise the mirrored library deck with the same gate, notes, presenter-window and print checks.

The current release has two workshops, twenty slides and fifty minutes per protected deck, nine PDF/HTML resources, and a manual image carousel. Set `TCEA_SESSION_SLUG=project-management` for that deck’s presenter checks. `sessions.cjs` verifies carousel controls, session-specific math content, Project Management case interactions, actual plan clipboard/print/clear/privacy, and filtering. General browser checks cover 26 pages; the static verifier checks all 27 HTML pages and the unchanged approved hero.

Run `tests/remember-access.cjs` with TCEA_PASSWORD_FILE for persistent-browser access tests. Standard presenter tests uncheck Remember access to verify temporary reload locking. The persistence suite checks thirty-day cookies, browser restart, cross-workshop unlocking, non-exportable CryptoKeys, expiration, and forgetting.
