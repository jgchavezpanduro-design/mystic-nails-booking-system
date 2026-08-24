#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates blog/guide article pages, reusing the service-page design system."""
import os

TEMPLATE = '''<!DOCTYPE html>
<html lang="es-MX">
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
    {{ "@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://mysticnailsart.com/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Guía", "item": "https://mysticnailsart.com/#servicios-playa-del-carmen" }},
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
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400;6..96,600;6..96,700&family=Playfair+Display:wght@400;600;700&family=DM+Sans:wght@300;400;500;600;700&family=Big+Shoulders+Display:wght@400;600;700;800;900&display=swap" rel="stylesheet">

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
    background:var(--mn-bg); color:var(--mn-txt); font-family:'Big Shoulders Display',sans-serif; font-weight:300; line-height:1.6;
  }}
  h1, h2, h3 {{ font-family:'Big Shoulders Display',sans-serif; font-weight:600; line-height:1.15; }}
  a {{ color:var(--mn-pri); }}
  .wrap {{ max-width:800px; margin:0 auto; padding:0 24px; }}
  nav {{ padding:22px 0; border-bottom:1px solid var(--mn-bdr); }}
  nav .wrap {{ display:flex; justify-content:space-between; align-items:center; }}
  .brand {{ font-family:'Big Shoulders Display',sans-serif; font-size:22px; font-weight:600; background:linear-gradient(135deg,var(--mn-ga),var(--mn-gb)); -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; text-decoration:none; }}
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
  .faq-item h3 {{ font-size:17px; font-weight:600; margin-bottom:8px; color:var(--mn-txt); font-family:'Big Shoulders Display',sans-serif; }}
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
    <a class="back-link" href="https://mysticnailsart.com/">&larr; Volver al inicio</a>
  </div>
</nav>

<main>
  <div class="wrap">
    <p class="breadcrumb"><a href="https://mysticnailsart.com/">Inicio</a> / <a href="https://mysticnailsart.com/#servicios-playa-del-carmen">Gu&iacute;a</a> / {h1}</p>

    <p class="kicker">Gu&iacute;a Mystic Nails Art</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>

    <div class="cta-row">
      <a class="btn-primary" href="https://wa.me/529843108186?text={wa_text}" target="_blank" rel="noopener">Cotizar por WhatsApp</a>
      <a class="btn-secondary" href="https://mysticnailsart.com/#precios">Ver precios</a>
    </div>

{body_sections}

    <section>
      <h2>Preguntas frecuentes</h2>
{faq_html}
    </section>

    <section>
      <h2>Explora otros servicios</h2>
      <div class="related">
{related}
      </div>
    </section>
  </div>
</main>

<footer>
  <div class="wrap">
    <div>Mystic Nails Art &mdash; Calle 38 Nte Lote 73, Tohoku, Centro, Playa del Carmen, Q.R. \U0001f1f2\U0001f1fd</div>
    <div><a href="https://wa.me/529843108186" target="_blank" rel="noopener">+52 984 310 8186</a> &middot; Lun&ndash;Dom 09:00&ndash;20:00</div>
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
    "Softgel / Gel X": "softgel-gel-x-playa-del-carmen",
    "Acrílicas / Polygel": "acrilicas-polygel-playa-del-carmen",
    "Esmaltado Express": "esmaltado-express-playa-del-carmen",
    "Pedicure Ruso": "pedicure-ruso-playa-del-carmen",
    "Pedicure Místico": "pedicure-mistico-playa-del-carmen",
}

def related_block(items):
    return '\n'.join('        <a href="https://mysticnailsart.com/{slug}/">{name}</a>'.format(slug=NAME_TO_SLUG[n], name=n) for n in items) + \
           '\n        <a href="https://mysticnailsart.com/#gallery">Ver galería de diseños</a>'

GUIDES = []

# ---------------------------------------------------------------- Article 1
GUIDES.append(dict(
    slug="gelish-acrilico-polygel-diferencias-playa-del-carmen",
    title="Gelish vs. Acrílico vs. Polygel: ¿cuál elegir? | Mystic Nails Art",
    description="Comparamos Gelish, Rubber Base, Acrílico y Polygel: duración, resistencia y precio desde, para que elijas la técnica ideal en Playa del Carmen.",
    og_description="Comparativa completa de técnicas de uñas: Gelish, Rubber Base, Acrílico y Polygel. Duración, resistencia y precio.",
    og_image="gelish-rosa-diseno-playa-del-carmen.webp",
    date_published="2026-08-22",
    h1="Gelish vs. Acrílico vs. Polygel: ¿cuál elegir?",
    lead="Las cuatro técnicas más pedidas en Mystic Nails Art explicadas en simple: qué hace cada una, cuánto dura y para quién es ideal.",
    wa_text="Hola%2C%20le%C3%AD%20la%20gu%C3%ADa%20de%20t%C3%A9cnicas%20y%20quiero%20que%20me%20recomienden%20cu%C3%A1l%20me%20conviene",
    body_sections=[
        section("Qué es cada técnica", paragraphs=[
            "<strong>Gelish</strong> es un esmaltado en gel que se cura con lámpara UV/LED sobre tu uña natural. No agrega estructura ni largo, solo color y brillo de larga duración.",
            "<strong>Rubber Base</strong> es una base flexible que refuerza uñas débiles o delgadas antes de aplicar color, ayudando a nivelar y proteger sin perder flexibilidad natural.",
            "<strong>Acrílico</strong> es un sistema de polvo y líquido que se esculpe sobre la uña para dar largo, forma y estructura muy resistente; es la opción clásica para extensiones duraderas.",
            "<strong>Polygel</strong> combina lo mejor de gel y acrílico: se moldea como el acrílico pero cura con lámpara como el gel, dando un acabado más liviano y natural para kapping o extensiones."
        ]),
        section("Comparativa rápida", table_headers=["Técnica", "Duración", "Ideal para", "Precio desde"], table_rows=[
            ["Gelish", "3+ semanas", "Color y brillo en uña natural", "$430 MXN"],
            ["Rubber Base", "3+ semanas", "Uñas débiles o delgadas", "$500 MXN"],
            ["Acrílicas / Polygel", "3-4 semanas", "Largo y estructura resistente", "$740 MXN"],
            ["Kapping (Polygel)", "3+ semanas", "Reforzar sin hacer extensión", "$640 MXN"],
        ]),
        section("¿Cuál te conviene?", paragraphs=[
            "Si solo quieres color parejo y brillante en tu uña natural, <strong>Gelish</strong> es la opción más rápida y económica.",
            "Si tus uñas se rompen o doblan fácil, empieza con <strong>Rubber Base</strong> antes de pensar en extensiones.",
            "Si quieres más largo y una estructura que aguante el día a día, <strong>Acrílico o Polygel</strong> son la mejor inversión.",
            "Ante la duda, mandános una foto de referencia por WhatsApp y te decimos exactamente qué técnica y precio te conviene."
        ]),
    ],
    faq=[
        ("¿Puedo combinar técnicas, por ejemplo Rubber Base con diseño?", "Sí. Rubber Base admite el mismo nivel de diseño y nail art que el Gelish tradicional; solo cambia la base que se usa antes del color."),
        ("¿Cuál técnica es menos dañina para la uña natural?", "Gelish y Rubber Base son las más respetuosas con la uña natural. Acrílico y Polygel requieren más cuidado en el retiro para no debilitar la uña."),
        ("¿Cuánto cuesta cambiar de una técnica a otra?", "El retiro de un servicio anterior tiene un costo aparte, ya sea que vengas de Mystic Nails Art o de otro salón. Pregúntanos por WhatsApp con tu caso específico."),
    ],
    related=["Gelish", "Rubber Base", "Acrílicas / Polygel", "Kapping"],
))

# ---------------------------------------------------------------- Article 2
GUIDES.append(dict(
    slug="cuanto-dura-gelish-acrilico-rubber-base-playa-del-carmen",
    title="Cuánto dura cada técnica de uñas (guía completa) | Mystic Nails Art",
    description="Cuánto dura el Gelish, Rubber Base, Acrílico y Polygel, qué factores afectan la duración y cómo alargarla. Guía de Mystic Nails Art, Playa del Carmen.",
    og_description="Guía de duración por técnica de uñas y tips para que tu manicure dure más tiempo.",
    og_image="gelish-rubber-base-natural-playa-del-carmen.webp",
    date_published="2026-08-22",
    h1="Cuánto dura cada técnica de uñas",
    lead="La duración real de Gelish, Rubber Base, Acrílico y Polygel, y qué puedes hacer para que tu manicure aguante más.",
    wa_text="Hola%2C%20quiero%20saber%20cu%C3%A1nto%20me%20dura%20cada%20t%C3%A9cnica%20de%20u%C3%B1as",
    body_sections=[
        section("Duración por técnica", list_items=[
            ("Gelish", "Más de 3 semanas con brillo intacto sobre uña natural."),
            ("Rubber Base", "3+ semanas, con la ventaja de que refuerza la uña mientras dura."),
            ("Acrílicas / Polygel", "3 a 4 semanas antes de necesitar retoque de crecimiento."),
            ("Kapping (Polygel)", "3+ semanas, similar al Gelish pero con más resistencia."),
            ("Esmaltado Express", "5 a 10 días, al ser esmalte tradicional sin curado UV."),
        ]),
        section("Qué hace que dure menos", paragraphs=[
            "El contacto constante con agua de mar, cloro de alberca y protector solar puede acelerar el desgaste de cualquier técnica.",
            "Usar las uñas como herramienta (abrir latas, rascar) es la causa más común de que se levante o rompa antes de tiempo.",
            "Una aplicación mal sellada en los bordes (sin cap sellante) deja entrar humedad y acorta la duración."
        ]),
        section("Cómo alargar la duración", list_items=[
            ("Hidrata la cutícula", "Un aceite de cutícula a diario evita que el gel se levante en los bordes."),
            ("Usa guantes", "Para lavar trastes o limpiar, protege tus uñas de químicos y agua caliente."),
            ("Evita quitar el esmalte tirando", "Despegar el gel a la fuerza daña la uña natural y arruina el trabajo antes de tiempo."),
        ]),
    ],
    faq=[
        ("¿Puedo bañarme en el mar con Gelish o Acrílico recién hecho?", "Sí, pero espera al menos 2 horas después de tu cita para que cure por completo, y aplica protector de uñas o aceite después de nadar."),
        ("¿Qué técnica aguanta mejor el clima de Playa del Carmen?", "Rubber Base y Kapping suelen tener mejor comportamiento con calor y humedad porque son más flexibles que el acrílico tradicional."),
        ("¿Cada cuánto debo hacerme mantenimiento?", "Recomendamos retoque cada 3 semanas para extensiones y Rubber Base, y cada 3-4 semanas para Gelish, según qué tan rápido te crece la uña."),
    ],
    related=["Gelish", "Rubber Base", "Acrílicas / Polygel", "Esmaltado Express"],
))

# ---------------------------------------------------------------- Article 3
GUIDES.append(dict(
    slug="cuidado-unas-gel-playa-del-carmen",
    title="Cómo cuidar tus uñas con gel en la playa | Mystic Nails Art",
    description="Guía para cuidar tus uñas con gel, acílico o polygel en Playa del Carmen: sol, agua de mar, cloro y protector solar sin arruinar tu manicure.",
    og_description="Tips para que tu manicure sobreviva al sol, mar y cloro de Playa del Carmen.",
    og_image="manicure-ombre-french-almendra-playa-del-carmen.webp",
    date_published="2026-08-22",
    h1="Cómo cuidar tus uñas con gel en la playa",
    lead="Vivir o vacacionar en Playa del Carmen expone tus uñas a sol, sal y cloro todos los días. Así las cuidas sin sacrificar tu manicure.",
    wa_text="Hola%2C%20quiero%20unas%20que%20aguanten%20bien%20el%20clima%20de%20playa",
    body_sections=[
        section("Por qué el clima de playa afecta tus uñas", paragraphs=[
            "El sol directo reseca la cutícula y puede opacar el brillo del gel con el tiempo.",
            "El agua de mar y el cloro de alberca son abrasivos: debilitan poco a poco cualquier esmaltado, incluido el semipermanente.",
            "El protector solar en manos, si no se retira bien, deja una película que hace que el esmalte se vea opaco o se despegue antes."
        ]),
        section("Tips prácticos para cuidarlas", list_items=[
            ("Aplica aceite de cutícula", "Todos los días, especialmente después de nadar o tomar el sol."),
            ("Enjuaga tus manos tras el mar o alberca", "El agua dulce quita el exceso de sal y cloro que reseca la uña."),
            ("Usa protector solar en manos con cuidado", "Aplica en el dorso de la mano, evitando que se acumule justo en el borde de la uña."),
            ("Seca bien tus manos", "La humedad atrapada bajo el esmalte favorece que se despegue o cambie de color."),
        ]),
        section("Qué técnica recomendamos para turistas y locales activos", paragraphs=[
            "Si vas a estar mucho tiempo en el mar o alberca, <strong>Gelish</strong> o <strong>Rubber Base</strong> son más fáciles de mantener que las extensiones largas.",
            "Si quieres extensiones para tu viaje, prioriza un largo corto o medio: aguanta mejor el uso diario en la playa que un largo extremo."
        ]),
    ],
    faq=[
        ("¿Puedo hacerme las uñas un día antes de viajar a la playa?", "Sí, de hecho lo recomendamos: dale al menos 24 horas para que cure completamente antes de exponerlas al mar."),
        ("¿El cloro decolora el Gelish?", "Puede opacar el brillo con exposición prolongada y frecuente. Enjuagar tus manos después de la alberca ayuda a minimizar el efecto."),
        ("¿Qué hago si se me levanta una uña en pleno viaje?", "Escríbenos por WhatsApp; si estás en Playa del Carmen podemos agendarte un ajuste rápido antes de que se rompa más."),
    ],
    related=["Gelish", "Rubber Base", "Kapping", "Pedicure Místico"],
))

# ---------------------------------------------------------------- Article 4
GUIDES.append(dict(
    slug="precios-unas-playa-del-carmen",
    title="Cuánto cuesta hacerse las uñas en Playa del Carmen (guía de precios) | Mystic Nails Art",
    description="Precios reales de Gelish, Rubber Base, Acrílico, Polygel y pedicure en Playa del Carmen. Guía de precios 2026 de Mystic Nails Art.",
    og_description="Guía de precios de uñas en Playa del Carmen: Gelish, Rubber Base, extensiones y pedicure.",
    og_image="unas-doradas-elegantes-diseno-hoja-playa-del-carmen.webp",
    date_published="2026-08-22",
    h1="Cuánto cuesta hacerse las uñas en Playa del Carmen",
    lead="Precios reales, desde los más básicos hasta las extensiones más elaboradas, para que cotices tu cita sin sorpresas.",
    wa_text="Hola%2C%20vi%20la%20gu%C3%ADa%20de%20precios%20y%20quiero%20cotizar%20mi%20cita",
    body_sections=[
        section("Precios por técnica", table_headers=["Servicio", "Desde"], table_rows=[
            ["Gelish", "$430 MXN"],
            ["Rubber Base", "$500 MXN"],
            ["Builder Gel", "$520 MXN"],
            ["Kapping (Polygel)", "$640 MXN"],
            ["Softgel / Gel X", "$600 MXN"],
            ["Acrílicas / Polygel", "$740 MXN"],
            ["Esmaltado Express (pies)", "$200 MXN"],
            ["Pedicure Ruso", "$300 MXN"],
            ["Pedicure Místico", "$500 MXN"],
        ]),
        section("Qué hace que el precio suba o baje", list_items=[
            ("Nivel de diseño", "Un color liso cuesta menos que nail art elaborado, 3D o pedrería."),
            ("Largo de la extensión", "A mayor largo, mayor cantidad de material y tiempo de trabajo."),
            ("Retiro de servicio anterior", "Si vienes con uñas de otro salón o de Mystic Nails Art, el retiro se cotiza aparte."),
        ]),
        section("Cómo cotizar tu precio exacto", paragraphs=[
            "Los precios de esta guía son el punto de partida (“desde”); el precio final depende de diseño, largo y estado de tu uña natural.",
            "La forma más rápida de saber tu precio exacto es mandarnos una foto de referencia por WhatsApp: te respondemos con el costo antes de que agendes."
        ]),
    ],
    faq=[
        ("¿Los precios incluyen retiro de otro salón?", "No, el retiro se cotiza aparte y varía según la técnica que traigas puesta."),
        ("¿Manejan paquetes de manos y pies?", "Sí, pregunta por WhatsApp por combos de manicure y pedicure el mismo día."),
        ("¿Aceptan pagos con tarjeta?", "Sí, aceptamos efectivo y tarjeta."),
    ],
    related=["Gelish", "Rubber Base", "Acrílicas / Polygel", "Pedicure Místico"],
))

# ---------------------------------------------------------------- Article 5
GUIDES.append(dict(
    slug="unas-para-boda-evento-playa-del-carmen",
    title="Uñas para boda o evento en Playa del Carmen: qué elegir | Mystic Nails Art",
    description="Qué técnica y diseño de uñas elegir para tu boda o evento especial en Playa del Carmen, y cuándo agendar tu cita.",
    og_description="Guía de uñas para boda o evento: técnica, diseño y cuándo agendar en Playa del Carmen.",
    og_image="unas-3d-flores-rosa-holografico-playa-del-carmen.webp",
    date_published="2026-08-22",
    h1="Uñas para boda o evento: qué elegir",
    lead="Playa del Carmen es uno de los destinos de bodas favoritos de México. Esto es lo que recomendamos para que tus uñas luzcan perfectas todo el día.",
    wa_text="Hola%2C%20tengo%20una%20boda%2Fevento%20y%20quiero%20cotizar%20mis%20u%C3%B1as",
    body_sections=[
        section("Qué técnica dura más para el día del evento", paragraphs=[
            "Para bodas o eventos recomendamos <strong>Gelish o Rubber Base</strong> si quieres tu uña natural con acabado impecable, o <strong>Acrílico/Polygel</strong> si buscas más largo y presencia en las fotos.",
            "Ambas opciones aguantan un día completo de fotos, baile y actividades sin perder brillo ni forma."
        ]),
        section("Estilos más pedidos para eventos", list_items=[
            ("Francesita moderna", "Clásica, elegante y combina con cualquier vestido."),
            ("Nude con brillo sutil", "Discreta pero luminosa en fotos, ideal para novias."),
            ("Diseño con pedrería puntual", "Un detalle de pedrería o línea dorada da un toque especial sin saturar."),
        ]),
        section("Cuándo agendar antes del evento", paragraphs=[
            "Lo ideal es agendar entre 1 y 3 días antes del evento: suficiente tiempo para que cure bien, pero sin riesgo de crecimiento notorio.",
            "Si tu evento requiere prueba de diseño (por ejemplo bodas), podemos agendar una prueba previa por separado.",
            "En temporada alta de bodas, te recomendamos reservar tu fecha con anticipación por WhatsApp para asegurar tu horario."
        ]),
    ],
    faq=[
        ("¿Puedo llevar una foto de referencia de mi vestido para elegir color?", "Sí, mandánosla por WhatsApp junto con la fecha de tu evento y te ayudamos a elegir el tono ideal."),
        ("¿Hacen diseños para todo el cortejo de una boda?", "Sí, podemos coordinar citas para varias personas el mismo día; escríbenos con el número de personas y fecha."),
        ("¿Cuánto tiempo antes debo reservar en temporada alta?", "Recomendamos reservar con 2 a 3 semanas de anticipación en temporada alta de bodas para asegurar tu horario."),
    ],
    related=["Gelish", "Rubber Base", "Acrílicas / Polygel", "Pedicure Místico"],
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
        wa_text=g["wa_text"],
        body_sections="\n".join(g["body_sections"]),
        faq_schema=faq_schema,
        faq_html=faq_html,
        related=related_block(g["related"]),
    )
    outdir = os.path.join("guia", g["slug"])
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated:", outdir)
