
from YouTubeTrendingInterface import YouTubeTrendingInterface
import urllib2
from lxml import etree
from Utils import *

class YouTubeTrending_urllib2_lxml(YouTubeTrendingInterface):
    """description of class"""

    def getData(self):
        response = urllib2.urlopen("https://www.youtube.com/feed/trending")
        html = response.read()
        tree = etree.HTML(html)
        for div in tree.cssselect('div.yt-lockup-content'):
            heder = div.cssselect('h3.yt-lockup-title ')[0]
            title = heder.findall("a")[0]
            #print(title.text)
            url = "https://www.youtube.com" + title.attrib["href"]
            #print(url)
            duration = formatDuration(heder.findall("span")[0].text)
            #print(duration)
            for d in div.findall("div"):
                if("yt-lockup-byline" in d.attrib["class"]):
                    user = d
                if("yt-lockup-meta" in d.attrib["class"]):
                    meta = d
            user = user.findall("a")[0]
            #print(user.text)
            ul = meta.findall("ul")[0]
            for views in ul.findall("li"):
                if "views" in views.text:
                    break
            viewsi = formatViews(views.text)
            #print(viewsi)
            self._data.append({"URL": url, "title": title.text, "duration": duration, "username": user.text, "views":viewsi})
