# TCEA27 workshop deck standard

Use this standard for both current workshops and every future TCEA27 session.

## Visual identity

Use the canonical Web Deck v5 framework and its 1280×720 canvas, speaker notes, two-monitor presenter view, A−/A+ notes resizing, keyboard navigation, reflow, and slide PDF export. Keep project framework copies in `assets/webdeck/`. The shared TCEA27 skin is [tcea27-deck-theme.css](../assets/webdeck/tcea27-deck-theme.css): warm paper, rust title panel, teal accents, gold outlines, large serif headings, and rounded white cards. Change the skin through deck-local CSS, not framework behavior.

The approved website header/hero/ribbon is fixed; see [the approved screenshot](reference-approved-hero.webp). Do not change it to accommodate a deck, session carousel, or new workshop.

## Opening sequence

1. **Title:** a relevant, original photorealistic image, the workshop title, a concise purpose statement, and facilitator name. Keep timing/device directions in speaker notes; do not restore “Fifty minutes · Devices optional.”
2. **Facilitator:** use the reusable [Miguel profile](facilitator-miguel.json) and its portrait illustration. Verify current biographical claims against the linked source. Keep it brief and connect the background to the session.
3. **What this session addresses:** explain the problem, the few concepts participants will experience, and what they will produce or take away.
4. **Success criteria:** three or four observable “I can” outcomes that match the activities. Return to them in the final reflection. Distinguish them from a list of tool features.

## Content, conversation, and timing

Both initial workshops use twenty slides within exactly fifty minutes. A slide count is a design aid, not a pacing guarantee. Reserve time for quiet thinking, a neighbor exchange, an answer/model check, and revision. Participants remain in their seats; paper is a complete alternative. Keep models short and choose one case or instructional thread rather than racing through a larger course.

The math session retains its five blocks: noticing graphs, number models, a GraphSplat investigation, retrieval/feedback, and ACE application. The Project Management session is a focused adaptation of a four-hour supplied module; it does not claim to deliver that complete module or certification in fifty minutes.

Use the notes for approximate segment windows, first-person teleprompter guidance, discussion prompts, model reasoning, and transitions. Write around 90–130 words per slide, with enough flexibility to shorten an introduction. Add time by reducing content, not by removing all participant thinking.

## Images and infographics

Use local optimized WebP title photos, ideally around 1400px wide and near 160KB or less. Record the generation prompt and describe generated scenes as illustrative in metadata; do not imply they depict actual attendees. The title photo may also serve as that workshop's carousel image.

Use accessible native SVG or HTML for diagrams with precise labels and numbers. Original visual helpers live in `scripts/deck_visuals.py`, and the generated assets are in `assets/infographics/`. Put one instructional idea in a diagram: a sequence, relationship, feedback cycle, comparison, or decision. Use real text and accurate alt descriptions. Keep projected labels readable; an archived screenshot with tiny labels is not a substitute for a redesigned infographic.

## Reuse and publication

`render_deck.py` renders a private slide model using the shared theme. Each record has `start`, `end`, `title`, `content`, `notes`, and an optional slide kind. The source model and rendered plaintext must stay outside public Git. Publish only the encrypted result using `seal-presenter.cjs`. Include protected presenter resources in the offline packet. The current password is kept separately and must never appear in source, tests, screenshots, or public JSON.

Add a published workshop's image and alt text to `data/sessions.json`; the home carousel expands automatically. Keep math-specific content on the math page and project-management content on its own page. Verify slide geometry, title/facilitator/criteria order, fifty-minute totals, links, notes separation in PDF, password behavior, phone reflow, and presenter-window synchronization. Capture updated deck references outside public Git if they show private notes.
