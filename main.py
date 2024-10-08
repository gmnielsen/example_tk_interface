#IMPORTS
import tkinter as tk

# ROOT
frameroot = tk.Tk()
frameroot.title("example")
frameroot.geometry("300x200+1000+200")

# VARIABLES
variablename = tk.StringVar()

# COMMANDS
def buttoncommand():
    labelname.config(text=entryname.get())

# BUTTONS
buttonname = tk.Button(frameroot,text="button", command=buttoncommand)

# LABELS
labelname = tk.Label(frameroot,text="label")

# ENTRY
entryname = tk.Entry(frameroot,textvariable=variablename)


# PACK
labelname.pack(side=tk.LEFT)
entryname.pack(side=tk.LEFT)
buttonname.pack(side=tk.TOP)

# LOOP
frameroot.mainloop()

# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
