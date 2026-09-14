#!/usr/bin/env python3
"""
Builds the generic four-page site.

Every page comes out of ONE skeleton. That is the whole point: four pages that
share their bones cost barely more than one, and they cannot drift apart. If a
page ever needs a different layout, that is a deliberate decision and a
different conversation - not something that happens quietly.

Nothing here is bespoke per page except the words and which pictures are used.
"""

import hashlib
import html
from pathlib import Path

HERE = Path(__file__).parent


def css_version():
    """A short fingerprint of the stylesheet, added to its web address.

    Browsers hold on to a stylesheet for a while rather than fetching it again
    every time - which is normally a kindness, and once was not. A colour change
    went live and the person looking at it kept seeing the old colours, because
    their browser was still using the copy it already had. They were not doing
    anything wrong and had no way to know.

    Changing the file changes this fingerprint, which changes the address, which
    the browser has never seen before - so it fetches it. Nobody has to know to
    press anything.
    """
    css = HERE / "style.css"
    if not css.exists():
        return "1"
    return hashlib.sha1(css.read_bytes()).hexdigest()[:8]

# The four pages, in order. Title, file, nav label, and the words.
NAV = [
    ("index.html",       "Who we are"),
    ("what-we-do.html",  "What we do"),
    ("benefits.html",    "Benefits"),
    ("buy.html",         "Buy"),
]

LANGS = ["English", "Français", "Español", "Deutsch", "中文", "العربية"]


def slot(text):
    """Guidance that is impossible to mistake for real content."""
    return f'<p class="slot">{html.escape(text)}</p>'


