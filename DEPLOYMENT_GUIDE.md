# Deployment Guide for DEX Dumper Bot

This guide explains how to deploy your DEX Dumper Bot to free cloud platforms.

## Deploy to Railway (Recommended)

1. Sign up at [Railway](https://railway.app)
2. Create a new project
3. Connect your GitHub repository or upload the code
4. Railway will automatically detect the Dockerfile and deploy
5. Add your bot token as an environment variable:
   - Variable: `BOT_TOKEN`
   - Value: `8293626156:AAFO4sWwcQe1PjyyQZS1hi7Rd1t8SZye14k`
6. Redeploy the project

## Deploy to Render

1. Sign up at [Render](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Choose the Dockerfile deployment method
5. Set the runtime to Python
6. Add environment variable:
   - `BOT_TOKEN`: `8293626156:AAFO4sWwcQe1PjyyQZS1hi7Rd1t8SZye14k`
7. Deploy

## Environment Variables

If you want to make the bot token configurable, update the `run_bot.py` file to use environment variables:

```python
import os
bot_token = os.getenv('BOT_TOKEN', '8293626156:AAFO4sWwcQe1PjyyQZS1hi7Rd1t8SZye14k')
```

## Important Notes

- Both Railway and Render offer free tiers with some limitations
- Your bot will run 24/7 on these platforms
- Some free tiers may sleep after inactivity - check the platform documentation
- Make sure to secure your bot token and don't expose it publicly

## Alternative: GitHub Actions (Cron Job)

If you prefer GitHub Actions for periodic checks, you can also set up a cron job in GitHub Actions that runs the bot periodically rather than continuously. This would be triggered by a schedule rather than running constantly.