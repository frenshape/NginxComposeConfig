# NginxComposeConfig
Simple nginx configuration to serve multiple apps. 

This is probably the wrong way to set things up

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
