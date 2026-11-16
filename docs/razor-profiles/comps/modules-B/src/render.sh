#!/bin/bash
CH="google-chrome --headless=new --no-sandbox --user-data-dir=/tmp/chrome-comp --hide-scrollbars --virtual-time-budget=15000"
for f in "$@"; do n=${f%.html}
 h=$($CH --window-size=1600,800 --dump-dom file://$PWD/$f 2>/dev/null | grep -oE '<title>H[0-9]+' | grep -oE '[0-9]+')
 [ -z "$h" ] && h=1000
 $CH --force-device-scale-factor=2 --window-size=1600,$h --screenshot=../$n@2x.png file://$PWD/$f 2>/dev/null >/dev/null
 python3 -c "from PIL import Image;im=Image.open('../$n@2x.png');im.resize((1600,im.height//2),Image.LANCZOS).save('../$n.png')"
 echo "$n $h"
done
