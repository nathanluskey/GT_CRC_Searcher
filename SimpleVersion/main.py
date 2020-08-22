from requests import get
from bs4 import BeautifulSoup
from secrets import secrets
from time import sleep
from random import randint

def loadCRC(verbose = False):
    """Loads the CRC Webpage
    Parameters
    ----------
    verbose : bool, optional
        Default False. For printing out useful information.

    Returns
    -------
    openings : dict
        the raw HTML text of the webpage
    """
    rawHTML = get(CRC_URL).text
    soup = BeautifulSoup(rawHTML, 'html.parser')
    allTimeCards = soup.find_all("div", class_="caption program-schedule-card-caption")
    # print("Type: {0}, Object: {1}".format(type(allTimeCards), allTimeCards)) 
    # Check if there are items
    openings = dict()
    if (len(allTimeCards) != 0):
        for timeCard in allTimeCards:
            #TODO: Impliment below comments
                # I think I'll store values in a dict as such:
                # key - hash the time + date string 
                # value - number of spots available
            pass
    if verbose:
        print("Total Time Cards = {}".format(len(allTimeCards)))
    return openings

def checkDifferences(new, old):
    """ Check the old and new CRC dicts to see if there's been an update
    
    Parameters
    new : dict
        The most recent CRC openings
    old : dict
        The previous CRC openings

    Returns
    CRCUpdates : str
        The formatted string in Markdown
    """
    CRCUpdates = ""
    # If there is any update to be made
    if (new != old):
        # If the new dict isn't empty
        CRCUpdates = "UPDATES TO CRC 1ST FLOOR:\n"
        if (bool(new)):
            # Check all keys in the new dict for three situations: 1) It's a new key, so a new timeslot opened
            #                                                      2) It's a new value, so somehow the timeslot changed
            #                                                      3) Nothing has changed
            for key in (new.keys()):
                if key in old:
                    # Check value to see only if change in number of spots
                    if (new[key] > old[key]):
                        CRCUpdates += "New Openings: {0}, {1} --> {2}\n".format(key, old[key], new[key])
                else:
                    # Add key to update
                    CRCUpdates += "New Date: {0}, {1}\n".format(key, new[key])
    return CRCUpdates

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
    response = get(URL).text
    if verbose:
        print("URL:\n\t{0}\nResponse:\n\t{1}".format(URL, response))

if __name__ == "__main__":
    # I made a bitly link to shorten CRC 1st floor
    CRC_URL = "https://b.gatech.edu/2ErPqzW"
    DELAY = 5# * 60
    # CRCOpenings = loadCRC()
    # For quick debugging using an arbitrary exmaple
    CRCOpenings = {"one" : 1}
    keepRunning = True
    while keepRunning:
        # Load CRC page
        # newCRCOpenings = loadCRC(verbose=True)
        # For quick debugging using an arbitrary update
        newCRCOpenings = {"one" : 2, "two" : 3}
        # Check if there are changes over the last check
        CRCUpdates = checkDifferences(newCRCOpenings, CRCOpenings)
        if (CRCUpdates != ""):
            message = "{0}\n[CRC Website](https://b.gatech.edu/2ErPqzW)".format(CRCUpdates)
            sendNotification(message, verbose=True)
            # Set new dict to the current openings
            CRCOpenings = newCRCOpenings
        # Pause for DELAY amount of seconds +/- 30 seconds
        sleep(DELAY + randint(-3, 3))
        # # For debugging only run through the loop once
        # keepRunning = False