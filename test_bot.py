import asyncio
from dumper_bot import DexDumperBot
import json

async def test_bot():
    """Test the DEX dumper bot with sample data"""
    
    # Initialize bot with the provided token
    bot_token = "8293626156:AAFO4sWwcQe1PjyyQZS1hi7Rd1t8SZye14k"
    dumper_bot = DexDumperBot(bot_token)
    
    # Test token data similar to what DEX Screener might return
    test_token_data = {
        'baseToken': {
            'address': 'GH7uAw9nFBQc7te92VKeZhM4EqfdtAEkKzLkmk5CrDNq',
            'name': 'BallWorld',
            'symbol': 'BWL'
        },
        'quoteToken': {
            'address': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
            'name': 'USD Coin',
            'symbol': 'USDT'
        },
        'pairAddress': 'some_pair_address',
        'liquidity': {
            'usd': 35346.00,
            'base': 1000.00,
            'quote': 1000.00
        },
        'fdv': 2500000.00,
        'priceNative': 0.00127,
        'priceUsd': 0.00127,
        'priceChange': {
            'm5': -99,
            'h1': -99,
            'h6': -99,
            'h24': -99
        },
        'pairCreatedAt': 1695820800000,  # Timestamp in milliseconds
        'chainId': 'solana'
    }
    
    print("Testing token filtering...")
    
    # Test filtering
    is_valid, reason = dumper_bot.filter_token(test_token_data)
    print(f"Token filtering result: {is_valid}, Reason: {reason}")
    
    # Test spam name detection
    print("\nTesting spam name detection...")
    print(f"'BallWorld'/'BWL' is spam: {dumper_bot.is_spam_name('BallWorld', 'BWL')}")
    print(f"'MoonCoin'/'MOON' is spam: {dumper_bot.is_spam_name('MoonCoin', 'MOON')}")
    print(f"'FakeToken'/'FAKE' is spam: {dumper_bot.is_spam_name('FakeToken', 'FAKE')}")
    
    # Test suspicious patterns
    print("\nTesting suspicious patterns...")
    print(f"Normal token suspicious: {dumper_bot.has_suspicious_patterns(test_token_data)}")
    
    # Test message formatting
    print("\nTesting message formatting...")
    formatted_message = dumper_bot.format_token_message(test_token_data)
    print("Formatted message:")
    print(formatted_message[:500] + "..." if len(formatted_message) > 500 else formatted_message)
    
    # Test tax/honeypot checking (simulated)
    print("\nTesting tax/honeypot checking...")
    tax_info = await dumper_bot.check_token_taxes_and_honeypot('GH7uAw9nFBQc7te92VKeZhM4EqfdtAEkKzLkmk5CrDNq', 'solana')
    print(f"Tax info: {tax_info}")
    
    # Test message formatting with tax info
    print("\nTesting message formatting with tax info...")
    formatted_with_tax = dumper_bot.format_token_message(test_token_data, tax_info)
    print("Formatted message with tax info:")
    print(formatted_with_tax[:500] + "..." if len(formatted_with_tax) > 500 else formatted_with_tax)
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    asyncio.run(test_bot())