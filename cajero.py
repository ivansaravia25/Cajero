from queue import Empty
from tkinter import *
from tkinter import messageboxfrom 
from tkinter.ttk import Combobox

def calcular():
    try:
        precio = float(caja1.get())
        cantidad = int(caja2.get())
        subtotal = precio * cantidad
        com = cambo.get()
        descuentoporcentaje = Empty
        calculardescuento = Empty
        total = Empty

        if com == "":
            messagebox.showerror("Cajero","Elije un metodo de pago")
        elif com == "Tarjeta Credito o debito":
            descuentoporcentaje = "20%"
            calculardescuento = subtotal*0.20
            total = subtotal-calculardescuento
            messagebox.showinfo("Cajero",f"La cantidad de Producto es: {cantidad}, El Precio del producto es: ${precio}, El metodo de pago es: {com}, El descuento es: {descuentoporcentaje}, El total es: ${total}")
        elif com == "Efectivo":
            if subtotal < 20:
                descuentoporcentaje = "sin descuento"
                total = subtotal
                messagebox.showinfo("Cajero",f"La cantidad de Producto es: {cantidad}, El Precio del producto es: ${precio}, El metodo de pago es: {com}, El descuento es: {descuentoporcentaje}, El total es: ${total}")
            else:
                descuentoporcentaje = "10%"
                calculardescuento = subtotal*0.10
                total = subtotal-calculardescuento
                messagebox.showinfo("Cajero",f"La cantidad de Producto es: {cantidad}, El Precio del producto es: ${precio}, El metodo de pago es: {com}, El descuento es: {descuentoporcentaje}, El total es: ${total}")
           
    except:
        messagebox.showerror("Cajero","Ingrese los datos que se le solicitan")


def salir():
    mensaje = messagebox.askquestion("Operaciones Matematicas","Quieres salir?")
    if mensaje == "yes":
        interfaz.destroy()
    else:
        pass

interfaz = Tk()
interfaz.title("Cajero")
interfaz.resizable(0,0)
interfaz.configure(background='dark turquoise')

ancho_ventana = 400
alto_ventana = 300

x_ventana = interfaz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = interfaz.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
interfaz.geometry(posicion)
txt0 = Label(interfaz,text="CAJERO ",bg='Olive',font='Coolvetica 15 bold')
txt3 = Label(interfaz,text="Metodo de Pago: ",bg='Olive',font='Coolvetica 10 bold')
txt1 = Label(interfaz,text="Ingrese el precio del producto: ",bg='Olive',font='Coolvetica 9 bold')
caja1 = Entry(interfaz)
txt2 = Label(interfaz,text="Ingrese la cantidad de producto: ",bg='Olive',font='Coolvetica 9 bold')
caja2 = Entry(interfaz)
cambo = Combobox(interfaz,state="readonly")
cambo['values']=("Efectivo","Tarjeta Credito o debito")
btn1 = Button(interfaz,text ="Comprar",command=calcular,bg="red",font='Coolvetica 10 bold',fg="Silver")
btn2 = Button(interfaz,text ="Cerrar",command=salir,bg="red",font='Coolvetica 10 bold',fg="Silver")

txt0.pack()
txt1.place(x = 40,y = 40)
caja1.place(x = 220,y = 40,width = 150,height = 20)
txt2.place(x = 30,y = 70)
caja2.place(x = 220,y = 70,width = 150,height = 20)
cambo.place(x = 130,y = 140,width = 150)
txt3.place(x= 150,y= 120)
btn1.place(x = 50,y = 180,width = 150,height = 40)
btn2.place(x = 220,y = 180,width = 150,height = 40)
interfaz.mainloop()
