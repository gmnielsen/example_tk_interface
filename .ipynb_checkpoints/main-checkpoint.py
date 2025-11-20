#IMPORTS
    # tkinter is short for Tool Kit INTERface
import tkinter as tk

# ROOT
    # this is the overall window of our application
frameroot = tk.Tk()
frameroot.title("example")
    # width TIMES height PLUS x position PLUS y position
frameroot.geometry("300x200+1000+200")
frameroot.config(bg="RED")

# VARIABLES
    # these are global variables available to all our methods
variablename = tk.StringVar()

# COMMANDS
    # commands are executed by button presses
    # this command changes the text on a label
def buttoncommand():
    labelname.config(text=entryname.get())

# BUTTONS
    # buttons respond to mouse clicks
buttonname = tk.Button(frameroot,text="button", command=buttoncommand)

# LABELS
    # labels help the user identify different parts of our application
labelname = tk.Label(frameroot,text="label")

# ENTRY
    # an entry is a place where the user can type anything
entryname = tk.Entry(frameroot,textvariable=variablename)


# PACK
    # packing draws the object in their window
    # if an object isn't packed, it hasn't been drawn and doesn't appear in the window
labelname.pack(side=tk.TOP)
entryname.pack(side=tk.TOP)
buttonname.pack(side=tk.TOP)

# LOOP
    # this loop keeps the overall window from closing
frameroot.mainloop()

