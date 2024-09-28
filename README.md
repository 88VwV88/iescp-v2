# Influencer Engagement & Sponsorship Coordination Platform v2
It's a platform to connect Sponsors and Influencers so that sponsors can get their product/service advertised and influencers can get monetary benefit.

## Frameworks used
- SQLite for data storage
- Flask for API
- VueJS for UI
- VueJS Advanced for CLI
- Jinja2 templates
- Bootstrap for HTML generation and styling
- Redis for caching
- Redis and Celery for batch jobs

## Roles
- *Admin - root access*
  - monitor all the users/campaigns, see all the statistics.
  - flag inappropriate campaigns/users.
- *Sponsors - company/indivisual who want to advertise their product/service*
  - create campaigns, search for influencers and send ad resquests for a particular campaign.
  - create multiple campaigns and track each indivisual campaign.
  - accept ad requests by influencers for public campaigns.
  - can have:
    - Company/Indivisual Name
    - Industry
    - Budget
- *Influencers - indivisual who has significant social media following*
  - will recieve ad requests, accept or reject ad requests, negotiate terms and resend modified ad requests back to sponsors.
  - can search for ongoing campaigns (which are public) according to category, budget etc. and accept the request.
  - can update their profile page, which is publicly visible.
  - Influencer profile can have:
    - Name
    - Category
    - Niche
    - Reach (number of followers/activity etc.)
  
## Terminologies
### Ad Requests
  A contract between campaign and influencer, stating the requirements of the particular advertisement (e.g. show Samsung S23 in 3 videos for 10 seconds each), the amount to be paid, etc.
  May have:
  - campaign_id
  - influencer_id
  - requirements
  - payment_amount
  - status (pending/accepted/rejected)
### Campaign
  A container for ad requests for a paritcular goal (e.g. advertisement for Samsung S23). It can have multiple ad requests, a campaign description, budget, ability to set public or private.
  May have:
  - name
  - description
  - start_date
  - end_date
  - budget
  - visibility (public/private)
  - goals
