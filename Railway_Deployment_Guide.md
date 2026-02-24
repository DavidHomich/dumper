# Railway Deployment Guide for DEX Dumper Bot

This guide will walk you through deploying your DEX Dumper Bot on Railway for free hosting.

## Prerequisites

- A Railway account (sign up at https://railway.com)
- Your bot token from BotFather (already configured: 8442868358:AAF1WMiZTrgr3u4TXYvv1HNXg8vDp4QwQ0A)
- GitHub repository with the bot code (already pushed)

## Step-by-Step Deployment

### 1. Connect Your GitHub Repository
1. Log in to your Railway account at https://railway.com
2. Click "New Project" 
3. Select "Deploy from GitHub repo"
4. Find and select your dumper repository
5. Click "Install" to authorize Railway to access your repository

### 2. Configure the Project
1. Once connected, Railway will scan your repository
2. It should automatically detect this is a Python project
3. Make sure it selects the correct branch (likely `main`)

### 3. Set Environment Variables
1. In the Railway dashboard, go to the "Variables" tab
2. Add the following environment variable:
   - Key: `BOT_TOKEN`
   - Value: `8442868358:AAF1WMiZTrgr3u4TXYvv1HNXg8vDp4QwQ0A`

### 4. Configure Build and Start Commands
1. Go to the "Settings" tab for your service
2. Under "Build Command", enter: `pip install -r requirements.txt`
3. Under "Start Command", enter: `python run_bot.py`
4. Make sure the "Build Directory" is set to the root of your project

### 5. Deploy
1. Click "Deploy" or "Redeploy" if it starts automatically
2. Monitor the build logs to ensure all dependencies install correctly
3. Check the runtime logs to confirm the bot starts successfully

### 6. Monitor Your Bot
1. Once deployed, you can view logs in real-time
2. The bot should connect to Telegram and start monitoring for tokens
3. You can check the bot status by looking at the logs

## Important Notes

- **Free Tier Limitations**: Railway's free tier has some limitations on runtime hours and sleep policies
- **Environment Variables**: Never commit your bot token directly to the code; always use environment variables
- **Logs**: Monitor your bot's logs regularly to ensure it's running properly
- **Restart Policy**: Railway may restart your bot periodically; the bot should handle this gracefully

## Troubleshooting

If your bot doesn't start:
1. Check the deployment logs for error messages
2. Verify your BOT_TOKEN is correctly set as an environment variable
3. Confirm all dependencies in requirements.txt are installing correctly
4. Make sure the start command is `python run_bot.py`

## Updating Your Bot

When you push new changes to GitHub:
1. Railway can be configured to automatically redeploy on pushes to main branch
2. Or you can manually trigger a redeployment from the Railway dashboard

## Security Considerations

- Keep your bot token secure and never share it publicly
- Review access permissions for your Railway project
- Regularly audit who has access to your GitHub repository

Your bot should now be running on Railway and continuously monitoring DEX Screener for new tokens!