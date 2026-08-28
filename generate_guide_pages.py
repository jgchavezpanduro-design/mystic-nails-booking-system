#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates blog/guide article pages, reusing the service-page design system."""
import os
import re
from urllib.parse import quote

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://mysticnailsart.com/guia/{slug}/">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_description}">
<meta property="og:url" content="https://mysticnailsart.com/guia/{slug}/">
<meta property="og:image" content="https://mysticnailsart.com/assets/images/{og_image}">
<meta name="twitter:card" content="summary_large_image">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{h1}",
  "description": "{description}",
  "image": "https://mysticnailsart.com/assets/images/{og_image}",
  "author": {{ "@type": "Organization", "name": "Mystic Nails Art" }},
  "publisher": {{
    "@type": "Organization",
    "name": "Mystic Nails Art",
    "logo": {{ "@type": "ImageObject", "url": "https://mysticnailsart.com/assets/images/carolina-fundadora-mystic-nails-art.webp" }}
  }},
  "datePublished": "{date_published}",
  "mainEntityOfPage": "https://mysticnailsart.com/guia/{slug}/"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://mysticnailsart.com/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Guide", "item": "https://mysticnailsart.com/#servicios-playa-del-carmen" }},
    {{ "@type": "ListItem", "position": 3, "name": "{h1}", "item": "https://mysticnailsart.com/guia/{slug}/" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{faq_schema}
  ]
}}
</script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&display=swap" rel="stylesheet">

<script async src="https://www.googletagmanager.com/gtag/js?id=AW-16897215421"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'AW-16897215421');
  gtag('config', 'G-1PP2FT94K1');
</script>

