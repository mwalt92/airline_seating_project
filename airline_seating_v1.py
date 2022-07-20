import functools
import random

import numpy as np

from tkinter import *
import tkinter.messagebox

from PIL import ImageTk, Image

from functools import partial

''' Variables '''
home_selection = 0
class_selection = 0
passenger_selection = 0
plane_map_row = 0
plane_map_collumn = 0
index_start = 0
index_end = 0
flag = 0
passengers_booked_v = 0
passenger_manifest_v = 0
passenger_manifest_choice = 0
passenger_first_name = 0
passenger_last_name = 0
plane_map_seat_label = 0

'''Lists'''
passengers = ["Veronica Berry", "Marlee Stephens", "Krish Mayer", "Jon Mclaughlin", "Jose Gibson", "Jazlene Baird", "Desirae Hendricks",
              "Diya Bolton", "Aaron Haynes", "Raphael Barnett", "Kailyn Krause", "Moises Burton", "Ryland Ayala", "Cameron Aguirre", "Vicente Lambert",
              "Jesse Villanueva", "Lucas Salazar", "Hugo Mullen", "Jon Leonard", "Cecilia Farley", "Krista Blankenship", "Alexia Jacobs", "Chad Zuniga",
              "Haylee Valenzuela", "Ernesto Valenzuela"]
passengers_booked = [" "]
passengers_booked_with_seat_number = []
passengers_booked_with_seat_number_split_name = []
passengers_row_number = []
passengers_collumn_number = []
passenger_manifest_options = ["Option1: Alphebetical", "Option 2: Row and Seat Number"]
airline_class = ["First", "Business", "Economy"]
airline_row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
seat_in_row = [1, 2, 3, 4, 5, 6, 7]
x=[]
alph_sort = []
numb_sort = []

'''Arrays'''
plane_map = [[0,"x",0,"x",0,"x",0], ["x",0,"x",0,"x",0,"x"], [0,"x",0,"x",0,"x",0], ["x",0,"x",0,"x",0,"x"], [0,"x",0,"x",0,"x",0], ["x",0,"x",0,"x",0,"x"], [0,"x",0,"x",0,"x",0], ["x",0,"x",0,"x",0,"x"], [0,"x",0,"x",0,"x",0], ["x",0,"x",0,"x",0,"x"],
             [0,"x",0,"x",0,"x",0], ["x",0,"x",0,"x",0,"x"], [0,"x",0,"x",0,"x",0], ["x",0,"x",0,"x",0,"x"], [0,"x",0,"x",0,"x",0], ["x",0,"x",0,"x",0,"x"], [0,"x",0,"x",0,"x",0], ["x",0,"x",0,"x",0,"x"], [0,"x",0,"x",0,"x",0], ["x",0,"x",0,"x",0,"x"]]

'''Dictionaries'''
dict1 = {}
dict2 = {}

'''All Program Functions'''

''' Various Back Button Fucntions'''
def win1_back_f(win1):
    global class_selection
    global passenger_selection
    global passengers
    global airline_class
    global plane_map_row
    global plane_map

    win1.destroy()

def win2_back_f(win2):
    global class_selection
    global passenger_selection
    global passengers
    global airline_class
    global plane_map_row
    global plane_map

    win2.destroy()

def win3_back_f(win3):
    global class_selection
    global passenger_selection
    global passengers
    global airline_class
    global plane_map_row
    global plane_map

    win3.destroy()

def win4_back_f(win4):
    global class_selection
    global passenger_selection
    global passengers
    global airline_class
    global plane_map_row
    global plane_map

    win4.destroy()

def option5_f():
    win_home.destroy()

'''All Windows in Program'''
# Option 1 Window Call
def win1_call():
    global class_selection
    global passenger_selection
    global passengers
    global airline_class
    global plane_map_row
    global plane_map

    win1 = Tk()
    win1.title("Seat Assignment")

    # Generates the Main Structure of the Window
    seat_assignment_title_label = Label(win1, text="Welcome to Seat Selection!").grid(row=1, column=0, columnspan=2)
    seat_assignment_title_label2 = Label(win1, text="Make your selection below for class, and seat.").grid(row=2, column=0, columnspan=2)

    passenger_selection_label = Label(win1, text="Choose a Passenger").grid(row=3, column=0)
    class_selection_label = Label(win1, text="Class: ").grid(row=4, column=0)

    passenger_selection = StringVar()
    class_selection = StringVar()

    passenger_selection_menu = OptionMenu(win1, passenger_selection, *passengers).grid(row=3, column=1)
    class_selection_menu = OptionMenu(win1, class_selection, *airline_class).grid(row=4, column=1)

    assign_seat_button = Button(win1, text="Assign a Seat", command= lambda: assign_seat_f(win1), height=1).grid(row=5, column=0, columnspan=2)

    back_button = Button(win1, text="Back to Main Menu", command= lambda: win1_back_f(win1)).grid(row=9, column=0, columnspan=2)

    win1.mainloop()

