import urllib.request

url = "https://maps.app.goo.gl/jupzYsrjKezFDkYJ8"
try:
    req = urllib.request.Request(url, method="HEAD")
    with urllib.request.urlopen(req) as response:
        with open("url.txt", "w") as f:
            f.write(response.geturl())
except Exception as e:
    with open("url.txt", "w") as f:
        f.write(str(e))
