import pyttsx3
import speech_recognition as sr 
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro microfono y devolver el audio como texto 

def transformar_audio_a_texto():
    # almacenar recognizer en variable 

    r = sr.Recognizer()

    # configurar el microfono 
    with sr.Microphone() as origen: 
        # tiempo de espera 
        r.pause_threshold = 0.8 

        # informar que comenzó la grabación 

        print(' ya puedes hablar')

        # Guardar lo que escuche como audio

        audio = r.listen(origen)

        try: 
            #buscar en google lo que escucho
            pedido = r.recognize_google (audio, language = "es-mx")

            # prueba de que pudo ingresar 

            print( "Dijiste:"+ pedido)

            # devolver pedido 
            return pedido 
        
        # en caso de que no funcione
        except sr.UnknownValueError: 
            # no jalo 
            print('Ups , no entendi')

            # devolver error 
            return 'sigo esperando'
        
        # en caso de no resolver el pedido

        except sr.RequestError: 
                    # no jalo 
            print('Ups , no hay servicio')

            # devolver error
            return 'sigo esperando'
        
        except:
                                # no jalo 
            print('Ups , Algo salio mal')

            # devolver error
            return 'sigo esperando'
        

#funcion para que el asistente pueda ser escuchado 

def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()

    # pronunciar mensaje 
    engine.say(mensaje)
    engine.runAndWait()


# informar dia de la semana 

def pedir_dia():
    # crear variable con datos de hoy 
    dia = datetime.date.today()
    dia_semana =  dia.weekday()
    # diccionario 
    semana = {0:'Lunes',
              1:'Martes',
              2:'Miércoles',
              3:'Jueves',
              4:'Viernes',
              5:'Sábado',
              6:'Domingo',
             }
    
    #decir el dia de la semana 
    hablar(f'Hoy es {semana[dia_semana]}')

# informar hora 
def pedir_hora():
    # crear una variable con datos de hora 
    hora=datetime.datetime.now().hour
    minutos = datetime.datetime.now().minute
    hablar(f'Son las {hora} y {minutos}')

def saludo_inicial():
    hora = datetime.datetime.now()

    if hora.hour < 6 or  hora.hour > 20:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 13: 
        momento = 'Buen día'
    else: 
        momento = 'Buenas tardes'

    
    hablar(f"Que pedo papi, {momento} ,que pitote. Yo soy Churrolin AI tu asistente personal, que vamos a hacer hoy?")


def pedir_cosas():
    #activar saludo inicial
    saludo_inicial() 
    # variable de corte 
    comenzar = True 
    while comenzar:

        #activar el micro y guardar el pedido en una string 

        pedido = transformar_audio_a_texto().lower()


        if 'abrir youtube' in pedido: 
            hablar ('Claro que si papi')
            webbrowser.open('https://www.youtube.com')
            continue
        elif  'abrir navegador' in pedido: 
            hablar('San simonson')
            webbrowser.open('https://www.google.com')
            continue
        elif 'que día es hoy' in pedido: 
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('buscando en wikipedia')
            pedido = pedido.replace('buscar en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('buscando en internet')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue

        elif 'reproducir' in pedido: 
            hablar('Comenzando reproducir')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:

            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL',
                       }
            try: 
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['RegularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except: 
                hablar('Perdon pero no la he encontrado')
                continue

        elif 'adiós' in pedido: 
            hablar('Camara nos vemos papi')
            break

pedir_cosas()



