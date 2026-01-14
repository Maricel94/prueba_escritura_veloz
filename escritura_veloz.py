import tkinter as tk # Creación de interfaz gráfica
import random # Seleccionar frase aleatoria
import time # Medición de tiempo (inicio - final)

# Creamos un alista con varias frases,
# El programa se encargará de elegir una al azar
frases = [
    'La programación es una herramienta poderosa',
    'Python es un lenguaje versátil y amigable',
    'La práctica constante mejra tus habilidades',
    'Escribe esta frase lo mas rápido que puedas'
]

# Variable global para el tiempo 
# Se actualiza cada vesz que aparece una frase nueva
tiempo_inicial = 0

# Actualiza cada cambio de frase
def nueva_frase():
    global frase_actual, tiempo_inicial
    frase_actual = random.choice(frases) # Elige una frase de la lista
    etiqueta_frase.config(text=frase_actual) #Muestra la frase elegida
    entrada.delete(0, tk.END) # Limpia el campo de texto
    resultado.config(text='') # Limpia el mensaje de resultado
    tiempo_inicial = time.time() # Inicia el tiempo cuando aparece la frase

def evaluar():
    tiempo_fin = time.time() # Tiempo actual cuandoo usuario presiona "Evaluar"
    texto_usuario = entrada.get() # Obtiene lo que escribió el usuario

    if texto_usuario == frase_actual:
        tiempo_total = round(tiempo_fin - tiempo_inicial,2)
        resultado.config(text=f'¡Correcto! Tiempo: {tiempo_total} segundos')
    else:
        resultado.config(text=f'Hay errores en la escritura. Inténtelo nuevamente')

#Ventana principal
ventana = tk.Tk() 
ventana.title('Prueba de Escritura Veloz')

#Instrucciones
etiqueta_instruccion = tk.Label(ventana, text="Presiona 'Nueva Frase' para comenzar")
etiqueta_instruccion.pack(pady=10)

#Empezar a escribir (empieza vacía)
etiqueta_frase = tk.Label(ventana, text='', font=('Arial',14))
etiqueta_frase.pack(pady=10)

#Campo donde el usuario escribe la frase
entrada = tk.Entry(ventana, width=60)
entrada.pack(pady=10)

#Boton generador de nueva frase
boton_frase = tk.Button(ventana, text='Nurva frase', command=nueva_frase)
boton_frase.pack(pady=5)

#Boton para evaluar lo escrito
boton_evaluar = tk.Button(ventana, text='Evaluar', command=evaluar)
boton_evaluar.pack(pady=5)

#Etiqueta donde se muestra el resultado
resultado = tk.Label(ventana,text='', font=('Arial',12))
resultado.pack(pady=10)

ventana.mainloop() #Mantenemos la ventana abierta









