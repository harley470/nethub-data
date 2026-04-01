# nethub — Auto-updating Netball Data

This repo automatically scrapes and updates Suncorp Super Netball data every night using GitHub Actions. Zero cost. Zero manual work.

## What gets updated automatically

| Data | How often |
|---|---|
| Ladder standings | Every night 11pm AEST |
| Round results / scores | Every night + hourly on weekends |
| Player season stats | Every night |
| Team season stats | Every night |

## Your live data URL

```
https://raw.githubusercontent.com/harley470/nethub-data/main/data/nethub.json
```

Paste this URL into your BuildFire plugin settings.

## How to trigger a manual update

1. Go to the **Actions** tab in this repo
2. Click **Update Nethub Data**
3. Click **Run workflow**

Done — data updates in about 30 seconds.

## Cost

$0.00/month — GitHub Actions free tier covers this easily.
