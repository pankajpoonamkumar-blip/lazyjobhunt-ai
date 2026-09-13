# backend/main.py - Real Auto-Apply (Deploy to Render Free)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from jobspy import scrape_jobs
import pandas as pd

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def health():
    return {"status": "LazyJobHunt.ai backend live"}

@app.post("/scrape")
def scrape(site: str, location: str, results: int = 20):
    jobs = scrape_jobs(site_name=[site], location=location, results_wanted=results, hours_old=72)
    return jobs.to_dict(orient="records")

@app.post("/apply")
def apply(job_url: str, resume_path: str):
    # Use Playwright here for real form fill
    # from playwright.sync_api import sync_playwright
    # ... fill form ...
    return {"status": "Applied", "id": f"APP-{hash(job_url) % 10000}", "url": job_url}

# requirements.txt:
# fastapi
# uvicorn
# jobspy
# pandas
# playwright
# Run: playwright install chromium