<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    --mn-bg:#fdf8fb; --mn-card:#ffffff; --mn-bdr:rgba(0,0,0,0.08);
    --mn-pri:#7a3fa8; --mn-pdim:rgba(122,63,168,0.10); --mn-txt:#1e1428; --mn-mut:#7a6890;
    --mn-ga:#7a3fa8; --mn-gb:#c4577a; --mn-foot:#0a0814;
    background:var(--mn-bg); color:var(--mn-txt); font-family:'Fredoka',sans-serif; font-weight:300; line-height:1.6;
  }}
  h1, h2, h3 {{ font-family:'Fredoka',sans-serif; font-weight:600; line-height:1.15; }}
  a {{ color:var(--mn-pri); }}
  .wrap {{ max-width:800px; margin:0 auto; padding:0 24px; }}
  nav {{ padding:22px 0; border-bottom:1px solid var(--mn-bdr); }}
  nav .wrap {{ display:flex; justify-content:space-between; align-items:center; }}
  .brand {{ font-family:'Fredoka',sans-serif; font-size:22px; font-weight:600; background:linear-gradient(135deg,var(--mn-ga),var(--mn-gb)); -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; text-decoration:none; }}
  .back-link {{ font-size:14px; color:var(--mn-mut); text-decoration:none; }}
  .back-link:hover {{ color:var(--mn-pri); }}
  main {{ padding:56px 0 80px; }}
  .breadcrumb {{ font-size:13px; color:var(--mn-mut); margin-bottom:18px; }}
  .breadcrumb a {{ color:var(--mn-mut); text-decoration:none; }}
  .breadcrumb a:hover {{ color:var(--mn-pri); }}
  .kicker {{ font-size:11px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:var(--mn-pri); margin-bottom:12px; }}
  h1 {{ font-size:clamp(34px,5vw,48px); margin-bottom:18px; }}
  .lead {{ font-size:18px; color:var(--mn-mut); font-weight:300; margin-bottom:28px; max-width:640px; }}
  .cta-row {{ display:flex; gap:12px; flex-wrap:wrap; margin-bottom:48px; }}
  .btn-primary {{ background:linear-gradient(135deg,var(--mn-ga),var(--mn-gb)); color:#fff; padding:15px 30px; border-radius:50px; font-weight:600; text-decoration:none; display:inline-block; }}
  .btn-secondary {{ border:1.5px solid var(--mn-bdr); color:var(--mn-txt); padding:15px 28px; border-radius:50px; font-weight:500; text-decoration:none; display:inline-block; }}
  .btn-secondary:hover {{ border-color:var(--mn-pri); color:var(--mn-pri); }}
  section {{ margin-bottom:52px; }}
  h2 {{ font-size:clamp(24px,3.5vw,32px); margin-bottom:18px; }}
  section p {{ font-size:16px; color:var(--mn-mut); margin-bottom:14px; }}
  section p strong {{ color:var(--mn-txt); font-weight:600; }}
  ul.benefits {{ list-style:none; display:grid; gap:12px; }}
  ul.benefits li {{ background:var(--mn-card); border:1px solid var(--mn-bdr); border-radius:14px; padding:16px 20px; font-size:15px; color:var(--mn-mut); }}
  ul.benefits li strong {{ color:var(--mn-txt); font-weight:600; }}
  table {{ width:100%; border-collapse:collapse; background:var(--mn-card); border:1px solid var(--mn-bdr); border-radius:16px; overflow:hidden; }}
  th {{ text-align:left; padding:14px 18px; font-size:12px; letter-spacing:1px; text-transform:uppercase; color:var(--mn-pri); font-weight:700; background:var(--mn-pdim); }}
  td {{ padding:14px 18px; font-size:15px; color:var(--mn-mut); border-top:1px solid var(--mn-bdr); }}
  td:first-child {{ font-weight:600; color:var(--mn-txt); white-space:nowrap; }}
  .faq-item {{ border-bottom:1px solid var(--mn-bdr); padding:18px 0; }}
  .faq-item h3 {{ font-size:17px; font-weight:600; margin-bottom:8px; color:var(--mn-txt); font-family:'Fredoka',sans-serif; }}
  .faq-item p {{ font-size:15px; color:var(--mn-mut); }}
  .related {{ display:flex; gap:10px; flex-wrap:wrap; }}
  .related a {{ border:1px solid var(--mn-bdr); border-radius:50px; padding:9px 18px; font-size:14px; text-decoration:none; color:var(--mn-txt); }}
  .related a:hover {{ border-color:var(--mn-pri); color:var(--mn-pri); }}
  footer {{ background:var(--mn-foot); color:rgba(255,255,255,0.5); padding:40px 0; margin-top:40px; }}
  footer .wrap {{ display:flex; justify-content:space-between; flex-wrap:wrap; gap:16px; font-size:13px; }}
  footer a {{ color:rgba(255,255,255,0.6); }}
  footer .footer-links {{ display:flex; gap:14px; flex-wrap:wrap; }}
</style>
</head>
<body data-theme="light">

<nav>
  <div class="wrap">
    <a class="brand" href="https://mysticnailsart.com/">Mystic Nails Art</a>
    <a class="back-link" href="https://mysticnailsart.com/">&larr; Back to home</a>
  </div>
</nav>

<main>
  <div class="wrap">
    <p class="breadcrumb"><a href="https://mysticnailsart.com/">Home</a> / <a href="https://mysticnailsart.com/#servicios-playa-del-carmen">Guide</a> / {h1}</p>

    <p class="kicker">Mystic Nails Art Guide</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>

    <div class="cta-row">
      <a class="btn-primary" href="https://wa.me/529843108186?text={wa_text}" target="_blank" rel="noopener">Get a quote on WhatsApp</a>
      <a class="btn-secondary" href="https://mysticnailsart.com/#precios">View prices</a>
    </div>

{body_sections}

    <section>
      <h2>Frequently asked questions</h2>
{faq_html}
    </section>

    <section>
      <h2>Explore other services</h2>
      <div class="related">
{related}
      </div>
    </section>
  </div>
</main>

<footer>
  <div class="wrap">
    <div>Mystic Nails Art &mdash; Calle 38 Nte Lote 73, Tohoku, Centro, Playa del Carmen, Q.R. \U0001f1f2\U0001f1fd</div>
    <div><a href="https://wa.me/529843108186" target="_blank" rel="noopener">+52 984 310 8186</a> &middot; Mon&ndash;Sun 09:00&ndash;20:00</div>
    <div class="footer-links">
      <a href="https://mysticnailsart.com/about/">About</a>
      <a href="https://mysticnailsart.com/contact/">Contact</a>
      <a href="https://mysticnailsart.com/privacy/">Privacy</a>
    </div>
  </div>
</footer>

</body>
</html>
'''

def faq_block(items):
    schema_parts = []
    html_parts = []
    for q, a in items:
        schema_parts.append('''    {{
      "@type": "Question",
      "name": "{q}",
      "acceptedAnswer": {{ "@type": "Answer", "text": "{a}" }}
    }}'''.format(q=q, a=a))
        html_parts.append('''      <div class="faq-item">
        <h3>{q}</h3>
        <p>{a}</p>
      </div>'''.format(q=q, a=a))
    return ',\n'.join(schema_parts), '\n'.join(html_parts)

def section(heading, paragraphs=None, list_items=None, table_rows=None, table_headers=None):
    parts = ['    <section>', '      <h2>{}</h2>'.format(heading)]
    if paragraphs:
        for p in paragraphs:
            parts.append('      <p>{}</p>'.format(p))
    if list_items:
        parts.append('      <ul class="benefits">')
        for label, text in list_items:
            parts.append('        <li><strong>{label}:</strong> {text}</li>'.format(label=label, text=text))
        parts.append('      </ul>')
    if table_rows:
        parts.append('      <table>')
        parts.append('        <thead><tr>' + ''.join('<th>{}</th>'.format(h) for h in table_headers) + '</tr></thead>')
        parts.append('        <tbody>')
        for row in table_rows:
            parts.append('          <tr>' + ''.join('<td>{}</td>'.format(c) for c in row) + '</tr>')
        parts.append('        </tbody>')
        parts.append('      </table>')
    parts.append('    </section>')
    return '\n'.join(parts)

NAME_TO_SLUG = {
    "Gelish": "gelish-playa-del-carmen",
    "Rubber Base": "rubber-base-playa-del-carmen",
    "Builder Gel": "builder-gel-playa-del-carmen",
    "Kapping": "kapping-playa-del-carmen",
    "Soft Gel / Gel X": "softgel-gel-x-playa-del-carmen",
    "Acrylic / Polygel": "acrilicas-polygel-playa-del-carmen",
    "Express Polish": "esmaltado-express-playa-del-carmen",
    "Russian Pedicure": "pedicure-ruso-playa-del-carmen",
    "Mystic Pedicure": "pedicure-mistico-playa-del-carmen",
}

def related_block(items):
    return '\n'.join('        <a href="https://mysticnailsart.com/{slug}/">{name}</a>'.format(slug=NAME_TO_SLUG[n], name=n) for n in items) + \
           '\n        <a href="https://mysticnailsart.com/#gallery">View design gallery</a>'

def section_html_to_markdown(section_html):
    """Converts the predictable output of section() (h2/p/ul.benefits/table) to markdown."""
    heading = re.search(r'<h2>(.*?)</h2>', section_html, re.S).group(1)
    lines = ['## {}'.format(heading), '']
    for p in re.findall(r'<p>(.*?)</p>', section_html, re.S):
        p = re.sub(r'<strong>(.*?)</strong>', r'**\1**', p)
        lines.append(p)
        lines.append('')
    items = re.findall(r'<li><strong>(.*?):</strong>\s*(.*?)</li>', section_html, re.S)
    for label, text in items:
        lines.append('- **{}**: {}'.format(label, text))
    if items:
        lines.append('')
    headers = re.findall(r'<th>(.*?)</th>', section_html, re.S)
    if headers:
        lines.append('| ' + ' | '.join(headers) + ' |')
        lines.append('|' + '---|' * len(headers))
        for row in re.findall(r'<tr>(.*?)</tr>', section_html.split('<tbody>')[1] if '<tbody>' in section_html else '', re.S):
            cells = re.findall(r'<td>(.*?)</td>', row, re.S)
            lines.append('| ' + ' | '.join(cells) + ' |')
        lines.append('')
    return '\n'.join(lines)

def render_markdown(g):
    lines = ['# {}'.format(g['h1']), '', g['lead'], '']
    for sec in g['body_sections']:
        lines.append(section_html_to_markdown(sec))
        lines.append('')
    lines += ['## Frequently asked questions', '']
    for q, a in g['faq']:
        lines += ['**{}**'.format(q), a, '']
    lines += ['## Get a quote', '', 'WhatsApp: https://wa.me/529843108186?text={}'.format(quote(g['wa_message'])),
              'Website: https://mysticnailsart.com/guia/{}/'.format(g['slug']), '',
              '## Explore other services', '']
    for n in g['related']:
        lines.append('- [{}](https://mysticnailsart.com/{}/)'.format(n, NAME_TO_SLUG[n]))
    return '\n'.join(lines) + '\n'

GUIDES = []

# ---------------------------------------------------------------- Article 1
GUIDES.append(dict(
    slug="gelish-acrilico-polygel-diferencias-playa-del-carmen",
    title="Gelish vs. Acrylic vs. Polygel: Which Should You Choose? | Mystic Nails Art",
    description="We compare Gelish, Rubber Base, Acrylic and Polygel: duration, durability and starting price, so you can choose the ideal technique in Playa del Carmen.",
    og_description="A complete comparison of nail techniques: Gelish, Rubber Base, Acrylic and Polygel. Duration, durability and price.",
    og_image="gelish-rosa-diseno-playa-del-carmen.webp",
    date_published="2026-08-22",
    h1="Gelish vs. Acrylic vs. Polygel: Which Should You Choose?",
    lead="The four most requested techniques at Mystic Nails Art explained simply: what each one does, how long it lasts and who it's ideal for.",
    wa_message="Hi, I read the technique guide and I'd like a recommendation on what works best for me",
    body_sections=[
        section("What each technique is", paragraphs=[
            "<strong>Gelish</strong> is a gel polish cured under a UV/LED lamp over your natural nail. It doesn't add structure or length, only long-lasting color and shine.",
            "<strong>Rubber Base</strong> is a flexible base that reinforces weak or thin nails before color is applied, helping to level and protect without losing natural flexibility.",
            "<strong>Acrylic</strong> is a powder-and-liquid system sculpted over the nail to give length, shape and very resistant structure; it's the classic choice for long-lasting extensions.",
            "<strong>Polygel</strong> combines the best of gel and acrylic: it's molded like acrylic but cures under a lamp like gel, giving a lighter, more natural finish for Kapping or extensions."
        ]),
        section("Quick comparison", table_headers=["Technique", "Duration", "Ideal for", "Starting price"], table_rows=[
            ["Gelish", "3+ weeks", "Color and shine on natural nails", "$430 MXN"],
            ["Rubber Base", "3+ weeks", "Weak or thin nails", "$500 MXN"],
            ["Acrylic / Polygel", "3-4 weeks", "Length and resistant structure", "$740 MXN"],
            ["Kapping (Polygel)", "3+ weeks", "Reinforcing without a full extension", "$640 MXN"],
        ]),
        section("Which one is right for you?", paragraphs=[
            "If you just want even, glossy color on your natural nail, <strong>Gelish</strong> is the fastest and most affordable option.",
            "If your nails break or bend easily, start with <strong>Rubber Base</strong> before considering extensions.",
            "If you want more length and structure that holds up to daily use, <strong>Acrylic or Polygel</strong> are the best investment.",
            "When in doubt, send us a reference photo on WhatsApp and we'll tell you exactly which technique and price works for you."
        ]),
    ],
    faq=[
        ("Can I combine techniques, for example Rubber Base with a design?", "Yes. Rubber Base supports the same level of design and nail art as traditional Gelish; only the base used before color changes."),
        ("Which technique is gentler on the natural nail?", "Gelish and Rubber Base are the most gentle on the natural nail. Acrylic and Polygel require more careful removal to avoid weakening the nail."),
        ("How much does it cost to switch from one technique to another?", "Removing a previous service has a separate cost, whether you're coming from Mystic Nails Art or another salon. Ask us on WhatsApp about your specific case."),
    ],
    related=["Gelish", "Rubber Base", "Acrylic / Polygel", "Kapping"],
))

# ---------------------------------------------------------------- Article 2
GUIDES.append(dict(
    slug="cuanto-dura-gelish-acrilico-rubber-base-playa-del-carmen",
    title="How Long Each Nail Technique Lasts (Complete Guide) | Mystic Nails Art",
    description="How long Gelish, Rubber Base, Acrylic and Polygel last, what affects durability and how to make it last longer. A guide from Mystic Nails Art, Playa del Carmen.",
    og_description="A duration guide by nail technique, plus tips to make your manicure last longer.",
    og_image="gelish-rubber-base-natural-playa-del-carmen.webp",
    date_published="2026-08-22",
    h1="How Long Each Nail Technique Lasts",
    lead="The real duration of Gelish, Rubber Base, Acrylic and Polygel, and what you can do to make your manicure hold up longer.",
    wa_message="Hi, I'd like to know how long each nail technique lasts",
    body_sections=[
        section("Duration by technique", list_items=[
            ("Gelish", "More than 3 weeks with intact shine on the natural nail."),
            ("Rubber Base", "3+ weeks, with the added benefit of reinforcing the nail while it lasts."),
            ("Acrylic / Polygel", "3 to 4 weeks before needing a growth touch-up."),
            ("Kapping (Polygel)", "3+ weeks, similar to Gelish but more resistant."),
            ("Express Polish", "5 to 10 days, since it's traditional polish without UV curing."),
        ]),
        section("What makes it last less", paragraphs=[
            "Constant contact with seawater, pool chlorine and sunscreen can speed up wear on any technique.",
            "Using your nails as a tool (opening cans, scratching) is the most common cause of lifting or breaking early.",
            "A poorly sealed edge (no sealing top coat) lets in moisture and shortens how long it lasts."
        ]),
        section("How to make it last longer", list_items=[
            ("Moisturize your cuticles", "A daily cuticle oil keeps the gel from lifting at the edges."),
            ("Use gloves", "Protect your nails from chemicals and hot water when washing dishes or cleaning."),
            ("Avoid peeling off polish", "Forcing gel off damages the natural nail and ruins the work early."),
        ]),
    ],
    faq=[
        ("Can I swim in the sea with fresh Gelish or Acrylic?", "Yes, but wait at least 2 hours after your appointment for it to fully cure, and apply nail oil or protectant after swimming."),
        ("Which technique holds up best in Playa del Carmen's climate?", "Rubber Base and Kapping tend to perform better with heat and humidity because they're more flexible than traditional acrylic."),
        ("How often should I get maintenance?", "We recommend a touch-up every 3 weeks for extensions and Rubber Base, and every 3-4 weeks for Gelish, depending on how fast your nails grow."),
    ],
    related=["Gelish", "Rubber Base", "Acrylic / Polygel", "Express Polish"],
))

# ---------------------------------------------------------------- Article 3
GUIDES.append(dict(
    slug="cuidado-unas-gel-playa-del-carmen",
    title="How to Care for Gel Nails at the Beach | Mystic Nails Art",
    description="A guide to caring for gel, acrylic or polygel nails in Playa del Carmen: sun, seawater, chlorine and sunscreen without ruining your manicure.",
    og_description="Tips to help your manicure survive the sun, sea and chlorine of Playa del Carmen.",
    og_image="manicure-ombre-french-almendra-playa-del-carmen.webp",
    date_published="2026-08-22",
    h1="How to Care for Gel Nails at the Beach",
    lead="Living in or vacationing in Playa del Carmen exposes your nails to sun, salt and chlorine every day. Here's how to care for them without sacrificing your manicure.",
    wa_message="Hi, I'd like nails that hold up well to beach weather",
    body_sections=[
        section("Why beach weather affects your nails", paragraphs=[
            "Direct sun dries out cuticles and can dull the shine of gel over time.",
            "Seawater and pool chlorine are abrasive: they gradually weaken any polish, including semi-permanent gel.",
            "Sunscreen on your hands, if not fully absorbed, leaves a film that can make polish look dull or lift sooner."
        ]),
        section("Practical care tips", list_items=[
            ("Apply cuticle oil", "Every day, especially after swimming or sun exposure."),
            ("Rinse your hands after the sea or pool", "Fresh water removes the excess salt and chlorine that dries out the nail."),
            ("Use hand sunscreen carefully", "Apply to the back of the hand, avoiding buildup right at the nail edge."),
            ("Dry your hands thoroughly", "Trapped moisture under the polish makes it more likely to lift or discolor."),
        ]),
        section("Which technique we recommend for tourists and active locals", paragraphs=[
            "If you'll spend a lot of time in the sea or pool, <strong>Gelish</strong> or <strong>Rubber Base</strong> are easier to maintain than long extensions.",
            "If you want extensions for your trip, go for a short or medium length: it holds up better to daily beach wear than an extreme length."
        ]),
    ],
    faq=[
        ("Can I get my nails done the day before traveling to the beach?", "Yes, in fact we recommend it: give it at least 24 hours to fully cure before exposing it to the sea."),
        ("Does chlorine fade Gelish?", "It can dull the shine with prolonged, frequent exposure. Rinsing your hands after the pool helps minimize the effect."),
        ("What do I do if a nail lifts mid-trip?", "Message us on WhatsApp; if you're in Playa del Carmen we can schedule a quick fix before it breaks further."),
    ],
    related=["Gelish", "Rubber Base", "Kapping", "Mystic Pedicure"],
))

# ---------------------------------------------------------------- Article 4
GUIDES.append(dict(
    slug="precios-unas-playa-del-carmen",
    title="How Much Nails Cost in Playa del Carmen (Price Guide) | Mystic Nails Art",
    description="Real prices for Gelish, Rubber Base, Acrylic, Polygel and pedicure in Playa del Carmen. Mystic Nails Art's 2026 price guide.",
    og_description="A price guide for nails in Playa del Carmen: Gelish, Rubber Base, extensions and pedicure.",
    og_image="unas-doradas-elegantes-diseno-hoja-playa-del-carmen.webp",
    date_published="2026-08-22",
    h1="How Much Nails Cost in Playa del Carmen",
    lead="Real prices, from the most basic options to the most elaborate extensions, so you can quote your appointment with no surprises.",
    wa_message="Hi, I saw the price guide and I'd like a quote for my appointment",
    body_sections=[
        section("Prices by technique", table_headers=["Service", "Starting at"], table_rows=[
            ["Gelish", "$430 MXN"],
            ["Rubber Base", "$500 MXN"],
            ["Builder Gel", "$520 MXN"],
            ["Kapping (Polygel)", "$640 MXN"],
            ["Soft Gel / Gel X", "$600 MXN"],
            ["Acrylic / Polygel", "$740 MXN"],
            ["Express Polish (feet)", "$200 MXN"],
            ["Russian Pedicure", "$300 MXN"],
            ["Mystic Pedicure", "$500 MXN"],
        ]),
        section("What makes the price go up or down", list_items=[
            ("Design level", "A solid color costs less than elaborate nail art, 3D or rhinestones."),
            ("Extension length", "The longer the length, the more material and work time required."),
            ("Removing a previous service", "If you're coming with nails from another salon or from Mystic Nails Art, removal is quoted separately."),
        ]),
        section("How to get your exact price", paragraphs=[
            "The prices in this guide are the starting point (“from”); the final price depends on design, length and the condition of your natural nail.",
            "The fastest way to know your exact price is to send us a reference photo on WhatsApp: we'll reply with the cost before you book."
        ]),
    ],
    faq=[
        ("Do the prices include removal from another salon?", "No, removal is quoted separately and varies depending on the technique you're currently wearing."),
        ("Do you offer hands-and-feet packages?", "Yes, ask us on WhatsApp about manicure and pedicure combos on the same day."),
        ("Do you accept card payments?", "Yes, we accept cash and card."),
    ],
    related=["Gelish", "Rubber Base", "Acrylic / Polygel", "Mystic Pedicure"],
))

# ---------------------------------------------------------------- Article 5
GUIDES.append(dict(
    slug="unas-para-boda-evento-playa-del-carmen",
    title="Wedding or Event Nails in Playa del Carmen: What to Choose | Mystic Nails Art",
    description="Which nail technique and design to choose for your wedding or special event in Playa del Carmen, and when to book your appointment.",
    og_description="A guide to wedding and event nails: technique, design and when to book in Playa del Carmen.",
    og_image="unas-3d-flores-rosa-holografico-playa-del-carmen.webp",
    date_published="2026-08-22",
    h1="Wedding or Event Nails: What to Choose",
    lead="Playa del Carmen is one of Mexico's favorite wedding destinations. Here's what we recommend so your nails look perfect all day.",
    wa_message="Hi, I have a wedding/event and I'd like a quote for my nails",
    body_sections=[
        section("Which technique lasts longest for your event day", paragraphs=[
            "For weddings or events we recommend <strong>Gelish or Rubber Base</strong> if you want your natural nail with a flawless finish, or <strong>Acrylic/Polygel</strong> if you want more length and presence in photos.",
            "Both options hold up through a full day of photos, dancing and activities without losing shine or shape."
        ]),
        section("Most requested styles for events", list_items=[
            ("Modern French", "Classic, elegant and pairs with any dress."),
            ("Nude with subtle shine", "Discreet but luminous in photos, ideal for brides."),
            ("Design with a touch of rhinestones", "A hint of rhinestones or a gold line adds a special touch without overdoing it."),
        ]),
        section("When to book before your event", paragraphs=[
            "It's best to book between 1 and 3 days before the event: enough time for it to cure well, without the risk of noticeable growth.",
            "If your event requires a design trial (for example, weddings), we can schedule a separate trial appointment beforehand.",
            "During peak wedding season, we recommend booking your date in advance on WhatsApp to secure your time slot."
        ]),
    ],
    faq=[
        ("Can I bring a photo of my dress to help choose a color?", "Yes, send it to us on WhatsApp along with your event date and we'll help you choose the ideal shade."),
        ("Do you do designs for an entire bridal party?", "Yes, we can coordinate appointments for multiple people on the same day; message us with the number of people and the date."),
        ("How far in advance should I book during peak season?", "We recommend booking 2 to 3 weeks in advance during peak wedding season to secure your time slot."),
    ],
    related=["Gelish", "Rubber Base", "Acrylic / Polygel", "Mystic Pedicure"],
))

# ---------------------------------------------------------------- Article 6
GUIDES.append(dict(
    slug="manicura-rusa-vs-tradicional-playa-del-carmen",
    title="Russian Manicure vs. Traditional Manicure: The Differences | Mystic Nails Art",
    description="What the Russian manicure and pedicure technique is, how it differs from a traditional manicure, and where we apply it at Mystic Nails Art, Playa del Carmen.",
    og_description="The differences between the Russian technique and a traditional manicure: precision, durability and who it's ideal for.",
    og_image="rubber-base-nail-art-playa-del-carmen.webp",
    date_published="2026-08-23",
    h1="Russian Manicure vs. Traditional Manicure: The Differences",
    lead="The Russian technique became popular for its precision and neat finish. Here's what it involves and how it differs from the traditional method.",
    wa_message="Hi, I read about the Russian technique and I'd like a quote for my appointment",
    body_sections=[
        section("What the Russian technique is", paragraphs=[
            "The Russian technique (also called dry manicure/pedicure) uses an electric drill to remove cuticles and hangnails without soaking the nail in water, achieving a very clean, precise finish all around the nail.",
            "It's especially valued because it leaves the nail ready for gel polish to last longer, by better removing the excess skin that usually causes gel to lift at the edges."
        ]),
        section("What a traditional manicure is", paragraphs=[
            "A traditional manicure soaks hands or feet in warm water to soften the cuticle, which is then removed with clippers or a cuticle nipper.",
            "It's a faster method and works well for regular maintenance, though the finish around the nail isn't always as precise as with the dry technique."
        ]),
        section("Quick comparison", table_headers=["Technique", "Precision", "Polish longevity", "Ideal for"], table_rows=[
            ["Russian technique (dry)", "Very high", "Longer-lasting thanks to a better seal", "Short nails, thick cuticles, salon-quality result"],
            ["Traditional (soak)", "Standard", "Normal duration", "Quick, regular maintenance"],
        ]),
        section("Where we apply it at Mystic Nails Art", paragraphs=[
            "We use the Russian dry-cuticle technique in our <strong>Russian Pedicure</strong>, the service where its precision and finish stand out the most.",
            "For hands we work with Gelish, Rubber Base and Builder Gel with the same meticulous cuticle care; if you're specifically looking for the dry method on hands, let us know on WhatsApp and we'll review it based on your case."
        ]),
    ],
    faq=[
        ("Does the Russian technique hurt more than the traditional one?", "It shouldn't hurt if done correctly; we use the drill at low speed with controlled pressure for a comfortable, precise result."),
        ("Do you do Russian manicure on hands?", "We apply the Russian-style dry cuticle technique in our Russian Pedicure. For hands we work with the same level of care in Gelish and Rubber Base; message us on WhatsApp to discuss your specific case."),
        ("How often should I repeat a Russian Pedicure?", "We recommend every 3 to 4 weeks, similar to how long Gelish lasts, depending on how fast your nails grow."),
    ],
    related=["Russian Pedicure", "Mystic Pedicure", "Rubber Base", "Gelish"],
))

for g in GUIDES:
    faq_schema, faq_html = faq_block(g["faq"])
    html = TEMPLATE.format(
        slug=g["slug"],
        title=g["title"],
        description=g["description"],
        og_description=g["og_description"],
        og_image=g["og_image"],
        date_published=g["date_published"],
        h1=g["h1"],
        lead=g["lead"],
        wa_text=quote(g["wa_message"]),
        body_sections="\n".join(g["body_sections"]),
        faq_schema=faq_schema,
        faq_html=faq_html,
        related=related_block(g["related"]),
    )
    outdir = os.path.join("guia", g["slug"])
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    os.makedirs(os.path.join("md", "guia"), exist_ok=True)
    with open(os.path.join("md", "guia", g["slug"] + ".md"), "w", encoding="utf-8") as f:
        f.write(render_markdown(g))
    print("Generated:", outdir, "+ md/guia/" + g["slug"] + ".md")
