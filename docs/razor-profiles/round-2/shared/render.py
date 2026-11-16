"""Render HTML comps to PNG (@2x and 1x) with headless Chromium via Playwright.
usage: python3 render.py OUT_DIR WIDTH file1.html [file2.html ...]   (output name = html stem)"""
import sys, os, asyncio
from PIL import Image
from playwright.async_api import async_playwright
async def main(out, w, files):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={'width': w, 'height': 300}, device_scale_factor=2)
        for f in files:
            pg = await ctx.new_page()
            await pg.goto('file://' + os.path.abspath(f))
            await pg.evaluate('document.fonts.ready')
            await pg.wait_for_timeout(400)
            n = os.path.splitext(os.path.basename(f))[0]
            p2 = os.path.join(out, n + '@2x.png')
            await pg.screenshot(path=p2, full_page=True)
            im = Image.open(p2); im.resize((im.width // 2, im.height // 2), Image.LANCZOS).save(os.path.join(out, n + '.png'))
            print(n, im.width // 2, im.height // 2)
            await pg.close()
        await b.close()
asyncio.run(main(sys.argv[1], int(sys.argv[2]), sys.argv[3:]))
