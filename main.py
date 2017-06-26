import sys
reload(sys)
sys.setdefaultencoding('UTF8')
from YouTubeTrendingProxy import YouTubeTrendingProxy

def main():
    YouTube = YouTubeTrendingProxy("Requests_BeautifulSoup")
    #YouTube = YouTubeTrendingProxy("urllib2_lxml")
    #YouTube = YouTubeTrendingProxy("api")

    YouTube.getData()
    YouTube.saveToCsv("data.csv")
    YouTube.saveToJson("data.json")

if __name__ == "__main__":
    main()