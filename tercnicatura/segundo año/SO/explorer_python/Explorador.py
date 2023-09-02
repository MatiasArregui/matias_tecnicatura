#Explorador.py
import os
import shutil
import tkinter as tk
from tkinter import StringVar, Variable, ttk, messagebox
from tkinter.constants import S
from ttkbootstrap import Style
from tkinter.filedialog import askdirectory
from centrar_ventana import centrar
import glob
import time

class Application(ttk.Frame):

    def __init__(self, main_window):
        #Inicializa la ventana
        super().__init__(main_window)
        main_window.title('Copiar archivos')

        self.frame1 = ttk.Frame(self)
        self.frame1.grid(padx=5, pady=5, row=0, column=0)

        self.button1 = ttk.Button(self.frame1, command=self.getSource, text='Origen')
        self.button1.grid(padx=5, pady=5, row=0, column=0)

        self.source_dir = tk.StringVar()
        self.source_dir.set(os.getcwd())
        self.entry1 = ttk.Entry(self.frame1, textvariable=self.source_dir, width=40)
        self.entry1.grid(padx=5, pady=5, row=0, column=1)

        self.frame2 = ttk.Frame(self)
        self.frame2.grid(padx=5, pady=5, row=0, column=1)

        self.button2 = ttk.Button(self.frame2, command=self.getTarget, text='Destino')
        self.button2.grid(padx=5, pady=5, row=0, column=0)

        self.target_dir = tk.StringVar()
        self.target_dir.set(os.getcwd())
        self.entry2 = ttk.Entry(self.frame2, textvariable=self.target_dir, width=40)
        self.entry2.grid(padx=5, pady=5, row=0, column=1)

        self.frame3 = ttk.Frame(self)
        self.frame3.grid(padx=5, pady=5, row=1, column=0, columnspan=2)

        self.text1 = tk.Text(self.frame3, height=8, width=45)
        self.text1.insert(tk.INSERT, '*.*')
        self.text1.grid(padx=5, pady=0, row=0, column=0)

        self.scroll1 = ttk.Scrollbar(self.frame3, command=self.text1.yview)
        self.text1.configure(yscrollcommand=self.scroll1.set)
        self.scroll1.grid(row=0, column=0, sticky='nse')

        self.button3 = ttk.Button(self.frame3, command=self.myFilter, text='Filtrar')
        self.button3.grid(padx=5, pady=0, row=0, column=2)

        self.text2 = tk.Text(self.frame3, height=8, width=45)
        self.text2.insert(tk.INSERT, '*.*')
        self.text2.grid(padx=5, pady=0, row=0, column=3)

        self.scroll2 = ttk.Scrollbar(self.frame3, command=self.text2.yview)
        self.text2.configure(yscrollcommand=self.scroll1.set)
        self.scroll2.grid(row=0, column=3, sticky='nse')

        self.label1 = ttk.Label(self, text='Origen')
        self.label1.grid(padx=0, pady=0, row=3, column=0)

        self.label3 = ttk.Label(self, text='Destino')
        self.label3.grid(padx=0, pady=0, row=3, column=1)

        self.source_files = StringVar()
        self.listbox1 = tk.Listbox(self, listvariable=self.source_files, width=50, height=20)
        self.listbox1.grid(padx=5, pady=5, row=4, column=0)
        listatemp = os.listdir(self.source_dir.get())
        self.source_files.set(' '.join(listatemp))

        self.target_files = StringVar()
        self.listbox2 = tk.Listbox(self, listvariable=self.target_files, width=50, height=20)
        self.listbox2.grid(padx=5, pady=5, row=4, column=1)
        listatemp = os.listdir(self.target_dir.get())
        self.target_files.set([x for x in listatemp])

        self.frame5 = ttk.Frame(self)
        self.frame5.grid(padx=5, pady=5, row=5, columnspan=2)

        self.progressbar1 = ttk.Progressbar(self.frame5, orient='horizontal', mode='determinate', length=660, style='Striped.Horizontal.TProgressbar')
        self.progressbar1.grid(padx=5, pady=5, row=5, column=0)

        self.frame6 = ttk.Frame(self)
        self.frame6.grid(padx=5, pady=5, row=6, columnspan=2)

        self.button4 = ttk.Button(self.frame6, command=self.startCopy, text='Iniciar copia')
        self.button4.grid(padx=5, pady=5, row=6, column=0)

        self.button5 = ttk.Button(self.frame6, command=self.cancelCopy, text='cancelar copia')
        self.button5.grid(padx=5, pady=5, row=6, column=1)

        self.pack()

    def myFilter(self):
        # Obtiene la lista de archivos de la carpeta origen.
        listatemp = os.listdir(self.source_dir.get())
        self.source_files.set([x for x in listatemp])
        print('Lista de archivos', listatemp)

        # Obtiene la lista de patrones comodines
        filtro = self.text1.get(1.0, 'end-1c')
        filtro = filtro.split('\n')
        print('lista de filtro', filtro)

        # Si el filtro es vacio o igual *.* sale sin hacer nada.
        if '*.*' in filtro or '' in filtro:
            return

        # Obtiene la lista de archivos filtrados.
        nuevalista = [glob.glob(x) for x in filtro]
        print('lista de archivos filtrados', nuevalista)

        # Obtiene una lista aplanada de archivos filtrados.
        flat_list = [item for sublist in nuevalista for item in sublist if item != '']
        print('lista de archivos aplanada', flat_list)

        self.source_files.set(flat_list)

    def getSource(self):
        #Obtiene el directorio de origen en una variable temporal para que en caso
        # de elegir ningún directorio no se borre el Entry
        temp_dir = askdirectory(initialdir=str(self.source_dir)).replace('/', '\\')
        #Verifica que la ruta sea un directorio válido
        if os.path.isdir(temp_dir):
            self.source_dir.set(temp_dir)
            self.source_files.set(os.listdir(temp_dir))
            self.listbox1.delete(0, tk.END)

            for x in self.source_files.get():
                self.listbox1.insert(0, x)

    def getTarget(self):
        #Obtiene el directorio de destino en una variable temporal para que en caso
        # de elegir ningún directorio no se borre el Entry
        temp_dir = askdirectory(initialdir=self.target_dir).replace('/', '\\')
        #Verifica que la ruta sea un directorio válido
        if os.path.isdir(temp_dir):
            self.target_dir.set(temp_dir)
            self.target_files.set(os.listdir(temp_dir))
            self.listbox2.delete(0, tk.END)

            for x in self.target_files.get():
                self.listbox2.insert(0, x)

    def startCopy(self):
        if self.source_dir.get() == self.target_dir.get():
            messagebox.showinfo('Información', 'La carpeta origen y destino no pueden ser la misma')
        else:
            # Deshabiita el button de iniciar copia.
            self.button4.configure(state='disabled')

            tupla = eval(self.source_files.get())
            maxValue = len(tupla)
            self.progressbar1['value'] = 0
            self.progressbar1['maximum'] = maxValue

            self.progressbar1.start()

            for x in range(maxValue):
                self.progressbar1['value'] = x
                self.progressbar1.update()
                desde = self.source_dir.get() + '\\' + tupla[x]
                hacia = self.target_dir.get() + '\\' + tupla[x]
                # Está faltando copiar la metadata y advertir o copiar archivos y carpetas existentes.
                # Si es una carpeta utilizar treecopy.
                if os.path.isdir(desde) == True:
                    shutil.copytree(desde, hacia, dirs_exist_ok=True)
                else:
                    shutil.copyfile(desde, hacia)
                time.sleep(0.3)

            self.progressbar1.stop()
            self.button4.configure(state='normal')

    def cancelCopy(self):
        messagebox.showinfo(message='Copia cancelada', title='Cancelado')


if __name__ == '__main__':
    root = tk.Tk()
    Style = Style('darkly')
    root.geometry(centrar(ancho=800, alto=630, app=root))
    root.resizable(0,0)
    app = Application(root)
    root.mainloop()
