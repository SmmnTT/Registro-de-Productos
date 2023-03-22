
from tkinter import * #Importar libreria
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter as tk

#Ventana
raiz= Tk()
raiz.title("Registro de productos")
raiz.geometry("600x700")

#Variables
nameEntry=StringVar()
nameSKU=StringVar()

dpto=StringVar()
idioma=StringVar()
Proveedor=StringVar()

#Frame
frame=Frame(raiz,bg="#707070")
frame.pack(fill="both",expand=1)



#imagen
im=Image.open("gato.jpg")
imRe=im.resize((200,150))
imagen=ImageTk.PhotoImage(imRe)

imlabel=Label(frame,image=imagen)
imlabel.place(relx=0.3,rely=0.2)



def Registrar():
    print(f'''Producto registrado
          Producto: {nameEntry.get()} 
          SKU: {nameSKU.get()}
          Departamento: {dpto.get()}
          Proveedor: {Proveedor.get()}
          Idioma: {idioma.get()}
            ''')
    
    

#Etiqueta Registro
EtiquetaRegistro=Label(frame,text="Registro",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.4 ,rely=.05)

#Etiqueta Productos
EtiquetaProductos=Label(frame,text="Productos",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.375 ,rely=.125)

#Etiqueta Producto
labelProducto=Label(frame,text="Producto: ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.1 ,rely=.45)
#Entry Producto
ProductoEntry=Entry(frame,
                  font=("Roboto",18,"bold"),
                  textvariable=nameEntry).place(relx=0.4,rely=0.45)

#Etiqueta SKU
labelSKU=Label(frame,text="SKU: ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.1 ,rely=.525)
#Entry SKU
SKUEntry=Entry(frame,
                  font=("Roboto",18,"bold"),
                  textvariable=nameSKU).place(relx=0.4,rely=0.525)

#Etiqueta Departamento
labeelDPTO=Label(frame,text="Departamento: ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.1 ,rely=.6)


#Etiqueta Proveedor
labelProveedor=Label(frame,text="Proveedor:",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.1,rely=0.72)

Proveedor = ttk.Combobox(frame,state="readonly")
Proveedor.place(relx=.4,rely=.7375)
Proveedor["values"]=("Bimbo","Mi Casa","Tesla")

#Etiqueta Idioma
labelIdioma=Label(frame,text="Idioma:",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.1,rely=.775)





#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                         B O T O N E S 


#Boton
boton=Button(frame,text="Registrar",
             font=("Roboto",20,"bold"),
             width=15,
             height=1,
             command=Registrar,
             ).place(relx=.3,rely=.9)


#Botones de seleccion de dpt
btn_a=Radiobutton(frame,text="A",
                  font=("Roboto",20,"bold"),
                  bg="#707070",
                  value="A",
                  variable=dpto)
btn_a.place(relx=.3,rely=.65)

#Boton dpto B
btn_a=Radiobutton(frame,text="B",
                  font=("Roboto",20,"bold"),
                  bg="#707070",
                  value="B",
                  variable=dpto)
btn_a.place(relx=.45,rely=.65)

#Boton dpto C
btn_a=Radiobutton(frame,text="C",
                  font=("Roboto",20,"bold"),
                  bg="#707070",
                  value="C",
                  variable=dpto)
btn_a.place(relx=.6,rely=.65)



#Boton Idioma EN
btn_a=Radiobutton(frame,text="EN",
                  font=("Roboto",20,"bold"),
                  bg="#707070",
                  value="EN",
                  variable=idioma)
btn_a.place(relx=.3,rely=.8)

#Boton Idioma SP
btn_a=Radiobutton(frame,text="SP",
                  font=("Roboto",20,"bold"),
                  bg="#707070",
                  value="SP",
                  variable=idioma)
btn_a.place(relx=.5,rely=.8)





raiz.mainloop()


