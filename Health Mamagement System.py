"""Instructions:
Create a food log file for each client.
Create an exercise log file for each client.
Ask the user whether they want to log or retrieve client data.
Write a function that takes the user input of the client's name. After the client's name is entered,
it will display a message as "What you want to log- Diet or Exercise".
Use function
def getdate():
           import datetime
           return datetime.datetime.now()
The purpose of this function is to give time with every record of food or exercise added in the file.
Write a function to retrieve exercise or food file records for any client."""
""" # Method 1: with using IF and ELSE
print("|||...Health Management System...|||\n")

def getdate():
    # This func will take today DATE and CURRENT TIME.
    import datetime
    return datetime.datetime.now()

ask_work=int(input("To make logs: Press 1 and To retrieve data: Press 2\n"))
if ask_work==1:
    client_name= int(input("Please select client for which you want to make logs;\nHimanshu : Press 1 | Aditi : Press 2 | John : Press 3\n"))
    if client_name==1:
        purpose= int(input("To make Diet Logs: Press 1 and To make Exercise Logs: Press 2 \n"))
        if purpose==1:
            with open("Himanshu_Diet.txt","a") as f:
                diet= input("Enter Diet: \n")
                f.write(str([str(getdate())])+ ":" + diet + "\n")     #print([str(getdate())],":", diet) this is also correct.
                print("Data Logged Successfully!!!")

        else:
            with open("Himanshu_Exercise.txt","a") as f:
                exer= input("Enter Exercise: \n")
                f.write(str([str(getdate())])+ ":" + exer + "\n")     #print([str(getdate())],":", diet) this is also correct.
                print("Data Logged Successfully!!!")

    elif client_name==2:
        purpose= int(input("To make Diet Logs: Press 1 and To make Exercise Logs: Press 2 \n"))
        if purpose==1:
            with open("Aditi_Diet.txt","a") as f:
                diet= input("Enter Diet: \n")
                f.write(str([str(getdate())])+ ":" + diet + "\n")     #print([str(getdate())],":", diet) this is also correct.
                print("Data Logged Successfully!!!")

        else:
            with open("Aditi_Exercise.txt","a") as f:
                exer= input("Enter Exercise: \n")
                f.write(str([str(getdate())])+ ":" + exer + "\n")     #print([str(getdate())],":", diet) this is also correct.
                print("Data Logged Successfully!!!")

    elif client_name==3:
        purpose= int(input("To make Diet Logs: Press 1 and To make Exercise Logs: Press 2 \n"))
        if purpose==1:
            with open("John_Diet.txt","a") as f:
                diet= input("Enter Diet: \n")
                f.write(str([str(getdate())])+ ":" + diet + "\n")     #print([str(getdate())],":", diet) this is also correct.
                print("Data Logged Successfully!!!")

        else:
            with open("John_Exercise.txt","a") as f:
                exer= input("Enter Exercise: \n")
                f.write(str([str(getdate())])+ ":" + exer + "\n")     #print([str(getdate())],":", diet) this is also correct.
                print("Data Logged Successfully!!!")
elif ask_work==2:
    client_name= int(input("Please select client whose data you want to retrieve;\nHimanshu : Press 1 | Aditi : Press 2 | John : Press 3\n"))
    if client_name==1:
        purpose= int(input("To retrieve Diet Logs: Press 1 and To retrieve Exercise Logs: Press 2 \n"))
        if purpose==1:
            with open("Himanshu_Diet.txt","r") as f:
                print(f.read())
        else:
            with open("Himanshu_Exercise.txt","r") as f:
                print(f.read())
    if client_name==2:
        purpose= int(input("To retrieve Diet Logs: Press 1 and To retrieve Exercise Logs: Press 2 \n"))
        if purpose==1:
            with open("Aditi_Diet.txt","r") as f:
                print(f.read())
        else:
            with open("Aditi_Exercise.txt","r") as f:
                print(f.read())
    if client_name==3:
        purpose= int(input("To retrieve Diet Logs: Press 1 and To retrieve Exercise Logs: Press 2 \n"))
        if purpose==1:
            with open("John_Diet.txt","r") as f:
                print(f.read())
        else:
            with open("John_Exercise.txt","r") as f:
                print(f.read())
else:
    print("You made wrong selection!!!")
"""

#Method 2: With using functions
# import logging
# logging.basicConfig(filename="Health Mamagement System.log", level=logging.INFO, format="%(levelname)s %(asctime)s %(name)s %(message)s")
# try:
#     logging.info("I am trying to read a file")
#     with open("sudh.txt", "r"):
#         logging.info("Successfully it has read the file")
# except Exception as e:
#     logging.critical("This is a situation for us")
#     logging.error(e)
#     logging.exception(e)


def getdate():
    # This func will take today DATE and CURRENT TIME.
    import datetime
    return datetime.datetime.now()

