from datetime import datetime
import os


class Note:
    date_format = ["%Y-%m-%d %H:%M", "%Y-%m-%d"]
    calendar_notes = {}

    def __init__(self):
        self.current_date = datetime.now()

    def print_datetime(self):
        print("Current date and time:", self.current_date.strftime(Note.date_format[0]), sep='\n')

    @staticmethod
    def check_datetime(datetime_, type_):
        try:
            if type_ in ["birthday", "date"]:
                return datetime.strptime(datetime_, Note.date_format[1])
            else:
                return datetime.strptime(datetime_, Note.date_format[0])
        except ValueError:
            print("Incorrect date or time values")

    def read_file(self):
        self.calendar_notes.clear()
        if os.path.isfile("data.txt"):
            with open("data.txt", "r") as file:
                files = file.read().split("\n")[:-1]
                for item in files:
                    item = item.strip("()").split(", ")
                    if item[0] == "Note":
                        date = item[2].split(":")
                        schedule_date = self.check_datetime(f"{date[0]}:{date[1]}", item[0].lower())
                        days, hours, minutes = self.get_datetime(schedule_date)

                        print_ = f'Note: "{item[1]}" - {days} day(s), {hours} hour(s), {minutes} minute(s)'
                        self.calendar_notes[len(self.calendar_notes) + 1] = {"note": item[1],
                                                                             "message": print_,
                                                                             "date": schedule_date,
                                                                             "next_date": schedule_date,
                                                                             "days": days, }

                    else:
                        date = item[2].split()
                        birthdate = self.check_datetime(date[0], item[0].lower())
                        age, next_birthday, days = self.get_birthday(birthdate)

                        print_ = f'Birthday: "{item[1]} (turns {age})" - {days} day(s)'
                        self.calendar_notes[len(self.calendar_notes) + 1] = {"note": item[1],
                                                                             "message": print_,
                                                                             "date": birthdate,
                                                                             "next_date": next_birthday,
                                                                             "days": days, }

    def save_file(self):
        file = open("data.txt", "w")
        for item in self.calendar_notes.values():
            file.write(f'({item["message"].split(":")[0]}, {item["note"]}, {item["date"]})\n')
        file.close()
        self.calendar_notes.clear()

    def add_note(self, type_):
        new_notes = []
        try:
            if type_ == "note":
                notes = int(input("How many notes would you like to add: "))
                if notes < 1:
                    raise ValueError

                for num in range(notes):
                    schedule_date = input(f'{num + 1}. Enter datetime in "YYYY-MM-DD HH:MM" format: ')
                    schedule_date = self.check_datetime(schedule_date, type_)
                    note = input('Enter text: ')

                    days, hours, minutes = self.get_datetime(schedule_date)

                    print_ = f'Note: "{note}" - {days} day(s), {hours} hour(s), {minutes} minute(s)'
                    self.calendar_notes[len(self.calendar_notes) + 1] = {"note": note,
                                                                         "message": print_,
                                                                         "date": schedule_date,
                                                                         "next_date": schedule_date,
                                                                         "days": days, }
                    new_notes.append(print_)

            elif type_ == "birthday":
                notes = int(input("How many dates of birth would you like to add: "))
                if notes < 1:
                    raise ValueError

                for num in range(notes):
                    birthdate = input(f'{num + 1}. Enter date of birth in "YYYY-MM-DD" format: ')
                    birthdate = self.check_datetime(birthdate, type_)
                    name = input('Enter name: ')

                    age, next_birthday, days = self.get_birthday(birthdate)

                    print_ = f'Birthday: "{name} (turns {age})" - {days} day(s)'
                    self.calendar_notes[len(self.calendar_notes) + 1] = {"note": name,
                                                                         "message": print_,
                                                                         "date": birthdate,
                                                                         "next_date": next_birthday,
                                                                         "days": days, }
                    new_notes.append(print_)

            else:
                print("Incorrect type")
        except ValueError:
            print("Incorrect number")

        return new_notes

    def get_datetime(self, schedule_date):
        remaining_time = schedule_date - self.current_date
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes = remainder // 60 + 1

        if minutes == 60:
            hours, minutes = hours + 1, 0
        if hours == 24:
            days, hours = days + 1, 0

        return remaining_time.days, hours, minutes

    def get_birthday(self, birthdate):
        current_year = self.current_date.year
        next_birthday = birthdate.replace(year=current_year)
        age = current_year - birthdate.year

        if next_birthday < self.current_date:
            next_birthday = next_birthday.replace(year=current_year + 1)
            age += 1

        until_birthday = next_birthday - self.current_date

        return age, next_birthday, until_birthday.days + 1

    def action(self):
        self.read_file()
        cmd = input("Enter the command (add, view, delete, exit): ")

        if cmd == "add":
            type_ = input("Specify type (note, birthday): ")
            for item in self.add_note(type_):
                print(item)

            self.save_file()

        elif cmd == "view":
            filter_ = input("Specify filter (all, date, text, birthdays, notes, sorted): ")
            filtered_notes = []

            if filter_ == "notes":
                for item in self.calendar_notes.values():
                    if item["message"].startswith("Note:"):
                        filtered_notes.append(item["message"])

            elif filter_ == "birthdays":
                for item in self.calendar_notes.values():
                    if item["message"].startswith("Birthday:"):
                        filtered_notes.append(item["message"])

            elif filter_ == "text":
                text = input("Enter text: ")
                for item in self.calendar_notes.values():
                    if text.lower() in item["note"].lower():
                        filtered_notes.append(item["message"])

            elif filter_ == "date":
                date_ = input('Enter date in "YYYY-MM-DD" format: ')
                date_ = self.check_datetime(date_, filter_)
                for item in self.calendar_notes.values():
                    if date_.date() in [item["date"].date(), item["next_date"].date()]:
                        filtered_notes.append(item["message"])

            elif filter_ == "all":
                for item in self.calendar_notes.values():
                    filtered_notes.append(item["message"])

            elif filter_ == "sorted":
                sort_order = input("Specify way (ascending, descending): ")
                sorted_notes = self.calendar_notes.values()

                if sort_order == "ascending":
                    sorted_notes = sorted(sorted_notes, key=lambda x: (x["days"], x["note"]))
                elif sort_order == "descending":
                    sorted_notes = sorted(sorted_notes, key=lambda x: (x["days"], x["note"]), reverse=True)
                else:
                    print("Incorrect way")
                    exit()

                for item in sorted_notes:
                    filtered_notes.append(item["message"])

            else:
                print("Incorrect filter")
                exit()

            for item in filtered_notes:
                print(item)

        elif cmd == "delete":
            counter = 1
            for item in self.calendar_notes.items():
                print(f'{counter}.', item[1]["message"])
                counter += 1

            ids = input("Enter ids: ")
            if ids:
                to_delete = []
                ids = [int(x) for x in ids.split(',')]
                counter = 1
                for item in self.calendar_notes.items():
                    if counter in ids:
                        to_delete.append(item[0])
                    counter += 1
                for id_ in to_delete:
                    del self.calendar_notes[id_]

            self.save_file()

        elif cmd == "exit":
            print("Goodbye!")
            exit()
        else:
            print("Incorrect command")


calendar_ = Note()
calendar_.print_datetime()

while True:
    calendar_.action()
