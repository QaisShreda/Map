from tkinter import *
import pandas as pd
import numpy as np
import Tbl
from prettytable import PrettyTable


# create root window
root = Tk()
root.geometry("800x600")


x = PrettyTable()

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])



label1 = Label(root, text =x,)
label1.place(x=50, y = 120)

#ob.place(x = 10, y =20)



root.mainloop()