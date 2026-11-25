#!/usr/bin/env python3
"""Genera el sitio "Fusión en 5 minutos" (español e inglés).

Uso:  python3 scripts/build.py

Para publicar un artículo nuevo:
  1. Guarda el cuerpo en content/es/<slug-es>.html y content/en/<slug-en>.html
     (desde <header class="hero"> hasta el aviso; usa {{IMG}} para las imágenes).
  2. Agrega sus datos AL INICIO de articles.json.
  3. Ejecuta este script y sube los cambios.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800'
         '&family=Fraunces:opsz,wght@9..144,700;9..144,800&display=swap" rel="stylesheet">')

MONTHS = {
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
           "septiembre", "octubre", "noviembre", "diciembre"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August",
           "September", "October", "November", "December"],
}

L = {
    "es": {
        "brand": "Fusión en 5 minutos",
        "home": "Home", "about": "Sobre mí",
        "other": "English", "other_lang": "en",
        "home_file": "index.html", "about_file": "sobre-mi.html", "art_dir": "articulos",
        "home_title": "Fusión en 5 minutos · Energía de fusión explicada en español",
        "home_desc": "Cada semana, un artículo en español para entender la energía de fusión: su historia, la política detrás, la industria que la construye y cuánto cuesta.",
        "hero_h1": "En la década de 2030, la humanidad podría encender en la Tierra la misma energía que hace brillar a las estrellas.",
        "hero_p1": "Se llama <strong>fusión</strong>: dos núcleos de átomos ligeros se unen y liberan una cantidad enorme de energía, casi sin emisiones y con un combustible que se obtiene del agua. Durante décadas fue un experimento de laboratorio. Hoy es una carrera entre empresas y países por construir la primera central que lleve esa electricidad a nuestras casas.",
        "hero_p2": "Cada semana, un artículo para entender esta revolución: su historia, la política detrás, la industria que la construye y cuánto cuesta.",
        "by": "Por Humberto Torreblanca, PhD", "role": "Científico, Educador y Autor",
        "stats_label": "Datos sobre la fusión",
        "stats": [
            ("~ 10 hogares", "La energía de 1 gramo de combustible de fusión equivale al consumo eléctrico de unos 10 hogares durante un año"),
            ("150 M °C", "Temperatura en un reactor de fusión nuclear: 10 veces más caliente que el centro del Sol"),
            ("1 kg vs. 10 mil toneladas", "Combustible diario de una central de fusión frente a una de carbón del mismo tamaño"),
            ("$14.2 mil M", "Inversión acumulada en empresas de fusión (2026)"),
        ],
        "articles_h": "Artículos publicados",
        "articles_lead": "Del más reciente al más antiguo. Cada artículo se lee en unos minutos e incluye cifras, analogías y esquemas.",
        "filter_label": "Filtrar por eje",
        "all": "Todos",
        "axes": ["Historia", "Política", "Industria", "Economía", "Educación"],
        "empty": "Todavía no hay artículos de {x}. Llegan pronto.",
        "reading": "Lectura: {n} min",
        "read": "Leer artículo",
        "back": "Volver al inicio",
        "nav_label": "Principal",
        "hash": "#EnergíaDeFusión #Ciencia #Divulgación",
        "about_title": "Sobre mí · Fusión en 5 minutos",
        "about_desc": "Por qué existe Fusión en 5 minutos y quién la escribe: Humberto Torreblanca, PhD.",
        "about_pill": "Sobre mí",
        "about_h1": "Sobre la serie y su autor",
        "about_lead": "Por qué existe “Fusión en 5 minutos” y quién la escribe.",
        "about_h_init": "La iniciativa",
        "about_init": [
            "Llevo años trabajando en fusión, y hay algo que me preocupa: casi toda la información sobre ella está en inglés, desde los artículos científicos y los reportes de la industria hasta las noticias de cada nuevo récord. La fusión vive su momento más emocionante, con récords de laboratorio, miles de millones de dólares de inversión privada y una carrera entre países por construir la primera central. Mientras tanto, más de 640 millones de hispanohablantes miran desde afuera.",
            "Pienso en los estudiantes de Perú y en los hispanohablantes que podrían ser los científicos e ingenieros de esta industria, pero que no encuentran por dónde empezar en su idioma. Pienso también en los periodistas, los empresarios y los responsables de políticas públicas que tendrán que tomar decisiones sobre esta tecnología sin información clara a la mano.",
            "Por eso creé <strong>Fusión en 5 minutos</strong>. Cada semana escribo un artículo en español que explica un tema de fusión con un lenguaje claro, cifras verificadas, analogías de la vida diaria y esquemas que ayudan a visualizar los conceptos. Mi objetivo es simple: que el conocimiento sobre la energía de las estrellas no tenga barreras de idioma. También publico cada artículo en inglés, para que la conversación vaya en ambas direcciones.",
        ],
        "analogy": "Analogía",
        "about_analogy": "Si la conversación sobre la fusión fuera una gran conferencia, hoy casi la mitad de las charlas serían en inglés y solo 6 de cada 100 en español. Quiero ser el intérprete en la cabina para más de 640 millones de personas.",
        "about_h_author": "El autor",
        "about_author": [
            "Tuve la suerte de ser el último estudiante de doctorado de <strong>Francis F. Chen</strong>, autor de <em>Introduction to Plasma Physics and Controlled Fusion</em>, el libro con el que generaciones de físicos aprendieron sobre plasmas.",
            "Después de obtener mi doctorado en la <strong>Universidad de California, Los Ángeles (UCLA)</strong>, trabajé en <strong>Intel Corporation</strong>, donde estuve a cargo de equipos de grabado por plasma (<em>plasma etchers</em>) y desarrollé procesos para la fabricación de microprocesadores. Luego di el salto a la fusión nuclear en la <strong>DIII-D National Fusion Facility</strong>, primero en el grupo de operaciones y después en el sistema de calentamiento por resonancia ciclotrónica de electrones (ECH). Más tarde pasé a la <strong>EPFL</strong>, en Suiza, donde trabajé en la instalación FALCON con los girotrones para ITER. En <strong>Type One Energy</strong> fui ingeniero computacional y después estuve a cargo del diseño e implementación del sistema ECH. Hoy trabajo en <strong>Helion Energy</strong>, donde hago simulaciones multifísicas.",
            "Desde 2005 participo activamente en actividades de divulgación científica en Estados Unidos y Perú. También he dado charlas sobre fusión y sobre estudios de posgrado en diversas universidades del Perú.",
        ],
        "about_notice": "<strong>Aviso:</strong> El propósito de este contenido es educativo y de divulgación, por lo que busca ofrecer información objetiva. Cualquier opinión personal es mía y no representa la posición de la empresa en la que trabajo ni de ninguna otra organización. En la investigación, el desarrollo y el diseño de esta página web se utilizaron herramientas de inteligencia artificial.",
    },
    "en": {
        "brand": "Fusion in 5 Minutes",
        "home": "Home", "about": "About",
        "other": "Español", "other_lang": "es",
        "home_file": "index.html", "about_file": "about.html", "art_dir": "articles",
        "home_title": "Fusion in 5 Minutes · Fusion energy, clearly explained",
        "home_desc": "Every week, an article to understand fusion energy: its history, the politics behind it, the industry building it and what it costs.",
        "hero_h1": "In the 2030s, humanity could ignite on Earth the same energy that makes the stars shine.",
        "hero_p1": "It's called <strong>fusion</strong>: two light atomic nuclei join together and release an enormous amount of energy, with almost no emissions and with a fuel that comes from water. For decades it was a laboratory experiment. Today it is a race among companies and countries to build the first power plant that brings that electricity to our homes.",
        "hero_p2": "Every week, an article to understand this revolution: its history, the politics behind it, the industry building it and what it costs.",
        "by": "By Humberto Torreblanca, PhD", "role": "Scientist, Educator and Author",
        "stats_label": "Fusion facts",
        "stats": [
            ("~ 10 homes", "The energy in 1 gram of fusion fuel equals the electricity used by about 10 homes in a year"),
            ("150 M °C", "Temperature inside a fusion reactor: 10 times hotter than the center of the Sun"),
            ("1 kg vs. 10,000 tons", "Daily fuel for a fusion plant compared with a coal plant of the same size"),
            ("$14.2 B", "Cumulative investment in fusion companies (2026)"),
        ],
        "articles_h": "Published articles",
        "articles_lead": "Newest first. Each article takes a few minutes to read and includes figures, analogies and diagrams.",
        "filter_label": "Filter by topic",
        "all": "All",
        "axes": ["History", "Politics", "Industry", "Economics", "Education"],
        "empty": "No {x} articles yet. Coming soon.",
        "reading": "Reading time: {n} min",
        "read": "Read article",
        "back": "Back to home",
        "nav_label": "Main",
        "hash": "#FusionEnergy #Science #ScienceOutreach",
        "about_title": "About · Fusion in 5 Minutes",
        "about_desc": "Why Fusion in 5 Minutes exists and who writes it: Humberto Torreblanca, PhD.",
        "about_pill": "About",
        "about_h1": "About the series and its author",
        "about_lead": "Why “Fusion in 5 Minutes” exists and who writes it.",
        "about_h_init": "The initiative",
        "about_init": [
            "I have worked in fusion for years, and one thing worries me: almost all the information about it is in English, from scientific papers and industry reports to the news of every new record. Fusion is living its most exciting moment, with laboratory records, billions of dollars of private investment and a race among countries to build the first power plant. Meanwhile, more than 640 million Spanish speakers are watching from the outside.",
            "I think of students in Peru and of Spanish speakers who could become the scientists and engineers of this industry but can't find where to start in their own language. I also think of the journalists, business leaders and policymakers who will have to make decisions about this technology without clear information at hand.",
            "That's why I created <strong>Fusion in 5 Minutes</strong> (<em>Fusión en 5 minutos</em>). Every week I write an article in Spanish that explains a fusion topic with clear language, verified figures, everyday analogies and diagrams that help visualize the concepts. I also publish each article in English, so the conversation flows both ways. My goal is simple: knowledge about the energy of the stars should have no language barriers.",
        ],
        "analogy": "Analogy",
        "about_analogy": "If the conversation about fusion were a big conference, today almost half the talks would be in English and only 6 in 100 in Spanish. I want to be the interpreter in the booth for more than 640 million people.",
        "about_h_author": "The author",
        "about_author": [
            "I was lucky to be the last PhD student of <strong>Francis F. Chen</strong>, author of <em>Introduction to Plasma Physics and Controlled Fusion</em>, the book from which generations of physicists learned about plasmas.",
            "After earning my PhD at the <strong>University of California, Los Angeles (UCLA)</strong>, I worked at <strong>Intel Corporation</strong>, where I was responsible for plasma etchers and developed processes for manufacturing microprocessors. I then made the jump to nuclear fusion at the <strong>DIII-D National Fusion Facility</strong>, first in the operations group and then on the electron cyclotron heating (ECH) system. Later I moved to <strong>EPFL</strong> in Switzerland, where I worked at the FALCON facility with the gyrotrons for ITER. At <strong>Type One Energy</strong> I was a computational engineer and later led the design and implementation of the ECH system. Today I work at <strong>Helion Energy</strong>, where I run multiphysics simulations.",
            "Since 2005 I have been actively involved in science outreach in the United States and Peru. I have also given talks about fusion and about graduate studies at several universities in Peru.",
        ],
        "about_notice": "<strong>Disclaimer:</strong> This content is intended for educational and outreach purposes, so it aims to provide objective information. Any personal opinions are my own and do not represent the position of my employer or any other organization. Artificial intelligence tools were used in the research, development and design of this website.",
    },
}

THUMBS = {
    "sol": '<svg viewBox="0 0 400 150" preserveAspectRatio="xMaxYMid slice" aria-hidden="true"><circle cx="330" cy="70" r="46" fill="#F59E0B"/><circle cx="330" cy="70" r="66" fill="none" stroke="#FCD34D" stroke-width="2" stroke-dasharray="3 9" opacity=".8"/><circle cx="330" cy="70" r="86" fill="none" stroke="#fff" stroke-width="1.5" stroke-dasharray="2 10" opacity=".4"/></svg>',
    "fusion": '<svg viewBox="0 0 400 150" preserveAspectRatio="xMaxYMid slice" aria-hidden="true"><g stroke="#2B2F35" stroke-width="2"><circle cx="272" cy="72" r="14" fill="#E11D74"/><circle cx="294" cy="72" r="14" fill="#CBD5E1"/><circle cx="352" cy="58" r="14" fill="#E11D74"/><circle cx="374" cy="58" r="14" fill="#CBD5E1"/><circle cx="363" cy="80" r="14" fill="#CBD5E1"/></g><path d="M308 72 h28" stroke="#fff" stroke-width="3" stroke-dasharray="4 4"/></svg>',
}

FILTER_JS = """<script>
{
  const grid = document.getElementById("grid"), filters = document.getElementById("filters"), empty = document.getElementById("empty");
  filters.addEventListener("click", ev => {
    const b = ev.target.closest(".f"); if (!b) return;
    const x = b.dataset.e;
    filters.querySelectorAll(".f").forEach(f => f.setAttribute("aria-pressed", f === b));
    let n = 0;
    grid.querySelectorAll(".card").forEach(c => {
      const show = !x || c.dataset.axes.split("|").includes(x);
      c.hidden = !show; if (show) n++;
    });
    empty.hidden = n > 0;
    empty.textContent = empty.dataset.t.replace("{x}", b.textContent);
  });
}
</script>"""


def fmt_date(iso, lang):
    y, m, d = (int(p) for p in iso.split("-"))
    if lang == "es":
        return f"{d} de {MONTHS['es'][m - 1]} de {y}"
    return f"{MONTHS['en'][m - 1]} {d}, {y}"


def head(lang, title, desc, root, css, alt_href):
    other = L[lang]["other_lang"]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<link rel="alternate" hreflang="{other}" href="{alt_href}">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="{root}assets/css/{css}.css">
</head>
<body>
"""


