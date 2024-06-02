'''4. Реализуйте простой HTTP-клиент. Он принимает один параметр командной строки - URL.
Клиент делает запрос по указанному URL и выдает тело ответа на терминал как текст.'''

import sys
import requests

def fetch_content_from_url(url):
    try:
        result = requests.get(url)
        print(result.text)
    except requests.RequestException as error:
        print(f"Failed to fetch content: {error}")

def run_http_client():
    if len(sys.argv) != 2:
        print("Usage: python 4.py <URL>")
        return

    url_to_fetch = sys.argv[1]
    fetch_content_from_url(url_to_fetch)

if __name__ == "__main__":
    run_http_client()

'''
juliamekhtieva@MacBook-Pro-73 exam_net_sys % python 4.py http://example.com

<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>

'''