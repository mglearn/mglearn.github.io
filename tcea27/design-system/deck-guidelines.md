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

For Beyond the Rollout, use the shared case and completed worked examples; do not ask attendees to bring or draft a project. Most time is instruction, with short decision discussions. The user-supplied infographic instructions call for meaningful icon/sequence diagrams, pastel panels, navy/teal/gold hierarchy, and explicit takeaway ribbons. Adapt that teaching grammar to this conference skin and Web Deck v5; do not stamp unrelated module numbers or certification claims onto workshop slides.

## Warm, direct language for every webdeck

Speak to educators as colleagues. Use “you” and “we,” natural contractions, and first-person speaker notes (“Here’s how I’d approach this”). Prefer “What would you do next?” to “Participants will identify the subsequent action.” On audience slides, use relatable situations, clear choices, and short explanations; reserve formal terminology for precision, then explain it in everyday words. Give fictional cases a human focus and identify them as fictional. Avoid detached third-person phrases such as “the presenter supplies the model” when “I’ll walk you through it” fits. Do not add forced enthusiasm, slogans, or unsupported personal anecdotes. Apply this voice to titles, prompts, explanations, takeaways, and speaker notes while preserving factual accuracy and accessibility.

Math teaching slides also use meaningful infographic comparisons, pathways, number-line arrows, visual evidence, and takeaway ribbons; keep the graph values and exact fifty-minute timing intact.

Pair relevant photorealistic scenes with readable, case-specific explanations when requested. Define short labels such as scope, handoff, and KPI by showing who acts, what they do, and what evidence they check. Never leave the audience to infer the meaning from an icon or label alone. Presenter access now supports optional thirty-day remembered keys; keep the cookie opaque and provide Forget access and lock.

Keep access-management controls off projected slides. The Forget access and lock action belongs inside keyboard help or the separate presenter view, not in a persistent overlay.

Play, Explore, Explain uses small groups of three or four, a shared device when needed, two eight-minute exploration rounds, and whole-group sharing within its fifty minutes. Keep all six requested tool tasks and the distinction between independent cards and a live response room. Preserve the varied visual forms and a purposeful image or infographic on every slide.
