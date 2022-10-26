import requests
def get_novel_chapters():
    root_url=""
    r=requests.get(root_url)
    r.encoding="gbk"
    soup=Beautifulsoup(r.text,"html.parser")

    for dd in soup.find_all("dd"):
        link=dd.find("a")
        if not link:
            continue

            print(link)

get_novel_chapters()