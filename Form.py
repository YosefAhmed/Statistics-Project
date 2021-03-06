from lib2to3.fixes import fix_throw
from tkinter import *
from tkinter import messagebox
import statistics
import collections
import math
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from pandas._libs.parsers import basestring

#these 2 methods converts Y & X Entry to List of integers
from pandas.io.sas.sas7bdat import _column


def convertY_to_array():
    List = Y_txt.get().split()
    List = [int(x) for x in List]
    print(List)
    return List

def convertX_to_array():
    List = X_txt.get().split()
    List = [int(x) for x in List]
    print(List)
    return List

#this method clears all Entries
def clear():
    X_txt.delete(0, 'end')
    Y_txt.delete(0, 'end')
    mode_txt.delete(0, 'end')
    median_txt.delete(0, 'end')
    mean_txt.delete(0, 'end')
    standDev_txt.delete(0, 'end')
    variance_txt.delete(0, 'end')

#=============== Mode Calculator =================
def calcMode():
    try:
        mode_txt.config(state="normal")
        mode_txt.delete(0, END)
        mode_txt.insert(0,statistics.mode(convertX_to_array()))
        mode_txt.config(state=DISABLED)

    except:
        mode_txt.insert(0,"there is no mode in this list")

#=============== Mean Calculator =================
def calcMean():
    mean_txt.config(state="normal")
    mean_txt.delete(0, END)
    mean_txt.insert(0,statistics.mean(convertX_to_array()))
    mean_txt.config(state=DISABLED)

#=============== Median Calculator =================
def calcMedian():
    median_txt.config(state="normal")
    median_txt.delete(0, END)
    median_txt.insert(0,statistics.median(convertX_to_array()))
    median_txt.config(state=DISABLED)

#=============== Variance Calculator =================
def calcvariance():
    variance_txt.config(state="normal")
    variance_txt.delete(0, END)
    variance_txt.insert(0,statistics.variance(convertX_to_array()))
    variance_txt.config(state=DISABLED)

#=============== Stabdard Deviation Calculator =================
def calc_standard_dev():
    standDev_txt.config(state="normal")
    standDev_txt.delete(0, END)
    standDev_txt.insert(0, statistics.stdev(convertX_to_array()))
    standDev_txt.config(state=DISABLED)

#=============== Bar Chart Calculator =================
def bar_charts():
        plt.bar(collections.Counter(convertX_to_array()).keys(), collections.Counter(convertX_to_array()).values(), width=0.8, color=['red', 'blue'])
        plt.title('Bar Charts')
        plt.show()

#=============== Pie charts Calculator =================
def pie_charts():
        plt.pie(collections.Counter(convertX_to_array()).values(), labels=collections.Counter(convertX_to_array()).keys(), startangle=90, shadow=True,
                radius=1.2, autopct='%1.1f%%')
        plt.legend()
        plt.title('Pie Chart')
        plt.show()

#=============== Scatter Plot Calculator =================
def scatter_plot():
    if Y_txt.get()==""or X_txt.get()=="" or len(convertX_to_array()) != len(convertY_to_array()):
        print(" Enter 2 Lists with the same length ")
    else:
        plt.scatter(convertX_to_array(), convertY_to_array())
        plt.title('Scatter Charts')
        plt.show()

#=============== dot Plot Calculator =================
"""def dot_plot():
        plt.plot(convertX_to_array())
        plt.title('Dot Plot')
        plt.show()
"""

#=============== Histogram Calculator =================
def histogram():
    if Y_txt.get() == "":
        bins = 1 + 3.3*math.log10(len(convertX_to_array()))
        plt.hist(convertX_to_array(), bins=math.ceil(bins))
        plt.title('Histogram')
        plt.show()
    else:
        bins = 1 +3.3* math.log10(len(convertY_to_array()))
        plt.hist(convertY_to_array(), bins=math.ceil(bins))
        plt.title('Histogram')
        plt.show()

#=============== Box Plot Calculator =================
def boxPlot():
    try:
        if X_txt.get() != "":
            df = pd.DataFrame(convertX_to_array(), columns=['A'])
            df.plot.box()
            plt.title('Box Plot')
            plt.show()
        else:
            df = pd.DataFrame(convertY_to_array(), columns=['A'])
            df.plot.box()
            plt.title('Box Plot')
            plt.show()
    except:
        messagebox.showinfo("Error", "Invalid list")


#=============== Correlation Calculator =================
def correlation():
  try :
      R=numpy.corrcoef(convertX_to_array(), convertY_to_array())[0,1]
      msg = "\n"
      if R == -1:
          msg = "Perfect -ve"
      elif R >-1 and R <= -0.6 :
          msg += "Strong -ve"
      elif R > -0.6 and R <= -0.3 :
          msg += "Moderate -ve"
      elif R > -0.3 and R < 0 :
          msg += "Weak -ve"
      elif R == 0 :
          msg += "No Correlation"
      elif R > 0 and R <= 0.3 :
          msg += "Weak +ve"
      elif R >0.3 and R <= 0.6 :
          msg = "Moderate +ve"
      elif R > 0.6 and R < 1 :
          msg += "Strong +ve"
      elif R == 1:
          msg += "Perfect +ve"

      messagebox.showinfo("Error",( R , msg))
  except :
      messagebox.showinfo("Error", "Enter 2 lists of numbers")

