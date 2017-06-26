
from YouTubeTrendingInterface import YouTubeTrendingInterface
import requests
from BeautifulSoup import *
import re
from Utils import *

class YouTubeTrending_Requests_BeautifulSoup(YouTubeTrendingInterface):
    """description of class"""

    def getData(self):
        res = requests.get("https://www.youtube.com/feed/trending")
        soup = BeautifulSoup(res.text)
        for div in soup.findAll("div", attrs={"class":"yt-lockup-content"}):
            heder = div.find("h3", attrs = {"class": "yt-lockup-title "})
            title = heder.find("a")
            #print(title.text)
            url = "https://www.youtube.com" + title['href']
            #print(url)
            duration = formatDuration(heder.find("span").text)
            #print(duration)
            user = div.find("div", attrs = {"class": re.compile("yt-lockup-byline.*")})
            #print(user.text)
            meta = div.find("div", attrs = {"class": "yt-lockup-meta "})
            ul = meta.find("ul")
            for views in ul.findAll("li"):
                if "views" in views.text:
                    break
            viewsi = formatViews(views.text)
            #print(viewsi)
            self._data.append({"URL": url, "title": title.text, "duration": duration, "username": user.text, "views":viewsi})