def nav(lang, root, current, alt_href):
    t = L[lang]
    base = root + ("" if lang == "es" else "en/")
    cur = lambda k: ' aria-current="page"' if current == k else ""
    return f"""<nav class="bar" aria-label="{t['nav_label']}">
  <div class="inner">
    <a class="brand" href="{base}{t['home_file']}">{t['brand']}</a>
    <div class="tabs">
      <a class="tab" href="{base}{t['home_file']}"{cur('home')}>{t['home']}</a>
      <a class="tab" href="{base}{t['about_file']}"{cur('about')}>{t['about']}</a>
      <a class="tab lang" href="{alt_href}" hreflang="{t['other_lang']}" lang="{t['other_lang']}">{t['other']}</a>
    </div>
  </div>
</nav>
"""


def footer(lang):
    t = L[lang]
    return f"""<footer>
  <div class="inner">
    <span>{t['brand']} · Humberto Torreblanca, PhD</span>
    <span class="hash">{t['hash']}</span>
  </div>
</footer>
"""


def page_paths(lang):
    """Return (dir prefix, root) for home/about pages."""
    return ("", "") if lang == "es" else ("en/", "../")


def build_home(lang, arts):
    t = L[lang]
    prefix, root = page_paths(lang)
    other = t["other_lang"]
    alt = root + ("en/" if other == "en" else "") + "index.html"
    out = head(lang, t["home_title"], t["home_desc"], root, "home", alt)
    out += nav(lang, root, "home", alt)
    stats = "\n".join(
        f'      <div class="stat" style="--c:var(--{c})"><div class="n">{n}</div><div class="l">{l}</div></div>'
        for (n, l), c in zip(t["stats"], ["violet", "magenta", "orange", "violet"]))
    filters = f'<button class="f" type="button" data-e="" aria-pressed="true">{t["all"]}</button>' + "".join(
        f'<button class="f" type="button" data-e="{a}" aria-pressed="false">{a}</button>' for a in t["axes"])
    cards = []
    for a in arts:
        x = a[lang]
        tags = "".join(f'<span class="tag">{html.escape(e)}</span>' for e in x["axes"])
        cards.append(f"""      <article class="card" data-axes="{'|'.join(x['axes'])}">
        <div class="thumb" style="--g:{a['gradient']}">{THUMBS.get(a['thumb'], '')}<span class="week">{fmt_date(a['date'], lang)}</span></div>
        <div class="body">
          <h3>{html.escape(x['title'])}</h3>
          <p>{html.escape(x['summary'])}</p>
          <div class="meta">{tags}<span>· {t['reading'].format(n=a['minutes'])}</span></div>
          <a class="btn" href="{t['art_dir']}/{x['slug']}.html">{t['read']} <span aria-hidden="true">→</span></a>
        </div>
      </article>""")
    out += f"""
<header class="hero short">
  <div class="inner">
    <div class="txt">
      <h1>{t['hero_h1']}</h1>
      <p>{t['hero_p1']}</p>
      <p>{t['hero_p2']}</p>
    </div>
    <div class="autor"><b>{t['by']}</b><span>{t['role']}</span></div>
  </div>
</header>

<main class="inner">
  <section class="stats" aria-label="{t['stats_label']}">
{stats}
  </section>

  <section class="sec" aria-labelledby="h-art">
    <div class="sec-h"><span class="num" style="--c:var(--violet)">1</span><h2 id="h-art">{t['articles_h']}</h2></div>
    <p class="lead">{t['articles_lead']}</p>
    <div class="filters" id="filters" role="group" aria-label="{t['filter_label']}">{filters}</div>
    <div class="grid" id="grid">
{chr(10).join(cards)}
    </div>
    <p class="empty" id="empty" data-t="{t['empty']}" hidden></p>
  </section>
</main>
"""
    out += footer(lang) + FILTER_JS + "\n</body>\n</html>\n"
    (ROOT / prefix / "index.html").write_text(out, encoding="utf-8")


