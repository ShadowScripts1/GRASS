import asyncio
import random
import ssl
import json
import time
import uuid
import websockets
from loguru import logger
from fake_useragent import UserAgent

# Create a random user agent for Windows, PC, and Chrome browser
user_agent = UserAgent(os='windows', platforms='pc', browsers='chrome')
random_user_agent = user_agent.random

# Function to connect to the WebSocket server
async def connect_to_wss(user_id):
    device_id = str(uuid.uuid4())  # Generate a unique device ID
    logger.info(device_id)  # Log the device ID
    while True:
        try:
            # Sleep for a random interval before continuing
            await asyncio.sleep(random.randint(1, 10) / 10)
            
            # Set the custom headers for the WebSocket connection
            custom_headers = {
                "User-Agent": random_user_agent,
            }

            # Create SSL context for secure WebSocket connection
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            # List of possible WebSocket server URLs
            urilist = ["wss://proxy2.wynd.network:4444/", "wss://proxy2.wynd.network:4650/"]
            uri = random.choice(urilist)  # Select a random URI from the list
            server_hostname = "proxy2.wynd.network"

            # Connect to the WebSocket server with the specified URI and headers
            async with websockets.connect(uri, ssl=ssl_context, extra_headers=custom_headers,
                                          server_hostname=server_hostname) as websocket:
                # Function to send periodic PING messages to the server
                async def send_ping():
                    while True:
                        send_message = json.dumps(
                            {"id": str(uuid.uuid4()), "version": "1.0.0", "action": "PING", "data": {}})
                        logger.debug(send_message)  # Log the PING message
                        await websocket.send(send_message)  # Send the message to the server
                        await asyncio.sleep(5)  # Wait for 5 seconds before sending the next PING

                await asyncio.sleep(1)
                asyncio.create_task(send_ping())  # Start sending PING messages concurrently

                while True:
                    # Receive the server's response
                    response = await websocket.recv()
                    message = json.loads(response)
                    logger.info(message)  # Log the response message

                    # Handle different types of messages
                    if message.get("action") == "AUTH":
                        # Send an authentication response to the server
                        auth_response = {
                            "id": message["id"],
                            "origin_action": "AUTH",
                            "result": {
                                "browser_id": device_id,
                                "user_id": user_id,
                                "user_agent": custom_headers['User-Agent'],
                                "timestamp": int(time.time()),
                                "device_type": "desktop",
                                "version": "4.28.1",
                            }
                        }
                        logger.debug(auth_response)  # Log the authentication response
                        await websocket.send(json.dumps(auth_response))  # Send the response to the server

                    elif message.get("action") == "PONG":
                        # Send a PONG response to the server
                        pong_response = {"id": message["id"], "origin_action": "PONG"}
                        logger.debug(pong_response)  # Log the PONG response
                        await websocket.send(json.dumps(pong_response))  # Send the PONG response

        except Exception as e:
            # Log any errors that occur during the connection
            logger.error(e)

# Main function to prompt for user ID and start the connection
async def main():
    # Find the user_id on the site in the console localStorage.getItem('userId')
    # If you can't get it, just write allow pasting
    _user_id = input('Please Enter your user ID: ')
    await connect_to_wss(_user_id)  # Start the WebSocket connection with the provided user ID

if __name__ == '__main__':
    asyncio.run(main())  # Run the main function asynchronously
