import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.antarvasna3.com/videos/tags/hindi-porn-mms/"

def scrape_videos():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(BASE_URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    videos = []
    for video_div in soup.select("div.video-block"):
        a_tag = video_div.find("a")
        title = a_tag.get("title")
        video_page = a_tag.get("href")
        thumb = video_div.find("img").get("data-src")

        # Get full video URL
        video_resp = requests.get(video_page, headers=headers)
        vsoup = BeautifulSoup(video_resp.text, "html.parser")
        source = vsoup.find("source")
        video_url = source.get("src") if source else ""

        if title and video_url:
            videos.append({
                "title": title.strip(),
                "video_url": video_url,
                "watch_link": video_url,
                "thumbnail": thumb
            })
    return videos