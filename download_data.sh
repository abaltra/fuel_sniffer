#/usr/bin/bash

REGION=$1

wget -O token1.html --header="Host: www.bencinaenlinea.cl" --header="Connection: keep-alive" --header="Cache-Control: max-age=0" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" --header="User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36" --header="Accept-Encoding: gzip,deflate,sdch" --header="Accept-Language: en-US,en;q=0.8" --header="Cookie: PHPSESSID=p43ubr5pg7fi3t50b0ksm5tfl0; __utma=180638004.342772581.1407129747.1407129747.1407129747.1; __utmc=180638004; __utmz=180638004.1407129747.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)" http://www.bencinaenlinea.cl/web2/buscador.php?region=1

token=$(python get_token.py token1.html)
echo $token

wget -O coords1.html --header="Host: www.bencinaenlinea.cl" --header="Connection: keep-alive" --header="Content-Length: 77" --header="Cache-Control: max-age=0" --header="Accept: text/javascript, text/html, application/xml, text/xml, */*" --header="X-Prototype-Version: 1.7" --header="Origin: http://www.bencinaenlinea.cl" --header="X-Requested-With: XMLHttpRequest" --header="User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36" --header="Content-type: application/x-www-form-urlencoded; charset=UTF-8" --header="Referer: http://www.bencinaenlinea.cl/web2/buscador.php?region=$REGION" --header="Accept-Encoding: gzip,deflate,sdch" --header="Accept-Language: en-US,en;q=0.8" --header="Cookie: PHPSESSID=p43ubr5pg7fi3t50b0ksm5tfl0; __utma=180638004.342772581.1407129747.1407129747.1407129747.1; __utmb=180638004.2.10.1407129747; __utmc=180638004; __utmz=180638004.1407129747.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)" --post-data="region=$REGION&comuna=&token=$token&combustible=&bandera=" http://www.bencinaenlinea.cl/web2/mapa_mostrarresultados.php

#convert index.png -background white -flatten -resize 1000 index.tif
