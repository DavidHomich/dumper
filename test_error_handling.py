#!/usr/bin/env python3
"""
Test script to verify error handling functionality
"""

import asyncio
from dumper_bot import DexDumperBot


async def test_error_handling():
    """Test the bot's error handling functionality"""
    print("Testing DEX Dumper Bot Error Handling...")
    print("=" * 50)
    
    # Initialize bot with the token
    bot_token = "8442868358:AAF1WMiZTrgr3u4TXYvv1HNXg8vDp4QwQ0A"
    dumper_bot = DexDumperBot(bot_token)
    
    # Test connection first
    print("Testing bot connection...")
    if await dumper_bot.test_connection():
        print("✅ Bot connection successful!")
        
        # Test error notification (without a chat_id, it should log the error)
        print("\nTesting error notification functionality...")
        await dumper_bot.send_error_notification("This is a test error notification")
        
        print("\n📝 Note: Since no chat_id is set, the error was logged but not sent to Telegram.")
        print("   To receive error notifications in Telegram, send /start to @dump_sorry_bot first.")
        
    else:
        print("❌ Bot connection failed!")


if __name__ == "__main__":
    print("DEX Dumper Bot - Error Handling Test")
    print("=====================================")
    print("This script tests the bot's error notification functionality.\n")
    
    asyncio.run(test_error_handling())