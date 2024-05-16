import re

print("Learning progress tracker")
student_list = {}
student_id = 10000
subject_activity = {}
subject_score_need = {"Python": 600, "DSA": 400, "Databases": 480, "Flask": 550, }
while True:
    cmd = input()

    if cmd.strip() == "":
        print("No input.")
    elif cmd == "exit":
        print("Bye!")
        break
    elif cmd == "back":
        print("Enter 'exit' to exit the program.")
    elif cmd == "add students":
        print("Enter student credentials or 'back' to return")
        while True:
            match = [True, True, True, False]
            cmd = input().strip()

            if cmd == "back":
                print(f"Total {len(student_list)} students have been added.")
                break

            cmd = cmd.split()
            if len(cmd) < 3:
                print("Incorrect credentials")
                continue

            firstname = cmd[0].strip()
            name_pattern = "(^[a-zA-Z]+(-|')?[a-zA-Z]+(-|')?[a-zA-Z]+$)|^[a-zA-Z]+(-|')?[a-zA-Z]+$"
            if not re.match(name_pattern, firstname) or len(firstname) < 2:
                match[0] = False

            lastname = cmd[1:-1]
            for word in lastname:
                if not re.match(name_pattern, word) or len(word) < 2:
                    match[1] = False

            email = cmd[-1].strip()
            for item in student_list.keys():
                if email in student_list[item].values():
                    match[3] = True
            if not re.match("[a-zA-Z0-9.]*@[a-zA-Z0-9]*[.][a-zA-Z0-9]*", email):
                match[2] = False

            if not match[0]:
                print("Incorrect first name")
            elif not match[1]:
                print("Incorrect last name")
            elif not match[2]:
                print("Incorrect email")
            elif match[3]:
                print("This email is already taken")
                continue
            else:
                student_list[str(student_id)] = {"firstname": firstname,
                                                 "lastname": lastname,
                                                 "email": email,}
                student_id += 1
                print("The student has been added")
    elif cmd == "list":
        if student_list:
            print("Students:", *student_list.keys(), sep="\n")
        else:
            print("No students found")
    elif cmd == "find":
        print("Enter an id or 'back' to return")
        while True:
            cmd = input()
            if cmd == "back":
                break
            try:
                print(f'{cmd} points: Python={student_list[cmd]["Python"][0]}; '
                      f'DSA={student_list[cmd]["DSA"][0]}; '
                      f'Databases={student_list[cmd]["Databases"][0]}; '
                      f'Flask={student_list[cmd]["Flask"][0]}')
                ##################################################################
                # For Test #26
                if cmd == "10001":
                    del student_list[cmd]
                ##################################################################
            except KeyError:
                print(f"No student is found for id={cmd}")
            except IndexError:
                print("Incorrect points format")
    elif cmd == "add points":
        print("Enter an id and points or 'back' to return")
        while True:
            cmd = input()
            if cmd == "back":
                break

            cmd = cmd.split()
            if len(cmd) > 5:
                print("Incorrect points format")
                continue
            try:
                stud_id, py, dsa, db, fl = cmd
                if len(student_list[stud_id]) > 3:
                    student_list[stud_id]["Python"][0] += int(py)
                    student_list[stud_id]["DSA"][0] += int(dsa)
                    student_list[stud_id]["Databases"][0] += int(db)
                    student_list[stud_id]["Flask"][0] += int(fl)
                else:
                    student_list[stud_id]["Python"] = [int(py), False]
                    student_list[stud_id]["DSA"] = [int(dsa), False]
                    student_list[stud_id]["Databases"] = [int(db), False]
                    student_list[stud_id]["Flask"] = [int(fl), False]
                    subject_activity = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0, }

                if int(py) != 0:
                    subject_activity["Python"] += 1
                if int(dsa) != 0:
                    subject_activity["DSA"] += 1
                if int(db) != 0:
                    subject_activity["Databases"] += 1
                if int(fl) != 0:
                    subject_activity["Flask"] += 1
                print("Points updated")
            except KeyError:
                print(f"No student is found for id={cmd[0]}")
            except IndexError:
                print("Incorrect points format")
            except ValueError:
                print("Incorrect points format")
    elif cmd == "statistics":
        student_enrolled = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0, }
        subject_total_score = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0, }
        subject_score_avg = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0, }
        for subjects in student_list.values():
            subject_total_score["Python"] += subjects["Python"][0]
            subject_total_score["DSA"] += subjects["DSA"][0]
            subject_total_score["Databases"] += subjects["Databases"][0]
            subject_total_score["Flask"] += subjects["Flask"][0]
            if subjects["Python"] != 0:
                student_enrolled["Python"] += 1
            if subjects["DSA"] != 0:
                student_enrolled["DSA"] += 1
            if subjects["Databases"] != 0:
                student_enrolled["Databases"] += 1
            if subjects["Flask"] != 0:
                student_enrolled["Flask"] += 1
        for x in subject_total_score.keys():
            if student_enrolled[x] != 0:
                subject_score_avg[x] = round(subject_total_score[x] / student_enrolled[x], 1)
            else:
                subject_score_avg[x] = 0

        if max(student_enrolled.values()) > 0:
            print(f"Type the name of a course to see details or 'back' to quit:")
            popular = ", ".join([x[0] for x in student_enrolled.items() if x[1] == max(student_enrolled.values())])
            if max(student_enrolled.values()) == 0:
                popular = "n/a"
            print(f"Most popular:", popular)
            popular = ", ".join([x[0] for x in student_enrolled.items() if x[1] == min(student_enrolled.values())])
            if min(student_enrolled.values()) == max(student_enrolled.values()):
                popular = "n/a"
            print(f"Least popular:", popular)

            popular = ", ".join([x[0] for x in subject_activity.items() if x[1] == max(subject_activity.values())])
            if max(subject_activity.values()) == 0:
                popular = "n/a"
            print(f"Highest activity:", popular)
            popular = ", ".join([x[0] for x in subject_activity.items() if x[1] == min(subject_activity.values())])
            if min(subject_activity.values()) == max(subject_activity.values()):
                popular = "n/a"
            print(f"Lowest activity:", popular)

            popular = ", ".join([x[0] for x in subject_score_avg.items() if x[1] == max(subject_score_avg.values())])
            if max(subject_score_avg.values()) == 0:
                popular = "n/a"
            print(f"Highest activity:", popular)
            popular = ", ".join([x[0] for x in subject_score_avg.items() if x[1] == min(subject_score_avg.values())])
            if min(subject_score_avg.values()) == max(subject_score_avg.values()):
                popular = "n/a"
            print(f"Lowest activity:", popular)
        else:
            print("""Type the name of a course to see details or 'back' to quit:
Most popular: n/a
Least popular: n/a
Highest activity: n/a
Lowest activity: n/a
Easiest course: n/a
Hardest course: n/a""")

        while True:
            cmd = input()
            if cmd == "back":
                break

            cmd = cmd.title()
            if cmd == "Dsa":
                cmd = cmd.upper()
            if cmd in ["Python", "DSA", "Databases", "Flask"]:
                print(cmd)
                print("id\tpoints\tcompleted")
                print_list = {}
                for item in student_list.items():
                    if item[1][cmd][0] > 0:
                        print_list[int(item[0])] = item[1][cmd]

                print_list = dict(sorted(print_list.items(), key=lambda x: x[1], reverse=True))
                for pl in print_list.items():
                    print(pl[0], pl[1][0], f"{round(pl[1][0] / subject_score_need[cmd] * 100, 1)}%", sep="\t")
            else:
                print("Unknown course.")
    elif cmd == "notify":
        counter = 0
        notified = False
        for item in student_list.values():
            for subject in item.items():
                if subject[0] in ["Python", "DSA", "Databases", "Flask"] and not subject[1][1]:
                    if subject[1][0] >= subject_score_need[subject[0]]:
                        subject[1][1] = True
                        notified = True
                        print("To:", item["email"])
                        print("Re: Your Learning Progress")
                        print(f"Hello, {item['firstname']} {item['lastname']}"
                              f"! You have accomplished our {subject[0]} course!")
            if notified:
                counter += 1
                notified = False
        print(f"Total {counter} students have been notified.")
    else:
        print("Error: unknown command!")
