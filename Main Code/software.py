from tkinter import *
import tkinter.messagebox as tkmsg
from tkinter import Toplevel
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql
from tkinter import messagebox,filedialog
import time
import pandas as pd
import smtplib
import os


rect = []
ss = 'Welcome in 2020-2021 Session'
count = 0
text = '' 
root = Tk()
root.title('Login System')
photo = PhotoImage(file = 'school.png')
root.iconphoto(FALSE,photo)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
main_width = root.winfo_screenwidth()
main_heigth = root.winfo_screenheight()

def login():
    if operator.get() == 1 and cpassword.get() == 0:
        mydb = pymysql.connect(host="localhost",user="root",password="",database="school")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM operator where username = %s and password = %s",(uname.get(),passwrd.get()))
        myresult = mycursor.fetchall()
        mainl = str(len(myresult))
        if mainl == '1':
            messagebox.showinfo('Welcome','welcome')
            root.destroy()
            rootm = Tk()
            photo = PhotoImage(file = 'school.png')
            rootm.iconphoto(FALSE,photo)
            rootm.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth()-10,rootm.winfo_screenheight()-10))
            rootm.title('School Management')
            rootm.config(bg = 'cornsilk')
            menu1 = Label(rootm,text = 'Advance School management',font = ('times new roman',round((30/1360)*main_width),'bold'), bg ='cornflowerblue',fg = 'Black',relief = 'solid')
            menu1.pack(side = TOP,fill = X)
            f1m = Frame(rootm,bd = (4/1360)*main_width,relief = RIDGE,bg = 'skyblue' )
            f1m.place(x = (25/1360)*main_width ,y = (80/1360)*main_width,width = (1310/1360)*main_width,height = (590/768)*main_heigth)
            print(f1m.winfo_screenwidth())
            recenttime =  time.strftime('%H:%M:%S')
            rect.append(recenttime)
            print(rect)
            statusbar = Label(rootm,text = 'On the way',bd = 1,relief = SUNKEN,anchor = W)
            statusbar.pack(side = BOTTOM , fill = X)
            def teacherstaff():
                
                root1 = Toplevel(rootm)

                root1.title('Teachers Management system')
                photo = PhotoImage(file = 'school.png')
                root1.iconphoto(FALSE,photo)

                root1.config(bg = 'skyblue')
                root1.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth(),rootm.winfo_screenheight()))
                root1.grab_set()
                def main():
                    root1.destroy()
                def main1(event):
                    root1.destroy()
                root1.bind('<End>',main1)

                title = Label(root1,text = 'Teachers Management System',font = ('time now roman',round((35/1360)*main_width),'bold'),bg = 'lightpink',fg = 'Black',bd = round((10/1360)*main_width),relief = 'sunken')
                title.pack(side = TOP,fill = X)
                butn = Button(root1,text = 'MAIN MENU',width=round((10/1360)*main_width),font = ('time now roman',round((15/1360)*main_width),'bold'),bg = 'skyblue',fg = 'Black',command = main)
                butn.place(x = round((1200/1360)*main_width),y = round((15/768)*main_heigth),width = round((120/1360)*main_width),height = round((35/768)*main_heigth))

            ######### All Variables #########################################################################################################################################################
                Name = StringVar() # name
                Fathersname = StringVar()#  Fathersname
                Mothers_Name = StringVar()# Mother_Name
                DOB = StringVar()        # DOB 
                Phonenumber = StringVar()  # phone number
                Class = StringVar()      # class # Subjectteaching
                Accountno = StringVar()  # Accountno # teachingclass
                Aadharno = StringVar()   # Aadharno   # Aadharno
                SSSMID = StringVar()     # SSSMID   # Emailid
                Address = StringVar()    # Address   # Address
                search_by = StringVar()  # search_by  
                search_txt = StringVar() # search_txt
                scholar = StringVar()    # scholar   # scholar
            ################################### All Functions #######################################################################################################################################################################################################################################################################
            ######################### Add students fuction #####################################################################################################################################################################################################
                def add_students():
                    if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                        messagebox.showerror("Error",'All Fields are Required!!')
                    else:
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor()
                        cur.execute('insert into staff (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                        Name.get(),
                        Fathersname.get(),
                        Mothers_Name.get(),
                        DOB.get(),
                        scholar.get(),
                        Class.get(),
                        Accountno.get(),
                        Aadharno.get(),
                        SSSMID.get(),
                        txt_add.get('1.0',END)))
                        con.commit()
                        fetch_data()
                        clear()
                        con.close()
                        messagebox.showinfo("Success","Message has been inserted")
                def fetch_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute('select * from staff')
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                        student_table.delete(* student_table.get_children())
                        for row in rows:
                                student_table.insert('',END,values = row)
                        con.commit()
                    con.close()
                def clear():
                    Name.set('')
                    Fathersname.set('')
                    Mothers_Name.set('')
                    DOB.set('')
                    scholar.set('')
                    Class.set('')
                    Accountno.set('')
                    Aadharno.set('')
                    SSSMID.set('') 
                    txt_add.delete('1.0',END)

                ########## get_cursor ##################################################################
                def get_cursor(event):
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                    print(row)
                    Name.set(row[0])
                    Fathersname.set(row[1])
                    Mothers_Name.set(row[2])
                    DOB.set(row[3])
                    scholar.set(row[4])
                    Class.set(row[5])
                    Accountno.set(row[6])
                    Aadharno.set(row[7])
                    SSSMID.set(row[8])
                    txt_add.delete('1.0',END) 
                    txt_add.insert(END,row[9])

                ########### update_data ###############################################################
                def update_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('update  staff set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                    Name.get(),
                    Fathersname.get(),
                    Mothers_Name.get(),
                    DOB.get(),
                    Class.get(),
                    Accountno.get(),
                    Aadharno.get(),
                    SSSMID.get(),
                    txt_add.get('1.0',END),
                    scholar.get()))
                    con.commit()
                    fetch_data()
                    clear()
                    con.close()
    ############################ Delete_data #########################################################
                def delete_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    ask = messagebox.askyesno('Message','Are you Really Want to delete')
                    if ask == True:
                        cur.execute('delete  from staff where  scholar_id = %s',scholar.get())
                        con.commit()
                        con.close()
                        fetch_data()
                        clear()

                        ############### search_data #########################################################
                def search_data():
                    if search_by.get() == '' or  search_txt.get() == '':
                        messagebox.showerror("Error",'All Fields are Required!!')
                    else:        
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute("select * from staff where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                            student_table.delete(*student_table.get_children())
                            for row in rows:
                                student_table.insert('',END,values = row)
                            con.commit()
                        con.close()


                ############## Add students fuction ######################################################
                def add_students():
                    if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                        messagebox.showerror("Error",'All Fields are Required!!')
                    else:
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor()
                        cur.execute('insert into staff (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                        Name.get(),
                        Fathersname.get(),
                        Mothers_Name.get(),
                        DOB.get(),
                        scholar.get(),
                        Class.get(),
                        Accountno.get(),
                        Aadharno.get(),
                        SSSMID.get(),
                        txt_add.get('1.0',END)))
                        con.commit()
                        fetch_data()
                        clear()
                        con.close()
                        messagebox.showinfo("Success","Message has been inserted")
                def saad_stud(event):
                    add_students()
                root1.bind('<Control-s>',saad_stud)
                def fetch_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute('select * from staff')
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                            student_table.delete(* student_table.get_children())
                            for row in rows:
                                    student_table.insert('',END,values = row)
                            con.commit()
                        con.close()

                def clear():
                    Name.set('')
                    Fathersname.set('')
                    Mothers_Name.set('')
                    DOB.set('')
                    scholar.set('')
                    Class.set('')
                    Accountno.set('')
                    Aadharno.set('')
                    SSSMID.set('') 
                    txt_add.delete('1.0',END)
                def clr_stud(event):
                    clear()
                root1.bind('<Control-c>',clr_stud)
    ############ get_cursor ##################################################################
                def get_cursor(event):
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                    Name.set(row[0])
                    Fathersname.set(row[1])
                    Mothers_Name.set(row[2])
                    DOB.set(row[3])
                    scholar.set(row[4])
                    Class.set(row[5])
                    Accountno.set(row[6])
                    Aadharno.set(row[7])
                    SSSMID.set(row[8])
                    txt_add.delete('1.0',END) 
                    txt_add.insert(END,row[9])
                root1.bind('<Return>',get_cursor)

                ########### update_data ###############################################################
                def update_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('update  staff set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                    Name.get(),
                    Fathersname.get(),
                    Mothers_Name.get(),
                    DOB.get(),
                    Class.get(),
                    Accountno.get(),
                    Aadharno.get(),
                    SSSMID.get(),
                    txt_add.get('1.0',END),
                    scholar.get()))
                    con.commit()
                    fetch_data()
                    clear()
                    con.close()
                def upd_stud(event):
                    update_data()
                root1.bind('<Control-u>',upd_stud)

                ############## Delete_data #########################################################
                def delete_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    ask = messagebox.askyesno('Message','Are you Really Want to delete')
                    if ask == True:
                        cur.execute('delete  from staff where  Aadharno = %s',Aadharno.get())
                        con.commit()
                        con.close()
                        fetch_data()
                        clear()
                def del_stud(event):
                    delete_data()
                root1.bind('<Delete>',del_stud)

                        ############### search_data #########################################################
                def search_data():
                        if search_by.get() == '' or  search_txt.get() == '':
                                messagebox.showerror("Error",'All Fields are Required!!')
                        else:        
                                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                                cur = con.cursor() 
                                cur.execute("select * from staff where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                                rows = cur.fetchall()
                                if len(rows)!= 0:
                                    student_table.delete(*student_table.get_children())
                                    for row in rows:
                                        student_table.insert('',END,values = row)
                                    con.commit()
                                con.close()

                ########################## Manage Frame ###############################################
                Manage_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                Manage_Frame.place(x = (20/1360)*main_width,y = (100/768)*main_heigth,width = (450/1360)*main_width,height = (595/768)*main_heigth)

                m_title = Label(Manage_Frame,text = "Manage Teachers",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/768)*main_heigth),'bold'))
                m_title.grid(row = 0, columnspan = 2,pady =(8/768)*main_heigth,padx = (8/1360)*main_width)


                ######################### Name ########################################################
                lbl_name = Label(Manage_Frame,text = "Name" ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_name.grid(row = 2,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_name = Entry(Manage_Frame,textvariable = Name,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/768)*main_heigth),bg = 'skyblue' , relief = GROOVE)
                txt_name.grid(row = 2,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Father's Name ###############################################
                lbl_fname = Label(Manage_Frame,text = "Father's name",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_fname.grid(row = 3,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_fname = Entry(Manage_Frame,textvariable = Fathersname ,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd =round((5/768)*main_heigth),bg='skyblue' , relief = GROOVE)
                txt_fname.grid(row = 3,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Mothers name #############################################################
                lbl_mother = Label(Manage_Frame,text = "Mother's Name.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_mother.grid(row = 4,column = 0,pady = (8/1360)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_sssmid = Entry(Manage_Frame,textvariable = Mothers_Name ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width),bg ='skyblue', relief = GROOVE)
                txt_sssmid.grid(row = 4,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ####################### DOB #################################################################
                lbl_dob = Label(Manage_Frame,text = "Date of Birth",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_dob.grid(row = 5,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_dob = Entry(Manage_Frame,textvariable = DOB,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd = round((5/1360)*main_width),bg ='skyblue' , relief = GROOVE)
                txt_dob.grid(row = 5,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Scholar Id ##################################################
                lbl_scholar = Label(Manage_Frame,text = "Date of joining",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_scholar.grid(row = 6,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_pnumber = Entry(Manage_Frame,textvariable = scholar,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_pnumber.grid(row = 6,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ###################### class ##############################################################
                lbl_class = Label(Manage_Frame,text = "Subjects Teaching",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_class.grid(row = 7,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_class= Entry(Manage_Frame,textvariable = Class,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_class.grid(row = 7,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ##################### Account no. #########################################################
                lbl_acc = Label(Manage_Frame,text = "Class Name",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_acc.grid(row = 8,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_acc = Entry(Manage_Frame,textvariable = Accountno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_acc.grid(row = 8,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                #####################  Aadhar no. ##########################################################
                lbl_aadhar = Label(Manage_Frame,text = "Aadhar No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_aadhar.grid(row = 9,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_aadhar = Entry(Manage_Frame,textvariable =   Aadharno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_aadhar.grid(row = 9,column = 1,pady = round((8/768)*main_heigth),padx = round((18/1360)*main_width),sticky = W )

                ####################### SSSMID No #############################################################

                lbl_sssmid = Label(Manage_Frame,text = "Email Id",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_sssmid.grid(row = 10,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_sssmid = Entry(Manage_Frame,textvariable = SSSMID ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_sssmid.grid(row = 10,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################### Address. ###########################################################
                lbl_add = Label(Manage_Frame,text = "Address.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_add.grid(row = 11,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_add = Text(Manage_Frame,width  = round((37/1360)*main_width) ,height = round((2/768)*main_heigth),font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_add.grid(row = 11,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )



                ########################## Button Frame #################################################################
                btn_Frame = Frame(Manage_Frame,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                btn_Frame.place(x = (6/1360)*main_width ,y = (520/768)*main_heigth,width =round((420/1360)*main_width))

                Addbtn = Button(btn_Frame,text = 'Add',width=round((10/1360)*main_width),command = add_students,bg = 'Lightpink').grid(row=0,column = 0,padx = (15/1360)*main_width,pady = (10/768)*main_heigth)
                updatebtn = Button(btn_Frame,text = 'Update',width=round((10/1360)*main_width),command = update_data,bg = 'Lightpink').grid(row=0,column = 1,padx =(15/1360)*main_width,pady =(10/768)*main_heigth)
                deletebtn = Button(btn_Frame,text = 'Delete',width=round((10/1360)*main_width),command = delete_data,bg = 'Lightpink').grid(row=0,column = 2,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)
                cleartbtn = Button(btn_Frame,text = 'Clear',width=round((10/1360)*main_width),command = clear,bg = 'Lightpink').grid(row=0,column = 3,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

                ########################## Detail Frame ###############################################        
                Detail_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                Detail_Frame.place(x = round((500/1360)*main_width),y = round((100/768)*main_heigth),width = round((765/1360)*main_width),height = round((590/768)*main_heigth))


                lbl_serch = Label(Detail_Frame,text = "Search By",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((14/1360)*main_width),'bold'))
                lbl_serch.grid(row = 0,column = 0,pady = round((10/768)*main_heigth),padx = round((20/1360)*main_width),sticky = W )


                combo_serch = ttk.Combobox(Detail_Frame,textvariable = search_by,width = round((10/1360)*main_width),font = ('time new roman',round((13/1360)*main_width),'bold'),state = 'readonly')
                combo_serch['values'] = ['Name','Address']
                combo_serch.grid(row=0,column = 1 , padx = (20/1360)*main_width ,pady = (10/768)*main_heigth)

                txt_serch = Entry(Detail_Frame,textvariable = search_txt,font = ('time now roman',round((14/1360)*main_width),'bold'),bd = (5/1360)*main_width ,bg  = 'skyblue', relief = GROOVE)
                txt_serch.grid(row = 0,column = 2,pady = (10/1360)*main_heigth,padx = (20/1360)*main_width,sticky = W )


                serchbtn = Button(Detail_Frame,text = 'Search',width=round((10/1360)*main_width), pady = (5/768)*main_heigth,command = search_data,bg = 'Lightpink').grid(row=0,column = 3,padx =10,pady = 10)
                showalltbtn = Button(Detail_Frame,text = 'Show All',width=round((10/1360)*main_width),command =fetch_data,bg = 'Lightpink').grid(row=0,column = 4,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

                def next_w(event):
                    event.widget.tk_focusNext().focus()
                    return 'break'
                root1.bind_class('Entry','<Down>',next_w)
                def next_w(event):
                    event.widget.tk_focusPrev().focus()
                    return 'break'
                root1.bind_class('Entry','<Up>',next_w)
                def next_w(event):
                    event.widget.tk_focusNext().focus()
                    return 'break'
                root1.bind_class('Button','<Right>',next_w)
                
                
                ################################## Table-Frame #############################################################
                Table_Frame = Frame(Detail_Frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
                Table_Frame.place(x = (10/1360)*main_width,y = (70/768)*main_heigth,width = (740/1360)*main_width,height = (500/768)*main_heigth)
                scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
                scroll_y = Scrollbar(Table_Frame,orient = VERTICAL)

                student_table = ttk.Treeview(Table_Frame,columns = ('Name',"Father's Name","Mother's Name",'D.O.B','Scholar_ID','Class_ID','Account No.','Aadhar No.','SSSMID2','Address'),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
                scroll_x.pack(side = BOTTOM,fill = X)
                scroll_y.pack(side = RIGHT , fill =Y)
                scroll_x.config(command = student_table.xview)
                scroll_y.config(command = student_table.yview)

                student_table.heading('Name',text = 'Name' )
                student_table.heading("Father's Name",text = "Father's Name" )
                student_table.heading("Mother's Name",text = "Mother's Name" )
                student_table.heading('D.O.B',text = 'D.O.B' )
                student_table.heading('Scholar_ID',text = 'Date of joining')
                student_table.heading('Class_ID',text = 'Subjects Teaching' )
                student_table.heading('Account No.',text = 'Classes Teaching.' )
                student_table.heading('Aadhar No.',text = 'Aadhar No.' )
                student_table.heading('SSSMID2',text = 'Email ID' )
                student_table.heading('Address',text = 'Address' )
                student_table['show'] = 'headings'
                student_table.column('Name',width = 130)
                student_table.column("Father's Name",width =130 )
                student_table.column("Mother's Name",width = 130)
                student_table.column('D.O.B',width = 75)
                student_table.column('Scholar_ID',width = 130)
                student_table.column('Class_ID',width = 150)
                student_table.column('Account No.',width = 180)
                student_table.column('Aadhar No.',width = 180)
                student_table.column('SSSMID2',width = 180)
                student_table.column('Address',width = 200)
                student_table.pack(fill = BOTH,expand = 1)
                student_table.bind("<ButtonRelease-1>",get_cursor)
                style = ttk.Style()
                style.configure('Treeview.Heading',font = ('time now roman',round((12/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                style.configure('Treeview',font = ('time now roman',round((10/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                fetch_data()

                root1.mainloop()  

            def dis(event):
                rootm.destroy()
            rootm.bind('<Escape>',dis)
            def backup():
                
                root = Toplevel()
        
                root.grab_set()
                root.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth(),rootm.winfo_screenheight()))
                photo = PhotoImage(file = 'school.png')
                root.iconphoto(FALSE,photo)
                def main():
                    root.destroy()
                def main1(event):
                    root.destroy()
                root.bind('<End>',main1)

                title = Label(root,text = 'Backup System',font = ('time now roman',round((37/1360)*main_width),'bold'),bg = 'lightpink',fg = 'Black',bd = round((10/1360)*main_width),relief = 'sunken')
                title.pack(side = TOP,fill = X)
                butn = Button(root,text = 'MAIN MENU',width=round((10/1360)*main_width),font = ('time now roman',round((15/1360)*main_width),'bold'),bg = 'skyblue',fg = 'Black',command = main)
                butn.place(x = (1200/1360)*main_width,y = (15/768)*main_heigth,width = (120/1360)*main_width,height =(43/768)*main_heigth)
                root.title('Backup system')
                root.config(bg = 'skyblue')
            
            ############################## All Variable ##########################################################################################################
                Name = StringVar()
                Fathersname = StringVar()
                Mothers_Name = StringVar()
                DOB = StringVar()
                Phonenumber = StringVar()
                Class = StringVar()
                Accountno = StringVar()
                Aadharno = StringVar()
                SSSMID = StringVar() 
                Address = StringVar()
                search_by = StringVar()
                search_txt = StringVar()
                scholar = StringVar()
                firstname = StringVar()
                lastname = StringVar()
                ##################### Time Frame ########################################################

                def tick():
                    time_string = time.strftime('%H:%M:%S')
                    date_string = time.strftime('%d/%m/%Y')
                    clock_label.config(text = "Date:"+date_string+'\n'+'Time:'+ time_string)
                    clock_label.after(100,tick)

                time_frame = Frame(root,bd  = round((8/1360)*main_width) ,relief = GROOVE,bg = 'skyblue')
                time_frame.place(x = (15/1360)*main_width,y = (90/768)*main_heigth,width = (250/1360)*main_width,height = (70/768)*main_heigth)

                clock_label = Label(time_frame,font = ('New Roman times',round((18/1360)*main_width), 'bold'),bg = 'skyblue')
                clock_label.pack()
                tick()

                def fetch_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute('select * from students_backup')
                    rows = cur.fetchall()
            
                    if len(rows)!= 0:
                        student_table.delete(* student_table.get_children())
                        for row in rows:
                                student_table.insert('',END,values = row)
                        con.commit()
                    con.close()

                def get_cursor(event):
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                    Name.set(row[0])
                    Fathersname.set(row[1])
                    Mothers_Name.set(row[2])
                    DOB.set(row[3])
                    scholar.set(row[4])
                    Class.set(row[5])
                    Accountno.set(row[6])
                    Aadharno.set(row[7])
                    SSSMID.set(row[8])
                def add_students():
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('insert into students (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9]))
                    cur.execute('delete  from students_backup where  scholar_id = %s',row[4])
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Selected Data backuped successfully")
                    fetch_data()
                def Permanentlyd():
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                    messagebox.askyesno('Warning','Do you really wants to delete data permanently')
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('delete  from students_backup where  scholar_id = %s',row[4])
                    messagebox.showinfo("Notification",'Your selected data is permanently Erased!')
                    con.commit()
                    con.close()
                    fetch_data()

                def search_data():
                    if search_by.get() == '' or  search_txt.get() == '':
                        messagebox.showerror("Error",'All Fields are Required!!')
                    else:        
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute("select * from students_backup where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                            student_table.delete(*student_table.get_children())
                            for row in rows:
                                student_table.insert('',END,values = row)
                            con.commit()
                        con.close()

                    
                ################### Title Frame ############################################################

                title_frame = Frame(root,bd  = round((8/1360)*main_width) ,relief = GROOVE,bg = 'skyblue')
                title_frame.place(x = (430/1360)*main_width , y = (90/768)*main_heigth, width = (800/1360)*main_width , height = (65/768)*main_heigth)
                

                slider_label = Label(title_frame,text = ss,font = ('New Roman times',round((24/1360)*main_width), 'bold'),bg = 'skyblue')
                slider_label.pack()

                def IntroLabelTick():
                    global count,text
                    if count >= len(ss):

                        count = -1
                        text = ''
                        slider_label.config(text = text)
                    else:
                        text = text+ss[count]
                        slider_label.config(text = text)
                    count += 1
                    slider_label.after(300,IntroLabelTick)
                IntroLabelTick()
                
                ################### main Frame ##########################################################
                main_frame =  Frame(root,bd  = 8 ,relief = GROOVE,bg = 'skyblue')
                main_frame.place(x = (30/1360)*main_width,y = (163/768)*main_heigth,width = (1200/1360)*main_width,height = (535/768)*main_heigth)
                ################### Buttons ########################################
                btnframe = Frame(main_frame,bd  = (8/1360)*main_width ,relief = GROOVE,bg = 'skyblue')
                btnframe.place(x = (20/1360)*main_width,y = (450/768)*main_heigth,width = (1150/1360)*main_width,height = (60/768)*main_heigth)
                backupbtn = Button(btnframe,text = 'Backup Data',width=round((9/1360)*main_width),bg = 'Skyblue',font = ('time new roman',round((13/1360)*main_width),'bold'),activebackground = 'maroon3',command = add_students)
                backupbtn.place(x = (40/1360)*main_width,y = (12/1360)*main_width,width =(400/1360)*main_width,height = (30/768)*main_heigth)
                countbtn = Button(btnframe,text = 'Permanently Delete',width=round((9/1360)*main_width),bg = 'Skyblue',font = ('time new roman',round((13/1360)*main_width),'bold'),activebackground = 'maroon3',command = Permanentlyd)
                countbtn.place(x = (700/1360)*main_width,y = (12/1360)*main_width,width =(400/1360)*main_width,height = (30/768)*main_heigth)
                ########################## Search Frame ###################################################
                search_frame = Frame(main_frame,bd  = (8/1360)*main_width ,relief = GROOVE,bg = 'skyblue')
                search_frame.place(x = (20/1360)*main_width,y = (10/1360)*main_width,width = (1150/1360)*main_width,height = (73/768)*main_heigth)
                combo_serch = ttk.Combobox(search_frame,width = 10,font = ('time new roman',round((20/1360)*main_width),'bold'),state = 'readonly')
                combo_serch['values'] = ['Name','Address','Accountno','SSSMID','Class','Aadharno','Scholar_id']
                combo_serch.grid(row=0,column = 1 , padx = (20/1360)*main_width ,pady = (10/768)*main_heigth)

                txt_serch = Entry(search_frame,font = ('time now roman',round((20/1360)*main_width),'bold'),bd = round((5/1360)*main_width) , relief = GROOVE,bg = 'skyblue')
                txt_serch.grid(row = 0,column = 2,pady = (10/768)*main_heigth,padx = (130/1360)*main_width,sticky = W )


                serchbtn = Button(search_frame,text = 'Search',width=round((10/1360)*main_width), pady = (5/768)*main_heigth,bg = 'light pink',command = search_data).grid(row=0,column = 3,padx =8,pady = 10)
                showalltbtn = Button(search_frame,text = 'Show All',width=round((10/1360)*main_width),bg = 'light pink',command = fetch_data).grid(row=0,column = 4,padx =(8/1360)*main_width,pady = (10/768)*main_heigth)


                lbl_serch = Label(search_frame,text = "Search By",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((14/1360)*main_width),'bold'))
                lbl_serch.grid(row = 0,column = 0,pady = (10/768)*main_heigth,padx = (20/1360)*main_width,sticky = W )
                ########################## Table View #####################################################
                Table_Frame = Frame(main_frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
                Table_Frame.place(x = (10/1360)*main_width,y = (90/768)*main_heigth,width = (1150/1360)*main_width,height = (350/768)*main_heigth)
                scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
                scroll_y = Scrollbar(Table_Frame,orient = VERTICAL)

                student_table = ttk.Treeview(Table_Frame,columns = ('Name',"Father's Name","Mother's Name",'D.O.B','Scholar_ID','Class_ID','Account No.','Aadhar No.','SSSMID2','Address'),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
                scroll_x.pack(side = BOTTOM,fill = X)
                scroll_y.pack(side = RIGHT , fill =Y)
                scroll_x.config(command = student_table.xview)
                scroll_y.config(command = student_table.yview)
                student_table.bind("<ButtonRelease-1>",get_cursor)
                student_table.heading('Name',text = 'Name' )
                student_table.heading("Father's Name",text = "Father's Name" )
                student_table.heading("Mother's Name",text = "Mother's Name" )
                student_table.heading('D.O.B',text = 'D.O.B' )
                student_table.heading('Scholar_ID',text = 'Scholar ID.')
                student_table.heading('Class_ID',text = 'Class_ID' )
                student_table.heading('Account No.',text = 'Account No.' )
                student_table.heading('Aadhar No.',text = 'Aadhar No.' )
                student_table.heading('SSSMID2',text = 'SSSMID' )
                student_table.heading('Address',text = 'Address' )
                student_table['show'] = 'headings'
                student_table.column('Name',width = round((200/1360)*main_width))
                student_table.column("Father's Name",width =round((200/1360)*main_width))
                student_table.column('D.O.B',width = round((80/1360)*main_width))
                student_table.column('Scholar_ID',width = round((250/1360)*main_width))
                student_table.column('Class_ID',width = round((90/1360)*main_width))
                student_table.column('Account No.',width = round((260/1360)*main_width))
                student_table.column('Aadhar No.',width = round((260/1360)*main_width))
                student_table.column('SSSMID2',width = round((260/1360)*main_width))
                student_table.column('Address',width = round((300/1360)*main_width))
                student_table.pack(fill = BOTH,expand = 1)
                style = ttk.Style()
                style.configure('Treeview.Heading',font = ('time now roman',round((12/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                style.configure('Treeview',font = ('time now roman',round((10/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                fetch_data()
            
                root.mainloop()
            ################################# main fees management ########################################
            def feesm():
                root = Toplevel(rootm)
                root = root
                root.title('Fees Management system')
                photo = PhotoImage(file = 'school.png')
                root.iconphoto(FALSE,photo)
                root.config(bg = 'skyblue')
                root.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth(),rootm.winfo_screenheight()))
                root.grab_set()

                def main():
                    root.destroy()
                def main1(event):
                    root.destroy()
                root.bind('<End>',main1)
                title = Label(root,text = 'Fees Management System',font = ('time now roman',round((35/1360)*main_width),'bold'),bg = 'lightpink',fg = 'Black',bd = round((10/1360)*main_width),relief = 'sunken')
                title.pack(side = TOP,fill = X)
                butn = Button(root,text = 'MAIN MENU',width=round((10/1360)*main_width),font = ('time now roman',round((15/1360)*main_width),'bold'),bg = 'skyblue',fg = 'Black',command = main).place(x = round((1200/1360)*main_width),y = (15/768)*main_heigth ,width = (120/1360)*main_width,height = (40/768)*main_heigth)

                ########################## All Variables ######################################################
                Name = StringVar()
                Fathersname = StringVar()
                Phonenumber= StringVar()
                Class = StringVar()
                installment = StringVar()
                Deposit_1_Date = StringVar()
                Deposit_2_Date = StringVar()
                Deposit_3_Date = StringVar()
                search_by = StringVar()
                search_txt = StringVar()
                Fees_Deposit = IntVar()
                livedate = StringVar()
                Annual_Fees = IntVar()
                due_Fees = StringVar()


                ##################### Time Frame ########################################################

                def tick():
                    time_string = time.strftime('%H:%M:%S')
                    date_string = time.strftime('%d/%m/%Y')
                    clock_label.config(text = "Date:"+date_string+'\n'+'Time:'+ time_string)
                    clock_label.after(100,tick)

                time_frame = Frame(root,bd  = round((8/1360)*main_width) ,relief = GROOVE,bg = 'skyblue')
                time_frame.place(x = (15/1360)*main_width,y = (90/768)*main_heigth,width = (250/1360)*main_width,height = (70/768)*main_heigth)

                clock_label = Label(time_frame,font = ('New Roman times',round((18/1360)*main_width), 'bold'),bg = 'skyblue')
                clock_label.pack()
                tick()
                ####################################  Button Functions #########################################

                def fetch_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute('select Name,Fathersname,Phone_number,Class_id,Annual_Fees,Deposit_1,Deposit_1_Date,Deposit_2,Deposit_2_Date,Deposit_3,Deposit_3_Date,Due_Fees from students')
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                        student_table.delete(* student_table.get_children())
                        for row in rows:
                                student_table.insert('',END,values = row)
                        con.commit()
                    con.close()
                def clear():
                    Fees_Deposit.set('')
                    Name.set('')
                    Fathersname.set('')
                    Phonenumber.set('')
                    Class.set('')
                    installment.set('')
                    Fees_Deposit.set('')
                    Annual_Fees.set('')
                    due_Fees.set('')

                ################################# Get Cursor ###############################################

                def get_cursor(event):
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                
                    
                    Name.set(row[0])
                    Fathersname.set(row[1])
                    Phonenumber.set(row[2])
                    Class.set(row[3])
                    Annual_Fees.set(row[4])
                    Due_Fees = int(row[4])-(int(row[5])+int(row[7])+int(row[9]))
                    con = pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('update  students set Due_Fees = %s where  Class_id = %s' ,(Due_Fees,Class.get()))
                    con.commit()
                    con.close()
                    due_Fees.set(row[11])
                    if installment.get() == 'Deposit.1':
                        Fees_Deposit.set(row[5])
                    elif installment.get() == 'Deposit.2':
                        Fees_Deposit.set(row[7])
                    elif installment.get() == 'Deposit.3':
                        Fees_Deposit.set(row[9])


                ############################## Update ##############################################################
                def update_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    if installment.get() == 'Deposit.1':
                        livedate =  time.strftime('%d/%m/%Y')
                        cur.execute('update  students set Phone_number = %s,Deposit_1 = %s,Deposit_1_Date = %s , Annual_Fees = %s  where  Class_id = %s' ,(
                            Phonenumber.get(),
                            Fees_Deposit.get(),
                            livedate,
                            Annual_Fees.get(),
                            Class.get()))
                        messagebox.showwarning('update','Update Required')
                    elif installment.get() == 'Deposit.2':
                        livedate =  time.strftime('%d/%m/%Y')
                        cur.execute('update  students set Phone_number = %s, Deposit_2 = %s,Deposit_2_Date = %s , Annual_Fees = %s  where  Class_id = %s' ,(
                            Phonenumber.get(),
                            Fees_Deposit.get(),
                            livedate,
                            Annual_Fees.get(),
                            Class.get()))
                        messagebox.showwarning('update','Update Required')
                    elif installment.get() == 'Deposit.3':
                        livedate = time.strftime('%d/%m/%Y')
                        cur.execute('update  students set Phone_number = %s,Deposit_3 = %s,Deposit_3_Date = %s, Annual_Fees = %s where  Class_id = %s' ,(
                            Phonenumber.get(),
                            Fees_Deposit.get(),
                            livedate,
                            Annual_Fees.get(),
                            Class.get()))   
                        messagebox.showwarning('update','Update Required')
                    elif Name.get() == '' and Fathersname.get() == '' and Phonenumber.get() == '' and Class == '' :
                        messagebox.showerror("Error",'Fileds are Required!')
                    else:
                        cur.execute('update  students set Phone_number = %s, Annual_Fees = %s where  Class_id = %s' ,(
                            Phonenumber.get(),
                            Annual_Fees.get(),
                            Class.get()))
                        messagebox.showinfo('Updated','Selected Rows successfully updated!')
                    con.commit()
                    fetch_data()
                    clear()
                    con.close()

                ############### search_data #########################################################
                def search_data():
                    if search_by.get() == '' or  search_txt.get() == '':
                        messagebox.showerror("Error",'All Fields are Required!!')
                    elif search_by.get() == 'Less than Due Fees' :
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute("select  Name,Fathersname,Phone_number,Class_id,Annual_Fees,Deposit_1,Deposit_1_Date,Deposit_2,Deposit_2_Date,Deposit_3,Deposit_3_Date,Due_Fees  from students where Due_Fees < "+str(search_txt.get()))
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                            student_table.delete(* student_table.get_children())
                            for row in rows:
                                    student_table.insert('',END,values = row)
                            con.commit()
                        con.close()
                    elif search_by.get() == 'Greater than Due Fees' :
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute("select  Name,Fathersname,Phone_number,Class_id,Annual_Fees,Deposit_1,Deposit_1_Date,Deposit_2,Deposit_2_Date,Deposit_3,Deposit_3_Date,Due_Fees  from students where Due_Fees > "+str(search_txt.get()))
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                            student_table.delete(* student_table.get_children())
                            for row in rows:
                                    student_table.insert('',END,values = row)
                            con.commit()
                        con.close()


                    else:        
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute("select  Name,Fathersname,Phone_number,Class_id,Annual_Fees,Deposit_1,Deposit_1_Date,Deposit_2,Deposit_2_Date,Deposit_3,Deposit_3_Date,Due_Fees  from students where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                            student_table.delete(* student_table.get_children())
                            for row in rows:
                                student_table.insert('',END,values = row)
                            con.commit()
                        con.close()

                def exportstudent():
                    ff = filedialog.asksaveasfilename()  
                    gg = student_table.get_children()
                    name,fathersname,phonenumber,class_id,deposit_1,deposit_1_Date,deposit_2,deposit_2_Date,deposit_3,deposit_3_Date,annual_Fees,due_fees = [],[],[],[],[],[],[],[],[],[],[],[]
                    for i in gg:
                        content = student_table.item(i)
                        pp = content['values']
                        name.append(pp[0]),fathersname.append(pp[1]),phonenumber.append(pp[2]),class_id.append(pp[3]),deposit_1.append(pp[4]),deposit_1_Date.append(pp[5]),deposit_2.append(pp[6]),deposit_2_Date.append(pp[7]),deposit_3.append(pp[8]),deposit_3_Date.append(pp[9]),annual_Fees.append(pp[10]),due_fees.append(pp[11])
                    dd = ['name','fathersname','phonenumber','class_id','deposit_1','deposit_1_Date','deposit_2','deposit_2_Date','deposit_3','deposit_3_Date','annual_Fees','due_fees']
                    df = pd.DataFrame(list(zip(name,fathersname,phonenumber,class_id,deposit_1,deposit_1_Date,deposit_2,deposit_2_Date,deposit_3,deposit_3_Date,annual_Fees,due_fees)),columns =dd)
                    paths = r'{}.csv'.format(ff)
                    df.to_csv(paths,index=False)
                    messagebox.showinfo('Notification','Students data is Saved {}'.format(paths))
                #################### Hover Effect ###################################
                def onButton1(e):
                    updatebtn['bg'] ='light pink'
                def leaveButton1(e):
                    updatebtn['bg'] = 'skyblue'

                def onButton2(event):
                    cleartbtn['bg'] ='light pink'   
                def leaveButton2(event):
                    cleartbtn['bg'] = 'skyblue'

                def onButton3(event):
                    exportbtn['bg'] ='light pink'    
                def leaveButton3(event):
                    exportbtn['bg'] ='skyblue'

                ################### Title Frame ############################################################

                title_frame = Frame(root,bd  = (8/1360)*main_width ,relief = GROOVE,bg = 'skyblue')
                title_frame.place(x = (430/1360)*main_width , y = (90/768)*main_heigth, width = (800/1360)*main_width , height = (65/768)*main_heigth)
                ss = 'Prime Motivation 2020-2021 Session'
                count = 0
                text = '' 

                slider_label = Label(title_frame,text = ss,font = ('New Roman times',round((23/1360)*main_width), 'bold'),bg = 'skyblue')
                slider_label.pack()

                def IntroLabelTick():
                    global count,text
                    if count >= len(ss):
                        slider_label.config(text = text)
                    else:
                        text = text+ss[count]
                        slider_label.config(text = text)
                    count += 1
                    slider_label.after(300,IntroLabelTick)
                IntroLabelTick()

                ################# Manage Frame ##############################################################
                Manage_frame = Frame(root,bd  = (8/1360)*main_width ,relief = GROOVE,bg = 'skyblue')
                Manage_frame.place(x = (20/1360)*main_width , y = (180/768)*main_heigth, width = (450/1360)*main_width , height = (500/768)*main_heigth)

                ################## Name #################################################################
                lbl_name = Label(Manage_frame,text = "Name." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
                lbl_name.grid(row = 1,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
                txt_name = Entry(Manage_frame,textvariable = Name,font = ('time now roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
                txt_name.grid(row = 1,column = 1,pady = (8/1360)*main_heigth,padx = 18,sticky = W )

                ##################### Father's Name ###################################################
                lbl_fname = Label(Manage_frame,text = "Father's Name." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
                lbl_fname.grid(row = 2,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
                txt_fname = Entry(Manage_frame,textvariable = Fathersname,font = ('time now roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
                txt_fname.grid(row = 2,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )

                ##################### Phone Number ###################################################
                lbl_mname = Label(Manage_frame,text = "Phone Number." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
                lbl_mname.grid(row = 3,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
                txt_mname = Entry(Manage_frame,textvariable =Phonenumber, font = ('time now roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
                txt_mname.grid(row = 3,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )

                ##################### Class ID #########################################################
                lbl_classid = Label(Manage_frame,text = "Class ID." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
                lbl_classid.grid(row = 4,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
                txt_classid = Entry(Manage_frame,textvariable  = Class,font = ('time now roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
                txt_classid.grid(row = 4,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )

                ###################### Installment #######################################################
                lbl_install = Label(Manage_frame,text = "Installment No." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
                lbl_install.grid(row = 5,column = 0,pady =(8/768)*main_heigth,padx =(15/1360)*main_width,sticky = W )
                combo_install = ttk.Combobox(Manage_frame,textvariable  = installment,width = 10,font = ('time new roman',round((14/1360)*main_width),'bold'),state = 'readonly')
                combo_install['values'] = ['Deposit.1','Deposit.2','Deposit.3']
                combo_install.grid(row=5,column = 1 , padx = (20/1360)*main_width ,pady =(8/768)*main_heigth)

                ##################### Fees Deposit ###########################################################
                lbl_feesd = Label(Manage_frame,text = "Fees Deposit." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
                lbl_feesd.grid(row = 6,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
                txt_feesd = Entry(Manage_frame,textvariable  = Fees_Deposit,font = ('time now roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
                txt_feesd.grid(row = 6,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
                ##################### Annual Fees #########################################################
                lbl_annual = Label(Manage_frame,text = "Annual Fees." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
                lbl_annual.grid(row = 7,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
                txt_annual = Entry(Manage_frame,textvariable  = Annual_Fees,font = ('time new roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
                txt_annual.grid(row = 7,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )

                #################### Due Fees ###########################################################
                lbl_feesdue = Label(Manage_frame,text = "Due Fees" ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
                lbl_feesdue.grid(row = 8,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
                lbl_feesdue = Entry(Manage_frame,textvariable  = due_Fees,font = ('time new roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
                lbl_feesdue.grid(row = 8,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )

                ########################## Button Frame #################################################################
                btn_Frame = Frame(Manage_frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
                btn_Frame.place(x = (5/1360)*main_width ,y = (420/768)*main_heigth,width =(420/1360)*main_width)

                updatebtn = Button(btn_Frame,text = 'Update',width=9,bg = 'Skyblue',font = ('time new roman',round((13/1360)*main_width),'bold'),command =update_data,activebackground = 'maroon3')
                updatebtn.grid(row=0,column = 1,padx =(15/1360)*main_width,pady = (8/1360)*main_heigth)
                updatebtn.bind('<Enter>',onButton1)
                updatebtn.bind('<Leave>',leaveButton1)
                cleartbtn = Button(btn_Frame,text = 'Clear',width=round((9/1360)*main_width),bg = 'skyblue',font = ('time new roman',round((13/1360)*main_width),'bold'),command =clear,activebackground = 'Hotpink')
                cleartbtn.grid(row=0,column = 5,padx =(25/1360)*main_width,pady = (8/768)*main_heigth)
                cleartbtn.bind('<Enter>',onButton2)
                cleartbtn.bind('<Leave>',leaveButton2)
                exportbtn = Button(btn_Frame,text = 'Export',width = round((9/1360)*main_width),bg = 'skyblue',font =  ('time new roman',round((13/1360)*main_width),'bold'),command =exportstudent,activebackground = 'VioletRed2')
                exportbtn.grid(row=0,column = 8,padx =(15/1360)*main_width,pady = (8/768)*main_heigth)
                exportbtn.bind('<Enter>',onButton3)
                exportbtn.bind('<Leave>',leaveButton3)
                ################### Detail Frame ##########################################################
                detail_frame =  Frame(root,bd  = 8 ,relief = GROOVE,bg = 'skyblue')
                detail_frame.place(x = (500/1360)*main_width,y = (180/768)*main_heigth,width = (810/1360)*main_width,height = (500/768)*main_heigth)


                lbl_serch = Label(detail_frame,text = "Search By",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((14/1360)*main_width),'bold'))
                lbl_serch.grid(row = 0,column = 0,pady = 10,padx = 20,sticky = W )

                combo_serch = ttk.Combobox(detail_frame,textvariable = search_by,width = round((10/1360)*main_width),font = ('time new roman',round((13/1360)*main_width),'bold'),state = 'readonly')
                combo_serch['values'] = ['Name','Class_id','Fathers Name','Phone_number','Due_Fees','Less than Due Fees','Greater than Due Fees']
                combo_serch.grid(row=0,column = 1 , padx = (20/1360)*main_width ,pady = (10/768)*main_heigth)

                txt_serch = Entry(detail_frame,textvariable = search_txt,font = ('time now roman',round((13/1360)*main_width),'bold'),bd = 5 , relief = GROOVE,bg = 'skyblue')
                txt_serch.grid(row = 0,column = 2,pady = (10/768)*main_heigth,padx = (20/1360)*main_width,sticky = W )


                serchbtn = Button(detail_frame,text = 'Search',width=round((10/1360)*main_width), pady = (5/768)*main_heigth,bg = 'light pink',command = search_data).grid(row=0,column = 3,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)
                showalltbtn = Button(detail_frame,text = 'Show All',width=10,bg = 'light pink',command = fetch_data).grid(row=0,column = 4,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)
                def next_w(event):
                    event.widget.tk_focusNext().focus()
                    return 'break'
                txt_name.bind('<Down>',next_w)
                txt_fname.bind('<Down>',next_w)
                txt_mname.bind('<Down>',next_w)
                txt_classid.bind('<Down>',next_w)
                txt_feesd.bind('<Down>',next_w)
                txt_annual.bind('<Down>',next_w)
                def next_w(event):
                    event.widget.tk_focusPrev().focus()
                    return 'break'
                txt_feesd.bind('<Up>',next_w)
                txt_classid.bind('<Up>',next_w)
                txt_mname.bind('<Up>',next_w)
                txt_fname.bind('<Up>',next_w)
                txt_annual.bind('<Up>',next_w)
                txt_feesd.bind('<Up>',next_w)
            

                ################################## Table-Frame #############################################################
                Table_Frame = Frame(detail_frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
                Table_Frame.place(x = (10/1360)*main_width,y = (70/768)*main_heigth,width = (760/1360)*main_width,height = (400/768)*main_heigth)
                style = ttk.Style()
                style.configure('Treeview.Heading',font = ('time now roman',round((10/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                style.configure('Treeview',font = ('time now roman',round((8/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')

                scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
                scroll_y = Scrollbar(Table_Frame,orient = VERTICAL)
                student_table = ttk.Treeview(Table_Frame,columns = ('Name',"Father's Name","Phone number",'Class ID','Annual Fees','Deposit.1','Deposit.1 Date','Deposit.2','Deposit.2 Date','Deposit.3','Deposit.3 Date','Due Fees'),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
                scroll_x.pack(side = BOTTOM,fill = X)
                scroll_y.pack(side = RIGHT , fill =Y)
                scroll_x.config(command =student_table.xview,bg = 'skyblue')
                scroll_y.config(command =student_table.yview,bg = 'skyblue')
                student_table.bind("<ButtonRelease-1>",get_cursor)
                student_table.heading('Name',text = 'Name' )
                student_table.heading("Father's Name",text = "Father's Name" )
                student_table.heading("Phone number",text = "Phone number" )
                student_table.heading('Class ID',text = 'Class ID' )
                student_table.heading('Annual Fees',text = 'Annual Fees')
                student_table.heading('Deposit.1',text = 'Deposit.1' )
                student_table.heading('Deposit.1 Date',text = 'Deposit.1 Date' )
                student_table.heading('Deposit.2',text = 'Deposit.2' )
                student_table.heading('Deposit.2 Date',text = 'Deposit.2 Date' )
                student_table.heading('Deposit.3',text = 'Deposit.3' )
                student_table.heading('Deposit.3 Date',text = 'Deposit.3 Date' )
                student_table.heading('Due Fees',text = 'Due Fees' )
                student_table.column('Name',width = round((140/1360)*main_width))
                student_table.column("Father's Name",width =round((140/1360)*main_width))
                student_table.column("Phone number",width = round((120/1360)*main_width))
                student_table.column('Class ID',width = round((70/1360)*main_width))
                student_table.column('Annual Fees',width = round((90/1360)*main_width))
                student_table.column('Deposit.1',width = round((90/1360)*main_width))
                student_table.column('Deposit.1 Date',width = round((100/1360)*main_width))
                student_table.column('Deposit.2',width = round((100/1360)*main_width))
                student_table.column('Deposit.2 Date',width = round((100/1360)*main_width))
                student_table.column('Deposit.3',width = round((90/1360)*main_width))
                student_table.column('Deposit.3 Date',width = round((100/1360)*main_width))
                student_table.column('Due Fees',width = round((90/1360)*main_width))
                student_table['show'] = 'headings'

                student_table.pack(fill = BOTH,expand = 1)
                fetch_data()
                root.mainloop()
            def stud():

                root1 = Toplevel(rootm)

                root1.title('Student Management system')
                photo = PhotoImage(file = 'school.png')
                root1.iconphoto(FALSE,photo)

                root1.config(bg = 'skyblue')
                root1.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth(),rootm.winfo_screenheight()))
                root1.grab_set()
                def main():
                    root1.destroy()
                def main1(event):
                    root1.destroy()
                root1.bind('<End>',main1)

                title = Label(root1,text = 'Students Management System',font = ('time now roman',round((35/1360)*main_width),'bold'),bg = 'lightpink',fg = 'Black',bd = round((10/1360)*main_width),relief = 'sunken')
                title.pack(side = TOP,fill = X)
                butn = Button(root1,text = 'MAIN MENU',width=round((10/1360)*main_width),font = ('time now roman',round((15/1360)*main_width),'bold'),bg = 'skyblue',fg = 'Black',command = main)
                butn.place(x = round((1200/1360)*main_width),y = round((15/768)*main_heigth),width = round((120/1360)*main_width),height = round((35/768)*main_heigth))


            ######### All Variables #########################################################################################################################################################
                Name = StringVar()
                Fathersname = StringVar()
                Mothers_Name = StringVar()
                DOB = StringVar()
                Phonenumber = StringVar()
                Class = StringVar()
                Accountno = StringVar()
                Aadharno = StringVar()
                SSSMID = StringVar() 
                Address = StringVar()
                search_by = StringVar()
                search_txt = StringVar()
                scholar = StringVar()
            ################################### All Functions #######################################################################################################################################################################################################################################################################
            ######################### Add students fuction #####################################################################################################################################################################################################
                def add_students():
                        if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                                messagebox.showerror("Error",'All Fields are Required!!')
                        else:
                                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                                cur = con.cursor()
                                cur.execute('insert into students (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                Name.get(),
                                Fathersname.get(),
                                Mothers_Name.get(),
                                DOB.get(),
                                scholar.get(),
                                Class.get(),
                                Accountno.get(),
                                Aadharno.get(),
                                SSSMID.get(),
                                txt_add.get('1.0',END)))
                                con.commit()
                                fetch_data()
                                clear()
                                con.close()
                                messagebox.showinfo("Success","Message has been inserted")
                def fetch_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute('select * from students')
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                                student_table.delete(* student_table.get_children())
                                for row in rows:
                                        student_table.insert('',END,values = row)
                                con.commit()
                        con.close()
                def clear():
                        Name.set('')
                        Fathersname.set('')
                        Mothers_Name.set('')
                        DOB.set('')
                        scholar.set('')
                        Class.set('')
                        Accountno.set('')
                        Aadharno.set('')
                        SSSMID.set('') 
                        txt_add.delete('1.0',END)

                ########## get_cursor ##################################################################
                def get_cursor(event):
                        cursor_row = student_table.focus()
                        contents = student_table.item(cursor_row)
                        row = contents['values']
                        print(row)
                        Name.set(row[0])
                        Fathersname.set(row[1])
                        Mothers_Name.set(row[2])
                        DOB.set(row[3])
                        scholar.set(row[4])
                        Class.set(row[5])
                        Accountno.set(row[6])
                        Aadharno.set(row[7])
                        SSSMID.set(row[8])
                        txt_add.delete('1.0',END) 
                        txt_add.insert(END,row[9])

                ########### update_data ###############################################################
                def update_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor()
                        cur.execute('update  students set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                        Name.get(),
                        Fathersname.get(),
                        Mothers_Name.get(),
                        DOB.get(),
                        Class.get(),
                        Accountno.get(),
                        Aadharno.get(),
                        SSSMID.get(),
                        txt_add.get('1.0',END),
                        scholar.get()))
                        con.commit()
                        fetch_data()
                        clear()
                        con.close()
    ############################ Delete_data #########################################################
                def delete_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        ask = messagebox.askyesno('Message','Are you Really Want to delete')
                        if ask == True:
                                cur.execute('insert into students_backup (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                Name.get(),
                                Fathersname.get(),
                                Mothers_Name.get(),
                                DOB.get(),
                                scholar.get(),
                                Class.get(),
                                Accountno.get(),
                                Aadharno.get(),
                                SSSMID.get(),
                                txt_add.get('1.0',END)))
                                cur.execute('delete  from students where  scholar_id = %s',scholar.get())
                                con.commit()
                                con.close()
                                fetch_data()
                                clear()

                        ############### search_data #########################################################
                def search_data():
                        if search_by.get() == '' or  search_txt.get() == '':
                                messagebox.showerror("Error",'All Fields are Required!!')
                        else:        
                                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                                cur = con.cursor() 
                                cur.execute("select * from students where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                                rows = cur.fetchall()
                                if len(rows)!= 0:
                                        student_table.delete(*student_table.get_children())
                                        for row in rows:
                                                student_table.insert('',END,values = row)
                                        con.commit()
                                con.close()


                ############## Add students fuction ######################################################
                def add_students():
                        if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                                messagebox.showerror("Error",'All Fields are Required!!')
                        else:
                                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                                cur = con.cursor()
                                cur.execute('insert into students (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                Name.get(),
                                Fathersname.get(),
                                Mothers_Name.get(),
                                DOB.get(),
                                scholar.get(),
                                Class.get(),
                                Accountno.get(),
                                Aadharno.get(),
                                SSSMID.get(),
                                txt_add.get('1.0',END)))
                                con.commit()
                                fetch_data()
                                clear()
                                con.close()
                                messagebox.showinfo("Success","Message has been inserted")
                def saad_stud(event):
                    add_students()
                root1.bind('<Control-s>',saad_stud)
                def fetch_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute('select * from students')
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                                student_table.delete(* student_table.get_children())
                                for row in rows:
                                        student_table.insert('',END,values = row)
                                con.commit()
                        con.close()

                def clear():
                        Name.set('')
                        Fathersname.set('')
                        Mothers_Name.set('')
                        DOB.set('')
                        scholar.set('')
                        Class.set('')
                        Accountno.set('')
                        Aadharno.set('')
                        SSSMID.set('') 
                        txt_add.delete('1.0',END)
                def clr_stud(event):
                    clear()
                root1.bind('<Control-c>',clr_stud)
    ############ get_cursor ##################################################################
                def get_cursor(event):
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                    Name.set(row[0])
                    Fathersname.set(row[1])
                    Mothers_Name.set(row[2])
                    DOB.set(row[3])
                    scholar.set(row[4])
                    Class.set(row[5])
                    Accountno.set(row[6])
                    Aadharno.set(row[7])
                    SSSMID.set(row[8])
                    txt_add.delete('1.0',END) 
                    txt_add.insert(END,row[9])
                root1.bind('<Return>',get_cursor)

                ########### update_data ###############################################################
                def update_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor()
                        cur.execute('update  students set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                        Name.get(),
                        Fathersname.get(),
                        Mothers_Name.get(),
                        DOB.get(),
                        Class.get(),
                        Accountno.get(),
                        Aadharno.get(),
                        SSSMID.get(),
                        txt_add.get('1.0',END),
                        scholar.get()))
                        con.commit()
                        fetch_data()
                        clear()
                        con.close()
                def upd_stud(event):
                    update_data()
                root1.bind('<Control-u>',upd_stud)

                ############## Delete_data #########################################################
                def delete_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        ask = messagebox.askyesno('Message','Are you Really Want to delete')
                        if ask == True:
                                cur.execute('insert into students_backup (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                Name.get(),
                                Fathersname.get(),
                                Mothers_Name.get(),
                                DOB.get(),
                                scholar.get(),
                                Class.get(),
                                Accountno.get(),
                                Aadharno.get(),
                                SSSMID.get(),
                                txt_add.get('1.0',END)))
                                cur.execute('delete  from students where  scholar_id = %s',scholar.get())
                                con.commit()
                                con.close()
                                fetch_data()
                                clear()
                def del_stud(event):
                    delete_data()
                root1.bind('<Delete>',del_stud)

                        ############### search_data #########################################################
                def search_data():
                        if search_by.get() == '' or  search_txt.get() == '':
                                messagebox.showerror("Error",'All Fields are Required!!')
                        else:        
                                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                                cur = con.cursor() 
                                cur.execute("select * from students where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                                rows = cur.fetchall()
                                if len(rows)!= 0:
                                        student_table.delete(*student_table.get_children())
                                        for row in rows:
                                                student_table.insert('',END,values = row)
                                        con.commit()
                                con.close()

                ########################## Manage Frame ###############################################
                Manage_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                Manage_Frame.place(x = (20/1360)*main_width,y = (100/768)*main_heigth,width = (450/1360)*main_width,height = (595/768)*main_heigth)

                m_title = Label(Manage_Frame,text = "Manage Students",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/768)*main_heigth),'bold'))
                m_title.grid(row = 0, columnspan = 2,pady =(8/768)*main_heigth,padx = (8/1360)*main_width)


                ######################### Name ########################################################
                lbl_name = Label(Manage_Frame,text = "Name" ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_name.grid(row = 2,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_name = Entry(Manage_Frame,textvariable = Name,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/768)*main_heigth),bg = 'skyblue' , relief = GROOVE)
                txt_name.grid(row = 2,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Father's Name ###############################################
                lbl_fname = Label(Manage_Frame,text = "Father's name",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_fname.grid(row = 3,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_fname = Entry(Manage_Frame,textvariable = Fathersname ,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd =round((5/768)*main_heigth),bg='skyblue' , relief = GROOVE)
                txt_fname.grid(row = 3,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Mothers name #############################################################
                lbl_mother = Label(Manage_Frame,text = "Mother's Name.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_mother.grid(row = 4,column = 0,pady = (8/1360)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_sssmid = Entry(Manage_Frame,textvariable = Mothers_Name ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width),bg ='skyblue', relief = GROOVE)
                txt_sssmid.grid(row = 4,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ####################### DOB #################################################################
                lbl_dob = Label(Manage_Frame,text = "Date of Birth",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_dob.grid(row = 5,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_dob = Entry(Manage_Frame,textvariable = DOB,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd = round((5/1360)*main_width),bg ='skyblue' , relief = GROOVE)
                txt_dob.grid(row = 5,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Scholar Id ##################################################
                lbl_scholar = Label(Manage_Frame,text = "Scholar ID.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_scholar.grid(row = 6,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_pnumber = Entry(Manage_Frame,textvariable = scholar,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_pnumber.grid(row = 6,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ###################### class ##############################################################
                lbl_class = Label(Manage_Frame,text = "Class ID",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_class.grid(row = 7,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_class= Entry(Manage_Frame,textvariable = Class,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_class.grid(row = 7,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ##################### Account no. #########################################################
                lbl_acc = Label(Manage_Frame,text = "Account No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_acc.grid(row = 8,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_acc = Entry(Manage_Frame,textvariable = Accountno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_acc.grid(row = 8,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                #####################  Aadhar no. ##########################################################
                lbl_aadhar = Label(Manage_Frame,text = "Aadhar No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_aadhar.grid(row = 9,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_aadhar = Entry(Manage_Frame,textvariable =   Aadharno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_aadhar.grid(row = 9,column = 1,pady = round((8/768)*main_heigth),padx = round((18/1360)*main_width),sticky = W )

                ####################### SSSMID No #############################################################

                lbl_sssmid = Label(Manage_Frame,text = "SSSMID No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_sssmid.grid(row = 10,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_sssmid = Entry(Manage_Frame,textvariable = SSSMID ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_sssmid.grid(row = 10,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################### Address. ###########################################################
                lbl_add = Label(Manage_Frame,text = "Address.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_add.grid(row = 11,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_add = Text(Manage_Frame,width  = round((37/1360)*main_width) ,height = round((2/768)*main_heigth),font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_add.grid(row = 11,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )



                ########################## Button Frame #################################################################
                btn_Frame = Frame(Manage_Frame,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                btn_Frame.place(x = (6/1360)*main_width ,y = (520/768)*main_heigth,width =round((420/1360)*main_width))

                Addbtn = Button(btn_Frame,text = 'Add',width=round((10/1360)*main_width),command = add_students,bg = 'Lightpink').grid(row=0,column = 0,padx = (15/1360)*main_width,pady = (10/768)*main_heigth)
                updatebtn = Button(btn_Frame,text = 'Update',width=round((10/1360)*main_width),command = update_data,bg = 'Lightpink').grid(row=0,column = 1,padx =(15/1360)*main_width,pady =(10/768)*main_heigth)
                deletebtn = Button(btn_Frame,text = 'Delete',width=round((10/1360)*main_width),command = delete_data,bg = 'Lightpink').grid(row=0,column = 2,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)
                cleartbtn = Button(btn_Frame,text = 'Clear',width=round((10/1360)*main_width),command = clear,bg = 'Lightpink').grid(row=0,column = 3,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

                ########################## Detail Frame ###############################################        
                Detail_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                Detail_Frame.place(x = round((500/1360)*main_width),y = round((100/768)*main_heigth),width = round((765/1360)*main_width),height = round((590/768)*main_heigth))


                lbl_serch = Label(Detail_Frame,text = "Search By",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((14/1360)*main_width),'bold'))
                lbl_serch.grid(row = 0,column = 0,pady = round((10/768)*main_heigth),padx = round((20/1360)*main_width),sticky = W )


                combo_serch = ttk.Combobox(Detail_Frame,textvariable = search_by,width = round((10/1360)*main_width),font = ('time new roman',round((13/1360)*main_width),'bold'),state = 'readonly')
                combo_serch['values'] = ['Name','Address','Accountno','SSSMID','Class','Aadharno','Scholar_id']
                combo_serch.grid(row=0,column = 1 , padx = (20/1360)*main_width ,pady = (10/768)*main_heigth)

                txt_serch = Entry(Detail_Frame,textvariable = search_txt,font = ('time now roman',round((14/1360)*main_width),'bold'),bd = (5/1360)*main_width ,bg  = 'skyblue', relief = GROOVE)
                txt_serch.grid(row = 0,column = 2,pady = (10/1360)*main_heigth,padx = (20/1360)*main_width,sticky = W )


                serchbtn = Button(Detail_Frame,text = 'Search',width=round((10/1360)*main_width), pady = (5/768)*main_heigth,command = search_data,bg = 'Lightpink').grid(row=0,column = 3,padx =10,pady = 10)
                showalltbtn = Button(Detail_Frame,text = 'Show All',width=round((10/1360)*main_width),command =fetch_data,bg = 'Lightpink').grid(row=0,column = 4,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

                def next_w(event):
                    event.widget.tk_focusNext().focus()
                    return 'break'
                root1.bind_class('Entry','<Down>',next_w)
                def next_w(event):
                    event.widget.tk_focusPrev().focus()
                    return 'break'
                root1.bind_class('Entry','<Up>',next_w)
                def next_w(event):
                    event.widget.tk_focusNext().focus()
                    return 'break'
                root1.bind_class('Button','<Right>',next_w)
                
                
                ################################## Table-Frame #############################################################
                Table_Frame = Frame(Detail_Frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
                Table_Frame.place(x = (10/1360)*main_width,y = (70/768)*main_heigth,width = (740/1360)*main_width,height = (500/768)*main_heigth)
                scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
                scroll_y = Scrollbar(Table_Frame,orient = VERTICAL)

                student_table = ttk.Treeview(Table_Frame,columns = ('Name',"Father's Name","Mother's Name",'D.O.B','Scholar_ID','Class_ID','Account No.','Aadhar No.','SSSMID2','Address'),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
                scroll_x.pack(side = BOTTOM,fill = X)
                scroll_y.pack(side = RIGHT , fill =Y)
                scroll_x.config(command = student_table.xview)
                scroll_y.config(command = student_table.yview)

                student_table.heading('Name',text = 'Name' )
                student_table.heading("Father's Name",text = "Father's Name" )
                student_table.heading("Mother's Name",text = "Mother's Name" )
                student_table.heading('D.O.B',text = 'D.O.B' )
                student_table.heading('Scholar_ID',text = 'Scholar ID.')
                student_table.heading('Class_ID',text = 'Class_ID' )
                student_table.heading('Account No.',text = 'Account No.' )
                student_table.heading('Aadhar No.',text = 'Aadhar No.' )
                student_table.heading('SSSMID2',text = 'SSSMID' )
                student_table.heading('Address',text = 'Address' )
                student_table['show'] = 'headings'
                student_table.column('Name',width = 130)
                student_table.column("Father's Name",width =130 )
                student_table.column("Mother's Name",width = 130)
                student_table.column('D.O.B',width = 75)
                student_table.column('Scholar_ID',width = 70)
                student_table.column('Class_ID',width = 50)
                student_table.column('Account No.',width = 180)
                student_table.column('Aadhar No.',width = 180)
                student_table.column('SSSMID2',width = 180)
                student_table.column('Address',width = 200)
                student_table.pack(fill = BOTH,expand = 1)
                student_table.bind("<ButtonRelease-1>",get_cursor)
                style = ttk.Style()
                style.configure('Treeview.Heading',font = ('time now roman',round((12/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                style.configure('Treeview',font = ('time now roman',round((10/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                fetch_data()

                root1.mainloop()  
            def addmi():
                messagebox.showwarning('Attention','you will get this fuction in next update')  
            def idg():
                messagebox.showwarning('Attention','you will get this fuction in next update') 
            def resl():
               messagebox.showerror('Error','This function is only for superuser.  you are a operator')
                        
            imgm = ImageTk.PhotoImage(file = 'students.png')
            b2m = Button(f1m,text = 'Students',image = imgm,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = stud)
            b2m.grid(row = 1 , column = 1 , padx = (20/1360)*main_width,ipadx = (50/1360)*main_width)
            img2m = ImageTk.PhotoImage(file = 'formnew.png')
            b3m = Button(f1m,text = 'Staff-Details',image = img2m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = teacherstaff)
            b3m.grid(row = 1 , column = 5 , padx=(120/1360)*main_width , pady = (20/768)*main_heigth,ipadx = (50/1360)*main_width)
            img3m = ImageTk.PhotoImage(Image.open('time-and-date.png'))
            b3m = Button(f1m,text = 'Generate Result',image = img3m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = idg)
            b3m.grid(row = 1 , column = 7 , padx=(100/1360)*main_width , pady = (20/768)*main_heigth,ipadx = (50/1360)*main_width)
            img4m = ImageTk.PhotoImage(Image.open('fees.png'))
            b4m = Button(f1m,text = 'Fees Management',image = img4m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = feesm)
            b4m.grid(row = 5 , column = 1 , padx=(20/1360)*main_width,pady = (120/768)*main_heigth,ipadx = (50/1360)*main_width)
            img5m = ImageTk.PhotoImage(Image.open('Tc.png'))
            b5m = Button(f1m,text = 'Backup',image = img5m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = backup)
            b5m.grid(row = 5 , column = 5 , padx=(130/1360)*main_width,pady = (20/768)*main_heigth,ipadx = (40/1360)*main_width)
            img6m = ImageTk.PhotoImage(Image.open('result.png'))
            b6m = Button(f1m,text = 'Add New User',image = img6m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = resl)
            b6m.grid(row = 5 , column = 7 , padx=(130/1360)*main_width,pady = (20/768)*main_heigth,ipadx = (40/1360)*main_width)
            rootm.mainloop()















        else:
             messagebox.showerror('Error','Usernot found in database')
    elif operator.get() == 0 and cpassword.get() == 1:
        mydb = pymysql.connect(host="localhost",user="root",password="",database="school")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM teacher where username = %s and password = %s",(uname.get(),passwrd.get()))
        myresult = mycursor.fetchall()
        mainl = str(len(myresult))
        if mainl == '1':
            root.destroy()
            rootm = Tk()
            photo = PhotoImage(file = 'school.png')
            rootm.iconphoto(FALSE,photo)
            rootm.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth()-10,rootm.winfo_screenheight()-10))
            rootm.title('School Management')
            rootm.config(bg = 'cornsilk')
            menu1 = Label(rootm,text = 'Advance School management',font = ('times new roman',round((30/1360)*main_width),'bold'), bg ='cornflowerblue',fg = 'Black',relief = 'solid')
            menu1.pack(side = TOP,fill = X)
            f1m = Frame(rootm,bd = (4/1360)*main_width,relief = RIDGE,bg = 'skyblue' )
            f1m.place(x = (25/1360)*main_width ,y = (80/1360)*main_width,width = (1310/1360)*main_width,height = (590/768)*main_heigth)
            print(f1m.winfo_screenwidth())
            recenttime =  time.strftime('%H:%M:%S')
            rect.append(recenttime)
            print(rect)
            statusbar = Label(rootm,text = 'On the way',bd = 1,relief = SUNKEN,anchor = W)
            statusbar.pack(side = BOTTOM , fill = X)
            def teacherstaff():
                
                root1 = Toplevel(rootm)

                root1.title('Teachers Management system')
                photo = PhotoImage(file = 'school.png')
                root1.iconphoto(FALSE,photo)

                root1.config(bg = 'skyblue')
                root1.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth(),rootm.winfo_screenheight()))
                root1.grab_set()
                def main():
                    root1.destroy()
                def main1(event):
                    root1.destroy()
                root1.bind('<End>',main1)

                title = Label(root1,text = 'Teachers Management System',font = ('time now roman',round((35/1360)*main_width),'bold'),bg = 'lightpink',fg = 'Black',bd = round((10/1360)*main_width),relief = 'sunken')
                title.pack(side = TOP,fill = X)
                butn = Button(root1,text = 'MAIN MENU',width=round((10/1360)*main_width),font = ('time now roman',round((15/1360)*main_width),'bold'),bg = 'skyblue',fg = 'Black',command = main)
                butn.place(x = round((1200/1360)*main_width),y = round((15/768)*main_heigth),width = round((120/1360)*main_width),height = round((35/768)*main_heigth))

            ######### All Variables #########################################################################################################################################################
                Name = StringVar() # name
                Fathersname = StringVar()#  Fathersname
                Mothers_Name = StringVar()# Mother_Name
                DOB = StringVar()        # DOB 
                Phonenumber = StringVar()  # phone number
                Class = StringVar()      # class # Subjectteaching
                Accountno = StringVar()  # Accountno # teachingclass
                Aadharno = StringVar()   # Aadharno   # Aadharno
                SSSMID = StringVar()     # SSSMID   # Emailid
                Address = StringVar()    # Address   # Address
                search_by = StringVar()  # search_by  
                search_txt = StringVar() # search_txt
                scholar = StringVar()    # scholar   # scholar
            ################################### All Functions #######################################################################################################################################################################################################################################################################
            ######################### Add students fuction #####################################################################################################################################################################################################
                def add_students():
                    if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                        messagebox.showerror("Error",'All Fields are Required!!')
                    else:
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor()
                        cur.execute('insert into staff (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                        Name.get(),
                        Fathersname.get(),
                        Mothers_Name.get(),
                        DOB.get(),
                        scholar.get(),
                        Class.get(),
                        Accountno.get(),
                        Aadharno.get(),
                        SSSMID.get(),
                        txt_add.get('1.0',END)))
                        con.commit()
                        fetch_data()
                        clear()
                        con.close()
                        messagebox.showinfo("Success","Message has been inserted")
                def fetch_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute('select * from staff')
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                            student_table.delete(* student_table.get_children())
                            for row in rows:
                                    student_table.insert('',END,values = row)
                            con.commit()
                    con.close()
                def clear():
                    Name.set('')
                    Fathersname.set('')
                    Mothers_Name.set('')
                    DOB.set('')
                    scholar.set('')
                    Class.set('')
                    Accountno.set('')
                    Aadharno.set('')
                    SSSMID.set('') 
                    txt_add.delete('1.0',END)

                ########## get_cursor ##################################################################
                def get_cursor(event):
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                    print(row)
                    Name.set(row[0])
                    Fathersname.set(row[1])
                    Mothers_Name.set(row[2])
                    DOB.set(row[3])
                    scholar.set(row[4])
                    Class.set(row[5])
                    Accountno.set(row[6])
                    Aadharno.set(row[7])
                    SSSMID.set(row[8])
                    txt_add.delete('1.0',END) 
                    txt_add.insert(END,row[9])

                ########### update_data ###############################################################
                def update_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('update  staff set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                    Name.get(),
                    Fathersname.get(),
                    Mothers_Name.get(),
                    DOB.get(),
                    Class.get(),
                    Accountno.get(),
                    Aadharno.get(),
                    SSSMID.get(),
                    txt_add.get('1.0',END),
                    scholar.get()))
                    con.commit()
                    fetch_data()
                    clear()
                    con.close()
    ############################ Delete_data #########################################################
                def delete_data():
                    messagebox.showerror('Error','You cannot deleted Details.')

                        ############### search_data #########################################################
                def search_data():
                    if search_by.get() == '' or  search_txt.get() == '':
                        messagebox.showerror("Error",'All Fields are Required!!')
                    else:        
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute("select * from staff where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                            student_table.delete(*student_table.get_children())
                            for row in rows:
                                student_table.insert('',END,values = row)
                            con.commit()
                        con.close()


                ############## Add students fuction ######################################################
                def add_students():
                    if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                        messagebox.showerror("Error",'All Fields are Required!!')
                    else:
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor()
                        cur.execute('insert into staff (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                        Name.get(),
                        Fathersname.get(),
                        Mothers_Name.get(),
                        DOB.get(),
                        scholar.get(),
                        Class.get(),
                        Accountno.get(),
                        Aadharno.get(),
                        SSSMID.get(),
                        txt_add.get('1.0',END)))
                        con.commit()
                        fetch_data()
                        clear()
                        con.close()
                        messagebox.showinfo("Success","Message has been inserted")
                def saad_stud(event):
                    add_students()
                root1.bind('<Control-s>',saad_stud)
                def fetch_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute('select * from staff')
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                                student_table.delete(* student_table.get_children())
                                for row in rows:
                                        student_table.insert('',END,values = row)
                                con.commit()
                        con.close()

                def clear():
                        Name.set('')
                        Fathersname.set('')
                        Mothers_Name.set('')
                        DOB.set('')
                        scholar.set('')
                        Class.set('')
                        Accountno.set('')
                        Aadharno.set('')
                        SSSMID.set('') 
                        txt_add.delete('1.0',END)
                def clr_stud(event):
                    clear()
                root1.bind('<Control-c>',clr_stud)
    ############ get_cursor ##################################################################
                def get_cursor(event):
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                    Name.set(row[0])
                    Fathersname.set(row[1])
                    Mothers_Name.set(row[2])
                    DOB.set(row[3])
                    scholar.set(row[4])
                    Class.set(row[5])
                    Accountno.set(row[6])
                    Aadharno.set(row[7])
                    SSSMID.set(row[8])
                    txt_add.delete('1.0',END) 
                    txt_add.insert(END,row[9])
                root1.bind('<Return>',get_cursor)

                ########### update_data ###############################################################
                def update_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor()
                        cur.execute('update  staff set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                        Name.get(),
                        Fathersname.get(),
                        Mothers_Name.get(),
                        DOB.get(),
                        Class.get(),
                        Accountno.get(),
                        Aadharno.get(),
                        SSSMID.get(),
                        txt_add.get('1.0',END),
                        scholar.get()))
                        con.commit()
                        fetch_data()
                        clear()
                        con.close()
                def upd_stud(event):
                    update_data()
                root1.bind('<Control-u>',upd_stud)

                ############## Delete_data #########################################################
                def delete_data():
                        messagebox.showinfo('Sorry','You cannot delete details only superuser can')
                def del_stud(event):
                    delete_data()
                root1.bind('<Delete>',del_stud)

                        ############### search_data #########################################################
                def search_data():
                        if search_by.get() == '' or  search_txt.get() == '':
                                messagebox.showerror("Error",'All Fields are Required!!')
                        else:        
                                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                                cur = con.cursor() 
                                cur.execute("select * from staff where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                                rows = cur.fetchall()
                                if len(rows)!= 0:
                                        student_table.delete(*student_table.get_children())
                                        for row in rows:
                                                student_table.insert('',END,values = row)
                                        con.commit()
                                con.close()

                ########################## Manage Frame ###############################################
                Manage_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                Manage_Frame.place(x = (20/1360)*main_width,y = (100/768)*main_heigth,width = (450/1360)*main_width,height = (595/768)*main_heigth)

                m_title = Label(Manage_Frame,text = "Manage Teachers",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/768)*main_heigth),'bold'))
                m_title.grid(row = 0, columnspan = 2,pady =(8/768)*main_heigth,padx = (8/1360)*main_width)


                ######################### Name ########################################################
                lbl_name = Label(Manage_Frame,text = "Name" ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_name.grid(row = 2,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_name = Entry(Manage_Frame,textvariable = Name,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/768)*main_heigth),bg = 'skyblue' , relief = GROOVE)
                txt_name.grid(row = 2,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Father's Name ###############################################
                lbl_fname = Label(Manage_Frame,text = "Father's name",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_fname.grid(row = 3,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_fname = Entry(Manage_Frame,textvariable = Fathersname ,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd =round((5/768)*main_heigth),bg='skyblue' , relief = GROOVE)
                txt_fname.grid(row = 3,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Mothers name #############################################################
                lbl_mother = Label(Manage_Frame,text = "Mother's Name.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_mother.grid(row = 4,column = 0,pady = (8/1360)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_sssmid = Entry(Manage_Frame,textvariable = Mothers_Name ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width),bg ='skyblue', relief = GROOVE)
                txt_sssmid.grid(row = 4,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ####################### DOB #################################################################
                lbl_dob = Label(Manage_Frame,text = "Date of Birth",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_dob.grid(row = 5,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_dob = Entry(Manage_Frame,textvariable = DOB,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd = round((5/1360)*main_width),bg ='skyblue' , relief = GROOVE)
                txt_dob.grid(row = 5,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Scholar Id ##################################################
                lbl_scholar = Label(Manage_Frame,text = "Date of joining",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_scholar.grid(row = 6,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_pnumber = Entry(Manage_Frame,textvariable = scholar,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_pnumber.grid(row = 6,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ###################### class ##############################################################
                lbl_class = Label(Manage_Frame,text = "Subjects Teaching",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_class.grid(row = 7,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_class= Entry(Manage_Frame,textvariable = Class,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_class.grid(row = 7,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ##################### Account no. #########################################################
                lbl_acc = Label(Manage_Frame,text = "Class Name",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_acc.grid(row = 8,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_acc = Entry(Manage_Frame,textvariable = Accountno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_acc.grid(row = 8,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                #####################  Aadhar no. ##########################################################
                lbl_aadhar = Label(Manage_Frame,text = "Aadhar No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_aadhar.grid(row = 9,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_aadhar = Entry(Manage_Frame,textvariable =   Aadharno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_aadhar.grid(row = 9,column = 1,pady = round((8/768)*main_heigth),padx = round((18/1360)*main_width),sticky = W )

                ####################### SSSMID No #############################################################

                lbl_sssmid = Label(Manage_Frame,text = "Email Id",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_sssmid.grid(row = 10,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_sssmid = Entry(Manage_Frame,textvariable = SSSMID ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_sssmid.grid(row = 10,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################### Address. ###########################################################
                lbl_add = Label(Manage_Frame,text = "Address.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_add.grid(row = 11,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_add = Text(Manage_Frame,width  = round((37/1360)*main_width) ,height = round((2/768)*main_heigth),font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_add.grid(row = 11,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )



                ########################## Button Frame #################################################################
                btn_Frame = Frame(Manage_Frame,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                btn_Frame.place(x = (6/1360)*main_width ,y = (520/768)*main_heigth,width =round((420/1360)*main_width))

                Addbtn = Button(btn_Frame,text = 'Add',width=round((10/1360)*main_width),command = add_students,bg = 'Lightpink').grid(row=0,column = 0,padx = (15/1360)*main_width,pady = (10/768)*main_heigth)
                updatebtn = Button(btn_Frame,text = 'Update',width=round((10/1360)*main_width),command = update_data,bg = 'Lightpink').grid(row=0,column = 1,padx =(15/1360)*main_width,pady =(10/768)*main_heigth)
                deletebtn = Button(btn_Frame,text = 'Delete',width=round((10/1360)*main_width),command = delete_data,bg = 'Lightpink').grid(row=0,column = 2,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)
                cleartbtn = Button(btn_Frame,text = 'Clear',width=round((10/1360)*main_width),command = clear,bg = 'Lightpink').grid(row=0,column = 3,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

                ########################## Detail Frame ###############################################        
                Detail_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                Detail_Frame.place(x = round((500/1360)*main_width),y = round((100/768)*main_heigth),width = round((765/1360)*main_width),height = round((590/768)*main_heigth))


                lbl_serch = Label(Detail_Frame,text = "Search By",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((14/1360)*main_width),'bold'))
                lbl_serch.grid(row = 0,column = 0,pady = round((10/768)*main_heigth),padx = round((20/1360)*main_width),sticky = W )


                combo_serch = ttk.Combobox(Detail_Frame,textvariable = search_by,width = round((10/1360)*main_width),font = ('time new roman',round((13/1360)*main_width),'bold'),state = 'readonly')
                combo_serch['values'] = ['Name','Address']
                combo_serch.grid(row=0,column = 1 , padx = (20/1360)*main_width ,pady = (10/768)*main_heigth)

                txt_serch = Entry(Detail_Frame,textvariable = search_txt,font = ('time now roman',round((14/1360)*main_width),'bold'),bd = (5/1360)*main_width ,bg  = 'skyblue', relief = GROOVE)
                txt_serch.grid(row = 0,column = 2,pady = (10/1360)*main_heigth,padx = (20/1360)*main_width,sticky = W )


                serchbtn = Button(Detail_Frame,text = 'Search',width=round((10/1360)*main_width), pady = (5/768)*main_heigth,command = search_data,bg = 'Lightpink').grid(row=0,column = 3,padx =10,pady = 10)
                showalltbtn = Button(Detail_Frame,text = 'Show All',width=round((10/1360)*main_width),command =fetch_data,bg = 'Lightpink').grid(row=0,column = 4,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

                def next_w(event):
                    event.widget.tk_focusNext().focus()
                    return 'break'
                root1.bind_class('Entry','<Down>',next_w)
                def next_w(event):
                    event.widget.tk_focusPrev().focus()
                    return 'break'
                root1.bind_class('Entry','<Up>',next_w)
                def next_w(event):
                    event.widget.tk_focusNext().focus()
                    return 'break'
                root1.bind_class('Button','<Right>',next_w)
                
                
                ################################## Table-Frame #############################################################
                Table_Frame = Frame(Detail_Frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
                Table_Frame.place(x = (10/1360)*main_width,y = (70/768)*main_heigth,width = (740/1360)*main_width,height = (500/768)*main_heigth)
                scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
                scroll_y = Scrollbar(Table_Frame,orient = VERTICAL)

                student_table = ttk.Treeview(Table_Frame,columns = ('Name',"Father's Name","Mother's Name",'D.O.B','Scholar_ID','Class_ID','Account No.','Aadhar No.','SSSMID2','Address'),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
                scroll_x.pack(side = BOTTOM,fill = X)
                scroll_y.pack(side = RIGHT , fill =Y)
                scroll_x.config(command = student_table.xview)
                scroll_y.config(command = student_table.yview)

                student_table.heading('Name',text = 'Name' )
                student_table.heading("Father's Name",text = "Father's Name" )
                student_table.heading("Mother's Name",text = "Mother's Name" )
                student_table.heading('D.O.B',text = 'D.O.B' )
                student_table.heading('Scholar_ID',text = 'Date of joining')
                student_table.heading('Class_ID',text = 'Subjects Teaching' )
                student_table.heading('Account No.',text = 'Classes Teaching.' )
                student_table.heading('Aadhar No.',text = 'Aadhar No.' )
                student_table.heading('SSSMID2',text = 'Email ID' )
                student_table.heading('Address',text = 'Address' )
                student_table['show'] = 'headings'
                student_table.column('Name',width = 130)
                student_table.column("Father's Name",width =130 )
                student_table.column("Mother's Name",width = 130)
                student_table.column('D.O.B',width = 75)
                student_table.column('Scholar_ID',width = 130)
                student_table.column('Class_ID',width = 150)
                student_table.column('Account No.',width = 180)
                student_table.column('Aadhar No.',width = 180)
                student_table.column('SSSMID2',width = 180)
                student_table.column('Address',width = 200)
                student_table.pack(fill = BOTH,expand = 1)
                student_table.bind("<ButtonRelease-1>",get_cursor)
                style = ttk.Style()
                style.configure('Treeview.Heading',font = ('time now roman',round((12/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                style.configure('Treeview',font = ('time now roman',round((10/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                fetch_data()

                root1.mainloop()  

            def dis(event):
                rootm.destroy()
            rootm.bind('<Escape>',dis)
            def backup():
                
               messagebox.showinfo('Sorry','This fuction is not for you')
            ################################# main fees management ########################################
            def feesm():
                messagebox.showinfo('sorry','Not for you')
            def stud():

                root1 = Toplevel(rootm)

                root1.title('Student Management system')
                photo = PhotoImage(file = 'school.png')
                root1.iconphoto(FALSE,photo)

                root1.config(bg = 'skyblue')
                root1.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth(),rootm.winfo_screenheight()))
                root1.grab_set()
                def main():
                    root1.destroy()
                def main1(event):
                    root1.destroy()
                root1.bind('<End>',main1)

                title = Label(root1,text = 'Students Management System',font = ('time now roman',round((35/1360)*main_width),'bold'),bg = 'lightpink',fg = 'Black',bd = round((10/1360)*main_width),relief = 'sunken')
                title.pack(side = TOP,fill = X)
                butn = Button(root1,text = 'MAIN MENU',width=round((10/1360)*main_width),font = ('time now roman',round((15/1360)*main_width),'bold'),bg = 'skyblue',fg = 'Black',command = main)
                butn.place(x = round((1200/1360)*main_width),y = round((15/768)*main_heigth),width = round((120/1360)*main_width),height = round((35/768)*main_heigth))


            ######### All Variables #########################################################################################################################################################
                Name = StringVar()
                Fathersname = StringVar()
                Mothers_Name = StringVar()
                DOB = StringVar()
                Phonenumber = StringVar()
                Class = StringVar()
                Accountno = StringVar()
                Aadharno = StringVar()
                SSSMID = StringVar() 
                Address = StringVar()
                search_by = StringVar()
                search_txt = StringVar()
                scholar = StringVar()
            ################################### All Functions #######################################################################################################################################################################################################################################################################
            ######################### Add students fuction #####################################################################################################################################################################################################
                def add_students():
                        if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                                messagebox.showerror("Error",'All Fields are Required!!')
                        else:
                                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                                cur = con.cursor()
                                cur.execute('insert into students (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                Name.get(),
                                Fathersname.get(),
                                Mothers_Name.get(),
                                DOB.get(),
                                scholar.get(),
                                Class.get(),
                                Accountno.get(),
                                Aadharno.get(),
                                SSSMID.get(),
                                txt_add.get('1.0',END)))
                                con.commit()
                                fetch_data()
                                clear()
                                con.close()
                                messagebox.showinfo("Success","Message has been inserted")
                def fetch_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute('select * from students')
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                                student_table.delete(* student_table.get_children())
                                for row in rows:
                                        student_table.insert('',END,values = row)
                                con.commit()
                        con.close()
                def clear():
                        Name.set('')
                        Fathersname.set('')
                        Mothers_Name.set('')
                        DOB.set('')
                        scholar.set('')
                        Class.set('')
                        Accountno.set('')
                        Aadharno.set('')
                        SSSMID.set('') 
                        txt_add.delete('1.0',END)

                ########## get_cursor ##################################################################
                def get_cursor(event):
                        cursor_row = student_table.focus()
                        contents = student_table.item(cursor_row)
                        row = contents['values']
                        print(row)
                        Name.set(row[0])
                        Fathersname.set(row[1])
                        Mothers_Name.set(row[2])
                        DOB.set(row[3])
                        scholar.set(row[4])
                        Class.set(row[5])
                        Accountno.set(row[6])
                        Aadharno.set(row[7])
                        SSSMID.set(row[8])
                        txt_add.delete('1.0',END) 
                        txt_add.insert(END,row[9])

                ########### update_data ###############################################################
                def update_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor()
                        cur.execute('update  students set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                        Name.get(),
                        Fathersname.get(),
                        Mothers_Name.get(),
                        DOB.get(),
                        Class.get(),
                        Accountno.get(),
                        Aadharno.get(),
                        SSSMID.get(),
                        txt_add.get('1.0',END),
                        scholar.get()))
                        con.commit()
                        fetch_data()
                        clear()
                        con.close()
    ############################ Delete_data #########################################################
                def delete_data():
                     messagebox.showinfo('sorry','You cannot delete students')

                        ############### search_data #########################################################
                def search_data():
                        if search_by.get() == '' or  search_txt.get() == '':
                                messagebox.showerror("Error",'All Fields are Required!!')
                        else:        
                                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                                cur = con.cursor() 
                                cur.execute("select * from students where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                                rows = cur.fetchall()
                                if len(rows)!= 0:
                                        student_table.delete(*student_table.get_children())
                                        for row in rows:
                                                student_table.insert('',END,values = row)
                                        con.commit()
                                con.close()


                ############## Add students fuction ######################################################
                def add_students():
                        if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                                messagebox.showerror("Error",'All Fields are Required!!')
                        else:
                                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                                cur = con.cursor()
                                cur.execute('insert into students (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                Name.get(),
                                Fathersname.get(),
                                Mothers_Name.get(),
                                DOB.get(),
                                scholar.get(),
                                Class.get(),
                                Accountno.get(),
                                Aadharno.get(),
                                SSSMID.get(),
                                txt_add.get('1.0',END)))
                                con.commit()
                                fetch_data()
                                clear()
                                con.close()
                                messagebox.showinfo("Success","Message has been inserted")
                def saad_stud(event):
                    add_students()
                root1.bind('<Control-s>',saad_stud)
                def fetch_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor() 
                        cur.execute('select * from students')
                        rows = cur.fetchall()
                        if len(rows)!= 0:
                                student_table.delete(* student_table.get_children())
                                for row in rows:
                                        student_table.insert('',END,values = row)
                                con.commit()
                        con.close()

                def clear():
                        Name.set('')
                        Fathersname.set('')
                        Mothers_Name.set('')
                        DOB.set('')
                        scholar.set('')
                        Class.set('')
                        Accountno.set('')
                        Aadharno.set('')
                        SSSMID.set('') 
                        txt_add.delete('1.0',END)
                def clr_stud(event):
                    clear()
                root1.bind('<Control-c>',clr_stud)
    ############ get_cursor ##################################################################
                def get_cursor(event):
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                    Name.set(row[0])
                    Fathersname.set(row[1])
                    Mothers_Name.set(row[2])
                    DOB.set(row[3])
                    scholar.set(row[4])
                    Class.set(row[5])
                    Accountno.set(row[6])
                    Aadharno.set(row[7])
                    SSSMID.set(row[8])
                    txt_add.delete('1.0',END) 
                    txt_add.insert(END,row[9])
                root1.bind('<Return>',get_cursor)

                ########### update_data ###############################################################
                def update_data():
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor()
                        cur.execute('update  students set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                        Name.get(),
                        Fathersname.get(),
                        Mothers_Name.get(),
                        DOB.get(),
                        Class.get(),
                        Accountno.get(),
                        Aadharno.get(),
                        SSSMID.get(),
                        txt_add.get('1.0',END),
                        scholar.get()))
                        con.commit()
                        fetch_data()
                        clear()
                        con.close()
                def upd_stud(event):
                    update_data()
                root1.bind('<Control-u>',upd_stud)

                ############## Delete_data #########################################################
                def delete_data():
                     messagebox.showinfo('sorry','You cannot delete students')
                def del_stud(event):
                    delete_data()
                root1.bind('<Delete>',del_stud)

                        ############### search_data #########################################################
                def search_data():
                        if search_by.get() == '' or  search_txt.get() == '':
                                messagebox.showerror("Error",'All Fields are Required!!')
                        else:        
                                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                                cur = con.cursor() 
                                cur.execute("select * from students where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                                rows = cur.fetchall()
                                if len(rows)!= 0:
                                        student_table.delete(*student_table.get_children())
                                        for row in rows:
                                                student_table.insert('',END,values = row)
                                        con.commit()
                                con.close()

                ########################## Manage Frame ###############################################
                Manage_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                Manage_Frame.place(x = (20/1360)*main_width,y = (100/768)*main_heigth,width = (450/1360)*main_width,height = (595/768)*main_heigth)

                m_title = Label(Manage_Frame,text = "Manage Students",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/768)*main_heigth),'bold'))
                m_title.grid(row = 0, columnspan = 2,pady =(8/768)*main_heigth,padx = (8/1360)*main_width)


                ######################### Name ########################################################
                lbl_name = Label(Manage_Frame,text = "Name" ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_name.grid(row = 2,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_name = Entry(Manage_Frame,textvariable = Name,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/768)*main_heigth),bg = 'skyblue' , relief = GROOVE)
                txt_name.grid(row = 2,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Father's Name ###############################################
                lbl_fname = Label(Manage_Frame,text = "Father's name",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_fname.grid(row = 3,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_fname = Entry(Manage_Frame,textvariable = Fathersname ,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd =round((5/768)*main_heigth),bg='skyblue' , relief = GROOVE)
                txt_fname.grid(row = 3,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Mothers name #############################################################
                lbl_mother = Label(Manage_Frame,text = "Mother's Name.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_mother.grid(row = 4,column = 0,pady = (8/1360)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_sssmid = Entry(Manage_Frame,textvariable = Mothers_Name ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width),bg ='skyblue', relief = GROOVE)
                txt_sssmid.grid(row = 4,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ####################### DOB #################################################################
                lbl_dob = Label(Manage_Frame,text = "Date of Birth",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
                lbl_dob.grid(row = 5,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_dob = Entry(Manage_Frame,textvariable = DOB,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd = round((5/1360)*main_width),bg ='skyblue' , relief = GROOVE)
                txt_dob.grid(row = 5,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################## Scholar Id ##################################################
                lbl_scholar = Label(Manage_Frame,text = "Scholar ID.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_scholar.grid(row = 6,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_pnumber = Entry(Manage_Frame,textvariable = scholar,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_pnumber.grid(row = 6,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ###################### class ##############################################################
                lbl_class = Label(Manage_Frame,text = "Class ID",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_class.grid(row = 7,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_class= Entry(Manage_Frame,textvariable = Class,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_class.grid(row = 7,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ##################### Account no. #########################################################
                lbl_acc = Label(Manage_Frame,text = "Account No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_acc.grid(row = 8,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_acc = Entry(Manage_Frame,textvariable = Accountno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_acc.grid(row = 8,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                #####################  Aadhar no. ##########################################################
                lbl_aadhar = Label(Manage_Frame,text = "Aadhar No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_aadhar.grid(row = 9,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_aadhar = Entry(Manage_Frame,textvariable =   Aadharno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_aadhar.grid(row = 9,column = 1,pady = round((8/768)*main_heigth),padx = round((18/1360)*main_width),sticky = W )

                ####################### SSSMID No #############################################################

                lbl_sssmid = Label(Manage_Frame,text = "SSSMID No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_sssmid.grid(row = 10,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_sssmid = Entry(Manage_Frame,textvariable = SSSMID ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_sssmid.grid(row = 10,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                ######################### Address. ###########################################################
                lbl_add = Label(Manage_Frame,text = "Address.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
                lbl_add.grid(row = 11,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

                txt_add = Text(Manage_Frame,width  = round((37/1360)*main_width) ,height = round((2/768)*main_heigth),font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
                txt_add.grid(row = 11,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )



                ########################## Button Frame #################################################################
                btn_Frame = Frame(Manage_Frame,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                btn_Frame.place(x = (6/1360)*main_width ,y = (520/768)*main_heigth,width =round((420/1360)*main_width))

                Addbtn = Button(btn_Frame,text = 'Add',width=round((10/1360)*main_width),command = add_students,bg = 'Lightpink').grid(row=0,column = 0,padx = (15/1360)*main_width,pady = (10/768)*main_heigth)
                updatebtn = Button(btn_Frame,text = 'Update',width=round((10/1360)*main_width),command = update_data,bg = 'Lightpink').grid(row=0,column = 1,padx =(15/1360)*main_width,pady =(10/768)*main_heigth)
                deletebtn = Button(btn_Frame,text = 'Delete',width=round((10/1360)*main_width),command = delete_data,bg = 'Lightpink').grid(row=0,column = 2,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)
                cleartbtn = Button(btn_Frame,text = 'Clear',width=round((10/1360)*main_width),command = clear,bg = 'Lightpink').grid(row=0,column = 3,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

                ########################## Detail Frame ###############################################        
                Detail_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
                Detail_Frame.place(x = round((500/1360)*main_width),y = round((100/768)*main_heigth),width = round((765/1360)*main_width),height = round((590/768)*main_heigth))


                lbl_serch = Label(Detail_Frame,text = "Search By",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((14/1360)*main_width),'bold'))
                lbl_serch.grid(row = 0,column = 0,pady = round((10/768)*main_heigth),padx = round((20/1360)*main_width),sticky = W )


                combo_serch = ttk.Combobox(Detail_Frame,textvariable = search_by,width = round((10/1360)*main_width),font = ('time new roman',round((13/1360)*main_width),'bold'),state = 'readonly')
                combo_serch['values'] = ['Name','Address','Accountno','SSSMID','Class','Aadharno','Scholar_id']
                combo_serch.grid(row=0,column = 1 , padx = (20/1360)*main_width ,pady = (10/768)*main_heigth)

                txt_serch = Entry(Detail_Frame,textvariable = search_txt,font = ('time now roman',round((14/1360)*main_width),'bold'),bd = (5/1360)*main_width ,bg  = 'skyblue', relief = GROOVE)
                txt_serch.grid(row = 0,column = 2,pady = (10/1360)*main_heigth,padx = (20/1360)*main_width,sticky = W )


                serchbtn = Button(Detail_Frame,text = 'Search',width=round((10/1360)*main_width), pady = (5/768)*main_heigth,command = search_data,bg = 'Lightpink').grid(row=0,column = 3,padx =10,pady = 10)
                showalltbtn = Button(Detail_Frame,text = 'Show All',width=round((10/1360)*main_width),command =fetch_data,bg = 'Lightpink').grid(row=0,column = 4,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

                def next_w(event):
                    event.widget.tk_focusNext().focus()
                    return 'break'
                root1.bind_class('Entry','<Down>',next_w)
                def next_w(event):
                    event.widget.tk_focusPrev().focus()
                    return 'break'
                root1.bind_class('Entry','<Up>',next_w)
                def next_w(event):
                    event.widget.tk_focusNext().focus()
                    return 'break'
                root1.bind_class('Button','<Right>',next_w)
                
                
                ################################## Table-Frame #############################################################
                Table_Frame = Frame(Detail_Frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
                Table_Frame.place(x = (10/1360)*main_width,y = (70/768)*main_heigth,width = (740/1360)*main_width,height = (500/768)*main_heigth)
                scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
                scroll_y = Scrollbar(Table_Frame,orient = VERTICAL)

                student_table = ttk.Treeview(Table_Frame,columns = ('Name',"Father's Name","Mother's Name",'D.O.B','Scholar_ID','Class_ID','Account No.','Aadhar No.','SSSMID2','Address'),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
                scroll_x.pack(side = BOTTOM,fill = X)
                scroll_y.pack(side = RIGHT , fill =Y)
                scroll_x.config(command = student_table.xview)
                scroll_y.config(command = student_table.yview)

                student_table.heading('Name',text = 'Name' )
                student_table.heading("Father's Name",text = "Father's Name" )
                student_table.heading("Mother's Name",text = "Mother's Name" )
                student_table.heading('D.O.B',text = 'D.O.B' )
                student_table.heading('Scholar_ID',text = 'Scholar ID.')
                student_table.heading('Class_ID',text = 'Class_ID' )
                student_table.heading('Account No.',text = 'Account No.' )
                student_table.heading('Aadhar No.',text = 'Aadhar No.' )
                student_table.heading('SSSMID2',text = 'SSSMID' )
                student_table.heading('Address',text = 'Address' )
                student_table['show'] = 'headings'
                student_table.column('Name',width = 130)
                student_table.column("Father's Name",width =130 )
                student_table.column("Mother's Name",width = 130)
                student_table.column('D.O.B',width = 75)
                student_table.column('Scholar_ID',width = 70)
                student_table.column('Class_ID',width = 50)
                student_table.column('Account No.',width = 180)
                student_table.column('Aadhar No.',width = 180)
                student_table.column('SSSMID2',width = 180)
                student_table.column('Address',width = 200)
                student_table.pack(fill = BOTH,expand = 1)
                student_table.bind("<ButtonRelease-1>",get_cursor)
                style = ttk.Style()
                style.configure('Treeview.Heading',font = ('time now roman',round((12/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                style.configure('Treeview',font = ('time now roman',round((10/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
                fetch_data()

                root1.mainloop()  
            def addmi():
                messagebox.showwarning('Attention','you will get this fuction in next update')  
            def idg():
                messagebox.showwarning('Attention','you will get this fuction in next update') 
            def resl():
               messagebox.showinfo('sorry','This is only for superadmin')
                        
            imgm = ImageTk.PhotoImage(file = 'students.png')
            b2m = Button(f1m,text = 'Students',image = imgm,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = stud)
            b2m.grid(row = 1 , column = 1 , padx = (20/1360)*main_width,ipadx = (50/1360)*main_width)
            img2m = ImageTk.PhotoImage(file = 'formnew.png')
            b3m = Button(f1m,text = 'Staff-Details',image = img2m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = teacherstaff)
            b3m.grid(row = 1 , column = 5 , padx=(120/1360)*main_width , pady = (20/768)*main_heigth,ipadx = (50/1360)*main_width)
            img3m = ImageTk.PhotoImage(Image.open('time-and-date.png'))
            b3m = Button(f1m,text = 'Generate Result',image = img3m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = idg)
            b3m.grid(row = 1 , column = 7 , padx=(100/1360)*main_width , pady = (20/768)*main_heigth,ipadx = (50/1360)*main_width)
            img4m = ImageTk.PhotoImage(Image.open('fees.png'))
            b4m = Button(f1m,text = 'Fees Management',image = img4m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = feesm)
            b4m.grid(row = 5 , column = 1 , padx=(20/1360)*main_width,pady = (120/768)*main_heigth,ipadx = (50/1360)*main_width)
            img5m = ImageTk.PhotoImage(Image.open('Tc.png'))
            b5m = Button(f1m,text = 'Backup',image = img5m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = backup)
            b5m.grid(row = 5 , column = 5 , padx=(130/1360)*main_width,pady = (20/768)*main_heigth,ipadx = (40/1360)*main_width)
            img6m = ImageTk.PhotoImage(Image.open('result.png'))
            b6m = Button(f1m,text = 'Add New User',image = img6m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = resl)
            b6m.grid(row = 5 , column = 7 , padx=(130/1360)*main_width,pady = (20/768)*main_heigth,ipadx = (40/1360)*main_width)
            rootm.mainloop()
















        else:
            messagebox.showerror('Error','Usernot found in database')

      
    
    elif uname.get() == '' or passwrd.get() == '':
        tkmsg.showerror('Error',"All field are required!! ")
    elif uname.get() == 'developer' or passwrd.get() == '----':
        b = messagebox.askyesno('Permission','Do you want to install this software in this PC')
        if b == TRUE:
            c = messagebox.askyesno('Asking','Do you want to create Database in this PC')
            if  c == True:
                con =pymysql.connect(host = 'localhost',user = 'root',password = '')
                cur = con.cursor()
                cur.execute("CREATE DATABASE IF NOT EXISTS school")
                con.commit()
                con.close()
                messagebox.showinfo('Success','Database has been created successfully')
                d = messagebox.askyesno('Asking','Do you want to install First Table in this PC')
                if d == TRUE:
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute("CREATE TABLE IF NOT EXISTS students(Name VARCHAR(100),Fathersname VARCHAR(100), Mothers_Name VARCHAR(100),DOB VARCHAR(20),scholar_id VARCHAR(15),Class_id VARCHAR(10),Accountno VARCHAR(20),Aadharno VARCHAR(20),SSSMID VARCHAR(25),Address VARCHAR(150),Annual_Fees INT(10),Deposit_1 INT(8),Deposit_1_Date VARCHAR(12),Deposit_2 INT(8),Deposit_2_Date VARCHAR(12),Deposit_3 INT(8),Deposit_3_Date VARCHAR(12),Due_Fees INT(10),Phone_number VARCHAR(12))")
                    cur.execute("CREATE TABLE IF NOT EXISTS staff(Name VARCHAR(100),Fathersname VARCHAR(100), Mothers_Name VARCHAR(100),DOB VARCHAR(20),scholar_id VARCHAR(15),Class_id VARCHAR(10),Accountno VARCHAR(20),Aadharno VARCHAR(20),SSSMID VARCHAR(25),Address VARCHAR(150),Annual_Fees INT(10),Deposit_1 INT(8),Deposit_1_Date VARCHAR(12),Deposit_2 INT(8),Deposit_2_Date VARCHAR(12),Deposit_3 INT(8),Deposit_3_Date VARCHAR(12),Due_Fees INT(10),Phone_number VARCHAR(12))")
                    cur.execute("CREATE TABLE IF NOT EXISTS teacher(username VARCHAR(100),password VARCHAR(20))")
                    cur.execute("CREATE TABLE IF NOT EXISTS operator(username VARCHAR(100),password VARCHAR(20))")
                    con.commit()
                    con.close()
                    messagebox.showinfo('Thankyou','Table has been created successfully')
                e = messagebox.askyesno('Asking','Do you want to install Second Table in this PC')
                if e == True:
                        con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                        cur = con.cursor()
                        cur.execute("CREATE TABLE IF NOT EXISTS students_backup(Name VARCHAR(100),Fathersname VARCHAR(100), Mothers_Name VARCHAR(100),DOB VARCHAR(20),scholar_id VARCHAR(15),Class_id VARCHAR(10),Accountno VARCHAR(20),Aadharno VARCHAR(20),SSSMID VARCHAR(25),Address VARCHAR(150))")
                        con.commit()
                        con.close()
                        messagebox.showinfo('Thankyou','Table has been created successfully')

                else:
                    messagebox.showinfo('ok','ok')

            else:
                messagebox.showinfo('Ok','Have a nice day')
        uname.set('')  
        passwrd.set('')
            

        
        
    elif uname.get() == 'admin' and passwrd.get() == '....':
        root.destroy()
        rootm = Tk()
        photo = PhotoImage(file = 'school.png')
        rootm.iconphoto(FALSE,photo)
        rootm.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth()-10,rootm.winfo_screenheight()-10))
        rootm.title('School Management')
        rootm.config(bg = 'cornsilk')
        menu1 = Label(rootm,text = 'Advance School management',font = ('times new roman',round((30/1360)*main_width),'bold'), bg ='cornflowerblue',fg = 'Black',relief = 'solid')
        menu1.pack(side = TOP,fill = X)
        f1m = Frame(rootm,bd = (4/1360)*main_width,relief = RIDGE,bg = 'skyblue' )
        f1m.place(x = (25/1360)*main_width ,y = (80/1360)*main_width,width = (1310/1360)*main_width,height = (590/768)*main_heigth)
        print(f1m.winfo_screenwidth())
        recenttime =  time.strftime('%H:%M:%S')
        rect.append(recenttime)
        print(rect)
        statusbar = Label(rootm,text = 'On the way',bd = 1,relief = SUNKEN,anchor = W)
        statusbar.pack(side = BOTTOM , fill = X)
        def teacherstaff():
            
            root1 = Toplevel(rootm)

            root1.title('Teachers Management system')
            photo = PhotoImage(file = 'school.png')
            root1.iconphoto(FALSE,photo)

            root1.config(bg = 'skyblue')
            root1.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth(),rootm.winfo_screenheight()))
            root1.grab_set()
            def main():
                root1.destroy()
            def main1(event):
                root1.destroy()
            root1.bind('<End>',main1)

            title = Label(root1,text = 'Teachers Management System',font = ('time now roman',round((35/1360)*main_width),'bold'),bg = 'lightpink',fg = 'Black',bd = round((10/1360)*main_width),relief = 'sunken')
            title.pack(side = TOP,fill = X)
            butn = Button(root1,text = 'MAIN MENU',width=round((10/1360)*main_width),font = ('time now roman',round((15/1360)*main_width),'bold'),bg = 'skyblue',fg = 'Black',command = main)
            butn.place(x = round((1200/1360)*main_width),y = round((15/768)*main_heigth),width = round((120/1360)*main_width),height = round((35/768)*main_heigth))

        ######### All Variables #########################################################################################################################################################
            Name = StringVar() # name
            Fathersname = StringVar()#  Fathersname
            Mothers_Name = StringVar()# Mother_Name
            DOB = StringVar()        # DOB 
            Phonenumber = StringVar()  # phone number
            Class = StringVar()      # class # Subjectteaching
            Accountno = StringVar()  # Accountno # teachingclass
            Aadharno = StringVar()   # Aadharno   # Aadharno
            SSSMID = StringVar()     # SSSMID   # Emailid
            Address = StringVar()    # Address   # Address
            search_by = StringVar()  # search_by  
            search_txt = StringVar() # search_txt
            scholar = StringVar()    # scholar   # scholar
        ################################### All Functions #######################################################################################################################################################################################################################################################################
        ######################### Add students fuction #####################################################################################################################################################################################################
            def add_students():
                if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                    messagebox.showerror("Error",'All Fields are Required!!')
                else:
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('insert into staff (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    Name.get(),
                    Fathersname.get(),
                    Mothers_Name.get(),
                    DOB.get(),
                    scholar.get(),
                    Class.get(),
                    Accountno.get(),
                    Aadharno.get(),
                    SSSMID.get(),
                    txt_add.get('1.0',END)))
                    con.commit()
                    fetch_data()
                    clear()
                    con.close()
                    messagebox.showinfo("Success","Message has been inserted")
            def fetch_data():
                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                cur = con.cursor() 
                cur.execute('select * from staff')
                rows = cur.fetchall()
                if len(rows)!= 0:
                        student_table.delete(* student_table.get_children())
                        for row in rows:
                                student_table.insert('',END,values = row)
                        con.commit()
                con.close()
            def clear():
                Name.set('')
                Fathersname.set('')
                Mothers_Name.set('')
                DOB.set('')
                scholar.set('')
                Class.set('')
                Accountno.set('')
                Aadharno.set('')
                SSSMID.set('') 
                txt_add.delete('1.0',END)

            ########## get_cursor ##################################################################
            def get_cursor(event):
                cursor_row = student_table.focus()
                contents = student_table.item(cursor_row)
                row = contents['values']
                print(row)
                Name.set(row[0])
                Fathersname.set(row[1])
                Mothers_Name.set(row[2])
                DOB.set(row[3])
                scholar.set(row[4])
                Class.set(row[5])
                Accountno.set(row[6])
                Aadharno.set(row[7])
                SSSMID.set(row[8])
                txt_add.delete('1.0',END) 
                txt_add.insert(END,row[9])

            ########### update_data ###############################################################
            def update_data():
                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                cur = con.cursor()
                cur.execute('update  staff set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                Name.get(),
                Fathersname.get(),
                Mothers_Name.get(),
                DOB.get(),
                Class.get(),
                Accountno.get(),
                Aadharno.get(),
                SSSMID.get(),
                txt_add.get('1.0',END),
                scholar.get()))
                con.commit()
                fetch_data()
                clear()
                con.close()
############################ Delete_data #########################################################
            def delete_data():
                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                cur = con.cursor() 
                ask = messagebox.askyesno('Message','Are you Really Want to delete')
                if ask == True:
                        cur.execute('delete  from staff where  scholar_id = %s',scholar.get())
                        con.commit()
                        con.close()
                        fetch_data()
                        clear()

                    ############### search_data #########################################################
            def search_data():
                if search_by.get() == '' or  search_txt.get() == '':
                    messagebox.showerror("Error",'All Fields are Required!!')
                else:        
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute("select * from staff where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                        student_table.delete(*student_table.get_children())
                        for row in rows:
                            student_table.insert('',END,values = row)
                        con.commit()
                    con.close()


            ############## Add students fuction ######################################################
            def add_students():
                if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                    messagebox.showerror("Error",'All Fields are Required!!')
                else:
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('insert into staff (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    Name.get(),
                    Fathersname.get(),
                    Mothers_Name.get(),
                    DOB.get(),
                    scholar.get(),
                    Class.get(),
                    Accountno.get(),
                    Aadharno.get(),
                    SSSMID.get(),
                    txt_add.get('1.0',END)))
                    con.commit()
                    fetch_data()
                    clear()
                    con.close()
                    messagebox.showinfo("Success","Message has been inserted")
            def saad_stud(event):
                add_students()
            root1.bind('<Control-s>',saad_stud)
            def fetch_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute('select * from staff')
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                            student_table.delete(* student_table.get_children())
                            for row in rows:
                                    student_table.insert('',END,values = row)
                            con.commit()
                    con.close()

            def clear():
                    Name.set('')
                    Fathersname.set('')
                    Mothers_Name.set('')
                    DOB.set('')
                    scholar.set('')
                    Class.set('')
                    Accountno.set('')
                    Aadharno.set('')
                    SSSMID.set('') 
                    txt_add.delete('1.0',END)
            def clr_stud(event):
                clear()
            root1.bind('<Control-c>',clr_stud)
############ get_cursor ##################################################################
            def get_cursor(event):
                cursor_row = student_table.focus()
                contents = student_table.item(cursor_row)
                row = contents['values']
                Name.set(row[0])
                Fathersname.set(row[1])
                Mothers_Name.set(row[2])
                DOB.set(row[3])
                scholar.set(row[4])
                Class.set(row[5])
                Accountno.set(row[6])
                Aadharno.set(row[7])
                SSSMID.set(row[8])
                txt_add.delete('1.0',END) 
                txt_add.insert(END,row[9])
            root1.bind('<Return>',get_cursor)

            ########### update_data ###############################################################
            def update_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('update  staff set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                    Name.get(),
                    Fathersname.get(),
                    Mothers_Name.get(),
                    DOB.get(),
                    Class.get(),
                    Accountno.get(),
                    Aadharno.get(),
                    SSSMID.get(),
                    txt_add.get('1.0',END),
                    scholar.get()))
                    con.commit()
                    fetch_data()
                    clear()
                    con.close()
            def upd_stud(event):
                update_data()
            root1.bind('<Control-u>',upd_stud)

            ############## Delete_data #########################################################
            def delete_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    ask = messagebox.askyesno('Message','Are you Really Want to delete')
                    if ask == True:
                            cur.execute('delete  from staff where  Aadharno = %s',Aadharno.get())
                            con.commit()
                            con.close()
                            fetch_data()
                            clear()
            def del_stud(event):
                delete_data()
            root1.bind('<Delete>',del_stud)

                    ############### search_data #########################################################
            def search_data():
                    if search_by.get() == '' or  search_txt.get() == '':
                            messagebox.showerror("Error",'All Fields are Required!!')
                    else:        
                            con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                            cur = con.cursor() 
                            cur.execute("select * from staff where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                            rows = cur.fetchall()
                            if len(rows)!= 0:
                                    student_table.delete(*student_table.get_children())
                                    for row in rows:
                                            student_table.insert('',END,values = row)
                                    con.commit()
                            con.close()

            ########################## Manage Frame ###############################################
            Manage_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
            Manage_Frame.place(x = (20/1360)*main_width,y = (100/768)*main_heigth,width = (450/1360)*main_width,height = (595/768)*main_heigth)

            m_title = Label(Manage_Frame,text = "Manage Teachers",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/768)*main_heigth),'bold'))
            m_title.grid(row = 0, columnspan = 2,pady =(8/768)*main_heigth,padx = (8/1360)*main_width)


            ######################### Name ########################################################
            lbl_name = Label(Manage_Frame,text = "Name" ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
            lbl_name.grid(row = 2,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_name = Entry(Manage_Frame,textvariable = Name,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/768)*main_heigth),bg = 'skyblue' , relief = GROOVE)
            txt_name.grid(row = 2,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ######################## Father's Name ###############################################
            lbl_fname = Label(Manage_Frame,text = "Father's name",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
            lbl_fname.grid(row = 3,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_fname = Entry(Manage_Frame,textvariable = Fathersname ,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd =round((5/768)*main_heigth),bg='skyblue' , relief = GROOVE)
            txt_fname.grid(row = 3,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ######################## Mothers name #############################################################
            lbl_mother = Label(Manage_Frame,text = "Mother's Name.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
            lbl_mother.grid(row = 4,column = 0,pady = (8/1360)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_sssmid = Entry(Manage_Frame,textvariable = Mothers_Name ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width),bg ='skyblue', relief = GROOVE)
            txt_sssmid.grid(row = 4,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ####################### DOB #################################################################
            lbl_dob = Label(Manage_Frame,text = "Date of Birth",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
            lbl_dob.grid(row = 5,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_dob = Entry(Manage_Frame,textvariable = DOB,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd = round((5/1360)*main_width),bg ='skyblue' , relief = GROOVE)
            txt_dob.grid(row = 5,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ######################## Scholar Id ##################################################
            lbl_scholar = Label(Manage_Frame,text = "Date of joining",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_scholar.grid(row = 6,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_pnumber = Entry(Manage_Frame,textvariable = scholar,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_pnumber.grid(row = 6,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ###################### class ##############################################################
            lbl_class = Label(Manage_Frame,text = "Subjects Teaching",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_class.grid(row = 7,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_class= Entry(Manage_Frame,textvariable = Class,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_class.grid(row = 7,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ##################### Account no. #########################################################
            lbl_acc = Label(Manage_Frame,text = "Class Name",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_acc.grid(row = 8,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_acc = Entry(Manage_Frame,textvariable = Accountno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_acc.grid(row = 8,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            #####################  Aadhar no. ##########################################################
            lbl_aadhar = Label(Manage_Frame,text = "Aadhar No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_aadhar.grid(row = 9,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_aadhar = Entry(Manage_Frame,textvariable =   Aadharno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_aadhar.grid(row = 9,column = 1,pady = round((8/768)*main_heigth),padx = round((18/1360)*main_width),sticky = W )

            ####################### SSSMID No #############################################################

            lbl_sssmid = Label(Manage_Frame,text = "Email Id",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_sssmid.grid(row = 10,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_sssmid = Entry(Manage_Frame,textvariable = SSSMID ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_sssmid.grid(row = 10,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ######################### Address. ###########################################################
            lbl_add = Label(Manage_Frame,text = "Address.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_add.grid(row = 11,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_add = Text(Manage_Frame,width  = round((37/1360)*main_width) ,height = round((2/768)*main_heigth),font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_add.grid(row = 11,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )



            ########################## Button Frame #################################################################
            btn_Frame = Frame(Manage_Frame,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
            btn_Frame.place(x = (6/1360)*main_width ,y = (520/768)*main_heigth,width =round((420/1360)*main_width))

            Addbtn = Button(btn_Frame,text = 'Add',width=round((10/1360)*main_width),command = add_students,bg = 'Lightpink').grid(row=0,column = 0,padx = (15/1360)*main_width,pady = (10/768)*main_heigth)
            updatebtn = Button(btn_Frame,text = 'Update',width=round((10/1360)*main_width),command = update_data,bg = 'Lightpink').grid(row=0,column = 1,padx =(15/1360)*main_width,pady =(10/768)*main_heigth)
            deletebtn = Button(btn_Frame,text = 'Delete',width=round((10/1360)*main_width),command = delete_data,bg = 'Lightpink').grid(row=0,column = 2,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)
            cleartbtn = Button(btn_Frame,text = 'Clear',width=round((10/1360)*main_width),command = clear,bg = 'Lightpink').grid(row=0,column = 3,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

            ########################## Detail Frame ###############################################        
            Detail_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
            Detail_Frame.place(x = round((500/1360)*main_width),y = round((100/768)*main_heigth),width = round((765/1360)*main_width),height = round((590/768)*main_heigth))


            lbl_serch = Label(Detail_Frame,text = "Search By",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((14/1360)*main_width),'bold'))
            lbl_serch.grid(row = 0,column = 0,pady = round((10/768)*main_heigth),padx = round((20/1360)*main_width),sticky = W )


            combo_serch = ttk.Combobox(Detail_Frame,textvariable = search_by,width = round((10/1360)*main_width),font = ('time new roman',round((13/1360)*main_width),'bold'),state = 'readonly')
            combo_serch['values'] = ['Name','Address']
            combo_serch.grid(row=0,column = 1 , padx = (20/1360)*main_width ,pady = (10/768)*main_heigth)

            txt_serch = Entry(Detail_Frame,textvariable = search_txt,font = ('time now roman',round((14/1360)*main_width),'bold'),bd = (5/1360)*main_width ,bg  = 'skyblue', relief = GROOVE)
            txt_serch.grid(row = 0,column = 2,pady = (10/1360)*main_heigth,padx = (20/1360)*main_width,sticky = W )


            serchbtn = Button(Detail_Frame,text = 'Search',width=round((10/1360)*main_width), pady = (5/768)*main_heigth,command = search_data,bg = 'Lightpink').grid(row=0,column = 3,padx =10,pady = 10)
            showalltbtn = Button(Detail_Frame,text = 'Show All',width=round((10/1360)*main_width),command =fetch_data,bg = 'Lightpink').grid(row=0,column = 4,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

            def next_w(event):
                event.widget.tk_focusNext().focus()
                return 'break'
            root1.bind_class('Entry','<Down>',next_w)
            def next_w(event):
                event.widget.tk_focusPrev().focus()
                return 'break'
            root1.bind_class('Entry','<Up>',next_w)
            def next_w(event):
                event.widget.tk_focusNext().focus()
                return 'break'
            root1.bind_class('Button','<Right>',next_w)
            
            
            ################################## Table-Frame #############################################################
            Table_Frame = Frame(Detail_Frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
            Table_Frame.place(x = (10/1360)*main_width,y = (70/768)*main_heigth,width = (740/1360)*main_width,height = (500/768)*main_heigth)
            scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame,orient = VERTICAL)

            student_table = ttk.Treeview(Table_Frame,columns = ('Name',"Father's Name","Mother's Name",'D.O.B','Scholar_ID','Class_ID','Account No.','Aadhar No.','SSSMID2','Address'),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
            scroll_x.pack(side = BOTTOM,fill = X)
            scroll_y.pack(side = RIGHT , fill =Y)
            scroll_x.config(command = student_table.xview)
            scroll_y.config(command = student_table.yview)

            student_table.heading('Name',text = 'Name' )
            student_table.heading("Father's Name",text = "Father's Name" )
            student_table.heading("Mother's Name",text = "Mother's Name" )
            student_table.heading('D.O.B',text = 'D.O.B' )
            student_table.heading('Scholar_ID',text = 'Date of joining')
            student_table.heading('Class_ID',text = 'Subjects Teaching' )
            student_table.heading('Account No.',text = 'Classes Teaching.' )
            student_table.heading('Aadhar No.',text = 'Aadhar No.' )
            student_table.heading('SSSMID2',text = 'Email ID' )
            student_table.heading('Address',text = 'Address' )
            student_table['show'] = 'headings'
            student_table.column('Name',width = 130)
            student_table.column("Father's Name",width =130 )
            student_table.column("Mother's Name",width = 130)
            student_table.column('D.O.B',width = 75)
            student_table.column('Scholar_ID',width = 130)
            student_table.column('Class_ID',width = 150)
            student_table.column('Account No.',width = 180)
            student_table.column('Aadhar No.',width = 180)
            student_table.column('SSSMID2',width = 180)
            student_table.column('Address',width = 200)
            student_table.pack(fill = BOTH,expand = 1)
            student_table.bind("<ButtonRelease-1>",get_cursor)
            style = ttk.Style()
            style.configure('Treeview.Heading',font = ('time now roman',round((12/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
            style.configure('Treeview',font = ('time now roman',round((10/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
            fetch_data()

            root1.mainloop()  

        def dis(event):
            rootm.destroy()
        rootm.bind('<Escape>',dis)
        def backup():
            
            root = Toplevel()
    
            root.grab_set()
            root.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth(),rootm.winfo_screenheight()))
            photo = PhotoImage(file = 'school.png')
            root.iconphoto(FALSE,photo)
            def main():
                root.destroy()
            def main1(event):
                root.destroy()
            root.bind('<End>',main1)

            title = Label(root,text = 'Backup System',font = ('time now roman',round((37/1360)*main_width),'bold'),bg = 'lightpink',fg = 'Black',bd = round((10/1360)*main_width),relief = 'sunken')
            title.pack(side = TOP,fill = X)
            butn = Button(root,text = 'MAIN MENU',width=round((10/1360)*main_width),font = ('time now roman',round((15/1360)*main_width),'bold'),bg = 'skyblue',fg = 'Black',command = main)
            butn.place(x = (1200/1360)*main_width,y = (15/768)*main_heigth,width = (120/1360)*main_width,height =(43/768)*main_heigth)
            root.title('Backup system')
            root.config(bg = 'skyblue')
        
        ############################## All Variable ##########################################################################################################
            Name = StringVar()
            Fathersname = StringVar()
            Mothers_Name = StringVar()
            DOB = StringVar()
            Phonenumber = StringVar()
            Class = StringVar()
            Accountno = StringVar()
            Aadharno = StringVar()
            SSSMID = StringVar() 
            Address = StringVar()
            search_by = StringVar()
            search_txt = StringVar()
            scholar = StringVar()
            firstname = StringVar()
            lastname = StringVar()
            ##################### Time Frame ########################################################

            def tick():
                time_string = time.strftime('%H:%M:%S')
                date_string = time.strftime('%d/%m/%Y')
                clock_label.config(text = "Date:"+date_string+'\n'+'Time:'+ time_string)
                clock_label.after(100,tick)

            time_frame = Frame(root,bd  = round((8/1360)*main_width) ,relief = GROOVE,bg = 'skyblue')
            time_frame.place(x = (15/1360)*main_width,y = (90/768)*main_heigth,width = (250/1360)*main_width,height = (70/768)*main_heigth)

            clock_label = Label(time_frame,font = ('New Roman times',round((18/1360)*main_width), 'bold'),bg = 'skyblue')
            clock_label.pack()
            tick()

            def fetch_data():
                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                cur = con.cursor() 
                cur.execute('select * from students_backup')
                rows = cur.fetchall()
        
                if len(rows)!= 0:
                        student_table.delete(* student_table.get_children())
                        for row in rows:
                                student_table.insert('',END,values = row)
                        con.commit()
                con.close()

            def get_cursor(event):
                cursor_row = student_table.focus()
                contents = student_table.item(cursor_row)
                row = contents['values']
                Name.set(row[0])
                Fathersname.set(row[1])
                Mothers_Name.set(row[2])
                DOB.set(row[3])
                scholar.set(row[4])
                Class.set(row[5])
                Accountno.set(row[6])
                Aadharno.set(row[7])
                SSSMID.set(row[8])
            def add_students():
                cursor_row = student_table.focus()
                contents = student_table.item(cursor_row)
                row = contents['values']
                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                cur = con.cursor()
                cur.execute('insert into students (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9]))
                cur.execute('delete  from students_backup where  scholar_id = %s',row[4])
                con.commit()
                con.close()
                messagebox.showinfo("Success","Selected Data backuped successfully")
                fetch_data()
            def Permanentlyd():
                cursor_row = student_table.focus()
                contents = student_table.item(cursor_row)
                row = contents['values']
                messagebox.askyesno('Warning','Do you really wants to delete data permanently')
                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                cur = con.cursor()
                cur.execute('delete  from students_backup where  scholar_id = %s',row[4])
                messagebox.showinfo("Notification",'Your selected data is permanently Erased!')
                con.commit()
                con.close()
                fetch_data()

            def search_data():
                if search_by.get() == '' or  search_txt.get() == '':
                    messagebox.showerror("Error",'All Fields are Required!!')
                else:        
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute("select * from students_backup where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                        student_table.delete(*student_table.get_children())
                        for row in rows:
                                student_table.insert('',END,values = row)
                        con.commit()
                    con.close()

                
            ################### Title Frame ############################################################

            title_frame = Frame(root,bd  = round((8/1360)*main_width) ,relief = GROOVE,bg = 'skyblue')
            title_frame.place(x = (430/1360)*main_width , y = (90/768)*main_heigth, width = (800/1360)*main_width , height = (65/768)*main_heigth)
            

            slider_label = Label(title_frame,text = ss,font = ('New Roman times',round((24/1360)*main_width), 'bold'),bg = 'skyblue')
            slider_label.pack()

            def IntroLabelTick():
                global count,text
                if count >= len(ss):

                    count = -1
                    text = ''
                    slider_label.config(text = text)
                else:
                    text = text+ss[count]
                    slider_label.config(text = text)
                count += 1
                slider_label.after(300,IntroLabelTick)
            IntroLabelTick()
            
            ################### main Frame ##########################################################
            main_frame =  Frame(root,bd  = 8 ,relief = GROOVE,bg = 'skyblue')
            main_frame.place(x = (30/1360)*main_width,y = (163/768)*main_heigth,width = (1200/1360)*main_width,height = (535/768)*main_heigth)
            ################### Buttons ########################################
            btnframe = Frame(main_frame,bd  = (8/1360)*main_width ,relief = GROOVE,bg = 'skyblue')
            btnframe.place(x = (20/1360)*main_width,y = (450/768)*main_heigth,width = (1150/1360)*main_width,height = (60/768)*main_heigth)
            backupbtn = Button(btnframe,text = 'Backup Data',width=round((9/1360)*main_width),bg = 'Skyblue',font = ('time new roman',round((13/1360)*main_width),'bold'),activebackground = 'maroon3',command = add_students)
            backupbtn.place(x = (40/1360)*main_width,y = (12/1360)*main_width,width =(400/1360)*main_width,height = (30/768)*main_heigth)
            countbtn = Button(btnframe,text = 'Permanently Delete',width=round((9/1360)*main_width),bg = 'Skyblue',font = ('time new roman',round((13/1360)*main_width),'bold'),activebackground = 'maroon3',command = Permanentlyd)
            countbtn.place(x = (700/1360)*main_width,y = (12/1360)*main_width,width =(400/1360)*main_width,height = (30/768)*main_heigth)
            ########################## Search Frame ###################################################
            search_frame = Frame(main_frame,bd  = (8/1360)*main_width ,relief = GROOVE,bg = 'skyblue')
            search_frame.place(x = (20/1360)*main_width,y = (10/1360)*main_width,width = (1150/1360)*main_width,height = (73/768)*main_heigth)
            combo_serch = ttk.Combobox(search_frame,width = 10,font = ('time new roman',round((20/1360)*main_width),'bold'),state = 'readonly')
            combo_serch['values'] = ['Name','Address','Accountno','SSSMID','Class','Aadharno','Scholar_id']
            combo_serch.grid(row=0,column = 1 , padx = (20/1360)*main_width ,pady = (10/768)*main_heigth)

            txt_serch = Entry(search_frame,font = ('time now roman',round((20/1360)*main_width),'bold'),bd = round((5/1360)*main_width) , relief = GROOVE,bg = 'skyblue')
            txt_serch.grid(row = 0,column = 2,pady = (10/768)*main_heigth,padx = (130/1360)*main_width,sticky = W )


            serchbtn = Button(search_frame,text = 'Search',width=round((10/1360)*main_width), pady = (5/768)*main_heigth,bg = 'light pink',command = search_data).grid(row=0,column = 3,padx =8,pady = 10)
            showalltbtn = Button(search_frame,text = 'Show All',width=round((10/1360)*main_width),bg = 'light pink',command = fetch_data).grid(row=0,column = 4,padx =(8/1360)*main_width,pady = (10/768)*main_heigth)


            lbl_serch = Label(search_frame,text = "Search By",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((14/1360)*main_width),'bold'))
            lbl_serch.grid(row = 0,column = 0,pady = (10/768)*main_heigth,padx = (20/1360)*main_width,sticky = W )
            ########################## Table View #####################################################
            Table_Frame = Frame(main_frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
            Table_Frame.place(x = (10/1360)*main_width,y = (90/768)*main_heigth,width = (1150/1360)*main_width,height = (350/768)*main_heigth)
            scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame,orient = VERTICAL)

            student_table = ttk.Treeview(Table_Frame,columns = ('Name',"Father's Name","Mother's Name",'D.O.B','Scholar_ID','Class_ID','Account No.','Aadhar No.','SSSMID2','Address'),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
            scroll_x.pack(side = BOTTOM,fill = X)
            scroll_y.pack(side = RIGHT , fill =Y)
            scroll_x.config(command = student_table.xview)
            scroll_y.config(command = student_table.yview)
            student_table.bind("<ButtonRelease-1>",get_cursor)
            student_table.heading('Name',text = 'Name' )
            student_table.heading("Father's Name",text = "Father's Name" )
            student_table.heading("Mother's Name",text = "Mother's Name" )
            student_table.heading('D.O.B',text = 'D.O.B' )
            student_table.heading('Scholar_ID',text = 'Scholar ID.')
            student_table.heading('Class_ID',text = 'Class_ID' )
            student_table.heading('Account No.',text = 'Account No.' )
            student_table.heading('Aadhar No.',text = 'Aadhar No.' )
            student_table.heading('SSSMID2',text = 'SSSMID' )
            student_table.heading('Address',text = 'Address' )
            student_table['show'] = 'headings'
            student_table.column('Name',width = round((200/1360)*main_width))
            student_table.column("Father's Name",width =round((200/1360)*main_width))
            student_table.column('D.O.B',width = round((80/1360)*main_width))
            student_table.column('Scholar_ID',width = round((250/1360)*main_width))
            student_table.column('Class_ID',width = round((90/1360)*main_width))
            student_table.column('Account No.',width = round((260/1360)*main_width))
            student_table.column('Aadhar No.',width = round((260/1360)*main_width))
            student_table.column('SSSMID2',width = round((260/1360)*main_width))
            student_table.column('Address',width = round((300/1360)*main_width))
            student_table.pack(fill = BOTH,expand = 1)
            style = ttk.Style()
            style.configure('Treeview.Heading',font = ('time now roman',round((12/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
            style.configure('Treeview',font = ('time now roman',round((10/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
            fetch_data()
        
            root.mainloop()
        ################################# main fees management ########################################
        def feesm():
            root = Toplevel(rootm)
            root = root
            root.title('Fees Management system')
            photo = PhotoImage(file = 'school.png')
            root.iconphoto(FALSE,photo)
            root.config(bg = 'skyblue')
            root.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth(),rootm.winfo_screenheight()))
            root.grab_set()

            def main():
                root.destroy()
            def main1(event):
                root.destroy()
            root.bind('<End>',main1)
            title = Label(root,text = 'Fees Management System',font = ('time now roman',round((35/1360)*main_width),'bold'),bg = 'lightpink',fg = 'Black',bd = round((10/1360)*main_width),relief = 'sunken')
            title.pack(side = TOP,fill = X)
            butn = Button(root,text = 'MAIN MENU',width=round((10/1360)*main_width),font = ('time now roman',round((15/1360)*main_width),'bold'),bg = 'skyblue',fg = 'Black',command = main).place(x = round((1200/1360)*main_width),y = (15/768)*main_heigth ,width = (120/1360)*main_width,height = (40/768)*main_heigth)

            ########################## All Variables ######################################################
            Name = StringVar()
            Fathersname = StringVar()
            Phonenumber= StringVar()
            Class = StringVar()
            installment = StringVar()
            Deposit_1_Date = StringVar()
            Deposit_2_Date = StringVar()
            Deposit_3_Date = StringVar()
            search_by = StringVar()
            search_txt = StringVar()
            Fees_Deposit = IntVar()
            livedate = StringVar()
            Annual_Fees = IntVar()
            due_Fees = StringVar()


            ##################### Time Frame ########################################################

            def tick():
                time_string = time.strftime('%H:%M:%S')
                date_string = time.strftime('%d/%m/%Y')
                clock_label.config(text = "Date:"+date_string+'\n'+'Time:'+ time_string)
                clock_label.after(100,tick)

            time_frame = Frame(root,bd  = round((8/1360)*main_width) ,relief = GROOVE,bg = 'skyblue')
            time_frame.place(x = (15/1360)*main_width,y = (90/768)*main_heigth,width = (250/1360)*main_width,height = (70/768)*main_heigth)

            clock_label = Label(time_frame,font = ('New Roman times',round((18/1360)*main_width), 'bold'),bg = 'skyblue')
            clock_label.pack()
            tick()
            ####################################  Button Functions #########################################

            def fetch_data():
                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                cur = con.cursor() 
                cur.execute('select Name,Fathersname,Phone_number,Class_id,Annual_Fees,Deposit_1,Deposit_1_Date,Deposit_2,Deposit_2_Date,Deposit_3,Deposit_3_Date,Due_Fees from students')
                rows = cur.fetchall()
                if len(rows)!= 0:
                        student_table.delete(* student_table.get_children())
                        for row in rows:
                                student_table.insert('',END,values = row)
                        con.commit()
                con.close()
            def clear():
                Fees_Deposit.set('')
                Name.set('')
                Fathersname.set('')
                Phonenumber.set('')
                Class.set('')
                installment.set('')
                Fees_Deposit.set('')
                Annual_Fees.set('')
                due_Fees.set('')

            ################################# Get Cursor ###############################################

            def get_cursor(event):
                cursor_row = student_table.focus()
                contents = student_table.item(cursor_row)
                row = contents['values']
                print(row)
                
                Name.set(row[0])
                Fathersname.set(row[1])
                Phonenumber.set(row[2])
                Class.set(row[3])
                Annual_Fees.set(row[4])
                Due_Fees = int(row[4])-(int(row[5])+int(row[7])+int(row[9]))
                con = pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                cur = con.cursor()
                cur.execute('update  students set Due_Fees = %s where  Class_id = %s' ,(Due_Fees,Class.get()))
                con.commit()
                con.close()
                due_Fees.set(row[11])
                if installment.get() == 'Deposit.1':
                    Fees_Deposit.set(row[5])
                elif installment.get() == 'Deposit.2':
                    Fees_Deposit.set(row[7])
                elif installment.get() == 'Deposit.3':
                    Fees_Deposit.set(row[9])


            ############################## Update ##############################################################
            def update_data():
                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                cur = con.cursor()
                if installment.get() == 'Deposit.1':
                    livedate =  time.strftime('%d/%m/%Y')
                    cur.execute('update  students set Phone_number = %s,Deposit_1 = %s,Deposit_1_Date = %s , Annual_Fees = %s  where  Class_id = %s' ,(
                        Phonenumber.get(),
                        Fees_Deposit.get(),
                        livedate,
                        Annual_Fees.get(),
                        Class.get()))
                    messagebox.showwarning('update','Update Required')
                elif installment.get() == 'Deposit.2':
                    livedate =  time.strftime('%d/%m/%Y')
                    cur.execute('update  students set Phone_number = %s, Deposit_2 = %s,Deposit_2_Date = %s , Annual_Fees = %s  where  Class_id = %s' ,(
                        Phonenumber.get(),
                        Fees_Deposit.get(),
                        livedate,
                        Annual_Fees.get(),
                        Class.get()))
                    messagebox.showwarning('update','Update Required')
                elif installment.get() == 'Deposit.3':
                    livedate = time.strftime('%d/%m/%Y')
                    cur.execute('update  students set Phone_number = %s,Deposit_3 = %s,Deposit_3_Date = %s, Annual_Fees = %s where  Class_id = %s' ,(
                        Phonenumber.get(),
                        Fees_Deposit.get(),
                        livedate,
                        Annual_Fees.get(),
                        Class.get()))   
                    messagebox.showwarning('update','Update Required')
                elif Name.get() == '' and Fathersname.get() == '' and Phonenumber.get() == '' and Class == '' :
                    messagebox.showerror("Error",'Fileds are Required!')
                else:
                    cur.execute('update  students set Phone_number = %s, Annual_Fees = %s where  Class_id = %s' ,(
                        Phonenumber.get(),
                        Annual_Fees.get(),
                        Class.get()))
                    messagebox.showinfo('Updated','Selected Rows successfully updated!')
                con.commit()
                fetch_data()
                clear()
                con.close()

            ############### search_data #########################################################
            def search_data():
                if search_by.get() == '' or  search_txt.get() == '':
                    messagebox.showerror("Error",'All Fields are Required!!')
                elif search_by.get() == 'Less than Due Fees' :
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute("select  Name,Fathersname,Phone_number,Class_id,Annual_Fees,Deposit_1,Deposit_1_Date,Deposit_2,Deposit_2_Date,Deposit_3,Deposit_3_Date,Due_Fees  from students where Due_Fees < "+str(search_txt.get()))
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                        student_table.delete(* student_table.get_children())
                        for row in rows:
                                student_table.insert('',END,values = row)
                        con.commit()
                    con.close()
                elif search_by.get() == 'Greater than Due Fees' :
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute("select  Name,Fathersname,Phone_number,Class_id,Annual_Fees,Deposit_1,Deposit_1_Date,Deposit_2,Deposit_2_Date,Deposit_3,Deposit_3_Date,Due_Fees  from students where Due_Fees > "+str(search_txt.get()))
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                        student_table.delete(* student_table.get_children())
                        for row in rows:
                                student_table.insert('',END,values = row)
                        con.commit()
                    con.close()


                else:        
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute("select  Name,Fathersname,Phone_number,Class_id,Annual_Fees,Deposit_1,Deposit_1_Date,Deposit_2,Deposit_2_Date,Deposit_3,Deposit_3_Date,Due_Fees  from students where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                        student_table.delete(* student_table.get_children())
                        for row in rows:
                                student_table.insert('',END,values = row)
                        con.commit()
                    con.close()

            def exportstudent():
                ff = filedialog.asksaveasfilename()  
                gg = student_table.get_children()
                name,fathersname,phonenumber,class_id,deposit_1,deposit_1_Date,deposit_2,deposit_2_Date,deposit_3,deposit_3_Date,annual_Fees,due_fees = [],[],[],[],[],[],[],[],[],[],[],[]
                for i in gg:
                    content = student_table.item(i)
                    pp = content['values']
                    name.append(pp[0]),fathersname.append(pp[1]),phonenumber.append(pp[2]),class_id.append(pp[3]),deposit_1.append(pp[4]),deposit_1_Date.append(pp[5]),deposit_2.append(pp[6]),deposit_2_Date.append(pp[7]),deposit_3.append(pp[8]),deposit_3_Date.append(pp[9]),annual_Fees.append(pp[10]),due_fees.append(pp[11])
                dd = ['name','fathersname','phonenumber','class_id','deposit_1','deposit_1_Date','deposit_2','deposit_2_Date','deposit_3','deposit_3_Date','annual_Fees','due_fees']
                df = pd.DataFrame(list(zip(name,fathersname,phonenumber,class_id,deposit_1,deposit_1_Date,deposit_2,deposit_2_Date,deposit_3,deposit_3_Date,annual_Fees,due_fees)),columns =dd)
                paths = r'{}.csv'.format(ff)
                df.to_csv(paths,index=False)
                messagebox.showinfo('Notification','Students data is Saved {}'.format(paths))
            #################### Hover Effect ###################################
            def onButton1(e):
                updatebtn['bg'] ='light pink'
            def leaveButton1(e):
                updatebtn['bg'] = 'skyblue'



            def onButton2(event):
                cleartbtn['bg'] ='light pink'   
            def leaveButton2(event):
                cleartbtn['bg'] = 'skyblue'

            def onButton3(event):
                exportbtn['bg'] ='light pink'    
            def leaveButton3(event):
                exportbtn['bg'] ='skyblue'

            ################### Title Frame ############################################################

            title_frame = Frame(root,bd  = (8/1360)*main_width ,relief = GROOVE,bg = 'skyblue')
            title_frame.place(x = (430/1360)*main_width , y = (90/768)*main_heigth, width = (800/1360)*main_width , height = (65/768)*main_heigth)
            ss = 'Prime Motivation 2020-2021 Session'
            count = 0
            text = '' 

            slider_label = Label(title_frame,text = ss,font = ('New Roman times',round((23/1360)*main_width), 'bold'),bg = 'skyblue')
            slider_label.pack()

            def IntroLabelTick():
                global count,text
                if count >= len(ss):

                    count = -1
                    text = ''
                    slider_label.config(text = text)
                else:
                    text = text+ss[count]
                    slider_label.config(text = text)
                count += 1
                slider_label.after(300,IntroLabelTick)
            IntroLabelTick()

            ################# Manage Frame ##############################################################
            Manage_frame = Frame(root,bd  = (8/1360)*main_width ,relief = GROOVE,bg = 'skyblue')
            Manage_frame.place(x = (20/1360)*main_width , y = (180/768)*main_heigth, width = (450/1360)*main_width , height = (500/768)*main_heigth)

            ################## Name #################################################################
            lbl_name = Label(Manage_frame,text = "Name." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
            lbl_name.grid(row = 1,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
            txt_name = Entry(Manage_frame,textvariable = Name,font = ('time now roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
            txt_name.grid(row = 1,column = 1,pady = (8/1360)*main_heigth,padx = 18,sticky = W )

            ##################### Father's Name ###################################################
            lbl_fname = Label(Manage_frame,text = "Father's Name." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
            lbl_fname.grid(row = 2,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
            txt_fname = Entry(Manage_frame,textvariable = Fathersname,font = ('time now roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
            txt_fname.grid(row = 2,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )

            ##################### Phone Number ###################################################
            lbl_mname = Label(Manage_frame,text = "Phone Number." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
            lbl_mname.grid(row = 3,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
            txt_mname = Entry(Manage_frame,textvariable =Phonenumber, font = ('time now roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
            txt_mname.grid(row = 3,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )

            ##################### Class ID #########################################################
            lbl_classid = Label(Manage_frame,text = "Class ID." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
            lbl_classid.grid(row = 4,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
            txt_classid = Entry(Manage_frame,textvariable  = Class,font = ('time now roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
            txt_classid.grid(row = 4,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )

            ###################### Installment #######################################################
            lbl_install = Label(Manage_frame,text = "Installment No." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
            lbl_install.grid(row = 5,column = 0,pady =(8/768)*main_heigth,padx =(15/1360)*main_width,sticky = W )
            combo_install = ttk.Combobox(Manage_frame,textvariable  = installment,width = 10,font = ('time new roman',round((14/1360)*main_width),'bold'),state = 'readonly')
            combo_install['values'] = ['Deposit.1','Deposit.2','Deposit.3']
            combo_install.grid(row=5,column = 1 , padx = (20/1360)*main_width ,pady =(8/768)*main_heigth)

            ##################### Fees Deposit ###########################################################
            lbl_feesd = Label(Manage_frame,text = "Fees Deposit." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
            lbl_feesd.grid(row = 6,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
            txt_feesd = Entry(Manage_frame,textvariable  = Fees_Deposit,font = ('time now roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
            txt_feesd.grid(row = 6,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
            ##################### Annual Fees #########################################################
            lbl_annual = Label(Manage_frame,text = "Annual Fees." ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
            lbl_annual.grid(row = 7,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
            txt_annual = Entry(Manage_frame,textvariable  = Annual_Fees,font = ('time new roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
            txt_annual.grid(row = 7,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )

            #################### Due Fees ###########################################################
            lbl_feesdue = Label(Manage_frame,text = "Due Fees" ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/1360)*main_width),'bold'))
            lbl_feesdue.grid(row = 8,column = 0,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )
            lbl_feesdue = Entry(Manage_frame,textvariable  = due_Fees,font = ('time new roman',round((13/1360)*main_width),'bold'),bd  = 8 , relief = GROOVE,bg = 'skyblue')
            lbl_feesdue.grid(row = 8,column = 1,pady = (8/768)*main_heigth,padx = (15/1360)*main_width,sticky = W )

            ########################## Button Frame #################################################################
            btn_Frame = Frame(Manage_frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
            btn_Frame.place(x = (5/1360)*main_width ,y = (420/768)*main_heigth,width =(420/1360)*main_width)

            updatebtn = Button(btn_Frame,text = 'Update',width=9,bg = 'Skyblue',font = ('time new roman',round((13/1360)*main_width),'bold'),command =update_data,activebackground = 'maroon3')
            updatebtn.grid(row=0,column = 1,padx =(15/1360)*main_width,pady = (8/1360)*main_heigth)
            updatebtn.bind('<Enter>',onButton1)
            updatebtn.bind('<Leave>',leaveButton1)
            cleartbtn = Button(btn_Frame,text = 'Clear',width=round((9/1360)*main_width),bg = 'skyblue',font = ('time new roman',round((13/1360)*main_width),'bold'),command =clear,activebackground = 'Hotpink')
            cleartbtn.grid(row=0,column = 5,padx =(25/1360)*main_width,pady = (8/768)*main_heigth)
            cleartbtn.bind('<Enter>',onButton2)
            cleartbtn.bind('<Leave>',leaveButton2)
            exportbtn = Button(btn_Frame,text = 'Export',width = round((9/1360)*main_width),bg = 'skyblue',font =  ('time new roman',round((13/1360)*main_width),'bold'),command =exportstudent,activebackground = 'VioletRed2')
            exportbtn.grid(row=0,column = 8,padx =(15/1360)*main_width,pady = (8/768)*main_heigth)
            exportbtn.bind('<Enter>',onButton3)
            exportbtn.bind('<Leave>',leaveButton3)
            ################### Detail Frame ##########################################################
            detail_frame =  Frame(root,bd  = 8 ,relief = GROOVE,bg = 'skyblue')
            detail_frame.place(x = (500/1360)*main_width,y = (180/768)*main_heigth,width = (810/1360)*main_width,height = (500/768)*main_heigth)


            lbl_serch = Label(detail_frame,text = "Search By",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((14/1360)*main_width),'bold'))
            lbl_serch.grid(row = 0,column = 0,pady = 10,padx = 20,sticky = W )

            combo_serch = ttk.Combobox(detail_frame,textvariable = search_by,width = round((10/1360)*main_width),font = ('time new roman',round((13/1360)*main_width),'bold'),state = 'readonly')
            combo_serch['values'] = ['Name','Class_id','Fathers Name','Phone_number','Due_Fees','Less than Due Fees','Greater than Due Fees']
            combo_serch.grid(row=0,column = 1 , padx = (20/1360)*main_width ,pady = (10/768)*main_heigth)

            txt_serch = Entry(detail_frame,textvariable = search_txt,font = ('time now roman',round((13/1360)*main_width),'bold'),bd = 5 , relief = GROOVE,bg = 'skyblue')
            txt_serch.grid(row = 0,column = 2,pady = (10/768)*main_heigth,padx = (20/1360)*main_width,sticky = W )


            serchbtn = Button(detail_frame,text = 'Search',width=round((10/1360)*main_width), pady = (5/768)*main_heigth,bg = 'light pink',command = search_data).grid(row=0,column = 3,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)
            showalltbtn = Button(detail_frame,text = 'Show All',width=10,bg = 'light pink',command = fetch_data).grid(row=0,column = 4,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)
            def next_w(event):
                event.widget.tk_focusNext().focus()
                return 'break'
            txt_name.bind('<Down>',next_w)
            txt_fname.bind('<Down>',next_w)
            txt_mname.bind('<Down>',next_w)
            txt_classid.bind('<Down>',next_w)
            txt_feesd.bind('<Down>',next_w)
            txt_annual.bind('<Down>',next_w)
            def next_w(event):
                event.widget.tk_focusPrev().focus()
                return 'break'
            txt_feesd.bind('<Up>',next_w)
            txt_classid.bind('<Up>',next_w)
            txt_mname.bind('<Up>',next_w)
            txt_fname.bind('<Up>',next_w)
            txt_annual.bind('<Up>',next_w)
            txt_feesd.bind('<Up>',next_w)
        

            ################################## Table-Frame #############################################################
            Table_Frame = Frame(detail_frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
            Table_Frame.place(x = (10/1360)*main_width,y = (70/768)*main_heigth,width = (760/1360)*main_width,height = (400/768)*main_heigth)
            style = ttk.Style()
            style.configure('Treeview.Heading',font = ('time now roman',round((10/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
            style.configure('Treeview',font = ('time now roman',round((8/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')

            scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame,orient = VERTICAL)
            student_table = ttk.Treeview(Table_Frame,columns = ('Name',"Father's Name","Phone number",'Class ID','Annual Fees','Deposit.1','Deposit.1 Date','Deposit.2','Deposit.2 Date','Deposit.3','Deposit.3 Date','Due Fees'),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
            scroll_x.pack(side = BOTTOM,fill = X)
            scroll_y.pack(side = RIGHT , fill =Y)
            scroll_x.config(command =student_table.xview,bg = 'skyblue')
            scroll_y.config(command =student_table.yview,bg = 'skyblue')
            student_table.bind("<ButtonRelease-1>",get_cursor)
            student_table.heading('Name',text = 'Name' )
            student_table.heading("Father's Name",text = "Father's Name" )
            student_table.heading("Phone number",text = "Phone number" )
            student_table.heading('Class ID',text = 'Class ID' )
            student_table.heading('Annual Fees',text = 'Annual Fees')
            student_table.heading('Deposit.1',text = 'Deposit.1' )
            student_table.heading('Deposit.1 Date',text = 'Deposit.1 Date' )
            student_table.heading('Deposit.2',text = 'Deposit.2' )
            student_table.heading('Deposit.2 Date',text = 'Deposit.2 Date' )
            student_table.heading('Deposit.3',text = 'Deposit.3' )
            student_table.heading('Deposit.3 Date',text = 'Deposit.3 Date' )
            student_table.heading('Due Fees',text = 'Due Fees' )
            student_table.column('Name',width = round((140/1360)*main_width))
            student_table.column("Father's Name",width =round((140/1360)*main_width))
            student_table.column("Phone number",width = round((120/1360)*main_width))
            student_table.column('Class ID',width = round((70/1360)*main_width))
            student_table.column('Annual Fees',width = round((90/1360)*main_width))
            student_table.column('Deposit.1',width = round((90/1360)*main_width))
            student_table.column('Deposit.1 Date',width = round((100/1360)*main_width))
            student_table.column('Deposit.2',width = round((100/1360)*main_width))
            student_table.column('Deposit.2 Date',width = round((100/1360)*main_width))
            student_table.column('Deposit.3',width = round((90/1360)*main_width))
            student_table.column('Deposit.3 Date',width = round((100/1360)*main_width))
            student_table.column('Due Fees',width = round((90/1360)*main_width))
            student_table['show'] = 'headings'

            student_table.pack(fill = BOTH,expand = 1)
            fetch_data()
            root.mainloop()
        def stud():

            root1 = Toplevel(rootm)

            root1.title('Student Management system')
            photo = PhotoImage(file = 'school.png')
            root1.iconphoto(FALSE,photo)

            root1.config(bg = 'skyblue')
            root1.geometry("{0}x{1}+0+0".format(rootm.winfo_screenwidth(),rootm.winfo_screenheight()))
            root1.grab_set()
            def main():
                root1.destroy()
            def main1(event):
                root1.destroy()
            root1.bind('<End>',main1)

            title = Label(root1,text = 'Students Management System',font = ('time now roman',round((35/1360)*main_width),'bold'),bg = 'lightpink',fg = 'Black',bd = round((10/1360)*main_width),relief = 'sunken')
            title.pack(side = TOP,fill = X)
            butn = Button(root1,text = 'MAIN MENU',width=round((10/1360)*main_width),font = ('time now roman',round((15/1360)*main_width),'bold'),bg = 'skyblue',fg = 'Black',command = main)
            butn.place(x = round((1200/1360)*main_width),y = round((15/768)*main_heigth),width = round((120/1360)*main_width),height = round((35/768)*main_heigth))


        ######### All Variables #########################################################################################################################################################
            Name = StringVar()
            Fathersname = StringVar()
            Mothers_Name = StringVar()
            DOB = StringVar()
            Phonenumber = StringVar()
            Class = StringVar()
            Accountno = StringVar()
            Aadharno = StringVar()
            SSSMID = StringVar() 
            Address = StringVar()
            search_by = StringVar()
            search_txt = StringVar()
            scholar = StringVar()
        ################################### All Functions #######################################################################################################################################################################################################################################################################
        ######################### Add students fuction #####################################################################################################################################################################################################
            def add_students():
                    if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                            messagebox.showerror("Error",'All Fields are Required!!')
                    else:
                            con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                            cur = con.cursor()
                            cur.execute('insert into students (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                            Name.get(),
                            Fathersname.get(),
                            Mothers_Name.get(),
                            DOB.get(),
                            scholar.get(),
                            Class.get(),
                            Accountno.get(),
                            Aadharno.get(),
                            SSSMID.get(),
                            txt_add.get('1.0',END)))
                            con.commit()
                            fetch_data()
                            clear()
                            con.close()
                            messagebox.showinfo("Success","Message has been inserted")
            def fetch_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute('select * from students')
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                            student_table.delete(* student_table.get_children())
                            for row in rows:
                                    student_table.insert('',END,values = row)
                            con.commit()
                    con.close()
            def clear():
                    Name.set('')
                    Fathersname.set('')
                    Mothers_Name.set('')
                    DOB.set('')
                    scholar.set('')
                    Class.set('')
                    Accountno.set('')
                    Aadharno.set('')
                    SSSMID.set('') 
                    txt_add.delete('1.0',END)

            ########## get_cursor ##################################################################
            def get_cursor(event):
                    cursor_row = student_table.focus()
                    contents = student_table.item(cursor_row)
                    row = contents['values']
                    print(row)
                    Name.set(row[0])
                    Fathersname.set(row[1])
                    Mothers_Name.set(row[2])
                    DOB.set(row[3])
                    scholar.set(row[4])
                    Class.set(row[5])
                    Accountno.set(row[6])
                    Aadharno.set(row[7])
                    SSSMID.set(row[8])
                    txt_add.delete('1.0',END) 
                    txt_add.insert(END,row[9])

            ########### update_data ###############################################################
            def update_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('update  students set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                    Name.get(),
                    Fathersname.get(),
                    Mothers_Name.get(),
                    DOB.get(),
                    Class.get(),
                    Accountno.get(),
                    Aadharno.get(),
                    SSSMID.get(),
                    txt_add.get('1.0',END),
                    scholar.get()))
                    con.commit()
                    fetch_data()
                    clear()
                    con.close()
############################ Delete_data #########################################################
            def delete_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    ask = messagebox.askyesno('Message','Are you Really Want to delete')
                    if ask == True:
                            cur.execute('insert into students_backup (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                            Name.get(),
                            Fathersname.get(),
                            Mothers_Name.get(),
                            DOB.get(),
                            scholar.get(),
                            Class.get(),
                            Accountno.get(),
                            Aadharno.get(),
                            SSSMID.get(),
                            txt_add.get('1.0',END)))
                            cur.execute('delete  from students where  scholar_id = %s',scholar.get())
                            con.commit()
                            con.close()
                            fetch_data()
                            clear()

                    ############### search_data #########################################################
            def search_data():
                    if search_by.get() == '' or  search_txt.get() == '':
                            messagebox.showerror("Error",'All Fields are Required!!')
                    else:        
                            con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                            cur = con.cursor() 
                            cur.execute("select * from students where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                            rows = cur.fetchall()
                            if len(rows)!= 0:
                                    student_table.delete(*student_table.get_children())
                                    for row in rows:
                                            student_table.insert('',END,values = row)
                                    con.commit()
                            con.close()


            ############## Add students fuction ######################################################
            def add_students():
                    if Name.get() == '' or  Fathersname.get() == '' or DOB.get() == '' or scholar.get() == '' or Class.get() == '' or  Accountno.get() == '' or   Aadharno.get() == '' or SSSMID.get() == '' or txt_add.get('1.0',END) == '':
                            messagebox.showerror("Error",'All Fields are Required!!')
                    else:
                            con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                            cur = con.cursor()
                            cur.execute('insert into students (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                            Name.get(),
                            Fathersname.get(),
                            Mothers_Name.get(),
                            DOB.get(),
                            scholar.get(),
                            Class.get(),
                            Accountno.get(),
                            Aadharno.get(),
                            SSSMID.get(),
                            txt_add.get('1.0',END)))
                            con.commit()
                            fetch_data()
                            clear()
                            con.close()
                            messagebox.showinfo("Success","Message has been inserted")
            def saad_stud(event):
                add_students()
            root1.bind('<Control-s>',saad_stud)
            def fetch_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    cur.execute('select * from students')
                    rows = cur.fetchall()
                    if len(rows)!= 0:
                            student_table.delete(* student_table.get_children())
                            for row in rows:
                                    student_table.insert('',END,values = row)
                            con.commit()
                    con.close()

            def clear():
                    Name.set('')
                    Fathersname.set('')
                    Mothers_Name.set('')
                    DOB.set('')
                    scholar.set('')
                    Class.set('')
                    Accountno.set('')
                    Aadharno.set('')
                    SSSMID.set('') 
                    txt_add.delete('1.0',END)
            def clr_stud(event):
                clear()
            root1.bind('<Control-c>',clr_stud)
############ get_cursor ##################################################################
            def get_cursor(event):
                cursor_row = student_table.focus()
                contents = student_table.item(cursor_row)
                row = contents['values']
                Name.set(row[0])
                Fathersname.set(row[1])
                Mothers_Name.set(row[2])
                DOB.set(row[3])
                scholar.set(row[4])
                Class.set(row[5])
                Accountno.set(row[6])
                Aadharno.set(row[7])
                SSSMID.set(row[8])
                txt_add.delete('1.0',END) 
                txt_add.insert(END,row[9])
            root1.bind('<Return>',get_cursor)

            ########### update_data ###############################################################
            def update_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor()
                    cur.execute('update  students set Name = %s,Fathersname = %s,Mothers_Name = %s,DOB = %s , class_id = %s , Accountno = %s , Aadharno = %s,SSSMID = %s,Address = %s where  scholar_id = %s' ,(
                    Name.get(),
                    Fathersname.get(),
                    Mothers_Name.get(),
                    DOB.get(),
                    Class.get(),
                    Accountno.get(),
                    Aadharno.get(),
                    SSSMID.get(),
                    txt_add.get('1.0',END),
                    scholar.get()))
                    con.commit()
                    fetch_data()
                    clear()
                    con.close()
            def upd_stud(event):
                update_data()
            root1.bind('<Control-u>',upd_stud)

            ############## Delete_data #########################################################
            def delete_data():
                    con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                    cur = con.cursor() 
                    ask = messagebox.askyesno('Message','Are you Really Want to delete')
                    if ask == True:
                            cur.execute('insert into students_backup (Name,Fathersname,Mothers_Name,DOB,scholar_id,class_id,Accountno, Aadharno,SSSMID,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                            Name.get(),
                            Fathersname.get(),
                            Mothers_Name.get(),
                            DOB.get(),
                            scholar.get(),
                            Class.get(),
                            Accountno.get(),
                            Aadharno.get(),
                            SSSMID.get(),
                            txt_add.get('1.0',END)))
                            cur.execute('delete  from students where  scholar_id = %s',scholar.get())
                            con.commit()
                            con.close()
                            fetch_data()
                            clear()
            def del_stud(event):
                delete_data()
            root1.bind('<Delete>',del_stud)

                    ############### search_data #########################################################
            def search_data():
                    if search_by.get() == '' or  search_txt.get() == '':
                            messagebox.showerror("Error",'All Fields are Required!!')
                    else:        
                            con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                            cur = con.cursor() 
                            cur.execute("select * from students where "+str(search_by.get())+ " LIKE '%" +str(search_txt.get())+ "%'")
                            rows = cur.fetchall()
                            if len(rows)!= 0:
                                    student_table.delete(*student_table.get_children())
                                    for row in rows:
                                            student_table.insert('',END,values = row)
                                    con.commit()
                            con.close()

            ########################## Manage Frame ###############################################
            Manage_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
            Manage_Frame.place(x = (20/1360)*main_width,y = (100/768)*main_heigth,width = (450/1360)*main_width,height = (595/768)*main_heigth)

            m_title = Label(Manage_Frame,text = "Manage Students",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((15/768)*main_heigth),'bold'))
            m_title.grid(row = 0, columnspan = 2,pady =(8/768)*main_heigth,padx = (8/1360)*main_width)


            ######################### Name ########################################################
            lbl_name = Label(Manage_Frame,text = "Name" ,bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
            lbl_name.grid(row = 2,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_name = Entry(Manage_Frame,textvariable = Name,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/768)*main_heigth),bg = 'skyblue' , relief = GROOVE)
            txt_name.grid(row = 2,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ######################## Father's Name ###############################################
            lbl_fname = Label(Manage_Frame,text = "Father's name",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
            lbl_fname.grid(row = 3,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_fname = Entry(Manage_Frame,textvariable = Fathersname ,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd =round((5/768)*main_heigth),bg='skyblue' , relief = GROOVE)
            txt_fname.grid(row = 3,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ######################## Mothers name #############################################################
            lbl_mother = Label(Manage_Frame,text = "Mother's Name.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
            lbl_mother.grid(row = 4,column = 0,pady = (8/1360)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_sssmid = Entry(Manage_Frame,textvariable = Mothers_Name ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width),bg ='skyblue', relief = GROOVE)
            txt_sssmid.grid(row = 4,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ####################### DOB #################################################################
            lbl_dob = Label(Manage_Frame,text = "Date of Birth",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/768)*main_heigth),'bold'))
            lbl_dob.grid(row = 5,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_dob = Entry(Manage_Frame,textvariable = DOB,font = ('time now roman',round((10/768)*main_heigth),'bold'),bd = round((5/1360)*main_width),bg ='skyblue' , relief = GROOVE)
            txt_dob.grid(row = 5,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ######################## Scholar Id ##################################################
            lbl_scholar = Label(Manage_Frame,text = "Scholar ID.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_scholar.grid(row = 6,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_pnumber = Entry(Manage_Frame,textvariable = scholar,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_pnumber.grid(row = 6,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ###################### class ##############################################################
            lbl_class = Label(Manage_Frame,text = "Class ID",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_class.grid(row = 7,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_class= Entry(Manage_Frame,textvariable = Class,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_class.grid(row = 7,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ##################### Account no. #########################################################
            lbl_acc = Label(Manage_Frame,text = "Account No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_acc.grid(row = 8,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_acc = Entry(Manage_Frame,textvariable = Accountno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_acc.grid(row = 8,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            #####################  Aadhar no. ##########################################################
            lbl_aadhar = Label(Manage_Frame,text = "Aadhar No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_aadhar.grid(row = 9,column = 0,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_aadhar = Entry(Manage_Frame,textvariable =   Aadharno,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_aadhar.grid(row = 9,column = 1,pady = round((8/768)*main_heigth),padx = round((18/1360)*main_width),sticky = W )

            ####################### SSSMID No #############################################################

            lbl_sssmid = Label(Manage_Frame,text = "SSSMID No.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_sssmid.grid(row = 10,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_sssmid = Entry(Manage_Frame,textvariable = SSSMID ,font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_sssmid.grid(row = 10,column = 1,pady =(8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            ######################### Address. ###########################################################
            lbl_add = Label(Manage_Frame,text = "Address.",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((10/1360)*main_width),'bold'))
            lbl_add.grid(row = 11,column = 0,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )

            txt_add = Text(Manage_Frame,width  = round((37/1360)*main_width) ,height = round((2/768)*main_heigth),font = ('time now roman',round((10/1360)*main_width),'bold'),bd = round((5/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
            txt_add.grid(row = 11,column = 1,pady = (8/768)*main_heigth,padx = round((18/1360)*main_width),sticky = W )



            ########################## Button Frame #################################################################
            btn_Frame = Frame(Manage_Frame,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
            btn_Frame.place(x = (6/1360)*main_width ,y = (520/768)*main_heigth,width =round((420/1360)*main_width))

            Addbtn = Button(btn_Frame,text = 'Add',width=round((10/1360)*main_width),command = add_students,bg = 'Lightpink').grid(row=0,column = 0,padx = (15/1360)*main_width,pady = (10/768)*main_heigth)
            updatebtn = Button(btn_Frame,text = 'Update',width=round((10/1360)*main_width),command = update_data,bg = 'Lightpink').grid(row=0,column = 1,padx =(15/1360)*main_width,pady =(10/768)*main_heigth)
            deletebtn = Button(btn_Frame,text = 'Delete',width=round((10/1360)*main_width),command = delete_data,bg = 'Lightpink').grid(row=0,column = 2,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)
            cleartbtn = Button(btn_Frame,text = 'Clear',width=round((10/1360)*main_width),command = clear,bg = 'Lightpink').grid(row=0,column = 3,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

            ########################## Detail Frame ###############################################        
            Detail_Frame = Frame(root1,bd = round((4/1360)*main_width) ,relief = RIDGE,bg = 'skyblue')
            Detail_Frame.place(x = round((500/1360)*main_width),y = round((100/768)*main_heigth),width = round((765/1360)*main_width),height = round((590/768)*main_heigth))


            lbl_serch = Label(Detail_Frame,text = "Search By",bg = 'skyblue',fg = 'Black',font = ('time now roman',round((14/1360)*main_width),'bold'))
            lbl_serch.grid(row = 0,column = 0,pady = round((10/768)*main_heigth),padx = round((20/1360)*main_width),sticky = W )


            combo_serch = ttk.Combobox(Detail_Frame,textvariable = search_by,width = round((10/1360)*main_width),font = ('time new roman',round((13/1360)*main_width),'bold'),state = 'readonly')
            combo_serch['values'] = ['Name','Address','Accountno','SSSMID','Class','Aadharno','Scholar_id']
            combo_serch.grid(row=0,column = 1 , padx = (20/1360)*main_width ,pady = (10/768)*main_heigth)

            txt_serch = Entry(Detail_Frame,textvariable = search_txt,font = ('time now roman',round((14/1360)*main_width),'bold'),bd = (5/1360)*main_width ,bg  = 'skyblue', relief = GROOVE)
            txt_serch.grid(row = 0,column = 2,pady = (10/1360)*main_heigth,padx = (20/1360)*main_width,sticky = W )


            serchbtn = Button(Detail_Frame,text = 'Search',width=round((10/1360)*main_width), pady = (5/768)*main_heigth,command = search_data,bg = 'Lightpink').grid(row=0,column = 3,padx =10,pady = 10)
            showalltbtn = Button(Detail_Frame,text = 'Show All',width=round((10/1360)*main_width),command =fetch_data,bg = 'Lightpink').grid(row=0,column = 4,padx =(10/1360)*main_width,pady = (10/768)*main_heigth)

            def next_w(event):
                event.widget.tk_focusNext().focus()
                return 'break'
            root1.bind_class('Entry','<Down>',next_w)
            def next_w(event):
                event.widget.tk_focusPrev().focus()
                return 'break'
            root1.bind_class('Entry','<Up>',next_w)
            def next_w(event):
                event.widget.tk_focusNext().focus()
                return 'break'
            root1.bind_class('Button','<Right>',next_w)
            
            
            ################################## Table-Frame #############################################################
            Table_Frame = Frame(Detail_Frame,bd = (4/1360)*main_width ,relief = RIDGE,bg = 'skyblue')
            Table_Frame.place(x = (10/1360)*main_width,y = (70/768)*main_heigth,width = (740/1360)*main_width,height = (500/768)*main_heigth)
            scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame,orient = VERTICAL)

            student_table = ttk.Treeview(Table_Frame,columns = ('Name',"Father's Name","Mother's Name",'D.O.B','Scholar_ID','Class_ID','Account No.','Aadhar No.','SSSMID2','Address'),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
            scroll_x.pack(side = BOTTOM,fill = X)
            scroll_y.pack(side = RIGHT , fill =Y)
            scroll_x.config(command = student_table.xview)
            scroll_y.config(command = student_table.yview)

            student_table.heading('Name',text = 'Name' )
            student_table.heading("Father's Name",text = "Father's Name" )
            student_table.heading("Mother's Name",text = "Mother's Name" )
            student_table.heading('D.O.B',text = 'D.O.B' )
            student_table.heading('Scholar_ID',text = 'Scholar ID.')
            student_table.heading('Class_ID',text = 'Class_ID' )
            student_table.heading('Account No.',text = 'Account No.' )
            student_table.heading('Aadhar No.',text = 'Aadhar No.' )
            student_table.heading('SSSMID2',text = 'SSSMID' )
            student_table.heading('Address',text = 'Address' )
            student_table['show'] = 'headings'
            student_table.column('Name',width = 130)
            student_table.column("Father's Name",width =130 )
            student_table.column("Mother's Name",width = 130)
            student_table.column('D.O.B',width = 75)
            student_table.column('Scholar_ID',width = 70)
            student_table.column('Class_ID',width = 50)
            student_table.column('Account No.',width = 180)
            student_table.column('Aadhar No.',width = 180)
            student_table.column('SSSMID2',width = 180)
            student_table.column('Address',width = 200)
            student_table.pack(fill = BOTH,expand = 1)
            student_table.bind("<ButtonRelease-1>",get_cursor)
            style = ttk.Style()
            style.configure('Treeview.Heading',font = ('time now roman',round((12/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
            style.configure('Treeview',font = ('time now roman',round((10/1360)*main_width),'bold'),bg = 'skyblue',fg = 'black')
            fetch_data()

            root1.mainloop()  
        def addmi():
            messagebox.showwarning('Attention','you will get this fuction in next update')  
        def idg():
            messagebox.showwarning('Attention','you will get this fuction in next update') 
        def resl():
            firstname = StringVar()
            lastname = StringVar()  
            emailid = StringVar()
            contactnumber = StringVar()
            passwordm = StringVar()
            cpassword = IntVar()
            operator = IntVar()
            rootr = Toplevel(rootm)
            rootr.geometry('800x500+120+90')
            rootr.title('New User')
            rootr.config(bg = '#B9B4F8')
            photo = PhotoImage(file = 'school.png')
            rootr.iconphoto(FALSE,photo)
            menur1 = Label(rootr,text = 'Registration Form',font = ('times new roman',round((22/1360)*main_width),'bold'), bg ='#39E2D8',fg = 'Black',relief = 'solid')
            menur1.pack(side = TOP,fill = X)
            framer1 = Frame(rootr,bd  = round((8/1360)*main_width) ,relief = GROOVE,bg = 'skyblue')
            framer1.place(x = (50/1360)*main_width,y = (65/768)*main_heigth,width = (700/1360)*main_width,height = (400/768)*main_heigth)
            a = Label(framer1 ,text = "First Name",bg = 'skyblue',font = ('times new roman',round((18/1360)*main_width),'bold')).place(x = 60,y = 10)
            b = Label(framer1 ,text = "Last Name",bg = 'skyblue',font = ('times new roman',round((18/1360)*main_width),'bold')).place(x =60,y = 50)
            c = Label(framer1 ,text = "Email Id",bg = 'skyblue',font = ('times new roman',round((18/1360)*main_width),'bold')).place(x = 60,y = 100)
            d = Label(framer1 ,text = "Contact Number",bg = 'skyblue',font = ('times new roman',round((18/1360)*main_width),'bold')).place(x = 60,y = 150)
            e = Label(framer1 ,text = "Create Password",bg = 'skyblue',font = ('times new roman',round((18/1360)*main_width),'bold')).place(x = 60,y = 200)
            f = Label(framer1 ,text = "Working as",bg = 'skyblue',font = ('times new roman',round((18/1360)*main_width),'bold')).place(x = 60,y = 250)
            a1 = Entry(framer1,textvariable = firstname,font = ('times new roman',round((12/1360)*main_width),'bold')).place(x = 300,y = 10)
            b1 = Entry(framer1,textvariable = lastname,font = ('times new roman',round((12/1360)*main_width),'bold')).place(x = 300,y = 50) 
            c1 = Entry(framer1,textvariable = emailid,font = ('times new roman',round((12/1360)*main_width),'bold')).place(x = 300,y = 100) 
            d1 = Entry(framer1,textvariable =  contactnumber,font = ('times new roman',round((12/1360)*main_width),'bold')).place(x = 300,y = 150)
            e1 = Entry(framer1,textvariable = passwordm,font = ('times new roman',round((12/1360)*main_width),'bold')).place(x = 300,y = 200) 
            fieldt = Checkbutton(rootr,text = 'Teacher',font = ('time new roman', 12 , 'bold'),variable = cpassword,bg = 'skyblue',fg = 'black').place(x = 350,y = 330)
            fieldm = Checkbutton(rootr,text = 'Operator',font = ('time new roman', 12 , 'bold'),bg = 'skyblue',fg = 'black',variable = operator).place(x = 500,y = 330)
            def registeru():
                con =pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'school')
                cur = con.cursor()
                if cpassword.get() == 1 and operator.get() == 0:
                    cur.execute('insert into teacher (username,password)values(%s,%s)',(
                    firstname.get(),
                    passwordm.get()))
                    con.commit()
                    con.close() 
                    messagebox.showinfo('Successfully',firstname.get()+'  has become the active user')
                elif operator.get() == 1 and cpassword.get() == 0:
                    cur.execute('insert into operator (username,password)values(%s,%s)',(
                    firstname.get(),
                    passwordm.get()))
                    con.commit()
                    con.close() 
                    messagebox.showinfo('Successfully',firstname.get()+'  has become the active user')
                elif operator.get() == 0 and cpassword.get() == 0:
                    messagebox.showerror('Sorry','You have to  not selected working as Teacher and operator,Please select only one..')
                elif operator.get() == 1 and cpassword.get() == 1:
                    messagebox.showerror('Sorry','You have to selected working as Teacher and operator,Please select only one..')
            btn = Button(framer1,text = 'Register',width = 12 , font = ('time new roman', 18 , 'bold'),bg = 'skyblue',fg  = 'black',command =registeru )
            btn.place(x = 200,y = 300)
                    
        imgm = ImageTk.PhotoImage(file = 'students.png')
        b2m = Button(f1m,text = 'Students',image = imgm,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = stud)
        b2m.grid(row = 1 , column = 1 , padx = (20/1360)*main_width,ipadx = (50/1360)*main_width)
        img2m = ImageTk.PhotoImage(file = 'formnew.png')
        b3m = Button(f1m,text = 'Staff-Details',image = img2m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = teacherstaff)
        b3m.grid(row = 1 , column = 5 , padx=(120/1360)*main_width , pady = (20/768)*main_heigth,ipadx = (50/1360)*main_width)
        img3m = ImageTk.PhotoImage(Image.open('time-and-date.png'))
        b3m = Button(f1m,text = 'Generate Result',image = img3m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = idg)
        b3m.grid(row = 1 , column = 7 , padx=(100/1360)*main_width , pady = (20/768)*main_heigth,ipadx = (50/1360)*main_width)
        img4m = ImageTk.PhotoImage(Image.open('fees.png'))
        b4m = Button(f1m,text = 'Fees Management',image = img4m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = feesm)
        b4m.grid(row = 5 , column = 1 , padx=(20/1360)*main_width,pady = (120/768)*main_heigth,ipadx = (50/1360)*main_width)
        img5m = ImageTk.PhotoImage(Image.open('Tc.png'))
        b5m = Button(f1m,text = 'Backup',image = img5m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = backup)
        b5m.grid(row = 5 , column = 5 , padx=(130/1360)*main_width,pady = (20/768)*main_heigth,ipadx = (40/1360)*main_width)
        img6m = ImageTk.PhotoImage(Image.open('result.png'))
        b6m = Button(f1m,text = 'Add New User',image = img6m,font = ('times new roman',round((15/1360)*main_width),'bold'),compound = TOP,bg = 'lightpink',relief = SUNKEN,bd = (10/1360)*main_width,command = resl)
        b6m.grid(row = 5 , column = 7 , padx=(130/1360)*main_width,pady = (20/768)*main_heigth,ipadx = (40/1360)*main_width)
        rootm.mainloop()

    else:
        tkmsg.showerror('Error','Invalid Username or Password')
def Quit1(event):
    root.destroy()
    
def Quit():
    root.destroy()
root.bind('<Escape>',Quit1)
def retur(event):
    login()
root.bind('<Return>',retur)
######################### All Variables for New User #######################################


        
        


    

      

def about_us():
    roota = Toplevel(root)
    roota.geometry('900x600+120+90')
    roota.title('About us')
    roota.config(bg = '#B9B4F8')
    menu1 = Label(roota,text = 'About us',font = ('times new roman',round((22/1360)*main_width),'bold'), bg ='#39E2D8',fg = 'Black',relief = 'solid')
    menu1.pack(side = TOP,fill = X)
    frame1 = Frame(roota,bd  = round((8/1360)*main_width) ,relief = GROOVE,bg = 'skyblue')
    frame1.place(x = (45/1360)*main_width,y = (60/768)*main_heigth,width = (800/1360)*main_width,height = (500/768)*main_heigth)
    Title1 = Label(roota,text = 'MEET THE TEAM',font = ('times new roman',round((25/1360)*main_width),'bold'), bg = 'skyblue',fg = 'Black')
    Title1.place(x=  350,y =75)
    subtitle1 = Label(roota,text = 'Hey,nice to see you here!',font = ('times new roman',round((15/1360)*main_width),'roman'), bg = 'skyblue',fg = 'Black')
    subtitle1.place(x=  385,y =125)
    subtitle2 = Label(roota,text = 'Who We Are ?',font = ('times new roman',round((17/1360)*main_width),'bold'), bg = 'skyblue',fg = 'Black')
    subtitle2.place(x = 60 , y = 150)
    subtitle3 = Label(roota,text = 'This application is developed by:',font = ('times new roman',round((17/1360)*main_width),'roman'), bg = 'skyblue',fg = 'Black')
    subtitle3.place(x = 60 , y = 190)
    subtile4 =  Label(roota,text = '1.Rishabh sahu (Working With UltraCreation) \n2.Ishwar Jethwani     (UltraCreation)                  ',font = ('times new roman',round((13/1360)*main_width),'roman'), bg = 'skyblue',fg = 'Black')
    subtile4.place(x = 60 , y = 230)
    subtitle5 = Label(roota,text = 'About Company',font = ('times new roman',round((18/1360)*main_width),'bold'), bg = 'skyblue',fg = 'Black')
    subtitle5.place(x = 60 , y = 300)
    body  = Label(roota,text = 'Ultra creation provides a platform to purchase a website and software  Like a product within 3 days \n customers have a great platform listing our products and other information their own website customers \n have an admin panel which contains all the information about the business and it can be handled easily. ',font = ('times new roman',round((13/1360)*main_width),'roman'), bg = 'skyblue',fg = 'Black')
    body.place(x = 55 , y = 340)
    body1  = Label(roota,text = 'Contact US',font = ('times new roman',round((17/1360)*main_width),'bold'), bg = 'skyblue',fg = 'Black')
    body1.place(x = 55 , y = 420)
    txt_msg = Text(roota,width  = round(60) ,height = round((4/768)*main_heigth),font = ('time now roman',round((12/1360)*main_width),'bold'),bd = round((4/1360)*main_width) ,bg  = 'skyblue', relief = GROOVE)
    txt_msg.place(x = 55,y = 460)

    
    def send():
        try:
            SenderAddress = "Onlinewebsitemarket@gmail.com"
            passwrd1  = 'weckbhyqcfcepjtn'
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(SenderAddress,passwrd1)
            msg = txt_msg.get('1.0',END)
           
            subject = 'Mail From Client side'
            body = 'subject:{}\n\n{}'.format(subject,msg)
            server.sendmail(SenderAddress,'ultracreationteam@gmail.com',body)
            server.quit() 
            messagebox.showinfo('Congratulation','You message has been recived by developer')
        except:
            messagebox.showerror('Error','No check your Internet connection')
    btns =  Button(roota,text = 'Send',width = 12 , font = ('time new roman', 15 , 'bold'),bg = 'skyblue',fg  = 'black',command = send)
    btns.place(x = 650,y = 480)
       
####################### All #####################################################################################
bg_icon =  ImageTk.PhotoImage(file = 'LOGIN!.jpeg')
user_icon =  ImageTk.PhotoImage(file = 'user.png')
pass_icon =  ImageTk.PhotoImage(file = 'password.png')
logo_icon =  ImageTk.PhotoImage(file = 'boss.png')

################## variable ####################################################################################
uname = StringVar()
passwrd = StringVar()
cpassword = IntVar()
operator  = IntVar()
bg_lbl = Label(root,image = bg_icon).pack()

title = Label(root,text = 'Login System',font = ("times new roman" ,40 , 'bold'),bg = 'powder blue',fg = 'black',relief = GROOVE)
title.place(x=0,y=0,relwidth = 1)

Login_frame = Frame(root,bg = 'Skyblue')
Login_frame.place(x = main_width/2.75,y = main_heigth/4)

logolbl = Label(Login_frame,image = logo_icon,bg = 'Skyblue')
logolbl.grid(row = 0 , columnspan = 2 ,pady = 20)

lbluser = Label(Login_frame,text = 'Username',image = user_icon,compound = LEFT,font = ('time new roman' , 20,'bold'),bg = 'Skyblue').grid(row = 1 , column = 0 , padx = 20 , pady = 10)
txtuser = Entry(Login_frame,textvariable = uname,bd = 5 , relief = GROOVE,font = ('times new roman',15)).grid(row = 1 , column = 1,padx  =20)
lblpass = Label(Login_frame,text = 'Password',image = pass_icon,compound = LEFT,font = ('time new roman' , 20,'bold'),bg = 'Skyblue').grid(row = 2 , column = 0 , padx = 20 , pady = 10)  
txtpass = Entry(Login_frame,textvariable = passwrd,bd = 5 , relief = GROOVE,font = ('times new roman',15),show = '*').grid(row = 2 , column = 1,padx  =20)
fieldt = Checkbutton(root,text = 'Teacher',font = ('time new roman', 12 , 'bold'),variable = cpassword,bg = 'skyblue',fg = 'black').place(x = 500,y = 330)
fieldm = Checkbutton(root,text = 'Operator',font = ('time new roman', 12 , 'bold'),bg = 'skyblue',fg = 'black',variable = operator).place(x = 850,y = 330)
def onButton1(e):
    btn_log['bg'] ='#33E6FF'
def leaveButton1(e):
    btn_log['bg'] = 'skyblue'

def onButton2(event):
    btn_exit['bg'] ='#F25B5B'   
def leaveButton2(event):
    btn_exit['bg'] = 'skyblue'
btn_log = Button(Login_frame,text = 'Login',width = 15 , font = ('time new roman', 14 , 'bold'),bg = 'skyblue',fg  = 'black',command = login)
btn_log.grid(row = 3,column = 1 , pady = 10)
btn_log.bind('<Enter>',onButton1)
btn_log.bind('<Leave>',leaveButton1)
btn_exit = Button(Login_frame,text = 'Quit',width = 15 , font = ('time new roman', 14 , 'bold'),bg = 'skyblue',fg  = 'black',command = Quit)
btn_exit.place(x = 20 , y = 300)
btn_exit.bind('<Enter>',onButton2)
btn_exit.bind('<Leave>',leaveButton2)
imgma = ImageTk.PhotoImage(file = 'Aboutus.png')
b2m = Button(root,text = 'About us',image = imgma,font = ('Helvetica',round((16/1360)*main_width),'bold'),compound = TOP,bg = 'skyblue',fg = 'Black',command = about_us)
b2m.place(x = (1220/1360)*main_width , y = (560/768)*main_heigth)

def next_w(event):
    event.widget.tk_focusNext().focus()
    return 'break'
root.bind_class('Entry','<Down>',next_w)
def next_w(event):
    event.widget.tk_focusPrev().focus()
    return 'break'
root.bind_class('Entry','<Up>',next_w)

root.mainloop()

