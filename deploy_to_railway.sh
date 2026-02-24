#!/bin/bash

# DEX Dumper Bot - Railway Deployment Script
# This script provides instructions for deploying the bot to Railway

echo "==========================================="
echo "DEX Dumper Bot - Railway Deployment Helper"
echo "==========================================="
echo ""
echo "Follow these steps to deploy your bot to Railway:"
echo ""
echo "1. Go to https://railway.com and sign in/create an account"
echo "2. Click 'New Project'"
echo "3. Select 'Deploy from GitHub repo'"
echo "4. Choose your dumper repository"
echo ""
echo "CONFIGURATION:"
echo "- Environment Variable:"
echo "  * Key: BOT_TOKEN"
echo "  * Value: 8442868358:AAF1WMiZTrgr3u4TXYvv1HNXg8vDp4QwQ0A"
echo ""
echo "- Build Command: pip install -r requirements.txt"
echo "- Start Command: python run_bot.py"
echo ""
echo "5. Click 'Deploy' and monitor the logs"
echo ""
echo "Your bot will start monitoring DEX Screener for new tokens!"
echo "==========================================="