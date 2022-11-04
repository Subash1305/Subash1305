import pymongo

import json

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['guvi_ds_lit']

information = mydb.guviproject

f = open('C:/Users/Windows 10/Downloads/students.json')

data = json.load(f)
print(data)
   
# for i in information.aggregate([{'$project' : {'name' : 1, 'total_marks' : {'$max' : '$scores.score'}}},
 #                              {'$sort' : {'total_marks' : -1}}, {'$limit' : 1}
  #                             ]):
   # print(i)  