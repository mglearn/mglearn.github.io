# TCEA27 project instructions

Preserve the **TCEA27 Learning Adventure** design for future workshops. Read `design-system/README.md` and `design-system/theme.json`; compare `design-system/reference-desktop.webp` and `reference-mobile.webp` when making visual changes. The shared `assets/css/styles.css` is the implementation source of truth. Reuse the illustrated banner, warm paper, rust/teal/gold treatment, serif hero, rounded cards, shared page shell, and responsive behavior. Do not invent a separate visual identity for another session unless the user requests it.

Manage workshop records in `data/sessions.json`; only published sessions appear in home cards. Use `scripts/create-session.py <session-id>` for a new draft landing page. Add completed content and verify it before marking the session published. Keep links relative under `/tcea27/` and link only to completed resources.

Presenter guides and webdecks are encrypted. Private notes, plaintext presenter HTML, and passwords stay outside every public repository. Use `scripts/seal-presenter.cjs`, then rebuild the protected offline packet. Do not reintroduce private fields to public data or publish decrypted screenshots/PDFs containing notes.

Run `python3 tcea27/scripts/build-downloads.py` from the repository root, `scripts/verify.py`, and appropriate browser tests before publication. Web decks must follow the canonical Web Deck v5 specification; keep project copies of its framework and use local theme overrides. Preserve existing published resources and unrelated repository files.

The user's standing instruction authorizes commit, push, deploy, and live verification without routine confirmation.

## Approved hero and workshop decks

The user explicitly approved the header/hero/ribbon shown in `design-system/reference-approved-hero.webp`. Preserve its artwork, text, markup, and styling exactly unless the user specifically requests a hero change. Place the image carousel below it; render only published sessions from JSON, with accessible controls and no autoplay. Keep workshop-specific promotional content inside the relevant workshop.

For new decks: match `assets/webdeck/tcea27-deck-theme.css`; use a relevant photorealistic title image; put the facilitator profile second using `design-system/facilitator-miguel.json`; explain the session focus and measurable success criteria near the start. Add purposeful infographic visuals. Reserve time for individual thinking, neighbor talk, checking, and revision within the exact session duration. Keep pacing in notes, not a “Fifty minutes · Devices optional” line on the projected title. Read `design-system/deck-guidelines.md`.
