# Fusión en 5 minutos · Fusion in 5 Minutes

Sitio bilingüe (español / inglés) de artículos semanales sobre energía de fusión, por Humberto Torreblanca, PhD.

## Estructura

| Ruta | Contenido |
|---|---|
| `index.html`, `sobre-mi.html` | Portada y página "Sobre mí" en español |
| `articulos/` | Artículos en español |
| `en/index.html`, `en/about.html`, `en/articles/` | Versión en inglés |
| `assets/css/` | Estilos (template "Plomo + plasma") |
| `assets/img/` | Gráficos de los artículos (`es-*` y `en-*`) |
| `content/es/`, `content/en/` | Cuerpo de cada artículo (fuente) |
| `articles.json` | Lista de artículos, del más reciente al más antiguo |
| `scripts/build.py` | Genera todas las páginas HTML |

## Publicar un artículo nuevo

1. Guarda el cuerpo del artículo en `content/es/<slug>.html` y `content/en/<slug>.html`.
2. Agrega sus datos **al inicio** de `articles.json`.
3. Ejecuta `python3 scripts/build.py` y sube los cambios a `main`.

GitHub Pages publica el sitio automáticamente en un par de minutos.
