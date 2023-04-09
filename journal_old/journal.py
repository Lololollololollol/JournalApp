import datetime
import os


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('../journals/', name + '.jrl'))
    return filename


def load(name):
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
            # for entry in list(fin):
                data.append(entry.rstrip())

    return data


def journal_input():
    entry = dict()
    d = datetime.date.today()
    entry["date"] = d.strftime("%b-%d-%Y")
    entry["name"] = input("What's the title?")
    entry["bad"] = input("If any, What was the most challenging/regretful event/action from today?: ")
    entry["good"] = input("If any, What was the most grateful/happy event/moment you felt today?: ")
    entry["tomorrow"] = input("What do you expect from tomorrow?: ")
    return entry


def add_entry(journal_data: list, new_entry: dict) -> list:

    entry_date = {
        i: new_entry[i] for i in ['date', 'name', 'bad', 'good', 'tomorrow']
    }

    journal_data.append(entry_date)
    return journal_data


def create_entry_string(data: dict) -> str:
    entry_string = f"""tomorrow: {data['tomorrow']}, good: {data['good']}, bad: {data['bad']}, name: {data['name']}, date: {data['date']}"""

# entry_string = f"""name: {data['name']}
# bad: {data['bad']}
# good: {data['good']}
# tomorrow: {data['tomorrow']}
# date: {data['date']}"""


    return entry_string


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("..... saving to: {}".format(filename))

    with open(filename, 'a') as fout:
        for entry_date in journal_data:
            entry_string = create_entry_string(entry_date)
            fout.write(entry_string + '\r\n\n')
