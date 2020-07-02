import os
import csv
import shutil


# This procedure will read the file and display the data contained therein.
def readFile():
    file = open('python_assessment.txt', 'r+')
    lines = file.read()
    print(lines)
    file.close()

# This procedure will open the file and strip the lines
def new_user():
    file = open('python_assessment.txt', 'r+')
    lines = [i.strip() for i in file.readlines()]
    newid = len(lines)
    addUserDetail(newid)

    file.close()

# This procedure will add data in the file based on user input
def addUserDetail(newid):
    firstname = input("Please enter first name: ")
    secondname = input("Please enter surname: ")
    address1 = input("Please enter house number and street name: ")
    address2 = input("Please enter city: ")
    postcode = input("Please enter postcode: ")
    telephonenumber = input("Please enter telephone number: ")

    file = open('python_assessment.txt', 'r')
    line = file.readlines()

    newline = ("\n" + str(newid+1) + "       " + firstname + "   " + secondname + "    " + address1 + "   " + address2 + "   " + postcode + "   " + telephonenumber)

    file = open('python_assessment.txt', 'a')
    file.write(newline)
    file.close()

# Procedure to remove a particular person from this text file by picking user ID.
def delete_user_id():
    text_file = open("python_assessment.txt", "r")
    target_id = text_file.readlines()
    text_file.close()

    user_input = input("Add the ID to delete:")
    del target_id[1]
    new_file = open("python_assessment.txt", "w+")

# This for loop will iterate to delete the appropriate line
    for line in target_id:
        new_file.write(line)
    new_file.close()
    print("User ID successfully removed!")
    input("Press any key to return to main menu")


# This procedure will show a search functionality of a menu with options to search for a person based on their particulars
def show_single_user():
    while True:
        while True:
            print('Choose a search option:\n',
                  "1 - By ID\n",
                  "2 - By Name\n",
                  "3 - By Surname\n",
                  "4 - By Address\n",
                  "5 - By City\n",
                  "6 - By Post Code\n",
                  "7 - By Phone\n",
                  "8 - Exit\n")
            choice = input(":")
            if choice == "8": return
            elif choice == "1":
                option = 0
                break
            elif choice == "2":
                option = 1
                break
            elif choice == "3":
                option = 2
                break
            elif choice == "4":
                option = 3
                break
            elif choice == "5":
                option = 4
                break
            elif choice == "6":
                option = 5
                break
            elif choice == "7":
                option = 6
                break
            elif not choice.isdigit():
                input("This is not a valid option. Press any key to try again!")
            else:
                input("This is not a valid option. Press any key to try again!")
        #### Ask the user the pattern to search for
        print("Please enter the information you are looking for\n")
        pattern = input(":")
        file1 = open('python_assessment.txt', 'r')
        file_read = csv.reader(file1, delimiter='\t')
        for item in file_read:
            if pattern.lower() in item[option].lower():
                print(item)
        print("Press enter to try again")
        input(":")
        file1.close()

# This procedure will create a  back-up file
# It will externally import copyfile from shutil to enable the creation of a back-up copy.
def lets_copy():
    from shutil import copyfile
    copyfile('python_assessment.txt', 'back_up_file.txt')
    print("Back up file created was saved as: 'back_up_file.txt'", "\n")


# function to update a person that already exists in the text file
def update_entry():
    while True:
        # Menu to show the field to be modified
        while True:
            print('Please choose an field to modify:\n',
                    "1 - Name\n",
                    "2 - Surname\n",
                    "3 - Address\n",
                    "4 - City\n",
                    "5 - Post Code\n",
                    "6 - Phone\n",
                    "7 - Exit\n")
            field = input(":")
            if field == "7":
                return
            elif field == "1":
                option = 1
                break
            elif field == "2":
                option = 2
                break
            elif field == "3":
                option = 3
                break
            elif field == "4":
                option = 4
                break
            elif field == "5":
                option = 5
                break
            elif field == "6":
                option = 6
                break
            elif not field.isdigit():
                input("This is not a valid option. Press any key to try again!")
            else:
                input("This is not a valid option. Press any key to try again!")
        field = int(field)
        # Listing the file
        while True:
            info = open("python_assessment.txt", 'r')
            for i in info:
                print(i)
            print("Choose an user ID to modify:")
            user_id = input(":")
            if not user_id.isdigit():
                input("This is not a valid ID. Press any key to try again!")
            else:
                break
        # User inputs new values
        value = input("Input the new value: ")
        ID = int(ID)
        with open('python_assessment.txt', 'r') as file1:
            file_read = csv.reader(file1, delimiter='\t')
            file_write = open('python_assessment_copy.txt', 'w')
            for item in file_read:
                if ID == int(i[0]):
                    i[field] = value
                for word in i:
                    file_write.write(word)
                    file_write.write('\t')
                file_write.write('\n')
            file_write.close()
        shutil.copy("python_assessment_copy.txt", "python_assessment.txt")
        input("User info updated successfully. Press enter to return!")


# Procedure to show duplicated lines in the text file
def display_duplicates():
    with open('python_assessment.txt') as joe:
        initialise = set()

        for line in joe:
            amzn = line.lower()
            if amzn in initialise:
                print(line)
            else:
                initialise.add(amzn)
        print("There are no more duplicates!" + "\n")

# Main menu to be displayed
while True:
    print("****Choose Your Option below****\n",
    "Option 1: - Read the whole file\n",
    "Option 2: - Add new user\n",
    "Option 3: - Delete user\n",
    "Option 4: - Search for a user\n",
    "Option 5: - Create a Back-up file\n",
    "Option 6: - Update an entry\n",
    "Option 7: - Display duplicates\n",
    "Exit\n"
    )
    target = input(":>")
    if target == "1": readFile()
    elif target == "2": new_user()
    elif target == "3": delete_user_id()
    elif target == "4": show_single_user()
    elif target == "5": lets_copy()
    elif target == "6": update_entry()
    elif target == "7": display_duplicates()
    elif not option.isdigit(): input("Please try again and inputa valid option")

    else: input("Option not valid, press to return!")
