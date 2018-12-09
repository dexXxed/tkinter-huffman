from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from alg import algorithm


def openfile():
    try:
        filename = askopenfilename(parent=root)
        print(filename)
        out, d1, d2, dec = algorithm(filename)
        messagebox.showinfo("OK! Файл был сжат!", "Путь к сжатому файлу: {}\nВремя сжатия: {} секунд".format(str(out), str(d1)))
        messagebox.showinfo("OK! Файл был восстановлен!",
                            "Путь к восстановленному файлу: {}\nВремя восстановления: {} секунд".format(str(dec), str(d1)))
    except Exception as e:
        messagebox.showinfo("Неккоректный ввод", "Пожалуйста, выберете корректно имя файла!")


root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()