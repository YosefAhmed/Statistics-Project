from lib2to3.fixes import fix_throw
from tkinter import *
import statistics

def convert_to_array():
    List = list_txt.get().split()
    List = [int(x) for x in List]
    print(List)
    return List


def calcMode():
    mode_txt.delete(0, END)
    try:
        mode_txt.config(state="normal")
        mode_txt.insert(0,statistics.mode(convert_to_array()))
        mode_txt.config(state=DISABLED)

    except:
        mode_txt.insert(0,"there is no mode in this list")

def calcMean():
    mean_txt.delete(0, END)
    mean_txt.config(state="normal")
    mean_txt.insert(0,statistics.mean(convert_to_array()))
    mean_txt.config(state=DISABLED)

def calcMedian():
    median_txt.delete(0, END)
    median_txt.config(state="normal")
    median_txt.insert(0,statistics.median(convert_to_array()))
    median_txt.config(state=DISABLED)

def calcvariance():
    variance_txt.delete(0, END)
    variance_txt.config(state="normal")
    variance_txt.insert(0,statistics.variance(convert_to_array()))
    variance_txt.config(state=DISABLED)

def calc_standard_dev():
    standDev_txt.delete(0, END)
    standDev_txt.config(state="normal")
    standDev_txt.insert(0, statistics.stdev(convert_to_array()))
    standDev_txt.config(state=DISABLED)

root = Tk()
root.resizable(False,False)
root.geometry("700x500")
root.title("Statistics")

list_lbl=Label(root,text= "List ")


mode_btn=Button(root,text= "    Mode    ",command=calcMode)
median_btn=Button(root,text= "    Median    ",command=calcMedian)
mean_btn=Button(root,text= "    Mean    ",command=calcMean)
standDev_btn=Button(root,text= "    Standard Dev    ",command=calc_standard_dev)
variance_btn=Button(root,text= "    Variance    ",command=calcvariance)



list_txt=Entry(root)

mode_txt=Entry(root)
mode_txt.config(state=DISABLED)

median_txt=Entry(root)
median_txt.config(state=DISABLED)

mean_txt=Entry(root)
mean_txt.config(state=DISABLED)

standDev_txt=Entry(root)
standDev_txt.config(state=DISABLED)

variance_txt=Entry(root)
variance_txt.config(state=DISABLED)



list_lbl.grid(row=0,column=0)
list_txt.grid(row=0,column=1,ipadx="100",pady=30)
mode_txt.grid(row=2,column=0,ipadx="15",pady=30,padx=20)
median_txt.grid(row=2,column=1,ipadx="15",pady=30)
mean_txt.grid(row=2,column=2,ipadx="15",pady=30)
standDev_txt.grid(row=4,column=0,ipadx="15",pady=30)
variance_txt.grid(row=4,column=1,ipadx="15",pady=30)



mode_btn.grid(row=3,column=0,pady=5)
median_btn.grid(row=3,column=1,pady=5)
mean_btn.grid(row=3,column=2,pady=5)
standDev_btn.grid(row=5,column=0,pady=5)
variance_btn.grid(row=5,column=1,pady=5)


root.mainloop()

