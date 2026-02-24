#!/usr/bin/env python3
"""
Test script to check bot status and connectivity
"""

import asyncio
import time
from dumper_bot import DexDumperBot


async def test_bot_status():
    """Test the bot status functionality"""
    print("Testing DEX Dumper Bot Status...")
    print("=" * 40)
    
    # Initialize bot with the new token
    bot_token = "8442868358:AAF1WMiZTrgr3u4TXYvv1HNXg8vDp4QwQ0A"
    dumper_bot = DexDumperBot(bot_token)
    
    # Test connection
    print("Testing bot connection...")
    if await dumper_bot.test_connection():
        print("✅ Bot connection successful!")
        
        # Get bot info
        bot_info = await dumper_bot.get_me()
        print(f"📋 Bot Info: {bot_info}")
        
        # Get initial status
        print("\n📊 Initial Status:")
        print(dumper_bot.get_status())
        
        # Simulate some activity and check status again
        print("\n⏰ Waiting 5 seconds to show uptime...")
        await asyncio.sleep(5)
        
        print("\n📊 Updated Status:")
        print(dumper_bot.get_status())
        
    else:
        print("❌ Bot connection failed!")


if __name__ == "__main__":
    print("DEX Dumper Bot Status Test")
    print("==========================")
    print("This script tests the bot's connectivity and status reporting features.\n")
    
    asyncio.run(test_bot_status())