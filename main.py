import sqlite3
from collections import Counter

print("""
===============================================================
                     Easy Apply Workers System
===============================================================




""")

# pull data from sqlite3 and store it in a list called "items"
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute(f"SELECT * FROM students")
items = c.fetchall()


students =[]
x=0

# gets values from items list and store it in a dictionary in a more readable way
for item in items:

    # sqlite3 varubals keys on order Civilid - name - gender - number - email - advisor name - country - age - major - Uni name

    civilid_from_sqlite = items[x][0]
    name_from_sqlite = items[x][1]
    gender_from_sqlite = items[x][2]
    number_from_sqlite = items[x][3]
    email_from_sqlite = items[x][4]
    advisor_name_from_sqlite = items[x][5]
    country_from_sqlite = items[x][6]
    age_from_sqlite = items[x][7]
    major_from_sqlite = items[x][8]
    uni_from_sqlite = items[x][9]

    x +=1

    students.append(
        {
            "civilid": civilid_from_sqlite , "name": name_from_sqlite, "gender": gender_from_sqlite, "number": number_from_sqlite, "email": email_from_sqlite, 
            "advisor name": advisor_name_from_sqlite, "country": country_from_sqlite, "age": age_from_sqlite, "major": major_from_sqlite, "uni name": uni_from_sqlite
        }
    )


# prints stuff that helps the user
def excute_command(command):
    
    if command == 'help':
        output = """

        ====================
        
        type: \"student info\"

        if you need one of theese:
        1. name
        2. number
        3. Civil Id
        4. major
        5. age
        6. studying country
        7. uni name
        8. advisor name
        9. all of them

        -   -   -   -   -

        type: \"services\"

        if you need one of theese:
        1. add student
        2. remove student
        3. send email
        4. send whats


        -   -   -   -   -

        type: \"statics\"

        if you need one of theese:
        1. students in each country
        2. avrage age
        3. students in each uni
        4. students in each major
        5. male and female in each country

        ====================

        """

    if command == "student info":
        output = """

        ====================

        Please type one of theese:

        1. \"name\" for student name
        2. \"number\" for student phone number
        3. \"civil id\" for student civil id
        4. \"major\" for student major
        5. \"age\" for student age
        6. \"country\" for student studying country
        7. \"uni\" for student uni name
        8. \"advisor\" for student advisor name
        9. \"all\" for all of the student information
        
        ====================
        """
    if command == "statics":
        output = """

        ====================

        Please type one of theese:

        1. \"students in each country\" for the number of students in each country
        2. \"avrage age\" for student avrage age
        3. \"students in each uni\" for the number of students in each uni
        4. \"students in each major\" for the number of students in each major
        5. \"female and male statics\" for the female and male students statics

        ====================
        """
    
    if command == "services":
        output = """

        ====================

        Please type one of theese:

        1. \"add student\" if you want to add a student
        2. \"remove student\" if you want to remove a student

        ====================
        """


    return output


