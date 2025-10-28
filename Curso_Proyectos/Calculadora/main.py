import tkinter as tk


ventana1 = tk.Tk()
Entrada_numeros = tk.Entry(ventana1)
Entrada_numeros.pack(side=tk.TOP, fill="x")
Frame_grid = tk.Frame(ventana1)
Frame_grid.pack(side=tk.BOTTOM)
siete_boton = tk.Button(Frame_grid, text="7")
siete_boton.grid(row = 0 , column = 0)

ocho_boton = tk.Button(Frame_grid, text="8")
ocho_boton.grid(row = 0 , column = 1)

nueve_boton = tk.Button(Frame_grid, text="9")
nueve_boton.grid(row = 0 , column = 2)

division = tk.Button(Frame_grid, text="/")
division.grid(row = 0 , column = 3)

cuatro_boton = tk.Button(Frame_grid, text="4")
cuatro_boton.grid(row = 1 , column = 0)

cinco_boton = tk.Button(Frame_grid, text="5")
cinco_boton.grid(row = 1 , column = 1)

seis_boton = tk.Button(Frame_grid, text="6")
seis_boton.grid(row = 1 , column = 2)

mult = tk.Button(Frame_grid, text="*")
mult.grid(row = 1 , column = 3)

uno_boton = tk.Button(Frame_grid, text="1")
uno_boton.grid(row = 2 , column = 0)

dos_boton = tk.Button(Frame_grid, text="2")
dos_boton.grid(row = 2 , column = 1)

tres_boton = tk.Button(Frame_grid, text="3")
tres_boton.grid(row = 2 , column = 2)

suma = tk.Button(Frame_grid, text="+")
suma.grid(row = 2 , column = 3)
ventana1.mainloop()
