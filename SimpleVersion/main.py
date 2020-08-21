import requests
from bs4 import BeautifulSoup
from secrets import secrets
from time import sleep

def loadCRC():
    rawText = requests.get(CRC_URL).text
    print(rawText)


if __name__ == "__main__":
    # I made a bitly link to shorten CRC 1st floor
    CRC_URL = "https://b.gatech.edu/2ErPqzW"
    DELAY = 5 * 60
    CRCOpenings = ""
    keepRunning = True
    while keepRunning:
        #TODO: Load CRC page
        NewCRCOpenings = loadCRC()
        #TODO: Check if there are changes over the last check
        if not(NewCRCOpenings == CRCOpenings):
            #TODO: Send out notification to all users via HTTPS Requests & Telegram API
            pass
        keepRunning = False