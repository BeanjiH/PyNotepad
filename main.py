from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Note App")
appIcon = PhotoImage(file="Icons/notepad_icon.png")
root.iconphoto(False, appIcon)
root.minsize(width=400,height=400)

def openFile():
    target_file = filedialog.askopenfile(title="Select File", filetypes=(("txt files", "*.txt"),("All files", "*")))
    target_contents = target_file.read()
    text.delete("1.0", END)
    text.insert("1.0",target_contents)

def saveNote():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", "end-1c"))
        print("File saved.")


menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label="Open",command=openFile)
file_menu.add_command(label="Save",command=saveNote)
file_menu.add_separator()
file_menu.add_command(label="Quit",command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu,underline=0)


text = Text(root)
text.grid(row=1, column=0, sticky="nsew")

button = Button(root, text="Save Note",command=saveNote)
button.grid(row=2,column=0,columnspan=2,pady=5)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()