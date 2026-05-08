import json
print("Welcome to Grade Manager")
grades = {
    "Math": [],
    "Physics": [],
    "Chemistry": [],
    "Biology": [],
    "Uzbek language": [],
    "Russian language": [],
    "English": [],
    "History": [],
    "Geography": [],
    "Informatics": [],
    "Art": [],
    "Physical education": []
}
def save_grades():
    with open("grades.json", "w") as f:
        json.dump(grades, f)
try:
    with open("grades.json", "r") as file:
        grades.update(json.load(file))
except (FileNotFoundError, json.JSONDecodeError):
    print("Fatal error: grades.json not found.")
def subject():
    for num, grade in enumerate(grades, 1):
        print(f"{num}. {grade}")
    subj = int(input("Subject: "))
    if subj == 1:
        return "Math"
    elif subj == 2:
        return "Physics"
    elif subj == 3:
        return "Chemistry"
    elif subj == 4:
        return "Biology"
    elif subj == 5:
        return "Uzbek language"
    elif subj == 6:
        return "Russian language"
    elif subj == 7:
        return "English"
    elif subj == 8:
        return "History"
    elif subj == 9:
        return "Geography"
    elif subj == 10:
        return "Informatics"
    elif subj == 11:
        return "Art"
    elif subj == 12:
        return "Physical education"
    else:
        print("Fatal error: subject was not found.")
    return None
def add_grade(grade , subject_name):
    global grades
    grades[subject_name].append(grade)
    save_grades()
def remove_grade(grade , subject_name):
    global grades
    if grade in grades[subject_name]:
        grades[subject_name].remove(grade)
    else:
        print("fatal error: grade not found")
    save_grades()
def avg_one(subject_name):
    if not grades[subject_name]:
        print("fatal error: no grades.")
        return
    avg1 = (sum(grades[subject_name]) / len(grades[subject_name]))
    print(f"The average of {subject_name}: {avg1}")
    if avg1 >= 9.5:
        print("The Best Performance! Keep it up!")
    elif avg1 >= 8:
        print("Great job! Continue in the same spirit!")
    elif avg1 >= 6:
        print("Good, but you can do better!")
    elif avg1 >= 4:
        print("You need to improve a bit!")
    else:
        print("Weak result — focus more on studying!")
def avg():
    all_grades = []
    for values in grades.values():
        all_grades.extend(values)
    if not all_grades:
        print("fatal error: no grades.")
        return
    avg2 = sum(all_grades) / len(all_grades)
    print('Your Performance: ',avg2)
    if avg2 >= 9.5:
        print("The Best Performance! Keep it up!")
    elif avg2 >= 8:
        print("Great job! Continue in the same spirit!")
    elif avg2 >= 6:
        print("Good, but you can do better!")
    elif avg2 >= 4:
        print("You need to improve a bit!")
    else:
        print("Weak result — focus more on studying!")
    for key, values in grades.items():
        if values and (sum(values) / len(values)) < 5:
            print(f'But you need to work more with {key}!')
def show_grades():
    for key, values in grades.items():
        print(key, ":", ", ".join(map(str, values)))
running = True
def exit_():
    global running
    running = False
    save_grades()

def main():
    while running:
        try:
            action = (int(input('1.Add grade\n2.Remove grade\n3.Average grade\n4.Show all grades\n5.Save grades\n0.Exit\nEnter your choice: ')))
            if action == 1:
                sub = subject()
                add_grade(int(input('Enter grade: ')) , sub)
            elif action == 2:
                sub  = subject()
                remove_grade(int(input('Enter grade: ')) , sub)
            elif action == 3:
                print('1.Avarege of one subject\n2.Avarege of all subjects ')
                choice_2 = int(input('Enter your choice: '))
                if choice_2 == 1:
                    sub = subject()
                    avg_one(sub)
                if choice_2 == 2:
                    avg()
            elif action == 4:
                show_grades()
            elif action == 5:
                save_grades()
            elif action == 0:
                save_grades()
                exit_()
        except ValueError:
            print("fatal error: invalid input.")
            continue
        except KeyboardInterrupt:
            print("fatal error: program terminated.")
            continue
        except ZeroDivisionError:
            print("fatal error: division by zero error.")
            continue
        except TypeError:
            print("fatal error: type error.")
            continue
main()
