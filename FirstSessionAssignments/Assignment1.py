# Part 1: Python Introduction and Data Types 
# 1 Personal Information 
name = "Birhane"
age = 21
height = 1.65
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Student: {is_student}")

# 2 Identify the Data Types 
name = "Abdurrahman"
age = 25
height = 1.75
is_student = True

print(f'Name: {name}, Type: {type(name)}')
print(f'Age: {age}, Type: {type(age)}')
print(f'Height: {height}, Type: {type(height)}')
print(f'Student: {is_student}, Type: {type(is_student)}')

# Part 2: Lists
# 3 Favourite Foods 
favorite_foods = ["Injera", "Doro", "Kitfo", "Tibis", "Dabo"]
print(f"Favorite Foods: {favorite_foods}")
print(f"First Favorite Food: {favorite_foods[0]}")
print(f"Last Favorite Food: {favorite_foods[-1]}")

favorite_foods.append("Shiro")
favorite_foods.remove("Kitfo")
favorite_foods[2] = "Firfir"
print(f"Final Favorite Foods: {favorite_foods}")

# 4 Student Scores
scores = [75, 80, 65, 90, 85]
print(f"Scores: {scores}")
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
scores.append(95)
print(f"Updated Scores: {scores}")

# Part 3 Tuples
# 5 Days of the Week 
week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(f"Days of the Week: {week}")
print(f"First Day: {week[0]}")
print(f"Last Day: {week[-1]}")
week[0] = "January"  # This will raise an error because tuples are immutable
# Question: Why is a tuple different from a list? 
# Answer: A tuple is immutable, meaning its elements cannot be changed after creation, while a list is mutable and allows modifications.


# Part 4: Sets
# 6 Remove Duplicate Values 
numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1]
list_numbers = set(numbers) 
print(f"Unique Numbers: {list_numbers}")
# Casting lists to sets removes duplicate values because sets only allow unique elements.


# 7 Unique Programming Languages 
Languages = ["Python", "Java", "Python", "C++", "JavaScript", "Python"]
set_languages = set(Languages)
print(f"Unique Languages: {set_languages}")
set_languages.add("Django") 

# Part 5: Dictionaries
# 8 Student Profile 
student_info = {"Name":"Abebe", "Age": 20, "Course":"Backend", "Level": "Beginner", 
                "Skills": ["Python", "JavaScript", "HTML"]}
print(f"Student Info: {student_info}")
print(f"Student Name: {student_info['Name']}")
student_info["Email"] = "birhane.telayneh@gmail.com"
student_info["Level"]= "Intermediate"
student_info.pop("Age")
print(f"Final Student Info: {student_info}")

# 9 Student Management Data 
Student1 = {"Name": "Abebe", "Age": 20, "Course": "Backend", "Skills": ["Python", "JavaScript", "HTML"]}
Student2 = {"Name": "Kebede", "Age": 21, "Course": "Frontend", "Level": "Intermediate", "Skills": ["CSS", "JavaScript", "React"]}
student3 = {"Name": "Glory", "Age": 22, "Course": "Fullstack", "Level": "Advanced", "Skills": ["Python", "Django", "React"]}

print(f"Student1:\n Name: {Student1['Name']}\n Age: {Student1['Age']}\n Course: {Student1['Course']}\n Skills: {Student1['Skills'][0]}, {Student1['Skills'][1]}, {Student1['Skills'][2]}")
print(f"Student2:\n Name: {Student2['Name']}\n Age: {Student2['Age']}\n Course: {Student2['Course']}\n Skills: {Student2['Skills'][0]}, {Student2['Skills'][1]}, {Student2['Skills'][2]}")
print(f"Student3:\n Name: {student3['Name']}\n Age: {student3['Age']}\n Course: {student3['Course']}\n Skills: {student3['Skills'][0]}, {student3['Skills'][1]}, {student3['Skills'][2]}")