# Option 2 Window Call
def win2_call():
    global class_selection
    global passenger_selection
    global passengers
    global airline_class
    global plane_map_row
    global plane_map
    global passengers_booked_v

    win2 = Tk()
    win2.title("Boarding Pass")

    # Generates the Main Structure of the Window
    boarding_pass_label1 = Label(win2, text="Welcome to the Boarding Pass Station!").grid(row=0, column=0)
    boarding_pass_label2 = Label(win2, text="Please input the name of the person you would like to print a Boarding Pass for.").grid(row=1, column=0)

    passengers_booked_v = StringVar()

    # Menu is populated only from those who have already been booked.
    passengers_booked_menu = OptionMenu(win2, passengers_booked_v, *passengers_booked).grid(row=2,column=0)
    passengers_booked_button = Button(win2, text="Choose Passenger", command= lambda: passengers_booked_f(win2)).grid(row=3, column=0)

    back_button = Button(win2, text="Back to Main Menu", command=lambda: win2_back_f(win2)).grid(row=8, column=0, columnspan=2)
    win2.mainloop()

# Option 3 Window Call
def win3_call():
    global class_selection
    global passenger_selection
    global passengers
    global passengers_booked_with_seat_number
    global airline_class
    global plane_map_row
    global plane_map_collumn
    global plane_map
    global index_start
    global index_end
    global flag
    global dict

    win3 = Tk()
    win3.title("Plane Map")

    plane_map_label1 = Label(win3, text="Welcome to the Plane Map!").grid(row=0, column=0, columnspan=7)
    plane_map_label2 = Label(win3, text="Below are a series of buttons.").grid(row=1, column=0, columnspan=7)
    plane_map_label3 = Label(win3, text="Clicking them will select and display all information associated with that seat.").grid(row=2, column=0, columnspan=7)

    plane_map_button1 = Button(win3, text="Plane Map Generator", command= lambda: plane_map_f(win3)).grid(row=3, column=0, columnspan=7)

    back_button = Button(win3, text="Back to Main Menu", command=lambda: win3_back_f(win3)).grid(row=50, column=0, columnspan=7)

    win3.mainloop()

# Option 4 Window Call
def win4_call():
    global class_selection
    global passenger_selection
    global passengers
    global passengers_booked_with_seat_number
    global airline_class
    global plane_map_row
    global plane_map_collumn
    global plane_map
    global index_start
    global index_end
    global flag
    global passenger_manifest_v
    global passenger_manifest_choice
    global passenger_manifest_options

    win4 = Tk()
    win4.title("Passenger Manifest")

    # Generates the Main Structure of the Window
    passenger_manifest_label1 = Label(win4, text="Welcome to the Passenger Manifest!").grid(row=0, column=0, columnspan=4)
    passenger_manifest_label2 = Label(win4, text="Below is a dropdown box with two options for viewing the passenger manifest.").grid(row=1, column=0, columnspan=4)
    passenger_manifest_label3 = Label(win4, text="Option 1 is an Alphabetical View, and Option 2 is a view by row number and seat number.").grid(row=2, column=0, columnspan=4)

    passenger_manifest_v = StringVar()

    passenger_manifest_menu = OptionMenu(win4, passenger_manifest_v, *passenger_manifest_options).grid(row=3, column=0, columnspan=4)
    passenger_manifest_button = Button(win4, text="Enter Option", command=lambda: passenger_manifest_f(win4)).grid(row=4, column=0, columnspan=4)

    back_button = Button(win4, text="Back to Main Menu", command=lambda: win4_back_f(win4)).grid(row=50, column=0, columnspan=4)

    win4.mainloop()

