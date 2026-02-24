#!/usr/bin/env python3
"""
DEX Dumper Bot - Monitors DEX for new tokens and sends notifications to Telegram
"""
import asyncio
from dumper_bot import DexDumperBot
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

async def main():
    import os
    # Initialize bot with your token from environment variable
    bot_token = os.getenv('BOT_TOKEN', '8442868358:AAF1WMiZTrgr3u4TXYvv1HNXg8vDp4QwQ0A')
    
    print("Initializing DEX Dumper Bot...")
    print("Bot will monitor DEX Screener for new tokens and apply filtering...")
    
    dumper_bot = DexDumperBot(bot_token)
    
    try:
        # Start monitoring
        print("Starting to monitor DEX Screener...")
        print("IMPORTANT: To receive messages, send /start to @dump_sorry_bot on Telegram first!")
        await dumper_bot.monitor_dexscreener()
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"Bot error: {e}")

if __name__ == "__main__":
    print("DEX Dumper Bot")
    print("===============")
    print("This bot monitors DEX Screener for new tokens and sends filtered notifications to Telegram.")
    print("Press Ctrl+C to stop the bot.\n")
    
    asyncio.run(main())