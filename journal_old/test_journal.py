from unittest import TestCase
from journal import get_full_pathname, create_entry_string, add_entry
import datetime


class Test(TestCase):
    def test_get_full_pathname(self):
        name = 'file1'
        fpn = get_full_pathname(name)
        self.assertEqual("C:\\Users\\hailey\\PycharmProjects\\JournalApp\\journals\\file1.jrl", fpn,
                          'Wrong full pathname returned')



    def test_add_entry(self):
        expected_journal_data = [{'date':'t_str','name':'a', 'bad':'b', 'good':'c', 'tomorrow':'d'}]
        existing_journal_data = []
        # expected_journal_data = [{'date': '2022-04-01', 'name':'a', 'bad':'b', 'good':'c', 'tomorrow':'d'}]
        new_entry = {
            'date':'t_str',
            'name': 'a',
            'bad': 'b',
            'good': 'c',
            'tomorrow': 'd',
                  }
        returned_journal_data = add_entry(existing_journal_data, new_entry)



    def test_add_entry2(self):
        expected_journal_data = [
            {'date':'t_str2', 'name':'a', 'bad':'b', 'good':'c', 'tomorrow':'d'},
            {'date':'t_str', 'name': 'a', 'bad': 'b', 'good': 'c', 'tomorrow': 'd'}
        ]

        existing_journal_data = [
            {'date':'t_str2', 'name': 'a', 'bad': 'b', 'good': 'c', 'tomorrow': 'd'}
                    ]
        new_entry = {
            'date':'t_str',
            'name': 'a',
            'bad': 'b',
            'good': 'c',
            'tomorrow': 'd',
                  }
        returned_journal_data = add_entry(existing_journal_data, new_entry)

        self.assertEqual(expected_journal_data, returned_journal_data, 'wrong journal data')

    def test_date_entry(self):
        t = datetime.datetime(2022, 3, 1, 3, 10)
        t_str = t.strftime("%b-%d-%Y %H:%M")
        self.assertEqual('Mar-01-2022 03:10', t_str, 'wrong timestamp')

    def test_create_entry_string(self):
        expected_string = """name: A mango day
bad: mango surprised us while sleeping
good: made a great mango smoothie
tomorrow: make a fruit net for the falling mangos
created_time: 2022-03-20-19:10"""

        input_vars = {
            'name': 'A mango day',
            'bad': 'mango surprised us while sleeping',
            'good': 'made a great mango smoothie',
            'tomorrow': 'make a fruit net for the falling mangos',
            'created_time': datetime.datetime(2022, 3, 20, 19, 10)
        }

        entry_string = create_entry_string(input_vars)

        self.assertEqual(expected_string, entry_string, 'Generated entry string is wrong.')