# excute any thing related to student info
def student_info(for_what,index):
    list_index = 0
    y = 0

    # checks if the index is valid means if it exist in the data base so it dosen't crash
    for item in items:

        civilid_from_sqlite = items[y][0]
        name_from_sqlite = items[y][1]
        gender_from_sqlite = items[y][2]
        number_from_sqlite = items[y][3]
        email_from_sqlite = items[y][4]
        advisor_name_from_sqlite = items[y][5]
        country_from_sqlite = items[y][6]
        age_from_sqlite = items[y][7]
        major_from_sqlite = items[y][8]
        uni_from_sqlite = items[y][9]

        y +=1

        if index == civilid_from_sqlite or index == name_from_sqlite or index == gender_from_sqlite or index == number_from_sqlite or index == email_from_sqlite:
            break
        if index == advisor_name_from_sqlite or index == country_from_sqlite or index == age_from_sqlite or index == major_from_sqlite or index == uni_from_sqlite:
            break
        if y == len(items):
            output = "Please check your input!"

    # search for name
    if for_what == "name":

        for item in students:
            if item["civilid"] == index:  # checks if any of the students civilId match the function input
                output = students[list_index]["name"] # then it takes the matched student name
            
            list_index += 1
    
    # search for number
    if for_what == "number":

        # the if else to check if the user is using a name or civil id for searching
        if index.isdigit():
            for item in students:
                if item["civilid"] == index: # checks if any of the students civilId match the function input
                    output = students[list_index]["number"] # then it takes the matched student number
                
                list_index +=1
        
        else:
            for item in students:
                if item["name"] == index: # checks if any of the students name match the function input
                    output = students[list_index]["number"] # then it takes the matched student number
            list_index += 1           

    # search for civil id
    if for_what == "civil id":

        for item in students:
            if item["name"] == index: # checks if any of the students name match the function input
                output = students[list_index]["civilid"] # then it takes the matched student civilid
            
            list_index += 1

    # search for major
    if for_what == "major":

        # the if else to check if he is using a name or civil id for searching
        if index.isdigit():
            for item in students:
                if item["civilid"] == index: # checks if any of the students civilId match the function input
                    output = students[list_index]["major"] # then it takes the matched student major
                
                list_index +=1
        
        else:
            for item in students:
                if item["name"] == index: # checks if any of the students name match the function input
                    output = students[list_index]["major"] # then it takes the matched student major
            
            list_index += 1

    # search for age
    if for_what == "age":

        # the if else to check if he is using a name or civil id for searching
        if index.isdigit():
            for item in students:
                if item["civilid"] == index: # checks if any of the students civilId match the function input
                    output = students[list_index]["age"] # then it takes the matched student age
                
                list_index +=1
        
        else:
            for item in students:
                if item["name"] == index: # checks if any of the students name match the function input
                    output = students[list_index]["age"] # then it takes the matched student age
            
            list_index += 1

    # search for country
    if for_what == "country":

        # the if else to check if he is using a name or civil id for searching
        if index.isdigit():
            for item in students:
                if item["civilid"] == index: # checks if any of the students civilId match the function input
                    output = students[list_index]["country"] # then it takes the matched student country
                
                list_index +=1
        
        else:
            for item in students:
                if item["name"] == index: # checks if any of the students name match the function input
                    output = students[list_index]["country"] # then it takes the matched student country
            
            list_index += 1

    # search for uni
    if for_what == "uni":

        # the if else to check if he is using a name or civil id for searching
        if index.isdigit():
            for item in students:
                if item["civilid"] == index: # checks if any of the students civilId match the function input
                    output = students[list_index]["uni name"] # then it takes the matched student uni name
                
                list_index +=1
        
        else:
            for item in students:
                if item["name"] == index: # checks if any of the students name match the function input
                    output = students[list_index]["uni name"] # then it takes the matched student uni name
            
            list_index += 1

    # search for advisor
    if for_what == "advisor":

        # the if else to check if he is using a name or civil id for searching
        if index.isdigit():
            for item in students:
                if item["civilid"] == index: # checks if any of the students civilId match the function input
                    output = students[list_index]["advisor name"] # then it takes the matched student advisor name
                
                list_index +=1
        
        else:
            for item in students:
                if item["name"] == index: # checks if any of the students name match the function input
                    output = students[list_index]["advisor name"] # then it takes the matched student advisor name
            
            list_index += 1

    # search for all
    if for_what == "all":

        # the if else to check if he is using a name or civil id for searching
        if index.isdigit():
            for item in students:
                if item["civilid"] == index: # checks if any of the students civilId match the function input
                    child = students[list_index]

                    child_civilid = child["civilid"]
                    child_name = child["name"]
                    child_gender = child["gender"]
                    child_number = child["number"]
                    child_email = child["email"]
                    child_advisor_name = child["advisor name"]
                    child_country = child["country"]
                    child_age = child["age"]
                    child_major = child["major"]
                    child_uni = child["uni name"]

                    output =f"""
                    name: {child_name}
                    civil id: {child_civilid}
                    age: {child_age}
                    gender: {child_gender}
                    number: {child_number}
                    email: {child_email}
                    advisor name: {child_advisor_name}
                    country: {child_country}
                    major: {child_major}
                    uni name: {child_uni}
                    """
                list_index +=1
        
        else:
            for item in students:
                if item["name"] == index: # checks if any of the students name match the function input
                    child = students[list_index]

                    child_civilid = child["civilid"]
                    child_name = child["name"]
                    child_gender = child["gender"]
                    child_number = child["number"]
                    child_email = child["email"]
                    child_advisor_name = child["advisor name"]
                    child_country = child["country"]
                    child_age = child["age"]
                    child_major = child["major"]
                    child_uni = child["uni name"]

                    output =f"""
                    name: {child_name}
                    civil id: {child_civilid}
                    age: {child_age}
                    gender: {child_gender}
                    number: {child_number}
                    email: {child_email}
                    advisor name: {child_advisor_name}
                    country: {child_country}
                    major: {child_major}
                    uni name: {child_uni}
                    """
            
            list_index += 1

    return output


