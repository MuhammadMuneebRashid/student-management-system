# Function to add all students
def add_students():
# Take input from the user
    name=input("Enter the name:")
    marks=(input("Enter the marks :"))
# Opening file in append mode to store new records
    with open("file.txt","a") as f:
        f.write(name + "," + marks+"\n")
        print("Student added successfully")
# Function to view all students
def view_students():
    try:  
     # Opening file in read mode
        with open("file.txt","r") as f:
        # Read all record from the file
            records=f.readlines()
        # Check if the file is empty
            if(len(records))==0:
                print("No record found")
            else:
                print("\n --- Student Records ---") 
            # Display record of each student
                for record in records:
                # Separate name and marks
                    name,marks=record.strip().split(",")
                    print(f"Name:{name} , Marks:{marks}")
# Handles the FileNotFoundError
    except FileNotFoundError:
        print("No students record found")
# Function to search a student
def search_students():
    # Take input from the user
    search=input("Enter the name for search :")
    try:
    # Opening file in read mode
        with open ("file.txt","r")as f:
        # Record not Found
            found=False
            for record in f:
              name,marks=record.strip().split(",")
        # Check if the student's name matches the search name
              if(name . lower()== search.lower()):
                print(f"Name:{name} , Marks:{marks}")
            # Record Found
                found=True
                break
    # Display message if student is not found
            if not found:
                print("No student record found")
    # Handles FileNotFoundError
    except FileNotFoundError:
        print("No record  found")
# Student Managment System Menu
while True:
    print("=== Student Managment System ===")
    print("1. Add Students")
    print("2. view Students")
    print("3. Search Students")
    print("4. Exit")
# Take input from user
    choice=int(input("Enter the choice :"))
# Add new student record
    if(choice== 1):
        add_students()
    elif(choice==2):
# View all students record
        view_students()
    elif(choice==3):
# Search for student by name
        search_students()
# Exit application
    elif(choice==4):
        print("Good Bye!")
        break
# Handles invalid input
    else:
        print("Invalid choice")
    
    


