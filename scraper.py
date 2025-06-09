import requests
from bs4 import BeautifulSoup

def scrape_videos():
    base_url = "https://www.antarvasna3.com/videos/tags/hindi-porn-mms/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    data = []

    for vid in soup.select(".videotitle"):
        title = vid.get_text(strip=True)
        href = vid.find("a")["href"]
        full_url = "https://www.antarvasna3.com" + href

        # open each video page
        vres = requests.get(full_url, headers=headers)
        vsoup = BeautifulSoup(vres.text, "html.parser")

        iframe = vsoup.find("iframe")
        if not iframe:
            continue

        watch_url = iframe["src"]
        if "embed-" in watch_url:
            # try to build direct .mp4 url (depends on site logic)
            mp4_url = watch_url.replace("embed-", "").replace(".html", ".mp4")
        else:
            mp4_url = watch_url

        data.append({
            "title": title,
            "video_url": mp4_url,
            "watch_online": watch_url
        })

    return data
