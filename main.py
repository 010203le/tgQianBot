import asyncio
from _bot import start_bot

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())