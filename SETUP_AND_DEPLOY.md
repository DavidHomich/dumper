# DEX Dumper Bot - Complete Setup and Deployment Guide

## Overview
This bot monitors DEX Screener for new tokens and sends filtered notifications to Telegram. It includes spam filtering and 24/7 monitoring capabilities.

## Files Included
- `dumper_bot.py` - Main bot implementation
- `run_bot.py` - Script to run the bot (uses environment variables)
- `test_bot.py` - Test suite
- `requirements.txt` - Dependencies
- `Dockerfile` - Container configuration for deployment
- `Procfile` - Process definition
- `railway.json` - Railway configuration
- `.gitignore` - Files to exclude from git
- `.github/workflows/monitor.yml` - GitHub Actions workflow
- `pyproject.toml` - Python project configuration
- `README.md` - Main documentation
- `DEPLOYMENT_GUIDE.md` - Deployment options
- `GITHUB_DEPLOY_INSTRUCTIONS.md` - Step-by-step GitHub/Railway deployment

## Deployment Steps

### Step 1: Create GitHub Repository
1. Go to GitHub and create a new repository
2. Upload all these files to your repository

### Step 2: Deploy to Railway (Recommended - Free Tier)
1. Go to [Railway](https://railway.app) and sign in
2. Create new project from your GitHub repo
3. Add environment variable: `BOT_TOKEN = 8293626156:AAFO4sWwcQe1PjyyQZS1hi7Rd1t8SZye14k`
4. Deploy - the bot will run 24/7

### Step 3: Verify Operation
- Check the bot is sending notifications to your Telegram
- Monitor logs on Railway dashboard
- Adjust filtering parameters if needed

## Bot Features
- Monitors DEX Screener for new token pairs
- Filters out spam/low-quality tokens
- Sends formatted notifications to Telegram
- Includes DEX links for direct access
- Tax and honeypot checking capability
- 24/7 operation on cloud servers

## Filtering Parameters (Adjustable)
- Min liquidity: $10,000
- Min FDV: $50,000
- Min token age: 3 days
- Spam detection algorithms
- Suspicious pattern recognition

## After Deployment
The bot will run continuously on Railway servers, monitoring for new tokens and sending filtered notifications to your Telegram bot. It will work 24/7 regardless of whether your personal computer is on or off.

## Troubleshooting
- Check Railway logs for error messages
- Verify BOT_TOKEN is correctly set as environment variable
- Ensure your Telegram bot privacy settings allow receiving messages
- Review filtering parameters if not receiving expected notifications

Your bot will continuously scan for new tokens and send only quality notifications to your Telegram channel/group!