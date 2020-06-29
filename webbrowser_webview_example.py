import webbrowser

url = 'https://www.python.org/'
webbrowser.open(url)


# pip install pywebview
import webview
url = input("URL? ")
#http://time.gov
webview.create_window(f"webview display of {url}", url)