def log(client_name):
    if client_name==1:
        purpose= int(input("To make Diet Logs: Press 1 and To make Exercise Logs: Press 2 \n"))
        if purpose==1:
            with open("Himanshu_Diet.txt","a") as f:
                diet= input("Enter Diet: \n")
                f.write(str([str(getdate())])+ ":" + diet + "\n")     #print([str(getdate())],":", diet) this is also correct. This is called text wrapping
                print("Data Logged Successfully!!!")                  #print(name + 's diet table') this also works
        elif purpose==2:
            with open("Himanshu_Exercise.txt","a") as f:
                exer= input("Enter Exercise: \n")
                f.write(str([str(getdate())])+ ":" + exer + "\n")     #print([str(getdate())],":", diet) this is also correct. This is called text wrapping
                print("Data Logged Successfully!!!")

    elif client_name==2:
        purpose= int(input("To make Diet Logs: Press 1 and To make Exercise Logs: Press 2 \n"))
        if purpose==1:
            with open("Aditi_Diet.txt", "a") as f:
                diet= input("Enter Diet: \n")
                f.write(str([str(getdate())])+ ":" + diet + "\n")     #print([str(getdate())],":", diet) this is also correct. This is called text wrapping
                print("Data Logged Successfully!!!")
        elif purpose==2:
            with open("Aditi_Exercise.txt","a") as f:
                exer= input("Enter Exercise: \n")
                f.write(str([str(getdate())])+ ":" + exer + "\n")     #print([str(getdate())],":", diet) this is also correct.
                print("Data Logged Successfully!!!")

    elif client_name==3:
        purpose= int(input("To make Diet Logs: Press 1 and To make Exercise Logs: Press 2 \n"))
        if purpose==1:
            with open("John_Diet.txt","a") as f:
                diet= input("Enter Diet: \n")
                f.write(str([str(getdate())])+ ":" + diet + "\n")     #print([str(getdate())],":", diet) this is also correct.
                print("Data Logged Successfully!!!")
        elif purpose==2:
            with open("John_Exercise.txt","a") as f:
                exer= input("Enter Exercise: \n")
                f.write(str([str(getdate())])+ ":" + exer + "\n")     #print([str(getdate())],":", diet) this is also correct.
                print("Data Logged Successfully!!!")
    else:
        print("Please enter valid input.")

def retrieve(client_name):
    if client_name==1:
        purpose= int(input("To make Diet Logs: Press 1 and To make Exercise Logs: Press 2 \n"))
        if (purpose==1):
            with open("Himanshu_Diet.txt") as f:
                for i in f:
                    print(i, end="")
        elif (purpose==2):
            with open("Himanshu_Exercise.txt") as f:
                for i in f:
                    print(i, end="")
    elif client_name==2:
        purpose= int(input("To make Diet Logs: Press 1 and To make Exercise Logs: Press 2 \n"))
        if (purpose==1):
            with open("Aditi_Diet.txt") as f:
                for i in f:
                    print(i, end="")
        elif (purpose==2):
            with open("Aditi_Exercise.txt") as f:
                for i in f:
                    print(i, end="")
    elif client_name==3:
        purpose= int(input("To make Diet Logs: Press 1 and To make Exercise Logs: Press 2 \n"))
        if (purpose==1):
            with open("John_Diet.txt") as f:
                for i in f:
                    print(i, end="")
        elif (purpose==2):
            with open("John_Exercise.txt") as f:
                for i in f:
                    print(i, end="")
    else:
        print("Enter Valid name.")

print("|||...Health Management System...|||\n")
ask_work=int(input("To make logs: Press 1 and To retrieve data: Press 2\n"))
if ask_work==1:
    client_name= int(input("Please select client for which you want to make logs;\nHimanshu : Press 1 | Aditi : Press 2 | John : Press 3\n"))
    log(client_name)
else:
    client_name= int(input("Please select client for which you want to make logs;\nHimanshu : Press 1 | Aditi : Press 2 | John : Press 3\n"))
    retrieve(client_name)


"""
# This is 3rd Method
def getdate():
    import datetime
    return datetime.datetime.now()


def write_dirt(acess_client):
    if acess_client in list_of_clients:
        name = acess_client
        extension = '.txt'
        f = open(name + extension, 'a')
        diet_list = input('Enter today diet food: ')
        f.write(diet_list)
        f.write(' : '`)
        date= str(getdate())
        f.write(date)
        f.write("\n")
        print(name + "\'s diet table has successfully written!")
        f.close()
    else:`
        print('you have write incorrect name .. pleaese check')


def write_exercise(acess_client):
    if acess_client in list_of_clients:
        # print(list_of_clients[acess_client])
        name = acess_client
        extension = '.txt'
        f = open(name + extension, 'a')
        exercise_list = input('enter today exercise name : ')
        print(name + 's Exercise table')

        f.write(exercise_list)
        date = str(getdate())
        f.write(' = ')
        f.write(date)

        print(getdate())
        f.write('\n')
        f.close()
    else:
        print('you have write incorrect name .. pleaese check')


def read_files_of_clients(acess_client):
    file_name = acess_client
    extension = '.txt'
    f = open(file_name + extension)
    print(f.read())
    f.close()


list_of_clients = ['Harry', 'Rohan', 'Hamad']
acess_client = input('enter names to select client and update databese : ')
do_what = input('what you want to do with client ?  1 for diet 2 for exercise 3 for readfiles')
if do_what == '1':
    write_dirt(acess_client)
if do_what == '2':
    write_exercise(acess_client)
if do_what == '3':
    read_files_of_clients(acess_client)
"""

