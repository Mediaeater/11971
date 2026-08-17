# Regenerates /og-card.png (the 1200x630 social card) from card.html.
#   pip install playwright && playwright install chromium
#   python3 .card/card.py
# Note: social platforms cache og:image hard. If the card changes materially,
# rename the file and update the og:image / twitter:image URLs in index.html.
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "og-card.png"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1, color_scheme="light")
    pg.goto((HERE / "card.html").as_uri())
    pg.wait_for_timeout(400)
    pg.screenshot(path=str(OUT))
    b.close()

print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
