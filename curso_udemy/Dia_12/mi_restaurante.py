from tkinter import * 
import random 
import datetime 
from tkinter import filedialog, messagebox

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]



operador = ''


def click_boton(boton_presionado): 
    global operador 
    operador = operador + boton_presionado
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador

    resultado=str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador =""

def revisar_check():
    x = 0 
    for c in cuadros_comida: 
        if variables_comida[x].get() == 1: 
            cuadros_comida[x].config(state=NORMAL)

            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x +=1

    x = 0 
    for c in cuadros_bebida: 
        if variables_bebida[x].get() == 1: 
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x +=1

    x = 0 
    for c in cuadros_postre: 
        if variables_postre[x].get() == 1: 
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0,END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x +=1

def total(): 

    sub_total_comida = 0 
    p =0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p+=1
    


    sub_total_bebidas = 0 
    p =0
    for cantidad1 in texto_bebida:
        sub_total_bebidas = sub_total_bebidas + (float(cantidad1.get()) * precios_bebida[p])
        p+=1
    
    


    sub_total_postre = 0 
    p =0
    for cantidad2 in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad2.get()) * precios_postres[p])
        p+=1
    
    sub_total_ = sub_total_bebidas + sub_total_comida + sub_total_postre

    impuestos = sub_total_* 0.07

    total = sub_total_ + impuestos

    var_costo_comida.set(f'${round(sub_total_comida,2)}')
    var_costo_bebida.set(f'${round(sub_total_bebidas,2)}')
    var_costo_postre.set(f'${round(sub_total_postre,2)}')
    var_costo_subtotal.set(f'${round(sub_total_,2)}')
    var_costo_impuesto.set(f'${round(impuestos,2)}')
    var_costo_total.set(f'${round(total,2)}')





def recibo(): 
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}: {fecha.minute}'
    texto_recibo.insert(END, f'Datos: \t{num_recibo}\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 63 + '\n')

    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items \n')
    texto_recibo.insert(END, f'-' *75 +'\n')

    x = 0

    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{listas_comidas[x]}\t\t{comida.get()}\t' + 
                                f'$ {int(comida.get()) * precios_comida[x]}\n')
        
        x +=1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t' + 
                                f'$ {int(bebida.get()) * precios_bebida[x]}\n')
        
        x +=1




    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{listas_postres[x]}\t\t{postre.get()}\t' + 
                                f'$ {int(postre.get()) * precios_postres[x]}\n')
        
        x +=1


    texto_recibo.insert(END, f'-'* 75 + '\n')
    texto_recibo.insert(END, f' Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de los postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-'* 75 + '\n')
    texto_recibo.insert(END, f' Sub-total: \t\t\t{var_costo_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_costo_impuesto.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_costo_total.get()}\n')
    texto_recibo.insert(END, f'*' * 63 + '\n')
    texto_recibo.insert(END, "Lo esperamos pronto ! ")


def guardar():

    info_recibo   = texto_recibo.get(1.0, END)

    archivo = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo a sido guardado')

def reset(): 
    texto_recibo.delete(0.1,END)

    for texto in texto_comida:
        texto.set('0')

    for texto in texto_bebida:
        texto.set('0')

    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)

    for v in variables_bebida:
        v.set(0)

    for v in variables_postre:
        v.set(0)


    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_costo_impuesto.set('')
    var_costo_subtotal.set('')
    var_costo_total.set('')

#------------------------------------------------GUI------------------    
    
ventana = Tk()
##Configuracion ventana
ventana.geometry('1020x630+0+0')
ventana.resizable(0,0)
ventana.title('Mi restaurante - Sistema de facturación')
ventana.config(bg = 'burlywood')



# panel superior 
panel_superior = Frame(ventana, bd=1 , relief = FLAT)
panel_superior.pack(side="top")

#etiqueta titulo 
etiqueta_titulo = Label(
    panel_superior, 
    text="Sistema de Facturación",
    fg= "azure4",
    font= ("Dosis", 58),
    bg = "burlywood",
    justify="center",
    width = 27 
    )
etiqueta_titulo.grid(row = 0 , column = 0)
#hacer que la label se pueda centrar
panel_superior.columnconfigure(0, weight=1)
#panel izquierdo 
panel_izq = Frame(ventana, bd=1, relief= FLAT)
panel_izq.pack(side=LEFT)

