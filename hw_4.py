import codecs
import csv
import urllib.request
from hw_2 import ExtendedList

url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
stream = urllib.request.urlopen(url)
csv_file = csv.reader(codecs.iterdecode(stream, 'utf-8'))

iris_lst = []
for i in csv_file:
    obj = ExtendedList(i)
    iris_lst.append(obj)


