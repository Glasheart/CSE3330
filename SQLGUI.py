from tkinter import *
import sqlite3

#might need to addd database here, or put it in a file and load it at the start
conn = sqlite3.connect("LMS.db")
c = conn.cursor()

with open('libraryCreate.sql', 'r') as file:
    c.executescript(file.read())

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
    conn = sqlite3.connect("LMS.db")
    c = conn.cursor()

    s_entry = SELentry.get()
    f_entry = FROMentry.get()
    w_entry = WHEREentry.get()
    g_entry = GROUPentry.get()
    h_entry = HAVINGentry.get()
    o_entry = ORDERentry.get()

    SQLCOMMAND = "SELECT " + s_entry
    if f_entry :
        SQLCOMMAND += (" FROM " + f_entry)
    if w_entry :
        SQLCOMMAND += (" WHERE " + w_entry)
    if g_entry :
        SQLCOMMAND += (" GROUP BY " + g_entry)
    if h_entry :
        SQLCOMMAND += (" HAVING " + w_entry)
    if o_entry :
        SQLCOMMAND += (" ORDER BY " + o_entry)

    SQLCOMMAND += ";"
    c.execute(SQLCOMMAND)
    records = c.fetchall()
    print(records)

    RESlabel = Label(selFrame, text = records).grid(row = 7)


    conn.commit()
    conn.close()
    SELentry.delete(0, END)
    FROMentry.delete(0, END)
    WHEREentry.delete(0, END)
    GROUPentry.delete(0, END)
    HAVINGentry.delete(0, END)
    ORDERentry.delete(0, END)
    return


def insCommand():
    #add implementation
    conn = sqlite3.connect("LMS.db")
    c = conn.cursor()

    i_entry = TABLEentry.get()
    v_entry = VALUESentry.get()

    SQLCOMMAND = "INSERT INTO " + i_entry + " VALUES (" + v_entry + ");"
    c.execute(SQLCOMMAND)
    
    conn.commit()
    conn.close()
    TABLEentry.delete(0, END)
    VALUESentry.delete(0, END)
    return


#Make the main frame
mainFrame = Frame(window)
mainFrame.pack()

#make the other frames in advance
selFrame = Frame(window)
insFrame = Frame(window)

#make the buttons for each frame
selButton = Button(mainFrame, text = "Select Query", width = 20, command = selQuery)
selButton.pack(padx=10, pady=10)
insButton = Button(mainFrame, text = "Insert Query", width = 20, command = insQuery)
insButton.pack(padx=10, pady=10)

#selFrame fields
SELlabel = Label(selFrame, text = "SELECT").grid(row = 0)
SELentry = Entry(selFrame, width=50)
SELentry.grid(row = 0, column = 1, padx=10, pady=3)

FROMlabel = Label(selFrame, text = "FROM").grid(row = 1)
FROMentry = Entry(selFrame, width=50)
FROMentry.grid(row = 1, column = 1, padx=10, pady=3)

WHERElabel = Label(selFrame, text = "WHERE").grid(row = 2)
WHEREentry = Entry(selFrame, width=50)
WHEREentry.grid(row = 2, column = 1, padx=10, pady=3)

GROUPlabel = Label(selFrame, text = "GROUP BY").grid(row = 3)
GROUPentry = Entry(selFrame, width=50)
GROUPentry.grid(row = 3, column = 1, padx=10, pady=3)

HAVINGlabel = Label(selFrame, text = "HAVING").grid(row = 4)
HAVINGentry = Entry(selFrame, width=50)
HAVINGentry.grid(row = 4, column = 1, padx=10, pady=3)

ORDERlabel = Label(selFrame, text = "ORDER BY").grid(row = 5)
ORDERentry = Entry(selFrame, width=50)
ORDERentry.grid(row = 5, column = 1, padx=10, pady=3)

backButton = Button(selFrame, text = "Back", width = 20, command = menu).grid(row = 6, padx=10, pady=10)
doneButton = Button(selFrame, text = "Done", width = 20, command = selCommand).grid(row = 6, column = 1, padx=10, pady=10)

#insFrame fields
TABLElabel = Label(insFrame, text = "INSERT INTO").grid(row = 0)
TABLEentry = Entry(insFrame, width=50)
TABLEentry.grid(row = 0, column = 1, padx=10, pady=3)

VALUESlabel = Label(insFrame, text = "VALUES").grid(row = 1)
VALUESentry = Entry(insFrame, width=50)
VALUESentry.grid(row = 1, column = 1, padx=10, pady=3)

insbackButton = Button(insFrame, text = "Back", width = 20, command = menu).grid(row = 3, padx=10, pady=10)
insdoneButton = Button(insFrame, text = "Done", width = 20, command = insCommand).grid(row = 3, column = 1, padx=10, pady=10)

conn.commit()
conn.close()
file.close()

window.mainloop()
