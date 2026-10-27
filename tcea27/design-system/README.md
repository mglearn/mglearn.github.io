# TCEA27 Learning Adventure · Reusable design system

This is the saved visual identity for **all TCEA27 sessions**, not just the first math workshop. Use it when adding future workshops. The approved reference is the current [TCEA27 hub](https://mglearn.github.io/tcea27/), with [desktop](reference-desktop.webp) and [mobile](reference-mobile.webp) snapshots saved here.

## Source of truth

- [Shared stylesheet](../assets/css/styles.css): the implementation of the theme. Extend this one stylesheet for components needed by future sessions; avoid copying or forking it per workshop.
- [Theme manifest](theme.json): named palette, typography, assets, signature treatments, and component selectors.
- [Print stylesheet](../assets/css/print.css): readable printable resources.
- [Original banner](../assets/images/learning-adventure.webp) and [generation prompt](../assets/images/learning-adventure-generation.json): reusable conference artwork.
- [Session body starter](session-body.html.tpl): uses the shared page shell and component classes.

## Preserve the look

Use the convention-inspired visual language: warm paper, illustrated discovery, a broad rust headline panel, teal and gold bands, large serif hero text, and white rounded cards with gold outlines. Navy remains the main reading and action color. Keep the illustration as a conference-wide asset so future workshop subjects feel part of the same site.

Use Georgia for the home hero headline and system sans-serif for body text and controls. Keep normal reading text at least 16px on phones. The homepage banner and session card are the main visual anchors; session pages use the gold-edged pale heading panel, shared navigation, and the same cards and controls. Do not replace this with a generic dashboard, a new color palette, or a separate per-session stylesheet.

Use the `.container` and `.section` spacing, `.grid` / `.split` layout, `.card`, `.activity`, `.callout`, `.button`, and `.session-card` components. Resource cards use colored header bands. Keep primary controls navy or gold with readable text. Gold is an accent, not small text on teal; use pale cream for that contrast. Reflow into a single column on phones without horizontal scrolling.

## Add a future session

1. Add the real workshop record to `data/sessions.json` with a unique ID/slug and `status: "draft"`. Include title, description, audience, duration, objectives, presenters, tools, strategies, and completed resources. Keep unpublished sessions out of the home cards.
2. Run `python3 tcea27/scripts/create-session.py <session-id>` from the repository root. It creates the draft landing page using this theme and the shared page shell, without overwriting an existing session. It links only to completed shared resources.
3. Build that workshop's real activities and downloads using shared classes. Add a session-specific contents menu only when those pages exist. A presenter guide or speaker notes must be encrypted before publication.
4. Run `python3 tcea27/scripts/build-downloads.py`, the static verifier, and appropriate browser checks. Compare desktop and phone views with the saved references. Check keyboard focus, contrast, 390px/320px reflow, print output, and link targets.
5. Mark the session published when complete and rebuild. Its home card is generated from the data record without a home-page redesign.

The initial math workshop keeps its stable path `sessions/math-without-price-tag/`; the displayed title is **High-Impact Teaching Math Tools Without the Price Tag**. Future workshops may have different subjects and formats while retaining this shared visual identity.

## Presenter material and deck identity

The webdeck follows the canonical [Web Deck v5](https://mguhlin.github.io/webdecks/) system, with a navy/gold/paper project skin that complements this site. Do not change the shared deck framework to restyle a session; use deck-local tokens. Keep its 1280×720 canvas, two-monitor presenter view, notes resizing, reflow, keyboard navigation, and audience-slide PDF export.

Private authoring inputs and passwords stay outside public repositories. Publish only sealed presenter HTML using `scripts/seal-presenter.cjs`. Do not put private notes or passwords in JSON, source, screenshots, or an unencrypted offline download. Earlier public revisions are a separate historical limitation; the current theme and protected resource files are the maintained release.
