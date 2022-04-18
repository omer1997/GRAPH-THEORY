from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

import gmplot

import warnings
import tkinter
warnings.filterwarnings("ignore")

import folium
from branca.element import Figure


#######################################
gui = Tk(className=' NIU PATHFINDER ')
# set window size
gui.geometry("1200x700")

####################################
# Create label
l = Label(gui, text = "Shortest Distance between NIU Computer Science building and famous eateries and recreational spots in Dekalb")
l.config(font =("Courier bold", 14))
l.pack()


############################################
# Create the list of options
options_list = ["SUBWAY", "CHIPOTLE", "TACO BELL", "DUNKIN","VINNYS PIZZA","AMC DEKALB","SHABBONA LAKE","ELLWOOD HOUSE MUSEUM"]
  
# Variable to keep track of the option
# selected in OptionMenu
value_inside = tkinter.StringVar(gui)


# Set the default value of the variable
value_inside.set("Select an Option")
  
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
question_menu = tkinter.OptionMenu(gui, value_inside, *options_list)
question_menu.pack()
  
# # Function to print the submitted option-- testing purpose
  
  
# def print_answers():
#     print("Selected Option: {}".format(value_inside.get()))
#     print("Finding the best possible route to : {}".format(value_inside.get()))
#     return None
  



