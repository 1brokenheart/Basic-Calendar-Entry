from time import sleep, strftime
import datetime
users_name = input("What is your name? ")
#create an empty dictionary
today = datetime.date.today()
time = datetime.datetime.now()
calendar = {} 

#Welcome message to user
def welcome():
    print ("Welcome " + users_name + " to your calendar" +".")
    print ("Your calendar is starting now...")
    sleep(1)
    print ("Today is: " + today.strftime("%m, %d, %Y"))
    print (time.strftime( "Time: %H: %M: %S"))
    sleep(1)
    print ("What would you like to do?")

#create a menu where the user can choose from: add an event, update an event , delete an event, or exit the calendar.
def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == "V":
            if len(calendar.keys()) < 1:
                print ("No events in calendar.")
            else:
                print (calendar)
        
        #update events in the calendar
        elif user_choice == "U":
            date = input("What date? ") 
            update = input("Enter the update: ")
            calendar[date] = update 
            print ("you have succesfuly updated your calendar.")  
            print (calendar)
    
        # To add an event to the calendar      
        elif user_choice == "A":
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")

            #looking for invalid years entered by the user
            if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print ("You entered and invalid date")
                try_again = "Try Again? Y for yes, N for NO: "
                try_again = try_again.upper()
                if try_again == "Y": 
                    continue
                else:
                        start == False
                        calendar[date] = event
                        print ("Your event was successfully added.")  
                        print (calendar)

        # To delete an event from the calendar         
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print ("No events.")
            else:
                event = input("What event?: ")
                for date in calendar.keys():
                    if event == calendar[date]:      
                        del calendar[date]
                        print ("You have successfully deleted the event.")
                        print (calendar)
                    else:
                        print ("You entered an invalid event")

        #to exit the the program and chaging the value to start.
        elif user_choice == "X":
            start = False
        else:
            print ("Sorry, invalid command.")

start_calendar()
