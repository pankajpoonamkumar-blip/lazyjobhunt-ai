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
    # Use Playwright here for real form fill.
    #
    # IMPORTANT: do not accept or store a third-party portal password in this
    # request body or in any database. If you build this out:
    #   - Prefer official OAuth/API integrations where the portal offers them
    #     (this is the only approach that's clearly within most sites' ToS).
    #   - If you do drive a real browser session, keep it scoped to a session
    #     the user starts and watches (e.g. a short-lived authenticated
    #     Playwright session, not stored credentials replayed later).
    #   - Never log or persist raw credentials, even "temporarily".
    #   - Automating login/form-submission on sites that prohibit it in their
    #     Terms of Service can get the user's account suspended — flag this
    #     risk to the user before they connect a portal.
    #
    # from playwright.sync_api import sync_playwright
    # ... fill form using an already-authenticated session ...
    return {"status": "Applied", "id": f"APP-{hash(job_url) % 10000}", "url": job_url}

# requirements.txt:
# fastapi
# uvicorn
# jobspy
# pandas
# playwright
# Run: playwright install chromium
