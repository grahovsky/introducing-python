import urllib.request as ur

url = 'http://www.example.com'
conn = ur.urlopen(url)

print(conn.status)

data = conn.read()
print(data[:50])

str_data = data.decode('utf8')
print(str_data[:50])

for key, value in conn.getheaders():
    print(key, value)


import requests
resp = requests.get('http://example.com')
print(resp)
print(resp.text[:50])

print('\n','{0:!^30s}'.format('json response'))

import sys
def search(title):
    url = "http://archive.org/advancedsearch.php"
    params = {"q": f"title:({title})",
              "output": "json",
              "fields": "identifier,title",
              "rows": 50,
              "page": 1, }
    resp = requests.get(url, params=params)
    return resp.json()


if __name__ == "__main__":
    title = sys.argv[1]
    data = search(title)
    docs = data["response"]["docs"]
    print(f"Found {len(docs)} items, showing first 10")
    print("identifier\ttitle")
    for row in docs[:10]:
        print(row["identifier"], row["title"], sep="\t")