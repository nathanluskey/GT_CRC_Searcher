import requests
from bs4 import BeautifulSoup
from secrets import secrets
from time import sleep

def loadCRC():
    """Loads the CRC Webpage

    Returns
    -------
    rawText
        the raw HTML text of the webpage
    """
    rawText = requests.get(CRC_URL).text
    # TODO: Use bs4 to look format text into something useable
    # print(rawText)
    return rawText

def sendNotification(message, verbose=False):
    """Send out notification to all users via HTTPS Requests & Telegram API

    Parameters
    ----------
    message : str
        The message to be sent in the chat
    verbose : bool, optional
        Default False. For printing out useful information.
    """
    URL = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}&parse_mode=Markdown".format(secrets.CHAT_BOT_TOKEN, secrets.CHANNEL_ID, message)
    response = requests.get(URL)
    if verbose:
        print("URL:\n\t{0}\nResponse:\n\t{1}".format(URL, response))

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
            message = "Hello\nWorld!"
            sendNotification(message, verbose=True)
        keepRunning = False