#panel costos 
panel_costos = Frame(panel_izq,
                     bd=1,
                     relief=FLAT,
                     bg= "azure4",
                     padx=60
                     )
panel_costos.pack(side=BOTTOM)


panel_comidas = LabelFrame(panel_izq,
                           text='Comida',
                           font = ("Dosis", 19, "bold"),
                           bd=1,
                           relief=FLAT,
                           fg="azure4")
panel_comidas.pack(side=LEFT)



panel_bebidas = LabelFrame(panel_izq,
                           text='Bebidas',
                           font = ("Dosis", 19, "bold"),
                           bd=1,
                           relief=FLAT,
                           fg="azure4")
panel_bebidas.pack(side=LEFT)

#postres
panel_postres = LabelFrame(panel_izq,
                           text='Postres',
                           font = ("Dosis", 19, "bold"),
                           bd=1,
                           relief=FLAT,
                           fg="azure4")
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(ventana,
                           bd=1,
                           relief=FLAT,
                           )
panel_derecha.pack(side=RIGHT)


# panel calculadora

panel_calculadora = Frame(
    panel_derecha,
    bd=1,
    relief=FLAT,
    bg="burlywood"
    )
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(
    panel_derecha,
    bd=1,
    relief=FLAT,
    bg="burlywood"
    )
panel_recibo.pack()


# panel botones 

panel_botones = Frame(
    panel_derecha,
    bd=1,
    relief=FLAT,
    bg="burlywood"
    )
panel_botones.pack()

# lista de productos 

listas_comidas = ['pollo','cordero', 'salmon', 'merluza','pizza1','pizza2','pizza3','pizza4']

lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1','cerveza2']

listas_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse','pastel1', 'pastel2','pastel3']

#Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []


contador = 0
for comida in listas_comidas: 

    #crear check buttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(
        panel_comidas, 
        text = comida.title(), 
        font= ("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_comida[contador],
        command = revisar_check
        )
    
    comida.grid(row = contador, column=0, sticky = W)

#Crear cuadros de entrada 
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    cuadros_comida[contador] = Entry(
        panel_comidas,
        font = ("Dosis", 18, "bold"),
        width= 6,
        state= DISABLED,
        textvariable=texto_comida[contador]
        )
    
    cuadros_comida[contador].grid(row=contador,
                                  column = 1, 
                                  )
    contador +=1



    #Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []


contador = 0
for bebida in lista_bebidas: 
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(
        panel_bebidas,
        text = bebida.title(), 
        font= ("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_bebida[contador],
        command = revisar_check
        )
    
    bebida.grid(row = contador, column=0, sticky = W)

#Crear cuadros de entrada 
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(
        panel_bebidas,
        font = ("Dosis", 18, "bold"),
        width= 6,
        state= DISABLED,
        textvariable=texto_bebida[contador]
        )
    
    cuadros_bebida[contador].grid(row=contador,
                                  column = 1, 
                                  )

    contador +=1


variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0

for postre in listas_postres: 
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(
        panel_postres,
        text = postre.title(), 
        font= ("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_postre[contador],
        command = revisar_check
        )
    
    postre.grid(row = contador, column=0, sticky = W)


#Crear cuadros de entrada 
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set("0")
    cuadros_postre[contador] = Entry(
        panel_postres,
        font = ("Dosis", 18, "bold"),
        width= 6,
        state= DISABLED,
        textvariable=texto_postre[contador]
        )
    
    cuadros_postre[contador].grid(row=contador,
                                  column = 1, 
                                  )
    contador +=1


#Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_costo_subtotal = StringVar()
var_costo_impuesto = StringVar()
var_costo_total = StringVar()

etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                               font = ("Dosis", 12 ,"bold"),
                               bg= "azure4",
                               fg = "white"
                               )
etiqueta_costo_comida.grid(row=0, column=0 )



texto_costo_comida = Entry(panel_costos,
                           font = ("Dosis", 12 ,"bold"),
                           bd=1,
                           width = 10,
                           state = 'readonly',
                           textvariable=var_costo_comida
                           )
texto_costo_comida.grid(row = 0, column=1,padx=41)


etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                               font = ("Dosis", 12 ,"bold"),
                               bg= "azure4",
                               fg = "white"
                               )
etiqueta_costo_bebida.grid(row=1, column=0 )