def build_about(lang):
    t = L[lang]
    prefix, root = page_paths(lang)
    other = t["other_lang"]
    alt = root + ("en/" if other == "en" else "") + L[other]["about_file"]
    out = head(lang, t["about_title"], t["about_desc"], root, "home", alt)
    out += nav(lang, root, "about", alt)
    p = lambda items: "\n".join(f"      <p>{x}</p>" for x in items)
    out += f"""
<header class="hero" style="padding-bottom:clamp(48px,6vw,72px)">
  <div class="inner">
    <div>
      <span class="pill">{t['about_pill']}</span>
      <h1>{t['about_h1']}</h1>
      <p>{t['about_lead']}</p>
    </div>
  </div>
</header>

<main class="inner">
  <section class="sec about">
    <div class="sec-h"><span class="num" style="--c:var(--violet)">1</span><h2>{t['about_h_init']}</h2></div>
{p(t['about_init'])}
    <div class="analogia"><b>{t['analogy']}</b><p>{t['about_analogy']}</p></div>

    <div class="sec-h" style="margin-top:40px"><span class="num" style="--c:var(--magenta)">2</span><h2>{t['about_h_author']}</h2></div>
    <div class="autor" style="border-left-color:var(--magenta);margin:0 0 16px"><b>Humberto Torreblanca, PhD</b><span>{t['role']}</span></div>
{p(t['about_author'])}

    <div style="margin-top:56px"><p class="aviso">{t['about_notice']}</p></div>
  </section>
</main>
"""
    out += footer(lang) + "</body>\n</html>\n"
    (ROOT / prefix / t["about_file"]).write_text(out, encoding="utf-8")


