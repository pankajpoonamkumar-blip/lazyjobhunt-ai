# Deploy LazyJobHunt.ai to GitHub + Vercel (2 mins)

## Step 1: Create GitHub Repo
1. Go to github.com -> New Repository
2. Name: lazyjobhunt-ai
3. Public, no README
4. Create

## Step 2: Push Code
Open terminal in this folder:

```bash
git init
git add .
git commit -m "Launch LazyJobHunt.ai v11 - Clean + Logo + Loop"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/lazyjobhunt-ai.git
git push -u origin main
```

## Step 3: Deploy to Vercel (Free)
1. Go to vercel.com -> Add New Project
2. Import your GitHub repo lazyjobhunt-ai
3. Framework: Other (static)
4. Build Command: (leave empty)
5. Output Directory: ./
6. Deploy -> Live in 30 seconds at https://lazyjobhunt-ai.vercel.app

## Step 4: Add Custom Domain lazyjobhunt.ai
1. Buy domain lazyjobhunt.ai on Namecheap ($80/yr) or Porkbun
2. In Vercel -> Project -> Settings -> Domains -> Add lazyjobhunt.ai
3. Copy DNS records to Namecheap -> Done, SSL auto

## Step 5: Backend (Optional for Real LinkedIn/Naukri Auto-Apply)
Frontend alone simulates auto-apply with logs. For real form fill:

Deploy backend folder to Render Free:

1. Go to render.com -> New Web Service
2. Connect backend folder
3. Build: pip install -r requirements.txt
4. Start: uvicorn main:app --host 0.0.0.0 --port 10000
5. Copy Render URL -> Add to Vercel env VITE_API_URL

Backend code in /backend/main.py - 50 lines, uses JobSpy + Playwright.

## Step 6: Test All Functionalities
After deploy:
- Open lazyjobhunt.ai
- Continue with Google -> Upload Resume -> Connect LinkedIn (OTP 123456) -> Add Location Gurgaon, India -> Find Jobs (live) -> Select 2 -> ATS auto-downloads -> Auto-Apply -> Find More Jobs loop -> Works

## Owner Pricing Edit
- Normal users: Read-only pricing
- Owner: Triple-click logo 3x fast -> password: lazyowner123 -> Edit price/cap inline in the pricing modal -> stored in localStorage
- For production: move plan definitions + usage tracking to a real backend/database (e.g. Supabase or Postgres)
  tied to Stripe subscriptions. Client-side storage can be cleared by the user, so it's fine for a prototype
  but not for enforcing real billing limits.

## Pricing Tiers (current)
- Free: $0 one-time, 2 job applications
- Starter: $19/month, 100 job applications/month
- Unlimited: $49/month, unlimited job applications

## Future Enhancements
Tell Meta AI: "Enhance v12 with interview prep" -> We iterate.
