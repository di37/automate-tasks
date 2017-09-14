def print_links(url):
    import requests
    from bs4 import BeautifulSoup

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all("a")

    # for link in links:
    #     if "http" in link.get("href"):
    #         print("<a href='%s'>%s</a>" % (link.get("href"), link.text))

    g_data = soup.find_all("section", {"class": "left"})
    for item in g_data:
        print(item.contents[0].text)

    while i < 10:
        i = 1
        print_links("http://yellowpages.ae/s/uae/engineering-" + i + "-1.html")
        i = i + 1
