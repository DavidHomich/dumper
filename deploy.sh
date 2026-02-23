#!/bin/bash

echo "Setting up DEX Dumper Bot for deployment..."

# Create a deployment package
echo "Creating deployment package..."

# Create a zip file with all necessary files
zip -r dex-dumper-bot.zip *.py requirements.txt README.md DEPLOYMENT_GUIDE.md Dockerfile Procfile railway.json .github/

echo "Deployment package created: dex-dumper-bot.zip"

echo ""
echo "To deploy to Railway:"
echo "1. Go to https://railway.app"
echo "2. Create new project"
echo "3. Upload this folder or connect your GitHub repo"
echo "4. Add environment variable:"
echo "   BOT_TOKEN = 8293626156:AAFO4sWwcQe1PjyyQZS1hi7Rd1t8SZye14k"
echo "5. Deploy"

echo ""
echo "To deploy to Render:"
echo "1. Go to https://render.com"
echo "2. Create new Web Service"
echo "3. Connect your GitHub repo or upload files"
echo "4. Set environment variable:"
echo "   BOT_TOKEN = 8293626156:AAFO4sWwcQe1PjyyQZS1hi7Rd1t8SZye14k"
echo "5. Deploy"

echo ""
echo "Deployment guide is available in DEPLOYMENT_GUIDE.md"