########################################################
# function to open a new window
# on a button click
def openNewWindow():
    #to print the submitted option-- testing purpose 
    print("Selected Option: {}".format(value_inside.get()))
    print("Finding the best possible route to : {}".format(value_inside.get()))
    #print(value_inside.get())

    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(gui)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Route from NIU CS building to: {}".format(value_inside.get()))
 
    # sets the geometry of toplevel
    newWindow.geometry("400x400")
 
    # A Label widget to show in toplevel
    Label(newWindow,text ="Finding the best possible route to : {}".format(value_inside.get())).pack()
    
    # Create text widget and specify size.
    T = Text(newWindow, height = 1200, width = 700)
    if value_inside.get() == 'SUBWAY':
        route1 = " From NIU Computer Science Building \n( 100 Normal Rd, Dekalb, IL 60115) \n Head South on Normal Rd toward IL-38 E for 184 ft \n Turn right onto IL-38 W for 0.3 miles \n The destination will be on left\n Subway (928 W Lincoln Hwy Dekalb IL 60115) \n \n \n ESTIMATED TIME : 1 Min  \n \n ESTIMATED DISTANCE : 0.3 Mile "
        T.pack()
        T.insert(tk.END, route1)

        fig2=Figure(width=550,height=350)
        m2=folium.Map(location=[41.93055745, -88.7709822])
        fig2.add_child(m2)
        folium.TileLayer('Stamen Terrain').add_to(m2)
        folium.TileLayer('Stamen Toner').add_to(m2)
        folium.TileLayer('Stamen Water Color').add_to(m2)
        folium.TileLayer('cartodbpositron').add_to(m2)
        folium.TileLayer('cartodbdark_matter').add_to(m2)
        folium.LayerControl().add_to(m2)

        folium.Marker(location=[41.93055745, -88.7709822],popup='Subway (928 W Lincoln Hwy Dekalb IL 60115)',tooltip='Click here to see the DESTINATION').add_to(m2)
        folium.Marker(location=[41.93162315, -88.76493668],popup='NIU Computer Science Building',tooltip='Click here to see the SOURCE').add_to(m2)
        m2.save('/Users/omerbinalibajubair/Documents/JAVA/graph theory project files/map.py\SUBWAY.html')
        
  
        
    elif value_inside.get() == 'CHIPOTLE':
        route1 = " From NIU Computer Science Building \n( 100 Normal Rd, Dekalb, IL 60115) \n Head South on Normal Rd toward IL-38 E for 184 ft \n Turn right onto IL-38 W for 0.3 miles \n Turn Right \n The destination will be on left \n Chipotle (1013 W Lincoln Hwy, Dekalb, IL 60115) \n \n \n ESTIMATED TIME : 1 Min  \n \n ESTIMATED DISTANCE : 0.4 Mile"
        T.pack()
        T.insert(tk.END, route1)

        fig2=Figure(width=550,height=350)
        m2=folium.Map(location=[41.9313782, -88.7716679])
        fig2.add_child(m2)
        folium.TileLayer('Stamen Terrain').add_to(m2)
        folium.TileLayer('Stamen Toner').add_to(m2)
        folium.TileLayer('Stamen Water Color').add_to(m2)
        folium.TileLayer('cartodbpositron').add_to(m2)
        folium.TileLayer('cartodbdark_matter').add_to(m2)
        folium.LayerControl().add_to(m2)

        folium.Marker(location=[41.9313782, -88.7716679],popup='Chipotle (1013 W Lincoln Hwy, Dekalb, IL 60115)',tooltip='Click here to see the DESTINATION').add_to(m2)
        folium.Marker(location=[41.93162315, -88.76493668],popup='NIU Computer Science Building',tooltip='Click here to see the SOURCE').add_to(m2)
        m2.save('/Users/omerbinalibajubair/Documents/JAVA/graph theory project files/map.py\CHIPOTLE.html')


    elif value_inside.get() == 'TACO BELL':
        route1 = " From NIU Computer Science Building \n( 100 Normal Rd, Dekalb, IL 60115) \n Head South on Normal Rd toward IL-38 E for 184 ft \n Turn right onto IL-38 W for 0.5 miles \n Turn Right \n The destination will be on left \n Taco Bell ( 1209 W Lincoln Hwy, Dekalb, IL 60115) \n \n \n ESTIMATED TIME : 2 Min  \n \n ESTIMATED DISTANCE : 0.6 Mile"
        T.pack()
        T.insert(tk.END, route1)

        fig2=Figure(width=550,height=350)
        m2=folium.Map(location=[41.9312187, -88.77647305])
        fig2.add_child(m2)
        folium.TileLayer('Stamen Terrain').add_to(m2)
        folium.TileLayer('Stamen Toner').add_to(m2)
        folium.TileLayer('Stamen Water Color').add_to(m2)
        folium.TileLayer('cartodbpositron').add_to(m2)
        folium.TileLayer('cartodbdark_matter').add_to(m2)
        folium.LayerControl().add_to(m2)

        folium.Marker(location=[41.9312187, -88.77647305],popup='Taco Bell ( 1209 W Lincoln Hwy, Dekalb, IL 60115)',tooltip='Click here to see the DESTINATION').add_to(m2)
        folium.Marker(location=[41.93162315, -88.76493668],popup='NIU Computer Science Building',tooltip='Click here to see the SOURCE').add_to(m2)
        m2.save('/Users/omerbinalibajubair/Documents/JAVA/graph theory project files/map.py\TACOBELL.html')



    elif value_inside.get() == 'DUNKIN':
        route1 = " From NIU Computer Science Building \n( 100 Normal Rd, Dekalb, IL 60115) \n Head South on Normal Rd toward IL-38 E for 184 ft \n Turn right onto IL-38 W for 0.4 miles \n turn right after Dunkin (56 ft) \n Turn Left \n The destination will be on right\n Dunkin ( 1101 W Lincoln Hwy, Dekalb, IL 60115 ) \n \n \n ESTIMATED TIME : 2 Min  \n \n ESTIMATED DISTANCE : 0.5 Mile"
        T.pack()
        T.insert(tk.END, route1)

        fig2=Figure(width=550,height=350)
        m2=folium.Map(location=[41.93135175, -88.7736953])
        fig2.add_child(m2)
        folium.TileLayer('Stamen Terrain').add_to(m2)
        folium.TileLayer('Stamen Toner').add_to(m2)
        folium.TileLayer('Stamen Water Color').add_to(m2)
        folium.TileLayer('cartodbpositron').add_to(m2)
        folium.TileLayer('cartodbdark_matter').add_to(m2)
        folium.LayerControl().add_to(m2)

        folium.Marker(location=[41.93135175, -88.7736953],popup='Dunkin ( 1101 W Lincoln Hwy, Dekalb, IL 60115 )',tooltip='Click here to see the DESTINATION').add_to(m2)
        folium.Marker(location=[41.93162315, -88.76493668],popup='NIU Computer Science Building',tooltip='Click here to see the SOURCE').add_to(m2)
        m2.save('/Users/omerbinalibajubair/Documents/JAVA/graph theory project files/map.py\DUNKIN.html')



    elif value_inside.get() == 'VINNYS PIZZA':
        route1 = " From NIU Computer Science Building \n( 100 Normal Rd, Dekalb, IL 60115) \n Head South on Normal Rd toward IL-38 E for 184 ft \n Turn left onto IL-38 W for 0.3 miles \n The destination will be on left \n Vinnys Pizza (221 W Lincoln Hwy, Dekalb, IL 60115 ) \n \n \n ESTIMATED TIME : 1 Min  \n \n ESTIMATED DISTANCE : 0.4 Mile"
        T.pack() 
        T.pack()
        T.insert(tk.END, route1)

        fig2=Figure(width=550,height=350)
        m2=folium.Map(location=[41.931168, -88.7591379])
        fig2.add_child(m2)
        folium.TileLayer('Stamen Terrain').add_to(m2)
        folium.TileLayer('Stamen Toner').add_to(m2)
        folium.TileLayer('Stamen Water Color').add_to(m2)
        folium.TileLayer('cartodbpositron').add_to(m2)
        folium.TileLayer('cartodbdark_matter').add_to(m2)
        folium.LayerControl().add_to(m2)

        folium.Marker(location=[41.931168, -88.7591379],popup='Vinnys Pizza (221 W Lincoln Hwy, Dekalb, IL 60115 )',tooltip='Click here to see the DESTINATION').add_to(m2)
        folium.Marker(location=[41.93162315, -88.76493668],popup='NIU Computer Science Building',tooltip='Click here to see the SOURCE').add_to(m2)
        m2.save('/Users/omerbinalibajubair/Documents/JAVA/graph theory project files/map.py\VINNYSPIZZA.html')



    elif value_inside.get() == 'AMC DEKALB':
        route1 = " From NIU Computer Science Building \n( 100 Normal Rd, Dekalb, IL 60115) \n Head South on Normal Rd toward IL-38 E for 184 ft \n Turn left onto IL-38 W for 0.6 miles \n Continue on N 1st St Sycamore Rd for 1.5 miles \n The destination will be at the dead end at 0.4 miles \n AMC Market Square 10 (2160 Sycamore Rd, Dekalb, IL 60115) \n \n \n ESTIMATED TIME : 7 Min  \n \n ESTIMATED DISTANCE : 3.1 Mile"
        T.pack()
        T.insert(tk.END, route1)


        fig2=Figure(width=550,height=350)
        m2=folium.Map(location=[41.94727645, -88.72056275])
        fig2.add_child(m2)
        folium.TileLayer('Stamen Terrain').add_to(m2)
        folium.TileLayer('Stamen Toner').add_to(m2)
        folium.TileLayer('Stamen Water Color').add_to(m2)
        folium.TileLayer('cartodbpositron').add_to(m2)
        folium.TileLayer('cartodbdark_matter').add_to(m2)
        folium.LayerControl().add_to(m2)

        folium.Marker(location=[41.94727645, -88.72056275],popup='AMC Market Square 10 (2160 Sycamore Rd, Dekalb, IL 60115)',tooltip='Click here to see the DESTINATION').add_to(m2)
        folium.Marker(location=[41.93162315, -88.76493668],popup='NIU Computer Science Building',tooltip='Click here to see the SOURCE').add_to(m2)
        m2.save('/Users/omerbinalibajubair/Documents/JAVA/graph theory project files/map.py\AMCDEKALB.html')



    elif value_inside.get() == 'SHABBONA LAKE':
        route1 = " From NIU Computer Science Building \n( 100 Normal Rd, Dekalb, IL 60115) \n  Head South on Normal Rd toward IL-38 E for 184 ft  \n Take S Annie Glidden Rd to E fairview Dr for 0.2 miles \n Turn right onto E Fairview Dr after 3.8 mile \n Follow University Rd to Indian Rd in Shabonna Township for 10.3 miles \n Continue on Indian Rd to your destination for 1.2 miles \n Destination reached \n Shabbona Lake State Park ( 100 preserve Rd, Shabbona , IL 60550 ) \n \n \n ESTIMATED TIME : 22 Min  \n \n ESTIMATED DISTANCE : 17.4 Mile"
        T.pack()
        T.insert(tk.END, route1)

        fig2=Figure(width=550,height=350)
        m2=folium.Map(location=[41.74531085, -88.85733441])
        fig2.add_child(m2)
        folium.TileLayer('Stamen Terrain').add_to(m2)
        folium.TileLayer('Stamen Toner').add_to(m2)
        folium.TileLayer('Stamen Water Color').add_to(m2)
        folium.TileLayer('cartodbpositron').add_to(m2)
        folium.TileLayer('cartodbdark_matter').add_to(m2)
        folium.LayerControl().add_to(m2)

        folium.Marker(location=[41.74531085, -88.85733441],popup='Shabbona Lake State Park ( 100 preserve Rd, Shabbona , IL 60550 )',tooltip='Click here to see the DESTINATION').add_to(m2)
        folium.Marker(location=[41.93162315, -88.76493668],popup='NIU Computer Science Building',tooltip='Click here to see the SOURCE').add_to(m2)
        m2.save('/Users/omerbinalibajubair/Documents/JAVA/graph theory project files/map.py\SHABBONALAKE.html')


        
    elif value_inside.get() == 'ELLWOOD HOUSE MUSEUM':
        route1 = " From NIU Computer Science Building \n( 100 Normal Rd, Dekalb, IL 60115) \n Head South on Normal Rd toward IL-38 E for 184 ft \n Turn left  onto IL-38 W for 0.6 miles \n Turn left onto N 1st St after 0.2 miles \n Turn left onto Augusta Ave after 500 ft\n Turn right onto Linden PI after 300 ft \n The destination will be on right \n ELLWOOD House Museum ( 420 Linden PI, Dekalb ,IL 60115 ) \n \n \n ESTIMATED TIME : 3 Min  \n \n ESTIMATED DISTANCE : 1.0 Mile"
        T.pack()
        T.insert(tk.END, route1) 

        fig2=Figure(width=550,height=350)
        m2=folium.Map(location=[41.93550345, -88.75347558])
        fig2.add_child(m2)
        folium.TileLayer('Stamen Terrain').add_to(m2)
        folium.TileLayer('Stamen Toner').add_to(m2)
        folium.TileLayer('Stamen Water Color').add_to(m2)
        folium.TileLayer('cartodbpositron').add_to(m2)
        folium.TileLayer('cartodbdark_matter').add_to(m2)
        folium.LayerControl().add_to(m2)

        folium.Marker(location=[41.93550345, -88.75347558],popup='ELLWOOD House Museum ( 420 Linden PI, Dekalb ,IL 60115 )',tooltip='Click here to see the DESTINATION').add_to(m2)
        folium.Marker(location=[41.93162315, -88.76493668],popup='NIU Computer Science Building',tooltip='Click here to see the SOURCE').add_to(m2)
        m2.save('/Users/omerbinalibajubair/Documents/JAVA/graph theory project files/map.py\ELLWOODHOUSEMUSEUM.html')                       

        
    return None



# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = tkinter.Button(gui, text='FIND YOUR ROUTE TO THE DESTINATION', command=openNewWindow)
submit_button.pack()


##########################################
# Add the image file
bg = ImageTk.PhotoImage(file="/Users/omerbinalibajubair/Documents/JAVA/graph theory project files/CS2.png")

# Create a canvas
canvas = Canvas(gui,width= 400, height= 300)
canvas.pack(fill= "both", expand=True)

# Display image
canvas.create_image(0, 0, image=bg, anchor="nw")

gui.mainloop() 