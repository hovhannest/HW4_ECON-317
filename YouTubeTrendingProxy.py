from YouTubeTrending_Requests_BeautifulSoup import YouTubeTrending_Requests_BeautifulSoup
from YouTubeTrendingInterface import YouTubeTrendingInterface
from YouTubeTrending_urllib2_lxml import YouTubeTrending_urllib2_lxml

class YouTubeTrendingProxy(YouTubeTrendingInterface):
    """description of class"""

    def __init__(self, method):
        if(method == "Requests_BeautifulSoup"):
            self._dataSource = YouTubeTrending_Requests_BeautifulSoup()
        elif(method == "urllib2_lxml"):
            self._dataSource = YouTubeTrending_urllib2_lxml()
        elif(method == "api"):
            print("api not implemented")
            self._dataSource = None
        else:
            print("wrong method " + method)
            self._dataSource = None

    def getData(self):
        if(self._dataSource is not None):
            self._dataSource.getData()


