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
