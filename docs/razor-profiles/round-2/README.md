# Razor Profiles: round 2 visual identity directions
Rio for Stuart, Thu Nov 12, 2026 (ET). Comps only. Nothing pushed, committed or published. Round 1 files untouched.

- overview.jpg: both heroes side by side
- direction-1-clean-cut/: hero.png (+@2x), brand-board.png (+@2x), modules/01–10 (+@2x), modules/contact-sheet.jpg, mark/*.svg, src/ (HTML, Python builders, fonts, images)
- direction-2-live-build/: same structure
- shared/: mark.py (logo evolutions built from the real SVG geometry), render.py (Playwright → PNG), sheet.py, contrast.py

Rebuild: cd direction-N-*/src && python3 hero.py && python3 board.py && python3 modules.py, then
python3 ../../shared/render.py .. 1440 hero.html ; python3 ../../shared/render.py .. 1600 brand-board.html ; python3 ../../shared/render.py ../modules 1440 modules/*.html

Caveats: generated images (4) are placeholders; Walter portrait is a labeled placeholder; case-study problem/output lines and all metrics are sample slots; testimonials unattributed pending approval; headlines and service blurbs are proposed copy (the real copy Sheet is still inaccessible); "From $5k" comes from the HubSpot directory snippet; calendar slots and the build log are illustrative.
