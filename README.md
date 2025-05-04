# NginxComposeConfig
Simple nginx configuration to serve multiple apps. 

This is the example I wish I could've found when I was setting up a mini server on my LAN. This is intended as a trivial example to serve as a starting point,
I have no idea if this demonstrates good practices or not.

It does, however, seem to work correctly when tested on a Debian12 system with nginx/1.27.5. 


To run:
clone the depo


```bash
cd ./NginxComposeConfig/ncc/
docker compose up -d
```
from there
```bash
curl localhost
```

should produce
```html
<!DOCTYPE HTML>

<html>
        <head>
                <title>Generic landing page</title>
        </head>
        <body>
                This is the landing page.
                <ul>
                        <li><a href="/flask1/">App 1</a></li>
                        <li><a href="/flask2/">App 2</a></li>
                </ul>
        </body>
</html>
```

```bash

curl localhost/flask1/
```

```html
<h1>This is app F1</h1>
```

```bash
curl localhost/flask2/
```

```html
<h1>This is app F2</h1>
```

if you use your web browser instead of `curl` then remember to use `http://` (no s)

Finish with
```bash
docker compose down
```

