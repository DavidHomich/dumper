# GitHub Repository Setup and Railway Deployment Instructions

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and log in to your account
2. Click the "New" button to create a new repository
3. Name your repository (e.g., "dex-dumper-bot")
4. Select "Public" (or "Private" if you prefer)
5. Do NOT initialize with README, .gitignore, or license (we'll add these files later)
6. Click "Create repository"

## Step 2: Upload Files to Your Repository

After creating the repository, you'll need to upload all the bot files:

### Option A: Using Command Line (Recommended)
1. Open Terminal/Command Prompt
2. Navigate to this directory:
   ```bash
   cd /Users/davydkhomych/Desktop/дамбер
   ```
3. Initialize git in the current directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: DEX Dumper Bot"
   ```
4. Add your GitHub repository as remote:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   ```
5. Push to GitHub:
   ```bash
   git branch -M main
   git push -u origin main
   ```

### Option B: Manual Upload
1. On your GitHub repository page, click "Add file" → "Upload files"
2. Drag and drop all files from this folder to the browser window
3. Click "Commit changes"

## Step 3: Deploy to Railway

1. Go to [Railway](https://railway.app) and sign in (you can use GitHub OAuth)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose the repository you just created
5. Railway will automatically detect the `Dockerfile` and configure the project
6. After the project is created, go to the "Settings" tab
7. Click "Variables" in the left sidebar
8. Add a new variable:
   - NAME: `BOT_TOKEN`
   - VALUE: `8293626156:AAFO4sWwcQe1PjyyQZS1hi7Rd1t8SZye14k`
9. Go back to "Overview" and click "Deploy Now" or wait for automatic deployment

## Step 4: Verify Deployment

1. Once deployed, you'll see logs showing the bot is running
2. The bot will start monitoring DEX Screener for new tokens
3. Valid tokens will be sent to your Telegram bot as notifications
4. You can view logs anytime to monitor the bot's activity

## Important Notes

- The bot will run 24/7 on Railway's servers
- Even if your computer is turned off, the bot continues to run
- You can stop/start the bot from the Railway dashboard
- The free tier on Railway should be sufficient for basic operation

## Updating the Bot

If you make changes to the bot:
1. Update the files in your GitHub repository
2. Railway will automatically redeploy the bot, or you can manually trigger a deployment

Your bot will be operational once the deployment completes successfully!