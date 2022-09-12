import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def Tarea():
    now = datetime.now().strftime(("%H:%M:%S"))
    logging.info(now + ': Aplicacion Iniciada')

    textos = []
    
    while(True):

        print('¿Que quieres hacer?\n')
        print('1) Ingresar texto\n')
        print('2) Buscar texto mas corto y largo\n')
        print('3) Imprimir un texto\n')
        print('4) Comparar textos\n')
        print('5) Salir de la aplicacion\n')
        print('Ingresa una opcion: ')
        
        x = input()
        
        if(x == '1'):
            now = datetime.now().strftime(("%H:%M:%S"))
            logging.info(now + ': Escogida opcion 1')

            while(True):
                print('Ingresa el texto: ')
                y = input()
                if isinstance(y, str):
                    textos.append(y)
                    now = datetime.now().strftime(("%H:%M:%S"))
                    logging.info(now + ': Texto ingresado en la pila')
                    break
                else:
                    logging.warning('El termino ingresado no es un string')
        
        elif(x=='2'):
            now = datetime.now().strftime(("%H:%M:%S"))
            logging.info(now + ': Escogida opcion 2')

            max = 0
            tmax = ""
            min = 99999
            tmin = ""

            if len(textos) >= 2:
                for i in range(len(textos)):
                    if len(textos[i]) >= max:
                        max = len(textos[i])
                        tmax = textos[i]
                    if len(textos[i]) <= min:
                        min = len(textos[i])
                        tmin = textos[i]
                now = datetime.now().strftime(("%H:%M:%S"))
                logging.info(now + ': Comparativa iniciada')
                print('El texto mas largo es: {}, con un largo de {} caracteres\n'.format(tmax, max))
                print('El texto mas corto es: {}, con un largo de {} caracteres\n'.format(tmin, min))

            else:
                logging.warning('La pila es muy corta')

        elif(x=='3'):
            now = datetime.now().strftime(("%H:%M:%S"))
            logging.info(now + ': Escogida opcion 3')

            if len(textos) == 0:
                logging.warning('La pila no tiene textos guardados')
                continue
            else:
                while(True):
                    print('Escoge la posicion del texto a imprimir, partiendo desde el cero: ')
                    try:
                        y = int(input())
                    except:
                        logging.warning('Input invalido\n')
                        continue
                    if y >= 0 and y < len(textos):
                        now = datetime.now().strftime(("%H:%M:%S"))
                        logging.info(now + ': Resultado printado en consola')
                        print(textos[y])
                        break
                    else:
                        logging.warning('Input invalido\n')

        elif(x=='4'):
            now = datetime.now().strftime(("%H:%M:%S"))
            logging.info(now + ': Escogida opcion 4')
            while(True):
                if len(textos) >=2:
                    print('Selecciona una posicion mediante un numero, partiendo desde el cero: ')
                    try:
                        a = int(input())
                        print('\n')
                        print('Selecciona otra posicion: ')
                        b = int(input())
                    except:
                        logging.warning('Inputs invalidos\n')
                        continue

                    now = datetime.now().strftime(("%H:%M:%S"))
                    logging.info(now + ': Comparativa iniciada')

                    if a >= 0 and a < len(textos) and b >= 0 and b < len(textos):
                        if textos[a] < textos[b]:
                            print('El segundo texto es mas largo')
                            break
                        elif textos[a] > textos[b]:
                            print('El primer texto es mas largo')
                            break
                        else:
                            print('Ambos textos miden lo mismo')
                            break
                    else:
                        logging.warning('Inputs invalidos\n')
                else:
                    logging.warning('La pila es muy corta')
                    break

        elif(x=='5'):
            now = datetime.now().strftime(("%H:%M:%S"))
            logging.info(now + ': Escogida opcion 5, aplicacion terminada')

            print('Hasta Luego')
            break
        else:
            logging.warning('Input invalido\n')

        print('\n')

Tarea()