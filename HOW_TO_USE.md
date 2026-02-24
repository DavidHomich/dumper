# How to Receive Messages from DEX Dumper Bot

## Setting Up Communication with the Bot

To receive token alerts from the DEX Dumper Bot, you need to initiate a conversation with it first.

### Step 1: Find the Bot
1. Open Telegram
2. Search for the bot: **@dump_sorry_bot**
3. Start a conversation by clicking "Start" or sending `/start`

### Step 2: Verify Connection
Once you send a message to the bot, it will register your chat ID and will be able to send you token alerts.

### Step 3: Monitor for Alerts
After initiating the conversation:
- The bot will monitor DEX Screener for new tokens
- When a token passes the filtering criteria, you'll receive an alert
- Alerts will include token details, price changes, liquidity, and links

## What to Expect

When the bot finds a promising token, you'll receive a message similar to:

```
🔥 NEW TOKEN DISCOVERY 🔥

Finder_Bot
TOKEN/SOL - $0.001234
Finder
/SOLANA

Price Change:
5M: 25% 1H: 45%

Token name: SampleToken
Dexscreener price: 0.001234 → $0.001234$

Liquidity: $15,000.00
FDV: $500,000.00

Days: 5

Contract: CONTRACT_ADDRESS_HERE

Tax: N/A% Buy / N/A% Sell
Token Tax: N/A% Buy / N/A% Sell

Honeypot: Unknown
DEXTscore: Medium

DEX Link: https://dexscreener.com/solana/CONTRACT_ADDRESS

Finder Channel | Finder Subscription |
@FinderStatusBot | Rugcheck.xyz
```

## Troubleshooting

If you're not receiving messages:
1. Make sure you've sent a message to @dump_sorry_bot
2. Check that you're using the correct bot (@dump_sorry_bot)
3. Verify the bot is running (check Railway deployment logs)
4. Ensure your privacy settings allow bots to message you

## Filtering Criteria

The bot only sends alerts for tokens that meet these criteria:
- Minimum liquidity: $10,000
- Minimum FDV: $50,000
- Maximum tax: 15%
- Minimum token age: 3 days
- Passes spam detection filters