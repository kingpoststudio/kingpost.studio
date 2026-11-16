CH="google-chrome --headless=new --no-sandbox --user-data-dir=/tmp/chrome-light --hide-scrollbars --virtual-time-budget=20000"
for pair in "hero-light:light-hero" "hero-dark:dark-hero" "page:light-page"; do f=${pair%%:*}; o=${pair##*:}
 h=$($CH --window-size=1600,800 --dump-dom file://$PWD/$f.html 2>/dev/null | grep -oE '<title>H[0-9]+' | grep -oE '[0-9]+'); [ -z "$h" ] && h=1000
 $CH --force-device-scale-factor=2 --window-size=1600,$h --screenshot=../$o@2x.png file://$PWD/$f.html >/dev/null 2>&1
 python3 -c "from PIL import Image;im=Image.open('../$o@2x.png');im.resize((1600,im.height//2),Image.LANCZOS).save('../$o.png')"; echo $o $h; done