texto_costo_bebida = Entry(panel_costos,
                           font = ("Dosis", 12 ,"bold"),
                           bd=1,
                           width = 10,
                           state = 'readonly',
                           textvariable=var_costo_bebida
                           )
texto_costo_bebida.grid(row = 1, column=1,padx=41)



etiqueta_costo_postres = Label(panel_costos,
                              text='Costo postre',
                               font = ("Dosis", 12 ,"bold"),
                               bg= "azure4",
                               fg = "white"
                               )
etiqueta_costo_postres.grid(row=2, column=0)



texto_costo_postres = Entry(panel_costos,
                           font = ("Dosis", 12 ,"bold"),
                           bd=1,
                           width = 10,
                           state = 'readonly',
                           textvariable=var_costo_postre
                           )
texto_costo_postres.grid(row = 2, column=1,padx=41)


etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                               font = ("Dosis", 12 ,"bold"),
                               bg= "azure4",
                               fg = "white"
                               )
etiqueta_subtotal.grid(row=0, column=2)



texto_subtotal = Entry(panel_costos,
                           font = ("Dosis", 12 ,"bold"),
                           bd=1,
                           width = 10,
                           state = 'readonly',
                           textvariable=var_costo_subtotal
                           )
texto_subtotal.grid(row = 0, column=3,padx=41)


etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                               font = ("Dosis", 12 ,"bold"),
                               bg= "azure4",
                               fg = "white"
                               )
etiqueta_impuestos.grid(row=1, column=2)



texto_impuestos = Entry(panel_costos,
                           font = ("Dosis", 12 ,"bold"),
                           bd=1,
                           width = 10,
                           state = 'readonly',
                           textvariable=var_costo_impuesto
                           )
texto_impuestos.grid(row = 1, column=3,padx=41)


etiqueta_total = Label(panel_costos,
                              text='Total',
                               font = ("Dosis", 12 ,"bold"),
                               bg= "azure4",
                               fg = "white"
                               )
etiqueta_total.grid(row=2, column=2 )



texto_total = Entry(panel_costos,
                           font = ("Dosis", 12 ,"bold"),
                           bd=1,
                           width = 10,
                           state = 'readonly',
                           textvariable=var_costo_total
                           )
texto_total.grid(row = 2, column=3,padx=41)



#botones 
botones = ["Total","Recibo","Guardar","Reset"]
botones_creados =[]
columnas = 0 
for boton in botones: 
    boton = Button(
        panel_botones,
        text = boton.title(),
        font = ("Dosis", 14, "bold"),
        fg = "white",
        bg = "azure4",
        bd = 1,
        width = 9
        )
    panel_botones.columnconfigure(columnas, weight=1,uniform="col")
    boton.grid(row = 0 , column=columnas)
    botones_creados.append(boton)

    columnas +=1
    
botones_creados[0].config(command=total)
botones_creados[1].config(command =recibo)
botones_creados[2].config(command =guardar)
botones_creados[3].config(command =reset)
# Area recibo 

texto_recibo = Text(panel_recibo,
                    font = ("Dosis", 12 ,"bold"),
                    bd=1,
                    width=42,
                    height=10
                    )
texto_recibo.grid(row=0,column=0)


# Calculadora 

visor_calculadora = Entry(panel_calculadora,
                          font =("Dosis", 16, "bold"),
                          width = 32,
                          bd =1, 
                          )
visor_calculadora.grid(row= 0,
                       column=0,
                       columnspan=4
                       )

botones_calculadora = ['7','8','9','+',
                       '4','5','6','-',
                       '1','2','3','*',
                       '=','C','0','/',]


botones_guardados = []
fila = 1
columna = 0

for c in range (5):
    panel_calculadora.columnconfigure(c, weight=1)

for boton in botones_calculadora: 
    boton = Button(
        panel_calculadora,
        text=boton,
        font= ("Dosis",16 ,"bold"),
        fg = "white",
        bd =1 ,
        bg ="azure4",
        width = 8
        )
    botones_guardados.append(boton)

    
    boton.grid(row = fila,
               column = columna
               )
    
    if columna == 3: 
        fila +=1 
    columna +=1

    if columna == 4:
        columna = 0 

for i in range(16):
    botones_guardados[i].config(command = lambda i = i : click_boton(botones_calculadora[i]))

botones_guardados[13].config (command = borrar)
botones_guardados[12].config (command = obtener_resultado)


ventana.mainloop()