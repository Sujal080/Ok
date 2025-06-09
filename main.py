from fastapi import FastAPI
from scraper import scrape_videos

app = FastAPI()

@app.get("/videos")
def get_videos():
    return {"data": scrape_videos()}