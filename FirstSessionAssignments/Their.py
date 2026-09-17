#  Assignment: Student Information Manager Objective 
Name = "John"
Age = 23
Height = 1.75
is_currently_enrolled = False

# 1 List
Interests = ["Python", "Java", "Cooking", "Excersing", "Vlogging"]
print(f"First Interest: {Interests[0]}")
Interests.append("Traveling")
Interests.remove("Cooking")
print(f"Updated Interests: {Interests}")

# 2 Tuple
Favorite_numbers = (7, 12, 16, 21, 27)
print(f"Second Favorite Number: {Favorite_numbers[1]}")

# 3 Set
Hobbies = {"Reading", "Reading", "Swimming", 
           "Cycling","Photography", "Hiking", "Photography"}
print(f"Hobbies: {Hobbies}")
print("The duplicate values Reading and Photography are removed because sets only allow unique elements.")
Hobbies.add("Going to Church")

# 4 Dictionary
Student_Info = {"Name": "John", "Age": 23, "Height": 1.75, "is_currently_enrolled": False, 
                "Interests": Interests, "Favorite_numbers": Favorite_numbers, "Hobbies": Hobbies}
print(f"Student Name: {Student_Info['Name']}")
print(f"Skills: {Student_Info['Interests']}")
Student_Info["Country"] = "Ethiopia"
Student_Info["Age"] = 28
print(f"\nComplete Student Info: {Student_Info}")

# Bonus Challenge
my_info = {"Name": "Birhane", "Age": 21, 
           "Favorite_Pogramming_Languages": "Python"}
print(f"Hello, {my_info['Name']}! \nYou are {my_info['Age']} years old.\nYour favorite programming language is {my_info['Favorite_Pogramming_Languages']}.")