# excute any thing related to statics                
def statics(for_what):
    

    # gets the number of students in each country
    if for_what == "students in each country":
        v = 0
        random_list = []
        for student in students: # makes a list of all students country

            random_list.append(students[v]["country"])

            v +=1

            if v == len(students):
                countrys = set(random_list) # removes duplicates from the list

                for country in countrys:
                    counter = Counter(random_list) # make a dictionary that counts how many something is ducplicated 
                    the_number = counter[country]

                    print(f"{country} {the_number}")
    
    # gets the avrage student age
    if for_what == "avrage age":
        z = 0
        idk = [] # random list used to store age values
        for student in students:

            idk.append(students[z]["age"])
            z +=1

            if len(students) == z:
                
                total_age = sum(idk) # it gets the sum of the values
                avrage = total_age / len(students) # then we devide the total on the number of students to get المتوسط الحسابي the avrage
                avrage = round(avrage) # it rounds the float to the nearest integer

                print(f"the avrage age is {avrage}")
                
    # gets the students number in each uni
    if for_what == "students in each uni":
        n = 0
        random_list = []
        for student in students: # makes a list of all students uni name

            random_list.append(students[n]["uni name"]) 

            n +=1

            if n == len(students):
                unis = set(random_list) # removes duplicates from the list

                for uni in unis:
                    counter = Counter(random_list) # make a dictionary that counts how many something is ducplicated 
                    the_number = counter[uni]

                    print(f"{uni} {the_number}")
        
    # gets the students number in each major
    if for_what == "students in each major":
        q = 0
        random_list = []
        for student in students: # makes a list of all students major

            random_list.append(students[q]["major"]) 

            q +=1

            if q == len(students):
                majors = set(random_list) # removes duplicates from the list

                for major in majors:
                    counter = Counter(random_list) # make a dictionary that counts how many something is ducplicated 
                    the_number = counter[major]

                    print(f"{major} {the_number}")

    # gets the number of each gender ( male - female)
    if for_what == "female and male statics":
        g = 0
        random_list = []
        for student in students: # makes a list of all values related to gender

            random_list.append(students[g]["gender"])

            g +=1

            if g == len(students):
                gender = set(random_list) # removes duplicates from the list

                for person_gender in gender:
                    counter = Counter(random_list) # make a dictionary that counts how many something is ducplicated
                    the_number = counter[person_gender]

                    print(f"{person_gender} students {the_number}")


# infinite loop that keeps excuting inputs for the commands it runs forever unless the user types "quit"
while True:

    command = input("> ")
    command = str(command.strip().lower())
    choice = ""


    # student info
    if command == "student info":
        print(excute_command(command))
        choice = input("> ")
        choice = str(choice.strip().lower())

        if choice == "name":
            civil_id_ = input("please enter the student's civil id: ")
            print(student_info("name",civil_id_))
        
        if choice == "number":
            primary_key = input("Please enter the student's civil id or name: ")
            print(student_info("number",primary_key))

        if choice == "civil id":
            name = input("Please enter the studnet name: ")
            print(student_info("civilid",name))

        if choice == "major":
            primary_key = input("Please enter the student's civil id or name: ")
            print(student_info("major",primary_key))

        if choice == "age":
            primary_key = input("Please enter the student's civil id or name: ")
            print(student_info("age",primary_key))
 
        if choice == "country":
            primary_key = input("Please enter the student's civil id or name: ")
            print(student_info("country",primary_key))            

        if choice == "uni":
            primary_key = input("Please enter the student's civil id or name: ")
            print(student_info("uni",primary_key))          

        if choice == "advisor":
            primary_key = input("Please enter the student's civil id or name: ")
            print(student_info("advisor",primary_key))    

        if choice == "all":
            primary_key = input("Please enter the student's civil id or name: ")
            print(student_info("all",primary_key))   

    # statics
    if command == "statics":
        print(excute_command(command))
        choice = input("> ")
        choice = str(choice.strip().lower())

        if choice == "students in each country":
            statics("students in each country")

        if choice == "avrage age":
            statics("avrage age")

        if choice == "students in each uni":
            statics("students in each uni")

        if choice == "students in each major":
            print(statics("students in each major"))

        if choice == "female and male statics":
            print(statics("female and male statics"))

    # services
    if command == "services":
        # print(excute_command(command))
        # choice = input("> ")
        # choice = str(choice.strip().lower())
        print("coming soon!")

    if command == "help" or choice == "help":
       print(excute_command("help"))

    if command == "quit" or choice == "quit":
        print("the program has been quitted successfully! ")
        break
    
    else:
        print("""
        
        Type \"help\" if you need help with the commands
        """)
