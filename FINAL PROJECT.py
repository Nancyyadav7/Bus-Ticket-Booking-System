from tkinter import *
import sqlite3
from PIL import Image,ImageTk
from tkinter import messagebox

conn = sqlite3.connect("Bus_information_database.db")

c = conn.cursor()

c.execute("""CREATE TABLE if not exists Buses(id integer ,
    Travels_full_name text,
    Contact_no integer,
    Address text,
    Operator text,
    Bus_type text,
    from_starting_point text,
    to_destination text,
    date text,
    dept_time text,
    arr_time text,
    fare integer,
    seats integer,PRIMARY KEY (id AUTOINCREMENT)
)""")

conn.commit()

conn.close()


globl_list = []

def bus_main_screen():


    def search_bus():

        def search(bus_type_selection,frm,destination,date):

            root2.destroy()
            root3= Tk()


            Label(root3,text="BUS BOOKING SERVICE",font= 100,bg="Black",fg="white",border=10).grid(row=0,column =2,columnspan=3)

            img1 = Image.open("byd-adl-enviro200ev-transport-for-london-elektrobus-electric-bus-2019-01-min.png")
            x = 2
            y = 2
            re_img1 = img1.resize((1500//x,750//y))
            img1 = ImageTk.PhotoImage(re_img1)
            Label(root3,image = img1).grid(row=1,column=1,columnspan=8)

            def details_displaced_after_searched():
                Label(root3,text="BUS Details",font= 100,bg="Black",fg="white",border=10).grid(row=2,column = 2,columnspan=2)

                Label(root3,text="id",font=3).grid(row=3,column=0)

                Label(root3,text="Travels Name",font=3).grid(row=3,column=1)

                Label(root3,text="Type",font=3).grid(row=3,column=2)

                Label(root3,text="From",font=3).grid(row=3,column=3)

                Label(root3,text="To",font=3).grid(row=3,column=4)

                Label(root3,text="Date",font=3).grid(row=3,column=5)

                Label(root3,text="Dept Time",font=3).grid(row=3,column=6)

                Label(root3,text="Arr Time",font=3).grid(row=3,column=7)

                Label(root3,text="Fare",font=3).grid(row=3,column=8)

                Label(root3,text="Seats Availability",font=3).grid(row=3,column=9)



            details_displaced_after_searched()

            Label(root3,text="Select",font=3).grid(row=3,column=10)


            var_select = IntVar()

            conn = sqlite3.connect("Bus_information_database.db")

            c = conn.cursor()



            conn.commit()

            conn.close()

            Button(root3,text="Select Book",font=3).grid(row=49,column=10)
            def calling_global2():
                root3.destroy()
                bus_main_screen()


            Button(root3,text="Home",border=2,command=calling_global2).grid(row=49,column=0)

            root3.mainloop()


        root.destroy()

        root2 = Tk()

        root2.title("Booking Service")

        Label(root2,text="BUS BOOKING SERVICE",font= 100,bg="Black",fg="white",border=10).grid(row=0,column =3)
        img = Image.open("newbus_main.jpg")
        x = 2
        y = 2
        re_img = img.resize((634//x,500//y))
        img = ImageTk.PhotoImage(re_img)
        Label(image = img).grid(row=1,column=3)

        Label(root2,text="Listing Buses",font=50).grid(row=2,column=3)

        bus_type_selection = StringVar()
        bus_type_selection.set("Bus Type")
        Label(root2,text="Bus Type: ").grid(row=3,column=0)
        bustype = ['AC','Non-AC','AC-Sleeper','Non-Sleeper AC','All Types']
        OptionMenu(root2,bus_type_selection,*bustype).grid(row=3,column=3)


        Label(root2,text="From: ").grid(row=4,column=0)
        frm=""
        frm = Entry(root2)
        frm.grid(row=4,column=3)


        Label(root2,text="To: ").grid(row=5,column=0)
        destination=""
        destination= Entry(root2)
        destination.grid(row=5,column=3)


        Label(root2,text="Date(dd/mm/yyyy): ").grid(row=6,column=0)
        date=""
        date = Entry(root2)
        date.grid(row=6,column=3)

        def ms():
                messagebox.showwarning("warning","From and destination are equal")

        def ms1():
                messagebox.showwarning("warning","Wrong Date Format")

        def check_information():
            date_string = date.get()
            if(frm.get()==destination.get()):
                ms()
            elif((int(date_string[0])>=0 and int(date_string[0])<=2) and (int(date_string[1])>=0 and int(date_string[1])<=9) and  date_string[2]=='/' and ((int(date_string[3])==0 and (int(date_string[4])>=1 and int(date_string[4])<=9)) or (int(date_string[3])==1 and (int(date_string[4])>=0 and int(date_string[4])<=2))) and date_string[5]=='/' and int(date_string[6:10])>=1000 and int(date_string[6:10])<=9999):
                search(bus_type_selection,frm.get(),destination.get(),date.get())
            else:
                ms1()


        Button(root2,text="Search",border=2,command=check_information).grid(row=7,column=3)

        def calling_global1():
            root2.destroy()
            bus_main_screen()


        Button(root2,text="Home",border=2,command=calling_global1).grid(row=7,column=0)
        root2.mainloop()



    def add_bus():

        root.destroy()
        root1 = Tk()

        Label(root1,text="BUS BOOKING SERVICE",font= 100,bg="Black",fg="white",border=10).grid(row=0,column =3)
        img = Image.open("Interior-scenes-of-electric-buses-optimised-1280x720.jpg")
        x = 2
        y = 2
        re_img = img.resize((634//x,500//y))
        img = ImageTk.PhotoImage(re_img)
        Label(image = img).grid(row=1,column=3)

        Label(root1,text="Bus Operator Details Filling").grid(row=2,column=3)

        Label(root1,text=" Travels Full Name: ").grid(row=3,column=0)
        travelsfullname=""
        travelsfullname = Entry(root1)
        travelsfullname.grid(row=3,column=3)


        Label(root1,text="Contact No: ").grid(row=4,column=0)
        contactno=0
        contactno = Entry(root1)
        contactno.grid(row=4,column=3)


        Label(root1,text="Address: ").grid(row=5,column=0)
        address=""
        address = Entry(root1)
        address.grid(row=5,column=3)


        def add_details():

            def entry_details_in_database():

                conn = sqlite3.connect('Bus_information_database.db')
                c = conn.cursor()

                c.execute("INSERT INTO Buses( Travels_full_name,Contact_no , Address ,Operator ,Bus_type ,from_starting_point ,to_destination ,date ,dept_time ,arr_time , fare , seats ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(travelsfullname.get(),contactno.get(),address.get(),operator.get(),bustype.get(),frm.get(),destination.get(),date.get(), depttime.get(),arrtime.get(),fare.get(),seats.get()))


                conn.commit()
                conn.close()

                travelsfullname.delete(0,END)
                contactno.delete(0,END)
                address.delete(0,END)
                operator.delete(0,END)
                bustype.delete(0,END)
                frm.delete(0,END)
                destination.delete(0,END)
                date.delete(0,END)
                depttime.delete(0,END)
                arrtime.delete(0,END)
                fare.delete(0,END)
                seats.delete(0,END)

                '''root10 = Tk()
                Label(root10,text="Added Successfully").grid(row=17,column = 3)
                def exit_after():
                    root10.destroy()
                Button(root10,text="Exit",command=exit_after).grid(row=19,column=3)
                root10.mainloop()'''

                def save_pop():
                    messagebox.showwarning("warning","Bus has been added")

                save_pop()
                root1.destroy()

                bus_main_screen()




            Label(root1,text="Operator: ").grid(row=7,column=0)
            operator=""
            operator = Entry(root1)
            operator.grid(row=7,column=3)


            Label(root1,text="Bus Type: ").grid(row=8,column=0)
            bustype=""
            bustype = Entry(root1)
            bustype.grid(row=8,column=3)


            Label(root1,text="From: ").grid(row=9,column=0)
            frm=""
            frm = Entry(root1)
            frm.grid(row=9,column=3)


            Label(root1,text="To: ").grid(row=10,column=0)
            destination=""
            destination= Entry(root1)
            destination.grid(row=10,column=3)


            Label(root1,text="Date(dd/mm/yyyy): ").grid(row=11,column=0)
            date=""
            date = Entry(root1)
            date.grid(row=11,column=3)


            Label(root1,text="Dept time(): ").grid(row=12,column=0)
            depttime=""
            depttime = Entry(root1)
            depttime.grid(row=12,column=3)


            Label(root1,text="Arr time: ").grid(row=13,column=0)
            arrtime=""
            arrtime = Entry(root1)
            arrtime.grid(row=13,column=3)


            Label(root1,text="Fare: ").grid(row=14,column=0)
            fare=0
            fare = Entry(root1)
            fare.grid(row=14,column=3)


            Label(root1,text="Seats: ").grid(row=15,column=0)
            seats=0
            seats = Entry(root1)
            seats.grid(row=15,column=3)

            def ms():
                messagebox.showwarning("warning","Field is/are empty")


            def save_check_details_to_proceed():
                if(travelsfullname.get()!="" and contactno.get()!=0 and address.get() != "" and operator.get()!="" and bustype.get()!="" and frm.get()!="" and destination.get()!="" and date.get()!="" and depttime.get()!="" and arrtime.get()!="" and fare.get()!="" and seats.get()!="" ):
                    entry_details_in_database()

                else:
                    ms()


            Button(root1,text = "Save",command = save_check_details_to_proceed).grid(row=16,column =  3)
            def home_calling():
                root1.destroy()
                bus_main_screen()

            Button(root1,text="Home",command=home_calling).grid(row=16,column=0)


        Button(root1,text ="Add Details",command = add_details).grid(row=6,column = 3)

        root1.mainloop()




    root = Tk()

    root.title("Bus Booking Service")

    Label(root,text="BUS BOOKING SERVICE",font= 100,bg="Black",fg="white",border=10).grid(row=0,column =3)

    img = Image.open("TfL-Image-Route-94-electric-bus.jpg")
    x = 3
    y = 3
    re_img = img.resize((2048//x,1316//y))
    img = ImageTk.PhotoImage(re_img)
    Label(image = img).grid(row=1,column=3)

    # padx , pady , columnspan , ipadx , ipady in grid
    Button(root,text="Add Bus",font = 150,border = 2,command = add_bus).grid(row=2,column =0)

    Button(root,text="Search Bus",font = 150,border = 2,command = search_bus).grid(row=2,column=4)

    Button(root,text="Exit",command = root.destroy,border = 2).grid(row=3,column = 3)

    root.mainloop()



root_details = Tk()
#root_details.geometry('500x500')
root_details.configure(bg="black")
Label(root_details,text="Project Title : Bus Booking System",font="bold 30",bg="black",fg="#099FFF").grid(row=0,column=0)
Label(root_details,text="",bg="black").grid(row=1,column=0)

Label(root_details,text="Developed as a part of the coursde Advanced Programming Lab-1 & DBMS",font="bold 15",bg="black",fg="#099FFF").grid(row=2,column=0)
Label(root_details,text="",bg="black").grid(row=3,column=0)

Label(root_details,text="Developed by: XYZ",font="bold 20",bg="black",fg="#099FFF").grid(row=4,column=0)
Label(root_details,text="",bg="black").grid(row=5,column=0)

Label(root_details,text="-----------------------------------------------------------------------",font="bold 20",bg="black",fg="#099FFF").grid(row=6,column=0)
Label(root_details,text="",bg="black").grid(row=7,column=0)

Label(root_details,text="Project Supervisors: Dr Mahesh Kumar & DBMS Nilesh Patel",font="bold 20",bg="black",fg="#099FFF").grid(row=8,column=0)
Label(root_details,text="",bg="black").grid(row=9,column=0)

Label(root_details,text="make mouse movement to close this",font="bold 10",bg="black",fg="#099FFF").grid(row=10,column=0)


def close(e=2):
    root_details.destroy()
    bus_main_screen()

root_details.bind('<Motion>',close)
root_details.mainloop()