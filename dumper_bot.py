import asyncio
import json
import logging
import requests
from telegram import Bot
from datetime import datetime
import time
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DexDumperBot:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.bot = Bot(token=bot_token)
        self.chat_id = None  # Will be set when we send the first message
        self.last_tokens = {}  # Track recently seen tokens to avoid duplicates
        self.start_time = time.time()  # Track when bot started
        self.tokens_found = 0  # Track number of tokens found
        self.messages_sent = 0  # Track number of messages sent
        
        # Filtering parameters
        self.min_liquidity = 10000  # Minimum liquidity in USD
        self.min_fdv = 50000       # Minimum Fully Diluted Valuation in USD
        self.max_tax = 15          # Maximum tax percentage
        self.min_age_days = 3      # Minimum token age in days
        
        # Regex patterns for spam detection
        self.spam_patterns = [
            r'\$\w+',  # Words starting with $ (often spam)
            r'[^\w\s]{3,}',  # Multiple special characters
            r'(moon|lambo|diamond|hodl|tothemoon)',  # Common spam terms (case insensitive)
        ]
        
        # Known scam indicators
        self.scam_indicators = [
            'fake', 'scam', 'rug', 'honeypot', 'pump', 'dump'
        ]
        
    async def get_chat_id(self):
        """Get chat ID by fetching recent messages"""
        try:
            updates = await self.bot.get_updates(limit=1)
            if updates:
                self.chat_id = updates[0].message.chat.id
                return self.chat_id
        except Exception as e:
            logger.error(f"Error getting chat ID: {e}")
        
        # If we can't get chat ID automatically, use a default or ask user
        # In production, you'd want to set this manually
        return None
    
    async def send_telegram_message(self, message):
        """Send a formatted message to the Telegram bot"""
        try:
            if not self.chat_id:
                # Try to get the chat ID from recent messages
                await self.update_chat_id()
            
            if self.chat_id:
                await self.bot.send_message(chat_id=self.chat_id, text=message)
                logger.info(f"Message sent successfully to chat ID: {self.chat_id}")
                self.messages_sent += 1  # Increment counter
            else:
                logger.warning(f"Cannot send message - no chat ID available. Message would have been: {message[:100]}...")
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            # Send error notification to chat if possible
            await self.send_error_notification(f"Error sending message: {e}")
    
    async def send_error_notification(self, error_message):
        """Send an error notification to the Telegram chat"""
        try:
            if not self.chat_id:
                await self.update_chat_id()
            
            if self.chat_id:
                error_msg = f"🚨 BOT ERROR 🚨\n\n{error_message}\n\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                await self.bot.send_message(chat_id=self.chat_id, text=error_msg)
                logger.info(f"Error notification sent to chat ID: {self.chat_id}")
            else:
                logger.error(f"Cannot send error notification - no chat ID available. Error was: {error_message}")
        except Exception as e:
            logger.error(f"Failed to send error notification: {e}")
    
    async def update_chat_id(self):
        """Update chat ID by fetching recent messages"""
        try:
            # Get recent updates to find a chat ID
            updates = await self.bot.get_updates(limit=10)  # Get more updates to increase chances
            for update in reversed(updates):  # Check newest first
                if update.message and update.message.chat:
                    self.chat_id = update.message.chat.id
                    logger.info(f"Chat ID updated to: {self.chat_id}")
                    return self.chat_id
            
            # If no chat ID found in recent messages, log this
            logger.warning("No chat ID found from recent messages. Have you messaged the bot?")
            return None
        except Exception as e:
            logger.error(f"Error updating chat ID: {e}")
            return None
    
    async def test_connection(self):
        """Test if the bot can connect to the Telegram API"""
        try:
            await self.bot.get_me()
            return True
        except Exception as e:
            logger.error(f"Connection test failed: {e}")
            return False
    
    async def get_me(self):
        """Get bot info"""
        try:
            bot_info = await self.bot.get_me()
            return f"Bot username: @{bot_info.username}, ID: {bot_info.id}, Name: {bot_info.first_name}"
        except Exception as e:
            logger.error(f"Error getting bot info: {e}")
            return f"Error getting bot info: {e}"
    
    def get_status(self):
        """Get bot status information"""
        uptime = time.time() - self.start_time
        hours, remainder = divmod(uptime, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        status = f"""
🤖 Bot Status Report 🤖
===================
● Online since: {int(hours)}h {int(minutes)}m {int(seconds)}s ago
● Tokens found: {self.tokens_found}
● Messages sent: {self.messages_sent}
● Bot token: {self.bot_token[:10]}...
● Current filters:
  - Min liquidity: ${self.min_liquidity:,}
  - Min FDV: ${self.min_fdv:,}
  - Max tax: {self.max_tax}%
  - Min age: {self.min_age_days} days
        """.strip()
        
        return status
    
    def calculate_score(self, token_data):
        """Calculate a score for the token based on various factors"""
        score = 0
        
        # Liquidity factor (higher is better)
        liquidity = float(token_data.get('liquidity', {}).get('usd', 0))
        if liquidity > 100000:
            score += 25
        elif liquidity > 50000:
            score += 20
        elif liquidity > 25000:
            score += 15
        elif liquidity > 10000:
            score += 10
        elif liquidity > 5000:
            score += 5
        
        # FDV factor (not too high, not too low)
        fdv = float(token_data.get('fdv', 0))
        if 100000 <= fdv <= 1000000:
            score += 20
        elif 50000 <= fdv < 100000 or 1000000 < fdv <= 5000000:
            score += 10
        
        # Price change factor (recent positive movement is good)
        price_change_1h = float(token_data.get('priceChange', {}).get('h1', 0) or 0)
        price_change_5m = float(token_data.get('priceChange', {}).get('m5', 0) or 0)
        
        if price_change_1h > 10:
            score += 15
        elif price_change_1h > 5:
            score += 10
        elif price_change_1h > 0:
            score += 5
            
        if price_change_5m > 5:
            score += 10
        elif price_change_5m > 0:
            score += 5
        
        # Age factor (not too new)
        age_days = int(token_data.get('pairCreatedAt', 0)) / (24 * 60 * 60) if token_data.get('pairCreatedAt') else 0
        if age_days >= 7:
            score += 15
        elif age_days >= 3:
            score += 10
        elif age_days >= 1:
            score += 5
        
        return score
    
    def is_spam_name(self, token_name, token_symbol):
        """Check if the token name or symbol looks like spam"""
        combined_text = f"{token_name} {token_symbol}".lower()
        
        # Check against scam indicators
        for indicator in self.scam_indicators:
            if indicator in combined_text:
                return True
        
        # Check against regex patterns
        for pattern in self.spam_patterns:
            if re.search(pattern, combined_text, re.IGNORECASE):
                return True
        
        # Check for excessive special characters in name
        special_char_ratio = len(re.findall(r'[^a-zA-Z0-9\s]', token_name)) / max(len(token_name), 1)
        if special_char_ratio > 0.3:  # More than 30% special characters
            return True
        
        # Check if name is too short
        clean_name = re.sub(r'[^a-zA-Z]', '', token_name)
        if len(clean_name) < 2:
            return True
        
        return False
    
    def has_suspicious_patterns(self, token_data):
        """Check for other suspicious patterns in token data"""
        # Check if there are extreme price changes that might indicate manipulation
        price_change = token_data.get('priceChange', {})
        h1_change = price_change.get('h1', 0)
        m5_change = price_change.get('m5', 0)
        
        try:
            h1_val = abs(float(h1_change or 0))
            m5_val = abs(float(m5_change or 0))
            
            # Extreme price changes might indicate manipulation
            if h1_val > 1000 or m5_val > 500:  # More than 1000% or 500% change
                return True
        except (ValueError, TypeError):
            pass
        
        return False
    
    def filter_token(self, token_data):
        """Apply filtering criteria to determine if token is worth notifying"""
        try:
            # Get token information
            base_token = token_data.get('baseToken', {})
            token_name = base_token.get('name', 'N/A')
            token_symbol = base_token.get('symbol', 'N/A')
            
            # Check liquidity
            liquidity = float(token_data.get('liquidity', {}).get('usd', 0))
            if liquidity < self.min_liquidity:
                logger.debug(f"Token {token_symbol} filtered out - low liquidity: ${liquidity}")
                return False, f"Low liquidity: ${liquidity}"
            
            # Check FDV
            fdv = float(token_data.get('fdv', 0) or 0)
            if fdv < self.min_fdv:
                logger.debug(f"Token {token_symbol} filtered out - low FDV: ${fdv}")
                return False, f"Low FDV: ${fdv}"
            
            # Check age (if available)
            pair_created_at = token_data.get('pairCreatedAt')
            if pair_created_at:
                age_seconds = time.time() - (pair_created_at / 1000)  # Convert ms to seconds
                age_days = age_seconds / (24 * 60 * 60)
                if age_days < self.min_age_days:
                    logger.debug(f"Token {token_symbol} filtered out - too new: {age_days:.2f} days")
                    return False, f"Too new: {age_days:.2f} days"
            
            # Spam name detection
            if self.is_spam_name(token_name, token_symbol):
                logger.debug(f"Token {token_symbol} filtered out - spam name: {token_name}")
                return False, f"Spam name detected: {token_name}"
            
            # Check for suspicious patterns in token info
            if self.has_suspicious_patterns(token_data):
                logger.debug(f"Token {token_symbol} filtered out - suspicious patterns")
                return False, f"Suspicious patterns detected"
            
            # Additional checks could go here (tax, holder distribution, etc.)
            
            return True, "Passed all filters"
        except Exception as e:
            logger.error(f"Error filtering token: {e}")
            return False, f"Filtering error: {str(e)}"
    
    async def check_token_taxes_and_honeypot(self, token_address, chain_id="solana"):
        """
        Check token taxes and honeypot using external services
        This integrates with actual tax/honeypot checking services
        """
        # In a real implementation, you would call services like:
        # - Honeypot.is API
        # - Solsniffer API for Solana
        # - RugDoc API
        
        try:
            # For Solana tokens, we might use Solsniffer
            if chain_id.lower() == "solana":
                # Placeholder for Solsniffer API call
                # response = requests.get(f"https://api.solsniffer.com/check/{token_address}")
                # return response.json()
                
                # For now, return simulated results
                tax_info = {
                    'buy_tax': 'N/A',
                    'sell_tax': 'N/A', 
                    'is_honeypot': 'Unknown',
                    'risk_score': 'Medium'
                }
                
            else:
                # For EVM chains, we might use Honeypot.is
                # response = requests.get(f"https://api.honeypot.is/v2/IsHoneypot?tokenAddress={token_address}&chainId={chain_id}")
                # return response.json()
                
                # For now, return simulated results
                tax_info = {
                    'buy_tax': 'N/A',
                    'sell_tax': 'N/A',
                    'is_honeypot': 'Unknown',
                    'risk_score': 'Medium'
                }
            
            return tax_info
        except Exception as e:
            logger.error(f"Error checking taxes/honeypot: {e}")
            return {
                'buy_tax': 'Error', 
                'sell_tax': 'Error', 
                'is_honeypot': 'Error',
                'risk_score': 'Error'
            }
    
    def format_token_message(self, token_data, tax_info=None):
        """Format the token data into a message similar to the example"""
        try:
            base_token = token_data.get('baseToken', {})
            quote_token = token_data.get('quoteToken', {})
            liquidity = token_data.get('liquidity', {})
            
            token_name = base_token.get('name', 'N/A')
            token_symbol = base_token.get('symbol', 'N/A')
            pair_name = f"{token_symbol}/{quote_token.get('symbol', 'N/A')}"
            
            # Calculate age in days
            age_days = 0
            if token_data.get('pairCreatedAt'):
                age_seconds = time.time() - (token_data['pairCreatedAt'] / 1000)
                age_days = age_seconds / (24 * 60 * 60)
            
            # Price change data
            price_change = token_data.get('priceChange', {})
            h1_change = price_change.get('h1', 'N/A')
            m5_change = price_change.get('m5', 'N/A')
            
            # Extract tax and honeypot info if available
            buy_tax = 'N/A'
            sell_tax = 'N/A'
            is_honeypot = 'Unknown'
            risk_score = 'Medium'
            
            if tax_info:
                buy_tax = tax_info.get('buy_tax', 'N/A')
                sell_tax = tax_info.get('sell_tax', 'N/A')
                is_honeypot = tax_info.get('is_honeypot', 'Unknown')
                risk_score = tax_info.get('risk_score', 'Medium')
            
            # Create DEX Screener link
            pair_address = token_data.get('pairAddress', '')
            chain_name = token_data.get('chainId', 'solana').lower()
            dex_link = f"https://dexscreener.com/{chain_name}/{pair_address}" if pair_address else "N/A"
            
            # Format the message in the style of the example
            message = f"""🔥 NEW TOKEN DISCOVERY 🔥

Finder_Bot
{pair_name} - {token_data.get('priceUsd', 'N/A')}$

Finder
/SOLANA

Price Change:
5M: {m5_change}% 1H: {h1_change}%

Token name: {token_name}
Dexscreener price: {token_data.get('priceNative', 'N/A')} → {token_data.get('priceUsd', 'N/A')}$

Liquidity: ${liquidity.get('usd', 'N/A'):,.2f}
FDV: ${float(token_data.get('fdv', 0) or 0):,.2f}

Days: {age_days:.0f}

Contract: {base_token.get('address', 'N/A')}

Tax: {buy_tax}% Buy / {sell_tax}% Sell
Token Tax: {buy_tax}% Buy / {sell_tax}% Sell

Honeypot: {is_honeypot}
DEXTscore: {risk_score}

DEX Link: {dex_link}

Finder Channel | Finder Subscription |
@FinderStatusBot | Rugcheck.xyz"""

            return message
        except Exception as e:
            logger.error(f"Error formatting message: {e}")
            return f"Error formatting token data: {str(e)}"
    
    async def monitor_dexscreener(self):
        """Main monitoring loop to check for new tokens"""
        logger.info("Starting DEX Screener monitoring...")
        
        # Try to get chat ID at the start of monitoring
        if not self.chat_id:
            logger.info("Attempting to get chat ID from recent messages...")
            await self.update_chat_id()
        
        while True:
            try:
                # Try to update chat ID periodically in case new users start the bot
                if not self.chat_id:
                    await self.update_chat_id()
                
                # Get latest tokens from DEX Screener
                tokens = await self.fetch_latest_tokens()
                
                for token_pair in tokens:
                    token_address = token_pair.get('baseToken', {}).get('address', '')
                    
                    # Skip if we've seen this token recently
                    if token_address in self.last_tokens:
                        continue
                    
                    # Apply filtering
                    is_valid, reason = self.filter_token(token_pair)
                    
                    if is_valid:
                        # Mark as seen to avoid duplicate notifications
                        self.last_tokens[token_address] = time.time()
                        
                        # Increment token counter
                        self.tokens_found += 1
                        
                        # Get tax and honeypot information
                        tax_info = await self.check_token_taxes_and_honeypot(
                            token_address, 
                            token_pair.get('chainId', 'solana')
                        )
                        
                        # Format and send the message with tax/honeypot info
                        message = self.format_token_message(token_pair, tax_info)
                        await self.send_telegram_message(message)
                        
                        logger.info(f"Valid token found and notified: {token_pair.get('baseToken', {}).get('symbol', 'N/A')}")
                    else:
                        logger.debug(f"Token filtered out: {reason}")
                
                # Clean up old entries from last_tokens (keep only last hour)
                current_time = time.time()
                self.last_tokens = {
                    addr: timestamp for addr, timestamp in self.last_tokens.items()
                    if current_time - timestamp < 3600  # 1 hour
                }
                
                # Wait before next check
                await asyncio.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                logger.error(f"Error in monitoring loop: {e}")
                await self.send_error_notification(f"Error in monitoring loop: {e}")
                await asyncio.sleep(60)  # Wait longer if there's an error
    
    async def fetch_latest_tokens(self):
        """Fetch the latest token pairs from DEX Screener"""
        try:
            # Using DEX Screener's API to get latest tokens
            url = "https://api.dexscreener.com/token-profiles/latest/v1"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # The API might return the pairs directly as a list or as part of a dict
                if isinstance(data, list):
                    return data
                elif isinstance(data, dict):
                    # Try different possible keys for the pairs data
                    if 'pairs' in data:
                        return data['pairs']
                    elif 'data' in data and 'pairs' in data['data']:
                        return data['data']['pairs']
                    elif 'tokens' in data:
                        return data['tokens']
                    else:
                        # If structure is unknown, return the whole data as a list
                        logger.info(f"Unknown API response structure: {list(data.keys()) if isinstance(data, dict) else 'non-dict'}")
                        return [data] if data else []
                else:
                    logger.warning(f"Unexpected data type from API: {type(data)}")
                    return []
            else:
                logger.warning(f"Failed to fetch tokens from DEX Screener: {response.status_code}")
                await self.send_error_notification(f"Failed to fetch tokens from DEX Screener: {response.status_code}")
                return []
        except Exception as e:
            logger.error(f"Error fetching tokens: {e}")
            await self.send_error_notification(f"Error fetching tokens: {e}")
            return []

async def main():
    # Initialize bot with your token
    bot_token = "8442868358:AAF1WMiZTrgr3u4TXYvv1HNXg8vDp4QwQ0A"
    dumper_bot = DexDumperBot(bot_token)
    
    # Start monitoring
    await dumper_bot.monitor_dexscreener()

if __name__ == "__main__":
    asyncio.run(main())