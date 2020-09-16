from tkinter import *


class Table:

    def __init__(self, root,rows,column,brother_list):


        self.total_rows = rows
        self.total_column = column
        self.brother_list = brother_list
        # code for creating table
        w = [15,30]
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                self.e = Entry(root, width=w[j], fg='blue',
                               font=('Arial', 8, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, self.brother_List[i][j])

            # take the data

