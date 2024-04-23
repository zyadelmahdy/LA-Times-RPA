from robocorp import browser
from robocorp.tasks import task
from RPA.Excel.Files import Files as Excel
from pathlib import Path
import os
import requests

FILE_NAME = "news_data.xlsx"
OUTPUT_DIR = Path(os.environ.get('ROBOT_ARTIFACTS'))
EXCEL_URL = f"/Users/zyadelmahdy/Documents/GitHub/robocorp-rpa{FILE_NAME}"


@task
def solve_challenge():
    """
    Solve the RPA challenge
    
    Downloads the source data excel and uses Playwright to solve rpachallenge.com from challenge
    """
    browser.configure(
        browser_engine="chromium",
        screenshot="only-on-failure",
        headless=True,
    )
    try:
        from shared.latimes import LATimes

        with LATimes(teardown=True) as bot:
            bot.load_first_page()
            print('Successfully loaded LA Times first page.')
            bot.search('education')
            bot.filter([])
            bot.sort_newest()
            bot.pull_data()
            # bot.export() 

    finally:
        # Place for teardown and cleanups
        # Playwright handles browser closing
        print('Done')
