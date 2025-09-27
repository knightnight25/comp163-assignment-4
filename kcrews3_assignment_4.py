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