#/usr/bin/bash

wget --quiet -O token1.html --header="Host: www.bencinaenlinea.cl" --header="Connection: keep-alive" --header="Cache-Control: max-age=0" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" --header="User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36" --header="Accept-Encoding: gzip,deflate,sdch" --header="Accept-Language: en-US,en;q=0.8" --header="Cookie: PHPSESSID=p43ubr5pg7fi3t50b0ksm5tfl0; __utma=180638004.342772581.1407129747.1407129747.1407129747.1; __utmc=180638004; __utmz=180638004.1407129747.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)" http://www.bencinaenlinea.cl/web2/buscador.php?region=1

echo $(python get_token.py token1.html)

rm token1.html

