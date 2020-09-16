import csv
import pandas as pd
import numpy as np
from tkinter import *
from tkinter.ttk import Notebook,Entry


root = Tk()
root.geometry("800x600")
root.title = "Covide-19 Epidemic Map"


df = pd.read_csv("Data\\Student_Teacher.csv")
df = df[pd.notnull(df['Id'])]
d =[]
data = df.to_numpy()
print(data[0])
name = data[:,1]
f_name =  [x.split()[0] for x in name]
f_name = np.asarray(f_name)
l_name = [x.split()[1:] for x in name]
l_name = np.asarray(l_name)
l_name_string = [' '.join(x) for x in l_name]
l_name_string = np.asarray(l_name_string)

split_name = [x.split() for x in name]

l1_string =""
l2_string =""
l3_string =""


# Title
title = Label(root, text = " Epidemic Map")
title.config(font=(35))
title.place(x= 380, y=20)

# id input text
label1 = Label(root, text ="Enter ID Number :")
label1.place(x=50, y = 120)
id = Entry(root,width = 20)
id.place(x =150, y = 120)

#Split Label
split_label = Label(root,text = "-------------------------------------------------------------------------")
split_label.place(x = 40, y = 150)

# Layer One : Person



split_label2 = Label(root,text = "-------------------------------------------------------------------------")
split_label2.place(x = 40, y = 230)


def search_function(id_num):
    brothers = []
    for index,item  in enumerate(data):
        if id_num == item[0]:
            l1_title = Label(root, text="Layer 1 : Person was found")
            l1_title.place(x=60, y=180)
            person_index = index
            l1_string = "ID was found :   Name: {} , \t  School: {}  \t Posision:{}  \t ID: {}".format(item[1],item[2],item[3],id_num)
            l1_Label = Label(root, text=l1_string)
            l1_Label.place(x=60, y=200)






            for B_index,B_item in enumerate(l_name_string):

                if (l_name_string[index] == B_item and index != B_index):
                    brothers.append(B_index)


            x = 60
            for index,i in enumerate(brothers):
                if len(brothers) > 0:
                    l2_title = Label(root, text="Layer 2 : Number of Brother = {}".format(len(brothers)))
                    l2_title.place(x=60, y=260)

                    y = 300
                    brother_title = "Brother : {}".format(str(index+1))
                    name_string =  "Name: {} ".format(data[i][1])
                    school_string = "School : {}".format(data[i][2])
                    member_string = "Member : {}".format(data[i][3])



                    if member_string =="طالب":
                        class_string = "Member : {}".format(data[i][4])
                        class_Label = Label(root, text=class_string)
                        class_Label.place(x=x, y=y + 150)


                    id_string = "ID : {}".format(data[i][0])


                    title_Label = Label(root, text=brother_title )
                    title_Label.place(x=x, y=y)

                    name_Label = Label(root, text=name_string)
                    name_Label.place(x=x, y=y+30)

                    school_Label = Label(root, text=school_string)
                    school_Label.place(x=x, y=y+60)

                    member_Label = Label(root, text=member_string)
                    member_Label.place(x=x, y=y+90)

                    id_Label = Label(root, text=id_string)
                    id_Label.place(x=x, y=y + 120)
                    x += 240
                else:
                    l2_title = Label(root, text="Layer 2 : Brothers not found")
                    l2_title.place(x=60, y=260)

        #Father
                split_label3 = Label(root,text="-------------------------------------------------------------------------")
                split_label3.place(x=40, y=460)


            for index,item in  enumerate(split_name):
                if split_name[person_index][1] == item[0] and split_name[person_index][2] == item[1] and split_name[person_index][3] == item[3] :
                    l3_title = Label(root, text="Layer 3 : Parent Found")
                    l3_title.place(x=60, y=480)

                    parent_string = " Name: {} , \t  School: {}  \t Posision:{}  \t ID: {}".format(data[index][1], data[index][2], data[index][3], data[index][0])
                    l3_Label = Label(root, text=parent_string)
                    l3_Label.place(x=60, y=520)



def myClick():

    id_num = id.get()
    if(id_num != ""):
        search_function(id_num)
    else:
        l1_title = Label(root, text="You should Enter Id number")
        l1_title.place(x=60, y=180)



# Track Button
mybatton = Button(root,text= "Track >>",command = myClick )
mybatton.place(x=290,y = 117)
root.mainloop()
