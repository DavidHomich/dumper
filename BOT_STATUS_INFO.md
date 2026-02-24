# DEX Dumper Bot - Status & Health Check Information

## Bot Online Status

Your bot is now configured and ready to use with the following details:

- **Bot Username**: @dump_sorry_bot
- **Bot Token**: 8442868358:AAF1WMiZTrgr3u4TXYvv1HNXg8vDp4QwQ0A
- **Bot Name**: dbot

## How to Check if the Bot is Online

### Method 1: Using the Status Test Script
Run the test script to verify bot connectivity and status:
```bash
python3 test_status.py
```

This will show:
- Connection status (online/offline)
- Uptime information
- Number of tokens found
- Number of messages sent
- Current filtering parameters

### Method 2: Direct API Check
You can test the bot's API connectivity by making a direct call to Telegram:
```bash
curl -X POST https://api.telegram.org/bot8442868358:AAF1WMiZTrgr3u4TXYvv1HNXg8vDp4QwQ0A/getMe
```

### Method 3: Through Telegram
Simply message your bot @dump_sorry_bot on Telegram to see if it responds.

## Bot Status Report

The bot now provides detailed status reports showing:

- **Online Since**: How long the bot has been running
- **Tokens Found**: Count of tokens that passed the filtering criteria
- **Messages Sent**: Total number of notifications sent
- **Current Filters**: Shows the active filtering parameters
- **Bot Token**: Partially masked token for verification

## Running the Bot

To start the bot:
```bash
python3 run_bot.py
```

The bot will:
1. Connect to the Telegram API
2. Verify its online status
3. Begin monitoring DEX Screener for new tokens
4. Apply filtering criteria to identify quality tokens
5. Send notifications for valid tokens found

## Bot Filtering Criteria

The bot uses the following filters:
- Minimum liquidity: $10,000
- Minimum FDV: $50,000
- Maximum tax: 15%
- Minimum token age: 3 days

## Troubleshooting

If the bot appears offline:
1. Check that the token is correct
2. Ensure internet connectivity
3. Verify that the bot hasn't been restricted by Telegram
4. Check the logs for any error messages

## Security Note

Keep your bot token secure and never share it publicly. The token has been updated in all relevant files.