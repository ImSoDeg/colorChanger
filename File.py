from tkinter import *
from tkinter import filedialog

def getFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(filepath)
    return filepath


