from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from _config import TIME_ZONE

scheduler = AsyncIOScheduler(scheduler=BackgroundScheduler(timezone=TIME_ZONE))