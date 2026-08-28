#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the 8 remaining service landing pages from the Gelish template pattern."""
import os
from urllib.parse import quote

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://mysticnailsart.com/{slug}/">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_description}">
<meta property="og:url" content="https://mysticnailsart.com/{slug}/">
<meta property="og:image" content="https://mysticnailsart.com/assets/images/{og_image}">
<meta name="twitter:card" content="summary_large_image">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{service_name}",
  "serviceType": "{service_type}",
  "provider": {{
    "@type": "BeautySalon",
    "name": "Mystic Nails Art",
    "telephone": "+529843108186",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Calle 38 Nte Lote 73, Tohoku, Centro",
      "addressLocality": "Playa del Carmen",
      "addressRegion": "Quintana Roo",
      "addressCountry": "MX"
    }}
  }},
  "areaServed": "Playa del Carmen, Quintana Roo, Mexico",
  "url": "https://mysticnailsart.com/{slug}/"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://mysticnailsart.com/" }},
    {{ "@type": "ListItem", "position": 2, "name": "{h1}", "item": "https://mysticnailsart.com/{slug}/" }}
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
  h1 {{ font-size:clamp(34px,5vw,48px); margin-bottom:18px; }}
  .lead {{ font-size:18px; color:var(--mn-mut); font-weight:300; margin-bottom:28px; max-width:640px; }}
  .cta-row {{ display:flex; gap:12px; flex-wrap:wrap; margin-bottom:48px; }}
  .btn-primary {{ background:linear-gradient(135deg,var(--mn-ga),var(--mn-gb)); color:#fff; padding:15px 30px; border-radius:50px; font-weight:600; text-decoration:none; display:inline-block; }}
  .btn-secondary {{ border:1.5px solid var(--mn-bdr); color:var(--mn-txt); padding:15px 28px; border-radius:50px; font-weight:500; text-decoration:none; display:inline-block; }}
  .btn-secondary:hover {{ border-color:var(--mn-pri); color:var(--mn-pri); }}
  section {{ margin-bottom:52px; }}
  h2 {{ font-size:clamp(24px,3.5vw,32px); margin-bottom:18px; }}
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
    <p class="breadcrumb"><a href="https://mysticnailsart.com/">Home</a> / {h1}</p>

    <h1>{h1} 🇲🇽</h1>
    <p class="lead">{lead}</p>

    <div class="cta-row">
      <a class="btn-primary" href="https://wa.me/529843108186?text={wa_text}" target="_blank" rel="noopener">Book via WhatsApp</a>
      <a class="btn-secondary" href="https://mysticnailsart.com/#services">View all services</a>
    </div>

    <section>
      <h2>Why choose {service_name_short}?</h2>
      <ul class="benefits">
{benefits}
      </ul>
    </section>

    <section>
      <h2>{compare_title}</h2>
      <table>
        <thead><tr><th>Technique</th><th>Ideal for</th></tr></thead>
        <tbody>
{compare_rows}
        </tbody>
      </table>
    </section>

    <section>
      <h2>FAQ about {service_name_short}</h2>
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
    <div>Mystic Nails Art &mdash; Calle 38 Nte Lote 73, Tohoku, Centro, Playa del Carmen, Q.R. 🇲🇽</div>
    <div><a href="https://wa.me/529843108186" target="_blank" rel="noopener">+52 984 310 8186</a> &middot; Mon&ndash;Sun 09:00&ndash;20:00</div>
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

def benefits_block(items):
    return '\n'.join('        <li><strong>{label}:</strong> {text}</li>'.format(label=l, text=t) for l, t in items)

def compare_rows_block(rows):
    return '\n'.join('          <tr><td>{name}</td><td>{desc}</td></tr>'.format(name=n, desc=d) for n, d in rows)

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

def render_markdown(p):
    lines = ['# {}'.format(p['h1']), '', p['lead'], '', '## Why choose {}?'.format(p['service_name_short']), '']
    for label, text in p['benefits']:
        lines.append('- **{}**: {}'.format(label, text))
    lines += ['', '## {}'.format(p['compare_title']), '', '| Technique | Ideal for |', '|---|---|']
    for name, desc in p['compare_rows']:
        lines.append('| {} | {} |'.format(name, desc))
    lines += ['', '## FAQ about {}'.format(p['service_name_short']), '']
    for q, a in p['faq']:
        lines += ['**{}**'.format(q), a, '']
    lines += ['## Book', '', 'WhatsApp: https://wa.me/529843108186?text={}'.format(quote(p['wa_message'])),
              'Website: https://mysticnailsart.com/{}/'.format(p['slug']), '',
              '## Explore other services', '']
    for n in p['related']:
        lines.append('- [{}](https://mysticnailsart.com/{}/)'.format(n, NAME_TO_SLUG[n]))
    return '\n'.join(lines) + '\n'

COMPARE_ROWS_NATURAL = [
    ("Gelish", "Natural nails with shine and color, results lasting 3+ weeks"),
    ("Rubber Base", "Weak nails that need reinforcement with a natural finish"),
    ("Builder Gel", "Strengthening and adding structure to the natural nail"),
]

COMPARE_ROWS_EXTENSIONS = [
    ("Kapping", "Protection over the natural nail with polygel or acrylic overlay, greater durability"),
    ("Soft Gel / Gel X", "Lightweight, natural extensions, instant length and comfortable finish"),
    ("Acrylic / Polygel", "Strong extensions for more structure, length and elaborate designs"),
]

COMPARE_ROWS_FEET = [
    ("Express Polish", "Quick polish on toes, 20-30 min, solid color or French"),
    ("Russian Pedicure", "Deep dry cleaning, ideal for cuticles and a precise finish"),
    ("Mystic Pedicure", "Complete experience: exfoliation, hydration and Gelish included"),
]

PAGES = [
    dict(
        slug="rubber-base-playa-del-carmen",
        service_name="Rubber Base",
        service_name_short="Rubber Base",
        service_type="Nail reinforcement with Rubber Base",
        h1="Rubber Base in Playa del Carmen",
        title="Rubber Base in Playa del Carmen | Mystic Nails Art",
        description="Rubber Base in Playa del Carmen: flexible reinforcement for weak or thin nails, with a natural finish. Book on WhatsApp at Mystic Nails Art.",
        og_description="Flexible reinforcement to protect, level and strengthen weak or thin nails. Book on WhatsApp.",
        og_image="gelish-rubber-base-natural-playa-del-carmen.webp",
        lead="Flexible reinforcement to protect, level and strengthen weak or thin nails, with a natural finish that cares for your own nail while protecting it.",
        wa_message="Hi, I'd like to book a Rubber Base at Mystic Nails Art",
        benefits=[
            ("Reinforcement", "protects weak or thin nails without losing flexibility"),
            ("Natural finish", "more discreet than an extension, ideal for keeping your own length"),
            ("Duration", "60–90 minutes of application"),
            ("Ideal for", "nail-biters or anyone with brittle nails"),
        ],
        compare_title="Rubber Base vs. other techniques",
        compare_rows=COMPARE_ROWS_NATURAL,
        faq=[
            ("Who is Rubber Base for?", "For people with weak, thin nails or nail-biters looking for flexible, natural reinforcement."),
            ("How is it different from Gelish?", "Gelish is a polish focused on color and shine. Rubber Base is a structural reinforcement designed to protect fragile nails."),
            ("How long does the application take?", "Between 60 and 90 minutes, depending on the condition of the nail."),
            ("How do I book my appointment?", "On WhatsApp at +52 984 310 8186, letting us know the service and your availability."),
        ],
        related=["Gelish", "Builder Gel", "Soft Gel / Gel X", "Mystic Pedicure"],
    ),
    dict(
        slug="builder-gel-playa-del-carmen",
        service_name="Builder Gel",
        service_name_short="Builder Gel",
        service_type="Nail structure with Builder Gel",
        h1="Builder Gel in Playa del Carmen",
        title="Builder Gel in Playa del Carmen | Mystic Nails Art",
        description="Builder Gel in Playa del Carmen: structure and strength for natural nails that need extra support. Book on WhatsApp at Mystic Nails Art.",
        og_description="Structure and strength for natural nails that need extra support. Book on WhatsApp.",
        og_image="gelish-rubber-base-natural-playa-del-carmen.webp",
        lead="Structure and strength for natural nails that need extra support, ideal if you want to strengthen your nail without a full extension.",
        wa_message="Hi, I'd like to book a Builder Gel at Mystic Nails Art",
        benefits=[
            ("Support", "more structure than Rubber Base for nails that need extra reinforcement"),
            ("Strength", "ideal if your nails break or bend easily"),
            ("Duration", "90–120 minutes of application"),
            ("Ideal for", "anyone who wants to strengthen their natural nail without an extension"),
        ],
        compare_title="Builder Gel vs. other techniques",
        compare_rows=COMPARE_ROWS_NATURAL,
        faq=[
            ("What's the difference between Builder Gel and Rubber Base?", "Builder Gel gives more structure and support, while Rubber Base is more flexible and natural. Both reinforce the nail, but with a different level of firmness."),
            ("Is Builder Gel an extension?", "No, it's applied over the natural nail to add strength, not to lengthen it."),
            ("How long does the appointment take?", "Between 90 and 120 minutes."),
            ("How do I book my appointment?", "On WhatsApp at +52 984 310 8186, letting us know the service and your availability."),
        ],
        related=["Gelish", "Rubber Base", "Soft Gel / Gel X", "Mystic Pedicure"],
    ),
    dict(
        slug="kapping-playa-del-carmen",
        service_name="Polygel or Acrylic Overlay Kapping",
        service_name_short="Kapping",
        service_type="Kapping (polygel or acrylic overlay)",
        h1="Kapping in Playa del Carmen",
        title="Kapping in Playa del Carmen | Mystic Nails Art",
        description="Polygel or acrylic overlay Kapping in Playa del Carmen: extra protection and durability over your natural nail. Book on WhatsApp.",
        og_description="Protection over the natural nail with polygel or acrylic overlay for greater durability. Book on WhatsApp.",
        og_image="unas-doradas-3d-flores-perlas-playa-del-carmen.webp",
        lead="Protection over the natural nail with polygel or acrylic overlay for greater durability, ideal if you want a resistant finish without extending the length too much.",
        wa_message="Hi, I'd like to book a Kapping at Mystic Nails Art",
        benefits=[
            ("Durability", "more resistant than a traditional polish"),
            ("Protection", "covers and protects the natural nail from daily wear and knocks"),
            ("Duration", "120–150 minutes of application"),
            ("Ideal for", "anyone who wants resistance without a long extension"),
        ],
        compare_title="Kapping vs. other extensions",
        compare_rows=COMPARE_ROWS_EXTENSIONS,
        faq=[
            ("What is Kapping?", "It's a technique that covers the natural nail with polygel or acrylic overlay to give it more protection and durability."),
            ("Does Kapping add length?", "It adds a bit of length and structure, but not as much as a full extension like Soft Gel or Acrylics."),
            ("How long does the appointment take?", "Between 120 and 150 minutes."),
            ("How do I book my appointment?", "On WhatsApp at +52 984 310 8186, letting us know the service and your availability."),
        ],
        related=["Soft Gel / Gel X", "Acrylic / Polygel", "Gelish", "Mystic Pedicure"],
    ),
    dict(
        slug="softgel-gel-x-playa-del-carmen",
        service_name="Soft Gel / Gel X",
        service_name_short="Soft Gel / Gel X",
        service_type="Soft Gel / Gel X nail extensions",
        h1="Soft Gel / Gel X in Playa del Carmen",
        title="Soft Gel / Gel X in Playa del Carmen | Mystic Nails Art",
        description="Soft Gel / Gel X extensions in Playa del Carmen: instant length with a light, comfortable finish. Book your appointment on WhatsApp at Mystic Nails Art.",
        og_description="Lightweight, natural extensions. Ideal if you want instant length with a comfortable finish. Book on WhatsApp.",
        og_image="extensiones-french-minimalista-playa-del-carmen.webp",
        lead="Lightweight, natural extensions. Ideal if you want instant length with a comfortable finish, without the weight of a traditional acrylic extension.",
        wa_message="Hi, I'd like to book a Soft Gel / Gel X at Mystic Nails Art",
        benefits=[
            ("Lightweight", "much lighter than a traditional acrylic extension"),
            ("Instant length", "results right away, no waiting for natural growth"),
            ("Duration", "120–150 minutes of application"),
            ("Ideal for", "anyone looking for comfort and a natural finish with length"),
        ],
        compare_title="Soft Gel / Gel X vs. other extensions",
        compare_rows=COMPARE_ROWS_EXTENSIONS,
        faq=[
            ("What's the difference between Soft Gel/Gel X and acrylics?", "Soft Gel/Gel X is lighter and more comfortable, ideal for a natural finish. Acrylics offer more structure for elaborate designs or longer lengths."),
            ("Does the application hurt?", "No, it's a painless process that adapts to the natural shape of your nail."),
            ("How long does the appointment take?", "Between 120 and 150 minutes."),
            ("How do I book my appointment?", "On WhatsApp at +52 984 310 8186, letting us know the service and your availability."),
        ],
        related=["Kapping", "Acrylic / Polygel", "Gelish", "Mystic Pedicure"],
    ),
    dict(
        slug="acrilicas-polygel-playa-del-carmen",
        service_name="Acrylic / Polygel",
        service_name_short="Acrylic / Polygel",
        service_type="Acrylic or Polygel nail extensions",
        h1="Acrylic / Polygel in Playa del Carmen",
        title="Acrylic / Polygel in Playa del Carmen | Mystic Nails Art",
        description="Acrylic or Polygel extensions in Playa del Carmen: strength, length and elaborate designs. Book your appointment on WhatsApp at Mystic Nails Art.",
        og_description="Strong extensions for more structure, length and more elaborate designs. Book on WhatsApp.",
        og_image="unas-doradas-elegantes-diseno-hoja-playa-del-carmen.webp",
        lead="Strong extensions for more structure, length and more elaborate designs — the ideal choice if you want detailed nail art or longer nails.",
        wa_message="Hi, I'd like to book Acrylic / Polygel at Mystic Nails Art",
        benefits=[
            ("Strength", "the most durable option for longer lengths"),
            ("Structure", "supports 3D designs, rhinestones and elaborate nail art"),
            ("Duration", "150–180 minutes of application"),
            ("Ideal for", "anyone who wants eye-catching designs and more length"),
        ],
        compare_title="Acrylic / Polygel vs. other extensions",
        compare_rows=COMPARE_ROWS_EXTENSIONS,
        faq=[
            ("Do acrylics damage the natural nail?", "If applied and removed correctly by professionals, they don't damage the nail. Careful removal is key."),
            ("Can I get 3D designs or rhinestones?", "Yes, it's the technique that best supports elaborate nail art, rhinestones and 3D designs."),
            ("How long does the appointment take?", "Between 150 and 180 minutes."),
            ("How do I book my appointment?", "On WhatsApp at +52 984 310 8186, letting us know the service and your availability."),
        ],
        related=["Soft Gel / Gel X", "Kapping", "Gelish", "Mystic Pedicure"],
    ),
    dict(
        slug="esmaltado-express-playa-del-carmen",
        service_name="Express Polish",
        service_name_short="Express Polish",
        service_type="Express polish on toes",
        h1="Express Polish in Playa del Carmen",
        title="Express Polish in Playa del Carmen | Mystic Nails Art",
        description="Express Polish on toes in Playa del Carmen: clean finish in 20-30 minutes. Book your appointment on WhatsApp at Mystic Nails Art.",
        og_description="Quick polish on toes with a clean finish: one color or French. Book on WhatsApp.",
        og_image="manicure-ombre-french-almendra-playa-del-carmen.webp",
        lead="Quick polish on toes with a clean finish: one color or French — perfect when you're short on time but want your feet sandal-ready.",
        wa_message="Hi, I'd like to book Express Polish at Mystic Nails Art",
        benefits=[
            ("Speed", "just 20–30 minutes, ideal for tight schedules"),
            ("Clean finish", "solid color or well-defined French"),
            ("Affordable", "a lighter option when you don't need a full treatment"),
            ("Ideal for", "quick touch-ups between full pedicures"),
        ],
        compare_title="Express Polish vs. other foot services",
        compare_rows=COMPARE_ROWS_FEET,
        faq=[
            ("Does Express Polish include foot care?", "It's a service focused only on polish, without the full cuticle care and exfoliation of a pedicure."),
            ("How long does it take?", "Between 20 and 30 minutes."),
            ("Can I get French?", "Yes, you can choose solid color or French."),
            ("How do I book my appointment?", "On WhatsApp at +52 984 310 8186, letting us know the service and your availability."),
        ],
        related=["Russian Pedicure", "Mystic Pedicure", "Gelish"],
    ),
    dict(
        slug="pedicure-ruso-playa-del-carmen",
        service_name="Russian Pedicure",
        service_name_short="Russian Pedicure",
        service_type="Russian pedicure technique",
        h1="Russian Pedicure in Playa del Carmen",
        title="Russian Pedicure in Playa del Carmen | Mystic Nails Art",
        description="Russian Pedicure in Playa del Carmen: deep dry cleaning, ideal for cuticles and a precise finish. Book on WhatsApp at Mystic Nails Art.",
        og_description="Deep dry cleaning, ideal for cuticles and a more precise finish. Book on WhatsApp.",
        og_image="unas-blancas-azul-petroleo-floral-playa-del-carmen.webp",
        lead="Deep dry cleaning, ideal for cuticles and a more precise finish — the Russian technique focuses on long-lasting, highly detailed results.",
        wa_message="Hi, I'd like to book a Russian Pedicure at Mystic Nails Art",
        benefits=[
            ("Precision", "dry technique that allows a very detailed finish"),
            ("Longer-lasting result", "cuticles stay tidier for longer"),
            ("Appointment length", "60–90 minutes"),
            ("Ideal for", "anyone who wants a technical, long-lasting pedicure"),
        ],
        compare_title="Russian Pedicure vs. other foot services",
        compare_rows=COMPARE_ROWS_FEET,
        faq=[
            ("What makes Russian Pedicure different?", "It uses a dry technique (no soaking) that allows more precision on cuticles and calluses."),
            ("Is it painful?", "No, it's a professional, safe procedure done with specialized tools."),
            ("How long does the appointment take?", "Between 60 and 90 minutes."),
            ("How do I book my appointment?", "On WhatsApp at +52 984 310 8186, letting us know the service and your availability."),
        ],
        related=["Mystic Pedicure", "Express Polish", "Gelish"],
    ),
    dict(
        slug="pedicure-mistico-playa-del-carmen",
        service_name="Mystic Pedicure",
        service_name_short="Mystic Pedicure",
        service_type="Full spa pedicure",
        h1="Mystic Pedicure in Playa del Carmen",
        title="Mystic Pedicure in Playa del Carmen | Mystic Nails Art",
        description="Mystic Pedicure in Playa del Carmen: full spa experience with exfoliation, hydration and Gelish included. Book on WhatsApp.",
        og_description="Complete foot experience: exfoliation, hydration, deep care and Gelish included. Book on WhatsApp.",
        og_image="nail-art-tematico-frutas-playa-del-carmen.webp",
        lead="Complete foot experience: exfoliation, hydration, deep care and Gelish included — the most complete treatment to pamper your feet.",
        wa_message="Hi, I'd like to book a Mystic Pedicure at Mystic Nails Art",
        benefits=[
            ("All-inclusive", "exfoliation, hydration, deep care and Gelish in a single appointment"),
            ("Spa experience", "designed as a complete moment of relaxation"),
            ("Duration", "2 hours 30 minutes"),
            ("Ideal for", "special occasions or whenever you want to fully treat yourself"),
        ],
        compare_title="Mystic Pedicure vs. other foot services",
        compare_rows=COMPARE_ROWS_FEET,
        faq=[
            ("What's included in the Mystic Pedicure?", "Exfoliation, hydration, deep cuticle and callus care, and Gelish included in the service price."),
            ("How long does the appointment take?", "About 2 hours 30 minutes."),
            ("Is it a good choice for special occasions?", "Yes, it's our most complete treatment, ideal before an event or as a moment of relaxation."),
            ("How do I book my appointment?", "On WhatsApp at +52 984 310 8186, letting us know the service and your availability."),
        ],
        related=["Russian Pedicure", "Express Polish", "Gelish"],
    ),
]

for p in PAGES:
    faq_schema, faq_html = faq_block(p["faq"])
    html = TEMPLATE.format(
        title=p["title"],
        description=p["description"],
        og_description=p["og_description"],
        slug=p["slug"],
        og_image=p["og_image"],
        service_name=p["service_name"],
        service_type=p["service_type"],
        h1=p["h1"],
        lead=p["lead"],
        wa_text=quote(p["wa_message"]),
        service_name_short=p["service_name_short"],
        benefits=benefits_block(p["benefits"]),
        compare_title=p["compare_title"],
        compare_rows=compare_rows_block(p["compare_rows"]),
        faq_schema=faq_schema,
        faq_html=faq_html,
        related=related_block(p["related"]),
    )
    outdir = p["slug"]
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    os.makedirs("md", exist_ok=True)
    with open(os.path.join("md", p["slug"] + ".md"), "w", encoding="utf-8") as f:
        f.write(render_markdown(p))
    print("Generated:", outdir, "+ md/" + p["slug"] + ".md")