'''Core Functions From Each Window'''
# Window 1: Assigns Seat Number to Passenger
def assign_seat_f(win1):
    global class_selection
    global passenger_selection
    global passengers
    global passengers_booked_with_seat_number
    global passengers_booked
    global passengers_row_number
    global passengers_collumn_number
    global airline_class
    global plane_map_row
    global plane_map_collumn
    global plane_map
    global index_start
    global index_end
    global flag

    # Class determines the range of the following code
    if class_selection.get() == "First":
        index_start = 0
        index_end = 2
    elif class_selection.get() == "Business":
        index_start = 3
        index_end = 5
    else:
        index_start = 6
        index_end = 19

    # Variable to help the for loop know when to stop.
    flag = False

    # For Loop for Generating the 2D Array
    for plane_map_row in range(index_start,index_end):
        if flag == False:
            for plane_map_collumn in range(0,6):
                # print(str(plane_map_row) + "i")
                if flag == False:
                    if plane_map[plane_map_row][plane_map_collumn] == 0:
                        flag = True
                        plane_map[plane_map_row][plane_map_collumn] = passenger_selection.get()
                        # print(str(plane_map_collumn) + "j")
                else:
                    break
        else:
            break

    # Print statement used in development.
    for i in range(len(plane_map)):
        print(plane_map[i])

    ## Creating various lists to be used in several other places. ##
    # All Booked Passengers
    passengers_booked.append(passenger_selection.get())

    # Passengers Tuples with Seat Number
    passengers_booked_with_seat_number.append((passenger_selection.get(), plane_map_row, plane_map_collumn, class_selection.get()))
    # Passenger Row
    passengers_row_number.append(plane_map_row)
    # Passenger Column
    passengers_collumn_number.append(plane_map_collumn)
    print(passengers_booked_with_seat_number)

    # Removing passenger from original passenger list preventing double-booking error.
    passengers.remove(passenger_selection.get())

    # Labels for the user to confirm selections.
    assign_seat_label1 = Label(win1, text="Passenger: " + passenger_selection.get()).grid(row=6, column=0, columnspan=2)
    assign_seat_label2 = Label(win1, text="Class: " + class_selection.get()).grid(row=7, column=0, columnspan=2)
    assign_seat_label3 = Label(win1, text=" Seat: " + "Row " + str(plane_map_row) + " Seat " + str(plane_map_collumn)).grid(row=8, column=0, columnspan=2)

# Window 2: Displays the Boarding Pass of a Chosen Passenger
def passengers_booked_f(win2):
    global class_selection
    global passenger_selection
    global passengers
    global passengers_booked_with_seat_number
    global airline_class
    global plane_map_row
    global plane_map_collumn
    global plane_map
    global index_start
    global index_end
    global flag

    # Filter to find the entry chosen from the list of passengers already booked.
    filter_tuple = [item for item in passengers_booked_with_seat_number if item[0] == passengers_booked_v.get()]

    # Labels detailing flight info from chosen passenger.
    passengers_booked_label0 = Label(win2, text="Name: " + str(filter_tuple[0][0])).grid(row=4, column=0)
    passengers_booked_label1 = Label(win2, text="Class: " + str(filter_tuple[0][3])).grid(row=5, column=0)
    passengers_booked_label2 = Label(win2, text="Row: " + str(filter_tuple[0][1])).grid(row=6, column=0)
    passengers_booked_label2 = Label(win2, text="Seat: " + str(filter_tuple[0][2])).grid(row=7, column=0)

# Window 3: This function generates the buttons for the plane map using information from Option 1.
def plane_map_f(win3):
    global class_selection
    global passenger_selection
    global passengers
    global passengers_booked_with_seat_number
    global airline_class
    global plane_map_row
    global plane_map_collumn
    global plane_map
    global index_start
    global index_end
    global flag
    global dict1
    global dict2
    global plane_map_seat_label

    for i in range(1, 21):
        for j in range(1, 8):
            key = str("R" + str(i) + "S" + str(j))
            lock = str("r" + str(i) + "s" + str(j))
            dict1[key] = Button(win3, text=str(key), command= partial(plane_map_button_f,win3, i,j), height=1, width=8).grid(row=i + 3, column=j)
            # dict2[lock]=i,j

