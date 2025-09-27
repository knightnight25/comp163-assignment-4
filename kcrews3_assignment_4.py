student_name = 'Kami Crews'
current_gpa = 4.0 
study_hours = 5
social_points = 30
stress_level = 45

print("Welcome these are the starting stats:")
print(f"Name: {student_name}")
print(f"GPA: {current_gpa}")
print(f"Study hours: {study_hours}")
print(f"Social points: {social_points}")
print(f"Stress leves: {stress_level}")

print("Choose your course load:")
print("L) Light (12 credits)")
print("S) Standard (15 credits)")
print("H) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == 'L':
    if current_gpa >= 2.5 and current_gpa < 3.0:
        study_hours = study_hours - 2
        stress_level = stress_level - 25
    else:
        study_hours = study_hours + 1
        stress_level = stress_level - 10

elif choice == 'S':
    if current_gpa >= 3.0 and current_gpa < 3.5:
        study_hours  = study_hours + 2
        stress_level = stress_level - 10
    else:
        study_hours = study_hours + 5
        stress_level = stress_level - 3

elif choice == 'H':
    if current_gpa >= 3.5:
        study_hours = study_hours + 5
        stress_level = stress_level - 5
    else:
        study_hours = study_hours + 10
        stress_level = stress_level + 5

else: 
    print("Your choice is invalid")

print("New stats after course load decision")
print(f"New weekly study hours: {study_hours}")
print(f"New current stress levels: {stress_level}")

study_options = ["Programming", "Math", "English", "History"]
print(f"Your study options are: {study_options} pick one: ")
study_choice = input()

if study_choice in study_options:
    if study_choice == "Programming":
        if current_gpa >= 3.5 or study_hours < 20:
            current_gpa = current_gpa + 0.15
            social_points = social_points - 5
        elif study_choice == "Math":
            current_gpa = current_gpa + 0.05
            social_points = social_points - 2
    elif study_choice == "English":
        if not (current_gpa < 2.0):
            social_points = social_points + 10
            current_gpa = current_gpa + 0.02
        elif study_choice == "History":
            social_points = social_points - 2
            current_gpa = current_gpa - 0.02
elif study_choice not in study_options:
    social_points = social_points - 3
    current_gpa = current_gpa - 0.03

print("New stats after study decision")
print(f"New Current GPA: {current_gpa}")
print(f"New Social Points: {social_points}")

type_choice = input("Enter a number 0-5: ")
if type_choice is int:
    print(end="")
elif type_choice is not int:
    print("Choose a valid number")

if current_gpa >= 3.5:
    if social_points >= 30:
        print(f"Ending 1: Star Student")
        print("You maintained good grades and a social life")
    else:
        print("Ending 2: Academic Weapon")
        print("You maintained an amazing GPA, but your social life suffered")
    
elif current_gpa >= 2.5:
    if stress_level <= 35:
        print("Ending 3: Low stress student")
        print("You achived an okay GPA without burning out")
    else:
        print("Ending 4: Stress student")
        print("Your GPA is okay, but your stress levels put you at risk for burnout")
    
else:
    print("Ending 5: Bad student")
    print("Your GPA is failing you need to reasses your study habits")

print("Final Stats")
print(f"Final GPA: {current_gpa:.2f}")
print(f"Final Study Hours: {study_hours}")
print(f"Final Social Points: {social_points}")
print(f"Final Stress Level: {stress_level}")