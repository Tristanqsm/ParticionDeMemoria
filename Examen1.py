import math
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import simpledialog, messagebox, Toplevel

class MemoriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Gestión de Memoria")
        self.root.geometry("500x400")
        self.memoria = 2048
        self.memoriaInicial = self.memoria
        self.particiones = []

    #LOGOOOOO
        ttk.Label(root, text="Bienvenido a", font=("Helvetica", 20, "bold"), bootstyle=PRIMARY).pack(pady=(10, 5))
        ttk.Label(root, text="TristanOS", font=("Helvetica", 20, "bold"), bootstyle=PRIMARY).pack(pady=(10, 5))

    #MORSTRAR LA MEMORIA TOTAL
        self.label = ttk.Label(root, text=f"Memoria Total: {self.memoria} KB", font=("Helvetica", 14))
        self.label.pack(pady=10)

    #LOS BOTONES DE LAS FUNCIONES
        ttk.Button(root, text="Memoria Estática", command=self.memoria_estatica, bootstyle=INFO).pack(pady=5)
        ttk.Button(root, text="Memoria Dinámica", command=self.memoria_dinamica, bootstyle=SUCCESS).pack(pady=5)
        ttk.Button(root, text="Particionamiento", command=self.abrir_particionamiento, bootstyle=PRIMARY).pack(pady=5)
        ttk.Button(root, text="Segmentación", command=self.segmentacion, bootstyle=WARNING).pack(pady=5)
        ttk.Button(root, text="Reiniciar Memoria", command=self.reiniciar, bootstyle=SECONDARY).pack(pady=5)
        ttk.Button(root, text="Salir", command=root.quit, bootstyle=DANGER).pack(pady=10)

    def actualizar_memoria(self):
        self.label.config(text=f"Memoria Total: {self.memoria} KB")

    def memoria_estatica(self):
        messagebox.showinfo("Memoria Estática", f"Memoria Estática de tamaño {self.memoria} KB")

    def memoria_dinamica(self):
        proc = simpledialog.askinteger("Proceso", "Ingrese el tamaño del proceso:")
        if proc and proc <= self.memoria:
            self.memoria -= proc
            self.actualizar_memoria()
            while True:
                agregar = messagebox.askyesno("Agregar", "¿Desea agregar otro proceso?")
                if agregar:
                    proc = simpledialog.askinteger("Proceso", "Ingrese el tamaño del proceso:")
                    if proc and proc <= self.memoria:
                        self.memoria -= proc
                        self.actualizar_memoria()
                    else:
                        messagebox.showerror("Memoria", "Memoria Insuficiente. No se puede agregar el proceso.")
                        break
                else:
                    break
        else:
            messagebox.showerror("Memoria", "Memoria Insuficiente. No se puede agregar el proceso.")

    def abrir_particionamiento(self):
        self.ventana_particionamiento = Toplevel(self.root)
        self.ventana_particionamiento.title("Particiones")
        self.ventana_particionamiento.geometry("200x200")

        num = simpledialog.askinteger("Particiones", "Ingresa el número de particiones:", parent=self.ventana_particionamiento)
        if num:
            self.particiones.clear()
            for i in range(num):
                tam = simpledialog.askinteger("Partición", f"Tamaño de partición {i+1}:", parent=self.ventana_particionamiento)
                if tam and sum(self.particiones) + tam <= self.memoria:
                    self.particiones.append(tam)
                else:
                    messagebox.showerror("Memoria", "Memoria Insuficiente. Cambia el tamaño de los procesos.", parent=self.ventana_particionamiento)
                    self.ventana_particionamiento.destroy()
                    return
            
            self.memoria -= sum(self.particiones)
            self.actualizar_memoria()

            ttk.Button(self.ventana_particionamiento, text="Mostrar lista", command=self.mostrar_lista, bootstyle=INFO).pack(pady=2)
            ttk.Button(self.ventana_particionamiento, text="Editar partición", command=self.editar_particion, bootstyle=INFO).pack(pady=2)
            ttk.Button(self.ventana_particionamiento, text="Agregar partición", command=self.agregar_particion, bootstyle=INFO).pack(pady=2)
            ttk.Button(self.ventana_particionamiento, text="Calcular espacio", command=self.calcular_espacio, bootstyle=INFO).pack(pady=2)
            ttk.Button(self.ventana_particionamiento, text="Salir", command=self.ventana_particionamiento.destroy, bootstyle=DANGER).pack(pady=10)

    def mostrar_lista(self):
        messagebox.showinfo("Lista", f"Particiones: {self.particiones}")

    def editar_particion(self):
        idx = simpledialog.askinteger("Editar", "Índice de partición a editar:")
        if 0 <= idx-1 < len(self.particiones):
            nuevo = simpledialog.askinteger("Nuevo", "Nuevo tamaño:")
            self.memoria = self.memoria + self.particiones[idx-1] - nuevo
            if nuevo and self.memoria >= 0:
                #self.memoria = self.memoria + self.particiones[idx-1] - nuevo
                self.particiones[idx-1] = nuevo
                self.actualizar_memoria()
            else:
                messagebox.showerror("Error", "Memoria insuficiente para el nuevo tamaño.")
        else:
            messagebox.showerror("Error", "Índice inválido")

    def agregar_particion(self):
        nuevo = simpledialog.askinteger("Agregar", "Tamaño de nueva partición:")
        if nuevo and sum(self.particiones) + nuevo <= self.memoria:
            self.particiones.append(nuevo)
        else:
            messagebox.showerror("Error", "No se puede agregar partición. Memoria insuficiente.")

    def calcular_espacio(self):
        suma = sum(self.particiones)
        messagebox.showinfo("Espacio", f"Particiones: {self.particiones}\nTotal: {suma} KB")

    def segmentacion(self):
        proc = simpledialog.askinteger("Segmentación", "Tamaño del proceso:")
        if proc:
            if self.memoria >= proc:
                segm = math.floor(proc / 3)
                info = (f"Segmentación en 3 partes\n"
                        f"Data Segment: {segm} KB\n"
                        f"Code Segment: {segm} KB\n"
                        f"Stack Segment: {segm} KB")
                messagebox.showinfo("Segmentación", info)
                self.memoria -= proc
                self.actualizar_memoria()
            else:
                messagebox.showerror("Error", "Memoria insuficiente")

    def reiniciar(self):
        self.memoria = self.memoriaInicial
        messagebox.showinfo("Reinicio", f"Memoria Estática de tamaño {self.memoria} KB")
        self.actualizar_memoria()


if __name__ == "__main__":
    app = ttk.Window(themename="darkly")
    MemoriaApp(app)
    app.mainloop()