def head(page, title):
    nav_links = "\n".join(
        f'        <a href="{f}"{" aria-current=\"page\"" if f == page else ""}>{html.escape(l)}</a>'
        for f, l in NAV
    )
    opts = "\n".join(f'            <option>{html.escape(l)}</option>' for l in LANGS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — Your Business Name</title>
<meta name="description" content="Replace this with one plain sentence describing what this business does.">
<link rel="stylesheet" href="style.css?v={css_version()}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-head">
  <div class="wrap">
    <div class="head-row">
      <a class="brand" href="index.html">YOUR BUSINESS NAME<span>your tagline here</span></a>

      <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="nav">
        <span class="bars" aria-hidden="true"><i></i><i></i><i></i></span>
        Menu
      </button>

      <nav class="nav" id="nav" aria-label="Main">
{nav_links}
      </nav>

      <div class="lang">
        <label class="skip" for="lang">Choose a language</label>
        <select id="lang" name="lang">
{opts}
        </select>
      </div>
    </div>
  </div>
</header>

<div class="banner">
  <div class="wrap" style="padding:0">
    <img src="img/banner.svg" alt="Banner image — replace this" width="1600" height="400">
  </div>
</div>

<main id="main">
  <div class="wrap">
"""


FOOT = """  </div>
</main>

<div class="wrap">
  <ul class="strip">
    <li><img src="img/foot-1.svg" alt="Picture one — replace this" width="700" height="480"></li>
    <li><img src="img/foot-2.svg" alt="Picture two — replace this" width="700" height="480"></li>
    <li><img src="img/foot-3.svg" alt="Picture three — replace this" width="700" height="480"></li>
  </ul>
</div>

<footer class="site-foot">
  <div class="wrap">
    <div class="foot-cols">
      <div>
        <h3>Contact</h3>
        <p>
          Your Business Name<br>
          Street address<br>
          Town, State, Postcode
        </p>
        <p>
          Phone: <a href="tel:+00000000000">your phone number</a><br>
          Email: <a href="mailto:hello@example.com">your email address</a>
        </p>
      </div>
      <div>
        <h3>Pages</h3>
        <ul>
%s
        </ul>
      </div>
      <div>
        <h3>Hours</h3>
        <p>Monday to Friday<br>9am — 5pm</p>
        <h3>Legal</h3>
        <!-- A real, working link from day one, pointing at a placeholder PDF.
             The buyer overwrites terms.pdf with their own and changes nothing
             else - no editing, no re-linking, on any page. A link that works
             before the content exists is far safer than one added later and
             forgotten. -->
        <p><a href="terms.pdf">Terms &amp; Conditions (PDF)</a></p>
      </div>
    </div>
    <p class="legal">© <span id="yr">2026</span> Your Business Name. All rights reserved.</p>
  </div>
</footer>

<script>
/* The menu button. Plain, small, and it tells assistive software what it did -
   an icon that silently toggles a class is invisible to a screen reader. */
(function () {
  var b = document.getElementById('navToggle'), n = document.getElementById('nav');
  if (!b || !n) return;
  b.addEventListener('click', function () {
    var open = n.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
document.getElementById('yr').textContent = new Date().getFullYear();
</script>
</body>
</html>
"""


PAGES = {
    "index.html": dict(
        title="Who we are",
        h1="Who we are",
        stand="One sentence saying what this business actually does. Someone who "
              "landed here by accident should understand it before they scroll.",
        body=[
            ("slot", "Two or three short paragraphs about how the business started and who is "
                     "behind it. Say what you do BEFORE you say when you started — history is "
                     "interesting to you, but a first-time visitor needs to know what this is."),
            ("fig",  "A picture that shows the people or the place. Replace this."),
            ("slot", "The second half of the story. Keep paragraphs short — four or five lines "
                     "each. A wall of text is the fastest way to lose somebody who is not yet "
                     "sure they are in the right place."),
            ("h2",   "Where to find us"),
            ("html", '<p>Your Business Name<br>Street address<br>Town, State, Postcode</p>'
                     '<p>Phone: <a href="tel:+00000000000">your phone number</a><br>'
                     'Email: <a href="mailto:hello@example.com">your email address</a></p>'),
            ("slot", "Contact details appear here AND in the footer of every page, on purpose. "
                     "People look in both places and it costs nothing to be in both."),
        ],
    ),
    "what-we-do.html": dict(
        title="What we do",
        h1="What we do",
        stand="The background to the product or service. What it is, and why it "
              "exists at all.",
        body=[
            ("slot", "Open with the problem the product solves, in the customer's words rather "
                     "than yours. Two or three short paragraphs."),
            ("fig",  "A picture of the product, or of the work being done. Replace this."),
            ("slot", "Then the background — how it works, what makes it different, anything a "
                     "curious buyer would want before they get to the benefits page."),
            ("h2",   "How it works"),
            ("html", "<ol><li>First step — one line each.</li>"
                     "<li>Second step.</li>"
                     "<li>Third step.</li></ol>"),
        ],
    ),
    "benefits.html": dict(
        title="Benefits",
        h1="What it does for you",
        stand="Not a feature list. What actually changes for the person who buys it.",
        body=[
            ("slot", "Lead with the single biggest benefit. One short paragraph — resist the "
                     "urge to list everything at once."),
            ("fig",  "A picture showing the benefit rather than the object. Replace this."),
            ("h2",   "In short"),
            ("html", "<ul><li>Benefit one — a line, not a paragraph.</li>"
                     "<li>Benefit two.</li>"
                     "<li>Benefit three.</li>"
                     "<li>Benefit four.</li></ul>"),
            ("slot", "Close with whatever answers the objection you hear most often. If people "
                     "always ask about price, or delivery, or whether it lasts — answer it here, "
                     "before they have to ask."),
        ],
    ),
    "buy.html": dict(
        title="Buy",
        h1="Buy",
        stand="The page that asks for the sale. One job, and nothing on it that "
              "distracts from that job.",
        body=[
            ("slot", "A short paragraph restating what they get. They already know — this is "
                     "reassurance at the moment of deciding, not new information."),
            ("cta",  "Buy now"),
            ("slot", "Then the practical detail people want before paying: price, what is "
                     "included, how long delivery takes, and what happens if it is not right."),
            ("fig",  "A picture of exactly what arrives. Replace this."),
            ("h2",   "Before you buy"),
            ("html", "<ul><li>Price and what is included.</li>"
                     "<li>Delivery or collection.</li>"
                     "<li>Returns, guarantee or warranty.</li></ul>"),
            ("slot", "The payment button or link goes here. Never invent one — paste the real "
                     "link from whoever handles your payments, or leave it out until you have it."),
        ],
    ),
}


def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "slot":
            out.append("    " + slot(val))
        elif kind == "h2":
            out.append(f"    <h2>{html.escape(val)}</h2>")
        elif kind == "html":
            out.append("    " + val)
        elif kind == "cta":
            out.append(f'    <a class="cta" href="#">{html.escape(val)}</a>')
        elif kind == "fig":
            out.append(
                '    <figure>\n'
                '      <img src="img/mid.svg" alt="Picture — replace this" width="1200" height="620">\n'
                f'      <figcaption>{html.escape(val)}</figcaption>\n'
                '    </figure>'
            )
    return "\n".join(out)


def main():
    foot_links = "\n".join(
        f'          <li><a href="{f}">{html.escape(l)}</a></li>' for f, l in NAV
    )
    for fname, spec in PAGES.items():
        page = head(fname, spec["title"])
        page += f'    <h1>{html.escape(spec["h1"])}</h1>\n'
        page += f'    <p class="standfirst">{html.escape(spec["stand"])}</p>\n'
        page += render_body(spec["body"]) + "\n"
        page += FOOT % foot_links
        (HERE / fname).write_text(page, encoding="utf-8")
        print(f"wrote {fname}")


if __name__ == "__main__":
    main()