def plane_map_button_f(win3,i,j):
    global class_selection
    global passenger_selection
    global passengers
    global passengers_booked_with_seat_number
    global airline_class
    global plane_map_row
    global plane_map_collumn
    global plane_map
    global index_start
    global index_end
    global flag
    global dict1
    global dict2
    global plane_map_seat_label

    temp_map = plane_map[int(i)-1][int(j)-1]

    if temp_map == "x":
        plane_map_seat_label = Label(win3, text="Seat Restricted Due to COVID-19")
        plane_map_seat_label.grid(row=4, column=8)
    elif temp_map == 0:
        plane_map_seat_label = Label(win3, text="Open Seat. Ready for Passenger.")
        plane_map_seat_label.grid(row=4, column=8)
    else:
        plane_map_seat_label = Label(win3, text="Name " + str(temp_map))
        plane_map_seat_label.grid(row4, column=8)

    plane_map_button2 = Button(win3, text="Refresh", command=plane_map_seat_label.destroy).grid(row=3, column=8)

# Window 4: Displays the Manifest Given the Chosed Option
def passenger_manifest_f(win4):
    global class_selection
    global passenger_selection
    global passengers
    global passengers_booked_with_seat_number
    global airline_class
    global plane_map_row
    global plane_map_collumn
    global plane_map
    global index_start
    global index_end
    global passenger_manifest_v
    global passenger_manifest_choice
    global passenger_manifest_options
    global alph_sort
    global numb_sort

    passenger_manifest_choice = passenger_manifest_v.get()
    alph_sort = []
    numb_sort = []
    passengers_booked_with_seat_number_split_name = []

    # Creates Tupled List of Last Name, First Name, Row, Seat, Class
    for i in range(len(passengers_booked_with_seat_number)):
        y = passengers_booked_with_seat_number[i][0].split(" ")
        y_f = y[0]
        y_l = y[1]
        y_tuple = [y_l,y_f,passengers_booked_with_seat_number[i][1],
                                                             passengers_booked_with_seat_number[i][2],
                                                             passengers_booked_with_seat_number[i][3]]
        passengers_booked_with_seat_number_split_name.append(y_tuple)
        print(passengers_booked_with_seat_number_split_name)

    # Sorts List into Alphabetical or By Seat Number
    if passenger_manifest_choice == "Option1: Alphebetical":
        alph_sort = sorted(passengers_booked_with_seat_number_split_name, key=lambda y: y[0])
        print(passengers_booked_with_seat_number_split_name)
        print(alph_sort)
    else:
        numb_sort = sorted(passengers_booked_with_seat_number_split_name, key=lambda y: (y[2],y[3]))
        print(passengers_booked_with_seat_number_split_name)
        print(numb_sort)

    # Generated Labels in a Grid for the Manifest
    if passenger_manifest_choice == "Option1: Alphebetical":
        for i in range(len(alph_sort)):
            passenger_manifest_label = Label(win4, text=str(i) + ")" + " " + str(alph_sort[i][0]) + ", "
                                                        + str(alph_sort[i][1]) + ", Row: " +
                                                        str(alph_sort[i][2]) + ", Seat: " +
                                                        str(alph_sort[i][3]) + ", Class: " +
                                                        str(alph_sort[i][4]), justify=LEFT).grid(row=5 + i, column=0)
    else:
        for i in range(len(numb_sort)):
            passenger_manifest_label = Label(win4, text=str(i) + ")" + " " + str(numb_sort[i][0]) + ", "
                                                        + str(numb_sort[i][1]) + ", Row: " +
                                                        str(numb_sort[i][2]) + ", Seat: " +
                                                        str(numb_sort[i][3]) + ", Class: " +
                                                        str(numb_sort[i][4]), anchor="w").grid(row=5 + i, column=0)

'''Main Program Starts Here'''
win_home = Tk()
win_home.title("Home Page")

main_title_label1 = Label(win_home, text="Welcome!")
main_title_label1.grid(row=0, column=0)

main_title_label1 = Label(win_home, text="What would you like to do?")
main_title_label1.grid(row=1, column=0, padx=50, pady=10)

option1_button = Button(win_home, text="Option 1: Seat Assignment", height=3, width=20, command= win1_call)
option1_button.grid(row=2, column=0)

option2_button = Button(win_home, text="Option 2: Boarding Pass", height=3, width=20, command= win2_call)
option2_button.grid(row=3, column=0)

option3_button = Button(win_home, text="Option 3: Seat Map", height=3, width=20, command= win3_call)
option3_button.grid(row=4, column=0)

option4_button = Button(win_home, text="Option 4: Flight Manifest", height=3, width=20, command= win4_call)
option4_button.grid(row=5, column=0)

option5_button = Button(win_home, text="Option 5: Quit Program", height=3, width=20, command= option5_f)
option5_button.grid(row=6, column=0)

win_home.mainloop()