def build_article(lang, a):
    t = L[lang]
    other = t["other_lang"]
    x = a[lang]
    prefix = "" if lang == "es" else "en/"
    root = "../" if lang == "es" else "../../"
    home = "../index.html"
    alt = root + ("en/" if other == "en" else "") + f"{L[other]['art_dir']}/{a[other]['slug']}.html"
    body = (ROOT / "content" / lang / f"{x['slug']}.html").read_text(encoding="utf-8")
    body = body.replace("{{IMG}}", root + "assets/img/")
    out = head(lang, f"{x['title']} · {t['brand']}", x["summary"], root, "article", alt)
    out += f"""<nav class="volver-bar" aria-label="{t['nav_label']}"><div class="inner"><a class="marca" href="{home}">{t['brand']}</a><div class="acciones"><a class="volver lang" href="{alt}" hreflang="{other}" lang="{other}">{t['other']}</a><a class="volver" href="{home}"><span aria-hidden="true">←</span> {t['back']}</a></div></div></nav>

{body}
  <p style="margin:32px 0 0"><a class="volver" href="{home}"><span aria-hidden="true">←</span> {t['back']}</a></p>
</main>
</body>
</html>
"""
    d = ROOT / prefix / t["art_dir"]
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{x['slug']}.html").write_text(out, encoding="utf-8")


def main():
    arts = json.loads((ROOT / "articles.json").read_text(encoding="utf-8"))
    (ROOT / "en").mkdir(exist_ok=True)
    for lang in ("es", "en"):
        build_home(lang, arts)
        build_about(lang)
        for a in arts:
            build_article(lang, a)
    print(f"Built {len(arts)} article(s) in 2 languages.")


if __name__ == "__main__":
    main()
