# TCEA27 project instructions

Preserve the **TCEA27 Learning Adventure** design for future workshops. Read `design-system/README.md` and `design-system/theme.json`; compare `design-system/reference-desktop.webp` and `reference-mobile.webp` when making visual changes. The shared `assets/css/styles.css` is the implementation source of truth. Reuse the illustrated banner, warm paper, rust/teal/gold treatment, serif hero, rounded cards, shared page shell, and responsive behavior. Do not invent a separate visual identity for another session unless the user requests it.

Manage workshop records in `data/sessions.json`; only published sessions appear in home cards. Use `scripts/create-session.py <session-id>` for a new draft landing page. Add completed content and verify it before marking the session published. Keep links relative under `/tcea27/` and link only to completed resources.

Presenter guides and webdecks are encrypted. Private notes, plaintext presenter HTML, and passwords stay outside every public repository. Use `scripts/seal-presenter.cjs`, then rebuild the protected offline packet. Do not reintroduce private fields to public data or publish decrypted screenshots/PDFs containing notes.

Run `python3 tcea27/scripts/build-downloads.py` from the repository root, `scripts/verify.py`, and appropriate browser tests before publication. Web decks must follow the canonical Web Deck v5 specification; keep project copies of its framework and use local theme overrides. Preserve existing published resources and unrelated repository files.

The user's standing instruction authorizes commit, push, deploy, and live verification without routine confirmation.
