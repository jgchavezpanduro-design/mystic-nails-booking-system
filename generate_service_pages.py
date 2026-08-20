#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the 8 remaining service landing pages from the Gelish template pattern."""
import os

TEMPLATE = '''<!DOCTYPE html>
<html lang="es-MX">
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
  "areaServed": "Playa del Carmen, Quintana Roo, México",
  "url": "https://mysticnailsart.com/{slug}/"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://mysticnailsart.com/" }},
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
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400;6..96,600;6..96,700&family=Playfair+Display:wght@400;600;700&family=DM+Sans:wght@300;400;500;600;700&family=Bebas+Neue&display=swap" rel="stylesheet">

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
    --mn-bg:#0d0a1a; --mn-card:#1d1930; --mn-bdr:rgba(255,255,255,0.09);
    --mn-pri:#b06be0; --mn-pdim:rgba(176,107,224,0.15); --mn-txt:#ede7f8; --mn-mut:#9b8fb0;
    --mn-ga:#7b3fbf; --mn-gb:#c060a0; --mn-foot:#080613;
    background:var(--mn-bg); color:var(--mn-txt); font-family:'Bebas Neue',sans-serif; font-weight:300; line-height:1.6;
  }}
  h1, h2, h3 {{ font-family:'Bebas Neue',sans-serif; font-weight:600; line-height:1.15; }}
  a {{ color:var(--mn-pri); }}
  .wrap {{ max-width:800px; margin:0 auto; padding:0 24px; }}
  nav {{ padding:22px 0; border-bottom:1px solid var(--mn-bdr); }}
  nav .wrap {{ display:flex; justify-content:space-between; align-items:center; }}
  .brand {{ font-family:'Bebas Neue',sans-serif; font-size:22px; font-weight:600; background:linear-gradient(135deg,var(--mn-ga),var(--mn-gb)); -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; text-decoration:none; }}
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
  .faq-item h3 {{ font-size:17px; font-weight:600; margin-bottom:8px; color:var(--mn-txt); font-family:'Bebas Neue',sans-serif; }}
  .faq-item p {{ font-size:15px; color:var(--mn-mut); }}
  .related {{ display:flex; gap:10px; flex-wrap:wrap; }}
  .related a {{ border:1px solid var(--mn-bdr); border-radius:50px; padding:9px 18px; font-size:14px; text-decoration:none; color:var(--mn-txt); }}
  .related a:hover {{ border-color:var(--mn-pri); color:var(--mn-pri); }}
  footer {{ background:var(--mn-foot); color:rgba(255,255,255,0.5); padding:40px 0; margin-top:40px; }}
  footer .wrap {{ display:flex; justify-content:space-between; flex-wrap:wrap; gap:16px; font-size:13px; }}
  footer a {{ color:rgba(255,255,255,0.6); }}
</style>
</head>
<body data-theme="dark">

<nav>
  <div class="wrap">
    <a class="brand" href="https://mysticnailsart.com/">Mystic Nails Art</a>
    <a class="back-link" href="https://mysticnailsart.com/">&larr; Volver al inicio</a>
  </div>
</nav>

<main>
  <div class="wrap">
    <p class="breadcrumb"><a href="https://mysticnailsart.com/">Inicio</a> / {h1}</p>

    <h1>{h1} 🇲🇽</h1>
    <p class="lead">{lead}</p>

    <div class="cta-row">
      <a class="btn-primary" href="https://wa.me/529843108186?text={wa_text}" target="_blank" rel="noopener">Reservar por WhatsApp</a>
      <a class="btn-secondary" href="https://mysticnailsart.com/#services">Ver todos los servicios</a>
    </div>

    <section>
      <h2>&iquest;Por qu&eacute; elegir {service_name_short}?</h2>
      <ul class="benefits">
{benefits}
      </ul>
    </section>

    <section>
      <h2>{compare_title}</h2>
      <table>
        <thead><tr><th>T&eacute;cnica</th><th>Ideal para</th></tr></thead>
        <tbody>
{compare_rows}
        </tbody>
      </table>
    </section>

    <section>
      <h2>Preguntas frecuentes sobre {service_name_short}</h2>
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
    <div>Mystic Nails Art &mdash; Calle 38 Nte Lote 73, Tohoku, Centro, Playa del Carmen, Q.R. 🇲🇽</div>
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

def benefits_block(items):
    return '\n'.join('        <li><strong>{label}:</strong> {text}</li>'.format(label=l, text=t) for l, t in items)

def compare_rows_block(rows):
    return '\n'.join('          <tr><td>{name}</td><td>{desc}</td></tr>'.format(name=n, desc=d) for n, d in rows)

def related_block(items):
    return '\n'.join('        <a href="https://mysticnailsart.com/#services">{name}</a>'.format(name=n) for n in items) + \
           '\n        <a href="https://mysticnailsart.com/#gallery">Ver galería de diseños</a>'

PAGES = [
    dict(
        slug="rubber-base-playa-del-carmen",
        service_name="Rubber Base",
        service_name_short="Rubber Base",
        service_type="Refuerzo de uñas con Rubber Base",
        h1="Rubber Base en Playa del Carmen",
        title="Rubber Base en Playa del Carmen | Mystic Nails Art",
        description="Rubber Base en Playa del Carmen: refuerzo flexible para uñas débiles o delgadas, con acabado natural. Reserva por WhatsApp en Mystic Nails Art.",
        og_description="Refuerzo flexible para proteger, nivelar y fortalecer uñas débiles o delgadas. Reserva por WhatsApp.",
        og_image="gelish-rubber-base-natural-playa-del-carmen.webp",
        lead="Refuerzo flexible para proteger, nivelar y fortalecer uñas débiles o delgadas, con un acabado natural que cuida tu uña propia mientras la protege.",
        wa_text="Hola%2C%20quiero%20reservar%20un%20Rubber%20Base%20en%20Mystic%20Nails%20Art",
        benefits=[
            ("Refuerzo", "protege uñas débiles o delgadas sin perder flexibilidad"),
            ("Acabado natural", "más discreto que una extensión, ideal para mantener el largo propio"),
            ("Duración", "60–90 minutos de aplicación"),
            ("Ideal para", "quienes se muerden las uñas o tienen uñas quebradizas"),
        ],
        compare_title="Rubber Base vs. otras técnicas",
        compare_rows=[
            ("Gelish", "Uñas naturales con brillo y color, resultado de más de 3 semanas"),
            ("Rubber Base", "Uñas débiles que necesitan refuerzo con acabado natural"),
            ("Builder Gel", "Fortalecer y dar estructura a la uña natural"),
        ],
        faq=[
            ("¿Para quién es el Rubber Base?", "Para personas con uñas débiles, delgadas o que se muerden las uñas y buscan un refuerzo flexible y natural."),
            ("¿En qué se diferencia del Gelish?", "El Gelish es un esmaltado enfocado en color y brillo. El Rubber Base es un refuerzo estructural pensado para proteger uñas frágiles."),
            ("¿Cuánto dura la aplicación?", "Entre 60 y 90 minutos, dependiendo del estado de la uña."),
            ("¿Cómo reservo mi cita?", "Por WhatsApp al +52 984 310 8186, indicando el servicio y tu disponibilidad."),
        ],
        related=["Gelish", "Builder Gel", "Extensiones (Softgel / Gel X)", "Pedicure"],
    ),
    dict(
        slug="builder-gel-playa-del-carmen",
        service_name="Builder Gel",
        service_name_short="Builder Gel",
        service_type="Estructura de uñas con Builder Gel",
        h1="Builder Gel en Playa del Carmen",
        title="Builder Gel en Playa del Carmen | Mystic Nails Art",
        description="Builder Gel en Playa del Carmen: estructura y resistencia para uñas naturales que necesitan más soporte. Reserva por WhatsApp en Mystic Nails Art.",
        og_description="Estructura y resistencia para uñas naturales que necesitan más soporte. Reserva por WhatsApp.",
        og_image="gelish-rubber-base-natural-playa-del-carmen.webp",
        lead="Estructura y resistencia para uñas naturales que necesitan más soporte, ideal si buscas fortalecer tu uña sin recurrir a una extensión completa.",
        wa_text="Hola%2C%20quiero%20reservar%20un%20Builder%20Gel%20en%20Mystic%20Nails%20Art",
        benefits=[
            ("Soporte", "más estructura que el Rubber Base para uñas que necesitan refuerzo extra"),
            ("Resistencia", "ideal si tus uñas se rompen o doblan con facilidad"),
            ("Duración", "90–120 minutos de aplicación"),
            ("Ideal para", "quienes quieren fortalecer la uña natural sin extensión"),
        ],
        compare_title="Builder Gel vs. otras técnicas",
        compare_rows=[
            ("Gelish", "Uñas naturales con brillo y color, resultado de más de 3 semanas"),
            ("Rubber Base", "Uñas débiles que necesitan refuerzo con acabado natural"),
            ("Builder Gel", "Fortalecer y dar estructura a la uña natural"),
        ],
        faq=[
            ("¿Qué diferencia hay entre Builder Gel y Rubber Base?", "El Builder Gel da más estructura y soporte, mientras que el Rubber Base es más flexible y natural. Ambos refuerzan la uña, pero con distinto nivel de firmeza."),
            ("¿El Builder Gel es una extensión?", "No, se aplica sobre la uña natural para darle más resistencia, no para alargarla."),
            ("¿Cuánto dura la cita?", "Entre 90 y 120 minutos."),
            ("¿Cómo reservo mi cita?", "Por WhatsApp al +52 984 310 8186, indicando el servicio y tu disponibilidad."),
        ],
        related=["Gelish", "Rubber Base", "Extensiones (Softgel / Gel X)", "Pedicure"],
    ),
    dict(
        slug="kapping-playa-del-carmen",
        service_name="Kapping de polygel o baño de acrílico",
        service_name_short="Kapping",
        service_type="Kapping (polygel o baño de acrílico)",
        h1="Kapping en Playa del Carmen",
        title="Kapping en Playa del Carmen | Mystic Nails Art",
        description="Kapping de polygel o baño de acrílico en Playa del Carmen: protección y durabilidad extra sobre tu uña natural. Reserva por WhatsApp.",
        og_description="Protección sobre uña natural con polygel o baño de acrílico para mayor durabilidad. Reserva por WhatsApp.",
        og_image="unas-doradas-3d-flores-perlas-playa-del-carmen.webp",
        lead="Protección sobre uña natural con polygel o baño de acrílico para mayor durabilidad, ideal si quieres un acabado resistente sin extender demasiado el largo.",
        wa_text="Hola%2C%20quiero%20reservar%20un%20Kapping%20en%20Mystic%20Nails%20Art",
        benefits=[
            ("Durabilidad", "mayor resistencia que un esmaltado tradicional"),
            ("Protección", "cubre y protege la uña natural de golpes y desgaste diario"),
            ("Duración", "120–150 minutos de aplicación"),
            ("Ideal para", "quienes quieren resistencia sin extensión larga"),
        ],
        compare_title="Kapping vs. otras extensiones",
        compare_rows=[
            ("Kapping", "Protección sobre uña natural con polygel o baño de acrílico, mayor durabilidad"),
            ("Softgel / Gel X", "Extensiones ligeras y naturales, largo inmediato y acabado cómodo"),
            ("Acrílicas / Polygel", "Extensiones resistentes para más estructura, largo y diseños elaborados"),
        ],
        faq=[
            ("¿Qué es el Kapping?", "Es una técnica que cubre la uña natural con polygel o baño de acrílico para darle mayor protección y durabilidad."),
            ("¿El Kapping alarga la uña?", "Aporta un poco de largo y estructura, pero no tanto como una extensión completa como Softgel o Acrílicas."),
            ("¿Cuánto dura la cita?", "Entre 120 y 150 minutos."),
            ("¿Cómo reservo mi cita?", "Por WhatsApp al +52 984 310 8186, indicando el servicio y tu disponibilidad."),
        ],
        related=["Softgel / Gel X", "Acrílicas / Polygel", "Gelish", "Pedicure"],
    ),
    dict(
        slug="softgel-gel-x-playa-del-carmen",
        service_name="Softgel / Gel X",
        service_name_short="Softgel / Gel X",
        service_type="Extensiones de uñas Softgel / Gel X",
        h1="Softgel / Gel X en Playa del Carmen",
        title="Softgel / Gel X en Playa del Carmen | Mystic Nails Art",
        description="Extensiones Softgel / Gel X en Playa del Carmen: largo inmediato con acabado ligero y cómodo. Reserva tu cita por WhatsApp en Mystic Nails Art.",
        og_description="Extensiones ligeras y naturales. Ideal si quieres largo inmediato con acabado cómodo. Reserva por WhatsApp.",
        og_image="extensiones-french-minimalista-playa-del-carmen.webp",
        lead="Extensiones ligeras y naturales. Ideal si quieres largo inmediato con un acabado cómodo, sin el peso de una extensión acrílica tradicional.",
        wa_text="Hola%2C%20quiero%20reservar%20un%20Softgel%20%2F%20Gel%20X%20en%20Mystic%20Nails%20Art",
        benefits=[
            ("Ligereza", "mucho más liviano que una extensión acrílica tradicional"),
            ("Largo inmediato", "resultado al instante sin esperar crecimiento natural"),
            ("Duración", "120–150 minutos de aplicación"),
            ("Ideal para", "quienes buscan comodidad y un acabado natural con largo"),
        ],
        compare_title="Softgel / Gel X vs. otras extensiones",
        compare_rows=[
            ("Kapping", "Protección sobre uña natural con polygel o baño de acrílico, mayor durabilidad"),
            ("Softgel / Gel X", "Extensiones ligeras y naturales, largo inmediato y acabado cómodo"),
            ("Acrílicas / Polygel", "Extensiones resistentes para más estructura, largo y diseños elaborados"),
        ],
        faq=[
            ("¿Qué diferencia hay entre Softgel/Gel X y acrílicas?", "El Softgel/Gel X es más ligero y cómodo, ideal para un acabado natural. Las acrílicas ofrecen más estructura para diseños elaborados o largos mayores."),
            ("¿Duele la aplicación?", "No, es un proceso indoloro que se adapta a la forma natural de tu uña."),
            ("¿Cuánto dura la cita?", "Entre 120 y 150 minutos."),
            ("¿Cómo reservo mi cita?", "Por WhatsApp al +52 984 310 8186, indicando el servicio y tu disponibilidad."),
        ],
        related=["Kapping", "Acrílicas / Polygel", "Gelish", "Pedicure"],
    ),
    dict(
        slug="acrilicas-polygel-playa-del-carmen",
        service_name="Acrílicas / Polygel",
        service_name_short="Acrílicas / Polygel",
        service_type="Extensiones de uñas acrílicas o Polygel",
        h1="Acrílicas / Polygel en Playa del Carmen",
        title="Acrílicas / Polygel en Playa del Carmen | Mystic Nails Art",
        description="Extensiones acrílicas o Polygel en Playa del Carmen: resistencia, largo y diseños elaborados. Reserva tu cita por WhatsApp en Mystic Nails Art.",
        og_description="Extensiones resistentes para mayor estructura, largo y diseños más elaborados. Reserva por WhatsApp.",
        og_image="unas-doradas-elegantes-diseno-hoja-playa-del-carmen.webp",
        lead="Extensiones resistentes para mayor estructura, largo y diseños más elaborados — la opción ideal si quieres nail art detallado o uñas más largas.",
        wa_text="Hola%2C%20quiero%20reservar%20Ac%C3%ADlicas%20%2F%20Polygel%20en%20Mystic%20Nails%20Art",
        benefits=[
            ("Resistencia", "la opción más duradera para largos mayores"),
            ("Estructura", "soporta diseños 3D, piedras y nail art elaborado"),
            ("Duración", "150–180 minutos de aplicación"),
            ("Ideal para", "quienes quieren diseños llamativos y mayor largo"),
        ],
        compare_title="Acrílicas / Polygel vs. otras extensiones",
        compare_rows=[
            ("Kapping", "Protección sobre uña natural con polygel o baño de acrílico, mayor durabilidad"),
            ("Softgel / Gel X", "Extensiones ligeras y naturales, largo inmediato y acabado cómodo"),
            ("Acrílicas / Polygel", "Extensiones resistentes para más estructura, largo y diseños elaborados"),
        ],
        faq=[
            ("¿Las acrílicas dañan la uña natural?", "Si se aplican y retiran correctamente por profesionales, no dañan la uña. El cuidado en el retiro es clave."),
            ("¿Puedo pedir diseños 3D o piedras?", "Sí, es la técnica que mejor soporta nail art elaborado, piedras y diseños 3D."),
            ("¿Cuánto dura la cita?", "Entre 150 y 180 minutos."),
            ("¿Cómo reservo mi cita?", "Por WhatsApp al +52 984 310 8186, indicando el servicio y tu disponibilidad."),
        ],
        related=["Softgel / Gel X", "Kapping", "Gelish", "Pedicure"],
    ),
    dict(
        slug="esmaltado-express-playa-del-carmen",
        service_name="Esmaltado Express",
        service_name_short="Esmaltado Express",
        service_type="Esmaltado express en pies",
        h1="Esmaltado Express en Playa del Carmen",
        title="Esmaltado Express en Playa del Carmen | Mystic Nails Art",
        description="Esmaltado Express en pies en Playa del Carmen: acabado limpio en 20-30 minutos. Reserva tu cita por WhatsApp en Mystic Nails Art.",
        og_description="Esmaltado rápido en pies con acabado limpio: 1 color o french. Reserva por WhatsApp.",
        og_image="manicure-ombre-french-almendra-playa-del-carmen.webp",
        lead="Esmaltado rápido en pies con acabado limpio: 1 color o french — perfecto cuando tienes poco tiempo pero quieres los pies listos para sandalias.",
        wa_text="Hola%2C%20quiero%20reservar%20Esmaltado%20Express%20en%20Mystic%20Nails%20Art",
        benefits=[
            ("Rapidez", "solo 20–30 minutos, ideal para agendas apretadas"),
            ("Acabado limpio", "color sólido o french bien definido"),
            ("Económico", "opción ligera cuando no necesitas tratamiento completo"),
            ("Ideal para", "mantenimiento rápido entre pedicures completos"),
        ],
        compare_title="Esmaltado Express vs. otros servicios de pies",
        compare_rows=[
            ("Esmaltado Express", "Esmaltado rápido en pies, 20-30 min, color sólido o french"),
            ("Pedicure Ruso", "Limpieza profunda en seco, ideal para cutícula y acabado preciso"),
            ("Pedicure Místico", "Experiencia completa: exfoliación, hidratación y gelish incluido"),
        ],
        faq=[
            ("¿El Esmaltado Express incluye cuidado de pies?", "Es un servicio enfocado solo en el esmaltado, sin el tratamiento completo de cutícula y exfoliación del pedicure."),
            ("¿Cuánto dura?", "Entre 20 y 30 minutos."),
            ("¿Puedo pedir french?", "Sí, puedes elegir color sólido o french."),
            ("¿Cómo reservo mi cita?", "Por WhatsApp al +52 984 310 8186, indicando el servicio y tu disponibilidad."),
        ],
        related=["Pedicure Ruso", "Pedicure Místico", "Gelish"],
    ),
    dict(
        slug="pedicure-ruso-playa-del-carmen",
        service_name="Pedicure Ruso",
        service_name_short="Pedicure Ruso",
        service_type="Pedicure técnica rusa",
        h1="Pedicure Ruso en Playa del Carmen",
        title="Pedicure Ruso en Playa del Carmen | Mystic Nails Art",
        description="Pedicure Ruso en Playa del Carmen: limpieza profunda en seco, ideal para cutícula y acabado preciso. Reserva por WhatsApp en Mystic Nails Art.",
        og_description="Limpieza profunda en seco, ideal para cutícula y acabado más preciso. Reserva por WhatsApp.",
        og_image="unas-blancas-azul-petroleo-floral-playa-del-carmen.webp",
        lead="Limpieza profunda en seco, ideal para cutícula y acabado más preciso — la técnica rusa se enfoca en resultados duraderos y muy detallados.",
        wa_text="Hola%2C%20quiero%20reservar%20un%20Pedicure%20Ruso%20en%20Mystic%20Nails%20Art",
        benefits=[
            ("Precisión", "técnica en seco que permite un acabado muy detallado"),
            ("Duración del resultado", "cutícula más cuidada por más tiempo"),
            ("Duración de la cita", "60–90 minutos"),
            ("Ideal para", "quienes quieren un pedicure técnico y de larga duración"),
        ],
        compare_title="Pedicure Ruso vs. otros servicios de pies",
        compare_rows=[
            ("Esmaltado Express", "Esmaltado rápido en pies, 20-30 min, color sólido o french"),
            ("Pedicure Ruso", "Limpieza profunda en seco, ideal para cutícula y acabado preciso"),
            ("Pedicure Místico", "Experiencia completa: exfoliación, hidratación y gelish incluido"),
        ],
        faq=[
            ("¿Qué hace diferente al Pedicure Ruso?", "Usa una técnica en seco (sin remojar) que permite mayor precisión en cutícula y callosidad."),
            ("¿Es doloroso?", "No, es un procedimiento profesional y seguro realizado con herramientas especializadas."),
            ("¿Cuánto dura la cita?", "Entre 60 y 90 minutos."),
            ("¿Cómo reservo mi cita?", "Por WhatsApp al +52 984 310 8186, indicando el servicio y tu disponibilidad."),
        ],
        related=["Pedicure Místico", "Esmaltado Express", "Gelish"],
    ),
    dict(
        slug="pedicure-mistico-playa-del-carmen",
        service_name="Pedicure Místico",
        service_name_short="Pedicure Místico",
        service_type="Pedicure spa completo",
        h1="Pedicure Místico en Playa del Carmen",
        title="Pedicure Místico en Playa del Carmen | Mystic Nails Art",
        description="Pedicure Místico en Playa del Carmen: experiencia spa completa con exfoliación, hidratación y Gelish incluido. Reserva por WhatsApp.",
        og_description="Experiencia completa para pies: exfoliación, hidratación, cuidado profundo y Gelish incluido. Reserva por WhatsApp.",
        og_image="nail-art-tematico-frutas-playa-del-carmen.webp",
        lead="Experiencia completa para pies: exfoliación, hidratación, cuidado profundo y Gelish incluido — el tratamiento más completo para consentir tus pies.",
        wa_text="Hola%2C%20quiero%20reservar%20un%20Pedicure%20M%C3%ADstico%20en%20Mystic%20Nails%20Art",
        benefits=[
            ("Todo incluido", "exfoliación, hidratación, cuidado profundo y Gelish en una sola cita"),
            ("Experiencia spa", "pensado como un momento completo de relajación"),
            ("Duración", "2 horas 30 minutos"),
            ("Ideal para", "ocasiones especiales o cuando quieres consentirte a fondo"),
        ],
        compare_title="Pedicure Místico vs. otros servicios de pies",
        compare_rows=[
            ("Esmaltado Express", "Esmaltado rápido en pies, 20-30 min, color sólido o french"),
            ("Pedicure Ruso", "Limpieza profunda en seco, ideal para cutícula y acabado preciso"),
            ("Pedicure Místico", "Experiencia completa: exfoliación, hidratación y gelish incluido"),
        ],
        faq=[
            ("¿Qué incluye el Pedicure Místico?", "Exfoliación, hidratación, cuidado profundo de cutícula y callosidad, y Gelish incluido en el precio del servicio."),
            ("¿Cuánto dura la cita?", "Aproximadamente 2 horas 30 minutos."),
            ("¿Es una buena opción para ocasiones especiales?", "Sí, es nuestro tratamiento más completo, ideal antes de un evento o como un momento de relajación."),
            ("¿Cómo reservo mi cita?", "Por WhatsApp al +52 984 310 8186, indicando el servicio y tu disponibilidad."),
        ],
        related=["Pedicure Ruso", "Esmaltado Express", "Gelish"],
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
        wa_text=p["wa_text"],
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
    print("Generated:", outdir)
