import pandas
import numpy as np
import tkinter
from tkinter import filedialog
from collections import OrderedDict

def saveFile():
    data = pandas.DataFrame(np.random.randn(13, 5))
    print(data)
    outfilename = filedialog.asksaveasfile(filetypes=(("CSV files", "*.csv"), ("all files", "*.*")), defaultextension=".csv") #get save location
    data.to_csv(outfilename, mode='a', encoding = 'utf-8')
    outfilename.close()

window=tkinter.Tk()

window.title("제목")
window.geometry("500x280+100+100")
window.resizable(False, False)
button=tkinter.Button(window, text="save", command=saveFile)
button.pack()

window.mainloop()