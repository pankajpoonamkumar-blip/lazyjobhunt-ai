# LazyJobHunt.ai - The agent that hunts while you sleep

Premium .ai job hunting agent - Auto applies to jobs while you sleep.

## Live Demo
Deploy to Vercel in 2 mins -> lazyjobhunt.ai

## Features
- Gmail + Email OTP Auth (Continue with Google like meta.ai)
- Resume upload (mandatory)
- Connect to LinkedIn, Naukri, IIMJobs, Indeed, Glassdoor + Add Custom Site (verified with OTP)
- Custom locations worldwide (Gurgaon, India support)
- Live job fetching (Arbeitnow + Remotive APIs)
- ATS resume generation per job with auto-download Company_JobTitle_ATS_Resume_Date.txt
- Auto-apply with plan-enforced limits (owner editable):
  - Free — $0 one-time, 2 applications
  - Starter — $19/mo, 100 applications/month
  - Unlimited — $49/mo, unlimited applications
- Post-apply loop: Find More Jobs

## Tech Stack
- Frontend: React + Tailwind (single HTML file, no build needed)
- Backend (optional for real auto-apply): Python + Playwright + JobSpy

## Pricing (Editable by Owner)
- Free: $0 one-time - 2 applications
- Starter: $19/mo - 100 applications/month - Most Popular
- Unlimited: $49/mo - unlimited applications

Owner mode: Triple-click logo -> password lazyowner123 -> edit price/cap inline in the pricing modal.
Note: the demo enforces these caps client-side (localStorage) for the prototype. Before charging real
money, move plan selection + usage tracking to a backend tied to Stripe subscriptions — a client-side
cap can be bypassed by clearing browser storage.

## Security note on job-portal connections
The "Connect job portal" step in this build never stores your LinkedIn/Naukri/etc. password — the field
is cleared from memory immediately after the simulated connection. Real automated login to third-party
job sites can violate their Terms of Service and risks account restrictions. For production, prefer each
platform's official OAuth/API integration, or a backend automation service the user explicitly authorizes.

## Quick Start Locally
Just open index.html in browser - works 100% frontend-only.

## Deploy to Production
See DEPLOY_GUIDE.md
