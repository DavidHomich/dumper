#!/usr/bin/env python3
"""
Script to periodically send status updates to the bot's chat
"""

import asyncio
import time
from dumper_bot import DexDumperBot


async def send_periodic_status():
    """Send periodic status updates to the bot's chat"""
    print("Setting up DEX Dumper Bot Status Updates...")
    print("=" * 50)
    
    # Initialize bot with the new token
    bot_token = "8442868358:AAF1WMiZTrgr3u4TXYvv1HNXg8vDp4QwQ0A"
    dumper_bot = DexDumperBot(bot_token)
    
    # Test connection first
    print("Testing bot connection...")
    if not await dumper_bot.test_connection():
        print("❌ Cannot connect to bot. Please check the token.")
        return
    
    print("✅ Bot connected successfully!")
    print("Sending periodic status updates every 30 minutes...")
    print("Press Ctrl+C to stop.\n")
    
    try:
        while True:
            # Prepare status message
            status_msg = f"📊 DEX Dumper Bot Status Update\n\n{dumper_bot.get_status()}\n\nLast update: {time.strftime('%Y-%m-%d %H:%M:%S')}"
            
            # Note: This would require the bot to have received a message from a user first
            # to get the chat_id, which is needed to send messages back
            print(f"Status update prepared: {status_msg}")
            print("Note: Actual message sending requires a valid chat_id from user interaction.")
            
            # Wait for 30 minutes before next update
            await asyncio.sleep(1800)  # 30 minutes
            
    except KeyboardInterrupt:
        print("\nStopping status updates...")
        print("Status updates stopped.")


if __name__ == "__main__":
    print("DEX Dumper Bot - Periodic Status Updates")
    print("=========================================")
    print("This script would send periodic status updates to the bot's chat.")
    print("Note: Requires the bot to have an active chat to send messages to.\n")
    
    asyncio.run(send_periodic_status())