#=============== Regression Calculator =================
def regression():
    try:
        X = numpy.array(convertX_to_array())
        Y = numpy.array(convertY_to_array())
        n = numpy.size(X)
        xmean = statistics.mean(convertX_to_array())
        ymean = statistics.mean(convertY_to_array())
        SS_xy = numpy.sum(Y * X - n * ymean * xmean)
        SS_xx = numpy.sum(X * X - n * xmean * xmean)
        b1 = SS_xy / SS_xx
        b0 = ymean - b1 * xmean
        plt.scatter(X, Y)
        yPred = b0 + b1 * X
        plt.plot(X, yPred, color="r")
        plt.xlabel = ('x')
        plt.ylabel = ('y')
        plt.title('Line Regression')
        plt.show()
    except:
        messagebox.showinfo("Error", "Enter 2 valid lists of numbers")

#=================================================== Design ==================================

root = Tk()
root.resizable(False, False)
# root.geometry("700x500")
root.title("Statistics")
root.config(background='light blue')
list_lbl=Label(root,text= "List ")


mode_btn=Button(root,text= "    Mode    ", command=calcMode)
median_btn=Button(root,text= "    Median    ", command=calcMedian)
mean_btn=Button(root,text= "    Mean    ", command=calcMean)
standDev_btn=Button(root,text= "    Standard Dev    ", command=calc_standard_dev)
variance_btn=Button(root,text= "    Variance    ", command=calcvariance)

bar_btn = Button(root, text="  Bar Charts  ", command=bar_charts, bg='orange', fg='white')
pie_btn = Button(root, text="  Pie Charts  ", command=pie_charts, bg='orange', fg='white')
scutter_btn = Button(root, text="  Scatter Plot  ", command=scatter_plot, bg='orange', fg='white')

#dot_btn = Button(root, text="  Dot Plot  ", command=dot_plot, bg='orange', fg='white')
hist_btn = Button(root, text="  Histogram  ", command=histogram, bg='orange', fg='white')
box_btn = Button(root, text="  Box Plot  ", bg='orange', fg='white',command=boxPlot)

corrlation_btn = Button(root, text="  Correlation  ", bg='orange', fg='white', command=correlation)
rgresion_btn = Button(root, text="  Regression  ", bg='orange', fg='white', command=regression)

clear_btn = Button(root, text="  Clear  ", command=clear, bg='light green', fg='dark green')

X_txt = Entry(root,text="")
Y_txt = Entry(root,text="")
X_label = Label(root, text="X List ")
Y_label = Label(root, text="Y List ")



mode_txt = Entry(root)
mode_txt.config(state=DISABLED)

median_txt = Entry(root)
median_txt.config(state=DISABLED)

mean_txt=Entry(root)
mean_txt.config(state=DISABLED)

standDev_txt=Entry(root)
standDev_txt.config(state=DISABLED)

variance_txt=Entry(root)
variance_txt.config(state=DISABLED)



list_lbl.grid(row=0,column=0)
X_label.grid(row=0, column=0)
Y_label.grid(row=1, column=0)

X_txt.grid(row=0, column=1, ipadx="100", pady=10)
Y_txt.grid(row=1, column=1, ipadx="100", pady=15)
mode_txt.grid(row=2,column=0,ipadx="15",pady=30,padx=20)
median_txt.grid(row=2,column=1,ipadx="15",pady=30)
mean_txt.grid(row=2,column=2,ipadx="15",pady=30,padx=20)
standDev_txt.grid(row=4,column=0,ipadx="15",pady=20)
variance_txt.grid(row=4,column=2,ipadx="15",pady=20)



mode_btn.grid(row=3,column=0,pady=5)
median_btn.grid(row=3,column=1,pady=5)
mean_btn.grid(row=3,column=2,pady=5)
standDev_btn.grid(row=5,column=0,pady=0)
variance_btn.grid(row=5,column=2,pady=0)

bar_btn.grid(row=6, column=0, padx=30, pady=50)
pie_btn.grid(row=5, column=1,pady=50)
scutter_btn.grid(row=6, column=2, padx=30,pady=50)

#dot_btn.grid(row=7, column=0)
hist_btn.grid(row=6, column=1)
box_btn.grid(row=7, column=2, padx=30)

corrlation_btn.grid(row=7, column=1, pady=30)
rgresion_btn.grid(row=7, column=0, pady=10)

clear_btn.grid(row=8,column=1,pady=10)

root.mainloop()

