from journal_old import journal
import datetime


def print_header():
    print("-----------------------------------------------------")
    print("-------------Welcome to Three-point diary------------")
    print("-----------------------------------------------------")


def run_event_loop():
    print("What do you want to do with your journal?")
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)

        elif cmd == 'a':
            journal_data = []
            new_entry = journal.journal_input()
            journal.add_entry(journal_data, new_entry)
            # journal.create_entry_string(entry_date)
            journal.save(journal_name, journal_data)

        elif cmd != 'x':
            print('wrong input')

    print('Goodbye.')
    # journal.save(journal_name, journal_data)


def list_entries(data):

    print("Your journal entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


    
def date_entry():
    t = datetime.datetime.now()
    t_str = t.strftime("%b-%d-%Y %H:%M")

def main():
    print_header()
    run_event_loop()


if __name__ == '__main__':
    main()
