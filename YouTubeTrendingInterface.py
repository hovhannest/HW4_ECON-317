import json
import csv

class YouTubeTrendingInterface(object):
    # [{"URL": url(string), "title": title(string), "duration": duration(int in sec.), "username": name(string), "views":views(int)}]    
    _data = []

    def getData(self):
        pass


    def saveToCsv(self, filename):
        keys = self._data[0].keys()
        with open(filename, 'wb') as fout:
            dict_writer = csv.DictWriter(fout, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self._data)


    def saveToJson(self, filename):
        with open(filename, 'wb') as fout:
            json.dump(self._data, fout)


