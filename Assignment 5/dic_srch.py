marks = {"Viraj":100,"Yash":90,"Alice":85,"Rohan":70,"Rahul":75}
name = input("Enter Student's name: ")

if name in marks:
    print(f"{name}'s Marks:", marks[name])
else:
    print("Name not found")
