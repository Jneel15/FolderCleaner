from tkinter import *
import os


########################################################

folders = ("Downloads", "Documents", "Pictures", "Videos")

# Function to determine which option was selected in the List Box.

def fldrSel(event):
     
    sel = fldrLb.curselection()
    for idx in sel:
        if idx == 0:
            confFldrCleanDl()
        elif idx == 1:
            confFldrCleanDoc()
        elif idx == 2:
            confFldrCleanPic()
        elif idx == 3:
            confFldrCleanVid()

# Function to close the program window using the "Exit" button.

def closeWindowConf(event):
    def closeWindowNo(event):
        confWindow.destroy()
    
    def closeWindowYes(event):
        confWindow.destroy()
        window.destroy()
    
    confWindow = Tk()
    confWindow.geometry('250x100+10+10')
    confWindow.title('Close Confirmation')
    confLbl = Label(confWindow, text = "Are You Sure You Would Like To Close?", fg = 'Black')
    confLbl.place(x = 20, y = 10)
    yBtn = Button(confWindow, text = "YES", bg = "White", width = 5)
    yBtn.place(x = 55, y = 45)
    nBtn = Button(confWindow, text = "NO", bg = "White", width = 5)
    nBtn.place(x = 150, y = 45)
    yBtn.bind('<Button-1>', closeWindowYes)
    nBtn.bind('<Button-1>', closeWindowNo)

# Function to open Download Cleaning confirmation window and clean the downloads folder.

def confFldrCleanDl():
    def closeWindowNo(event):
        confWindow.destroy()
        
    def dlCln(event):    
        folder_location = 'C:\\Users\\joshn\\Downloads\\demo'
        os.chdir(folder_location)
        list_of_files = os.listdir()
        foldercontent = [content for content in list_of_files]
        for i in foldercontent:
            os.remove(str(i))
        confWindow.destroy()
        
    confWindow = Tk()
    confWindow.geometry('250x100+10+10')
    confWindow.title('Clean Confirmation')
    confLbl = Label(confWindow, text = "This Will Remove All Files In Downloads", fg = 'Black')
    confLbl.place(x = 20, y = 10)
    yBtn = Button(confWindow, text = "YES", bg = "White", width = 5)
    yBtn.place(x = 55, y = 45)
    nBtn = Button(confWindow, text = "NO", bg = "White", width = 5)
    nBtn.place(x = 150, y = 45)
    yBtn.bind('<Button-1>', dlCln)
    nBtn.bind('<Button-1>', closeWindowNo)

# Function to open Document Cleaning confirmation window and clean the documents folder.
    
def confFldrCleanDoc():
    def closeWindowNo(event):
        confWindow.destroy()
        
    def docCln(event):    
        folder_location = 'C:\\Users\\joshn\\Documents\\demo'
        os.chdir(folder_location)
        list_of_files = os.listdir()
        foldercontent = [content for content in list_of_files]
        for i in foldercontent:
            os.remove(str(i))    
        confWindow.destroy()
        
    confWindow = Tk()
    confWindow.geometry('250x100+10+10')
    confWindow.title('Clean Confirmation')
    confLbl = Label(confWindow, text = "This Will Remove All Files In Documents", fg = 'Black')
    confLbl.place(x = 20, y = 10)
    yBtn = Button(confWindow, text = "YES", bg = "White", width = 5)
    yBtn.place(x = 55, y = 45)
    nBtn = Button(confWindow, text = "NO", bg = "White", width = 5)
    nBtn.place(x = 150, y = 45)
    yBtn.bind('<Button-1>', docCln)
    nBtn.bind('<Button-1>', closeWindowNo)  
    
# Function to open Picture Cleaning confirmation window and clean the pictures folder.

def confFldrCleanPic():
    def closeWindowNo(event):
        confWindow.destroy()
        
    def picCln(event):    
        folder_location = 'C:\\Users\\joshn\\Pictures\\demo'
        os.chdir(folder_location)
        list_of_files = os.listdir()
        foldercontent = [content for content in list_of_files]
        for i in foldercontent:
            os.remove(str(i))    
        confWindow.destroy()
        
    confWindow = Tk()
    confWindow.geometry('250x100+10+10')
    confWindow.title('Clean Confirmation')
    confLbl = Label(confWindow, text = "This Will Remove All Files In Pictures", fg = 'Black')
    confLbl.place(x = 20, y = 10)
    yBtn = Button(confWindow, text = "YES", bg = "White", width = 5)
    yBtn.place(x = 55, y = 45)
    nBtn = Button(confWindow, text = "NO", bg = "White", width = 5)
    nBtn.place(x = 150, y = 45)
    yBtn.bind('<Button-1>', picCln)
    nBtn.bind('<Button-1>', closeWindowNo) 
    
# Function to open Video Cleaning confirmation window and clean the videos folder.    
    
def confFldrCleanVid():
    def closeWindowNo(event):
        confWindow.destroy()
        
    def vidCln(event):    
        folder_location = 'C:\\Users\\joshn\\Videos\\demo'
        os.chdir(folder_location)
        list_of_files = os.listdir()
        foldercontent = [content for content in list_of_files]
        for i in foldercontent:
            os.remove(str(i))    
        confWindow.destroy()
        
    confWindow = Tk()
    confWindow.geometry('250x100+10+10')
    confWindow.title('Clean Confirmation')
    confLbl = Label(confWindow, text = "This Will Remove All Files In Videos", fg = 'Black')
    confLbl.place(x = 20, y = 10)
    yBtn = Button(confWindow, text = "YES", bg = "White", width = 5)
    yBtn.place(x = 55, y = 45)
    nBtn = Button(confWindow, text = "NO", bg = "White", width = 5)
    nBtn.place(x = 150, y = 45)
    yBtn.bind('<Button-1>', vidCln)
    nBtn.bind('<Button-1>', closeWindowNo)
    
########################################################

# Window
window = Tk()
window.title("Folder Cleaner")
window.geometry("300x300+10+10")

# Exit button
mClose = Button(window, text = "Exit", fg = "Black", bg = "White", width = 30,)
mClose.place(x=40, y=240)
mClose.bind("<Button-1>", closeWindowConf)


# Username Label
unLbl = Label(window, text = "Username:", fg = "Black")
unLbl.place(x = 50, y = 50)

# Username Text Field
unTF = Entry(window)
unTF.place(x = 115, y = 50)

# Folder Listbox
fldrLb = Listbox(window, height = 5, width = 32, selectmode = "multiple")
fldrLb.place(x = 50, y = 85)
for fldr in folders:
    fldrLb.insert(END, fldr)
fldrLb.bind('<Double-1>', fldrSel)

# Info Label
inLbl = Label(window, text = "Double-Click folder that needs to be Cleaned", fg = "Black")
inLbl.place(x = 30, y = 185)

   
########################################################    


########################################################

window.mainloop()
