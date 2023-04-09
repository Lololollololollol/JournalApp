import pymongo

conn_str = 'mongodb+srv://admin01:1q2w3e@cluster0.ehepg.mongodb.net'
# conn_str = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn_str)
# https://www.mongodb.com/docs/manual/administration/connection-pool-overview/#:~:text=Definition,Connection%20pools%20are%20thread%2Dsafe.

db = client.journal_app

#insert some data
db.three_point.insert({})

