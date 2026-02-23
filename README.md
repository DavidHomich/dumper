# DEX Dumper Bot

A cryptocurrency token monitoring bot that tracks new token listings on decentralized exchanges (DEX) and sends filtered notifications to Telegram.

## Features

- **DEX Monitoring**: Continuously monitors DEX Screener for new token pairs
- **Smart Filtering**: Filters out spam, scam, and low-quality tokens based on multiple criteria
- **Tax & Honeypot Checking**: Integrates with external services to check token taxes and honeypot status
- **Telegram Integration**: Sends formatted notifications to your Telegram channel/group
- **Customizable Filters**: Configurable thresholds for liquidity, FDV, token age, and more

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The bot uses several filtering parameters that can be adjusted in the code:

- `min_liquidity`: Minimum liquidity threshold ($10,000 by default)
- `min_fdv`: Minimum Fully Diluted Valuation ($50,000 by default)  
- `max_tax`: Maximum acceptable tax percentage (15% by default)
- `min_age_days`: Minimum token age in days (3 days by default)

## Usage

Run the bot:
```bash
python3 run_bot.py
```

The bot will start monitoring DEX Screener for new tokens and send notifications for tokens that pass all filters.

## Message Format

Notifications are formatted in a style similar to popular finder bots:

```
🔥 NEW TOKEN DISCOVERY 🔥

Finder_Bot
TOKEN/USDT - $0.00127

Finder
/SOLANA

Price Change:
5M: -99% 1H: -99%

Token name: BallWorld
Dexscreener price: 0.00127 → 0.00127$

Liquidity: $35,346.00
FDV: $2,500,000.00

Days: 878

Contract: GH7uAw9nFBQc7te92VKeZhM4EqfdtAEkKzLkmk5CrDNq

Tax: N/A% Buy / N/A% Sell
Token Tax: N/A% Buy / N/A% Sell

Honeypot: Unknown
DEXTscore: Medium

Finder Channel | Finder Subscription |
@FinderStatusBot | Rugcheck.xyz
```

## Filtering Criteria

The bot applies multiple layers of filtering:

1. **Liquidity Filter**: Tokens must meet minimum liquidity requirements
2. **FDV Filter**: Tokens must meet minimum Fully Diluted Valuation
3. **Age Filter**: Tokens must be older than minimum age threshold
4. **Spam Detection**: Names and symbols are checked against spam patterns
5. **Suspicious Patterns**: Extreme price changes are flagged
6. **Tax/Honeypot Check**: External services verify token safety (placeholder implementation)

## Integration Notes

For production use, you would need to integrate with actual tax/honeypot checking services:

- [Honeypot.is API](https://docs.honeypot.is/ishoneypot) for EVM tokens
- [Solsniffer API](https://www.solsniffer.com/api-service) for Solana tokens
- [RugDoc](https://rugdoc.io/honeypot/) for additional security checks

## Security

⚠️ **Important**: This is a monitoring tool only. Always do your own research before investing in any cryptocurrency token. The bot provides no guarantees about token safety or investment outcomes.