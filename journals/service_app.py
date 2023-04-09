import datetime
import pymongo
import requests

import nosql.mongo_setup as mongo_setup
from nosql.three_point_journal import Journal

conn_str = "mongodb+srv://admin01:1q2w3e@cluster0.ehepg.mongodb.net"
client = pymongo.MongoClient(conn_str)
db = client.journal_app
col_good = db['good']


def main():
    print_header()
    config_mongo()
    user_loop()


def print_header():
    print('Welcome to Three-Point_Journal v.1')
    print()


def config_mongo():
    mongo_setup.global_init()


def list_journals():
    pass

def search_journals():
    search_key = input("What entries are you searching for?: ").lower().strip()
    result = db.three_point_journal.find({'good': {'$regex': search_key}})
    result = db.three_point_journal.find({'good': {'$regex': search_key}})
    print(result)
    # while search_key is None:
    #     search_key = input("What entries are you searching for?: ")
    # else:
    #     print(result)
    # db.three_point_journal.find()
    # result_count = db.three_point_journal.find({"good": {search_key}})
    # if result_count == 0:
    #    print("There's no records")
    # else:
    #     print(result)

    # for x in db.find({}, {"good": search_key}):
        # print(x)
    # result = db.find({}, {"date": search_date})
    # print(result)


def add_3p_journal():
    title = input("What's the title?")
    bad = input("If any, What was the most challenging/regretful event/action from today?: ")
    good = input("If any, What was the most grateful/happy event/moment you felt today?: ")
    tomorrow = input("What do you expect from tomorrow?: ")
    date = datetime.date.today()

    journal = Journal()
    journal.title = title
    journal.good = good
    journal.bad = bad
    journal.tomorrow = tomorrow
    journal.date = date

    journal.save()


def add_manifested_journals():
    pass
    # This function asks the random time in the future for what you want to see and send a notification on that date to the user
    #Example questions: what do you want to say to Hyunji from 2024/10/02 (Two years from now)
    # The email will be sent on 2024/10/02
    # Hi Hyunji, I'm glad and


def user_loop():
    cmd = None
    while cmd != 'x':
        cmd = input('[L]ist entries, Add an [3]p journal entry, [S]earch entries, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_journals()
        elif cmd == '3':
            add_3p_journal()
        elif cmd == 's':
            search_journals()
        elif cmd == 'm':
            add_manifested_journals()
        elif cmd == 's':
            search_journals()
        elif cmd != 'x':
            print('wrong input')
        # Todo: to add a dictionary
        # Todo: to show statistics


if __name__ == '__main__':
    main()
