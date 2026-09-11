# Generic four-page website template

A plain, readable starting point for a small business site. Four pages that
share one skeleton, so they cannot drift apart and a fifth page costs almost
nothing.

    Page 1  Who we are      history, and contact details on the page itself
    Page 2  What we do      product or service background
    Page 3  Benefits        what changes for the person who buys
    Page 4  Buy             the sale page

## What is deliberate here

- **Left aligned, never justified.** Justified text stretches the word spaces to
  force a straight right edge. Those gaps line up into vertical "rivers" that
  pull the eye down the page instead of along the line, which is the single
  worst thing you can do to somebody who finds reading hard.
- **Warm off-white paper, soft black ink.** Pure white glares under a lamp.
- **About 65 characters per line.** Past roughly that, the eye starts losing the
  beginning of the next line and re-reads the one it just finished.
- **Contact in the footer of every page,** and again on page one. People look in
  both places; it costs nothing to be in both.
- **Every page stands alone.** Most visitors do not arrive at the front door, so
  each page says what this is without relying on the one before it.
- **Placeholders that look like placeholders.** If one ever reaches a live site
  it should look obviously wrong, not blend in.

## Changing it

Nearly everything you will want to change is at the top of `style.css`:

    --accent      the one colour. Change this line, the whole site changes.
    --measure     how wide a line of text is allowed to get
    --line        line spacing

Pictures live in `img/` and are plain SVG drawings, not photographs — so there
is no licence attached to anything you pass on. Replace them with your own.

## Rebuilding

    python3 build.py

Every page is generated from one skeleton in `build.py`. Edit the skeleton and
all four pages change together. That is the point.
