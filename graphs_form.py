from tkinter import *
import collections
import matplotlib.pyplot as plt

try:
    def convert_to_array(e):
        list = e.get().split()
        list = [int(x) for x in list]
        return list


    def bar_charts():
        plt.bar(collections.Counter(convert_to_array(X_txt)).keys(), collections.Counter(convert_to_array(X_txt)).values(), width=0.8, color=['red', 'green'])
        plt.show()

    def pie_charts(X):
        plt.pie(convert_to_array(X))
        plt.show()

    def scatter_plot(X, Y):
        plt.scatter(convert_to_array(X), convert_to_array(Y))
        plt.show()

    def dot_plot(X):
        plt.plot(convert_to_array(X))
        plt.show()

    def histogram(Y):
        plt.hist(convert_to_array(Y))
        plt.show()
except:
    print("Error")

root =Tk
X_txt = Entry
Y_txt = Entry
def main():
    root = Tk()
    root.resizable(False, False)
#   root.geometry("700x500")
    root.title("Graphs")
    root.config(background='light blue')

    X_label = Label(root, text="X List ")
    Y_label = Label(root, text="Y List ")

    X_txt = Entry(root)
    Y_txt = Entry(root)

    bar_btn = Button(root, text="  Bar Charts  ", command=bar_charts)
    pie_btn = Button(root, text="  Pie Charts  ", command=pie_charts)
    scutter_btn = Button(root, text="  Scatter Plot  ", command=scatter_plot)

    dot_btn = Button(root, text="  Dot Plot  ", command=dot_plot)
    hist_btn = Button(root, text="  Histogram  ", command=histogram)
    box_btn = Button(root, text="  Box Plot  ")

    corrlation_btn = Button(root, text="  Correlation  ")
    rgresion_btn = Button(root, text="  Regression  ")


    X_label.grid(row=0, column=0)
    Y_label.grid(row=1, column=0)

    X_txt.grid(row=0, column=1, ipadx="100", pady=10)
    Y_txt.grid(row=1, column=1, ipadx="100", pady=15)


    bar_btn.grid(row=3,column=0, padx=30, pady=30)
    pie_btn.grid(row=3,column=1)
    scutter_btn.grid(row=3,column=2,padx=30)

    dot_btn.grid(row=4,column=0)
    hist_btn.grid(row=4,column=1)
    box_btn.grid(row=4,column=2,padx=30)

    corrlation_btn.grid(row=5,column=1,pady=30)
    rgresion_btn.grid(row=6,column=1, pady=10)

    root.mainloop()