from fastapi import FastAPI
from scraper import scrape_videos

app = FastAPI()

@app.get("/")
def root():
    return {"message": "✅ API is running. Visit /videos to get video data."}

@app.get("/videos")
def get_videos():
    return {"data": scrape_videos()}
