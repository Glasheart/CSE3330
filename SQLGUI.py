from tkinter import *

#might need to addd database here, or put it in a file and load it at the start
window = Tk()
window.title('SQL GUI')
SQLCOMMAND = ""

def selQuery():
    mainFrame.pack_forget()
    selFrame.pack()

def insQuery():
    mainFrame.pack_forget()
    insFrame.pack()

def menu():
    selFrame.pack_forget()
    insFrame.pack_forget()
    mainFrame.pack()

def selCommand():
    #add implementation
    return

def insCommand():
    #add implementation
    return

#Make the main frame
mainFrame = Frame(window)
mainFrame.pack()
#make the other frames in advance
selFrame = Frame(window)

insFrame = Frame(window)

#make the buttons for each frame
selButton = Button(mainFrame, text = "Select Query", width = 20, command = selQuery)
selButton.pack()
insButton = Button(mainFrame, text = "Insert Query", width = 20, command = insQuery)
insButton.pack()

#selFrame fields
SELlabel = Label(selFrame, text = "SELECT").grid(row = 0)
SELentry =Entry(selFrame).grid(row = 0, column = 1)

FROMlabel = Label(selFrame, text = "FROM").grid(row = 1)
FROMentry = Entry(selFrame).grid(row = 1, column = 1)

WHERElabel = Label(selFrame, text = "WHERE").grid(row = 2)
WHEREentry = Entry(selFrame).grid(row = 2, column = 1)

GROUPlabel = Label(selFrame, text = "GROUP BY").grid(row = 3)
GROUPentry = Entry(selFrame).grid(row = 3, column = 1)

HAVINGlabel = Label(selFrame, text = "HAVING").grid(row = 4)
HAVINGentry = Entry(selFrame).grid(row = 4, column = 1)

ORDERlabel = Label(selFrame, text = "ORDER BY").grid(row = 5)
ORDERentry = Entry(selFrame).grid(row = 5, column = 1)

backButton = Button(selFrame, text = "Back", width = 20, command = menu).grid(row = 6)
doneButton = Button(selFrame, text = "Done", width = 20, command = selCommand).grid(row = 6, column = 1)

#insFrame fields
TABLElabel = Label(insFrame, text = "INSERT INTO").grid(row = 0)
TABLEentry = Entry(insFrame).grid(row = 0, column = 1)

VALUESlabel = Label(insFrame, text = "VALUES").grid(row = 1)
VALUESentry = Entry(insFrame).grid(row = 1, column = 1)

insbackButton = Button(insFrame, text = "Back", width = 20, command = menu).grid(row = 3)
insdoneButton = Button(insFrame, text = "Done", width = 20, command = insCommand).grid(row = 3, column = 1)

window.mainloop()
