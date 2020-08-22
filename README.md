# GT_CRC_Searcher
## Looking for Open Spots in the CRC
Links to each of the 4 areas found on the [GT CRC Website](https://mycrc.gatech.edu/Program/GetProducts?classification=1a69ef55-313a-45e5-b068-1a96056ae8d6)
This will only look for spots opening on the 1st Floor Fitness.

[Link to Join Telegram Group](https://t.me/joinchat/AAAAAFWJsvgYM9gVLDM6vQ)

Python Libraries:
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse HTML
- [Requests](https://requests.readthedocs.io/en/master/) to retrieve information for the CRC Website & send updates through Telegram
- [Time](https://docs.python.org/3/library/time.html) to have delays when reloading the page

Other Resources:
- [Telegram Bot API](https://core.telegram.org/bots/api) to send out notifications. I'm not using the python library because sending updates through HTTPS directly is easier.

TODO:
- Upload to AWS EC2 to run. Found [these instructions](https://medium.com/@praneeth.jm/running-python-scripts-on-an-aws-ec2-instance-8c01f9ee7b2f) which seem very helpful.
