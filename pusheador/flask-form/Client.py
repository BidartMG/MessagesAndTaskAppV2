import time
import requests
import datetime  #


class Client:
    """
    La class Client posee dos atributos numero y estado, este último no se usa en este momento pero toma relevancia si
    se pretende tener un listado de los emisores y su estado
    Un cambio posible es agregar la estructura lista que guarde los mensajes asignados para luego seleccionar uno random,
    otra estructura posible es la que guardaría los numeros telefónicos que no existen para eliminarlos de la lista
    """

    def __init__(self, numero):
        self.numero_linea = numero
        self.estado = "ESPERANDO"

    def cambiar_estado(self, nuevo_estado):
        """
            Setter que cambia el estado al objeto, se inicializa en ESPERANDO.
        """
        self.estado = nuevo_estado

    def get_linea(self):
        return self.numero_linea

    def get_json_cliente(self):
        return {"SOY": self.numero_linea}

    def get_estado_cliente(self):  # VUELA VUELA
        return self.estado

    def conectar_x_get(self, url):  # Es a modo de prueba de conexión
        response = requests.get(url)
        print(response.status_code)
        return response.status_code

    # TODO Falta resolver como responde si no encuentra coincidencias para él en la lista. Camino feliz resuelto
    def conectar_x_post(self, url):

        payload = Client.get_json_cliente(self)

        response = requests.post(url, json=payload)
        print(response, 'Response del status del post....')

        # resp = response.json()
        # print(resp, 'print del response json.....')


        if response.status_code == 200 or response.status_code == 204:
            contador = 0  # CONTADOR PROVISORIO PARA COMPROBAR QUE FUNCIONA
            mensajes_recibidos = [] # Estructura para guardar las task asignadas a este cliente
            contactos_recibidos = []
            while contador != 10 and response.status_code == 200:

                json = response.json()
                print(json, 'Este es el json que recibí y exploro')
                if json['message'] == "":
                    print('Vino el JSON VACIO!!')
                    pass

                else:
                    mensajes_recibidos.append(json["message"])
                    contactos_recibidos.append(json["receiver"])
                    # Puede de las task recibidas elegir una random
                    print('ACÁ TIENE QUE EJECUTAR EL ENVIO DEL MENSAJE..........')
                    print("Tarea: ", json['message'], "Fecha actual: ", datetime.datetime.now())
                    print(mensajes_recibidos)
                    print(contactos_recibidos,'printeo los contactosssssssssssssssssssssssssssssssss')
                    # El time.sleep() simula el tiempo de receso entre la ejecucion de una tarea y otra
                    time.sleep(3)
                    # Acá puede ir una lógica de que si paso X tiempo despues de la ultima tarea, retome el ciclo
                    # continue #break

                contador += 1
                # vuelvo a hacer el post para seguir iterando...
                response = requests.post(url, json=payload)

        else:
            print('Error en la conexion, manejar con try - exception')


    def informar_invalido(self, invalidnumber, url):
        payload = {
            "SOY": self.numero_linea,
            "NumInv": invalidnumber
        }
        print("PRINTEO EL PAYLOAD: ",payload, "*******************************************************************************")
        response = requests.post(url, json=payload)
        print(response, 'Response del status del post....post post post ')
        if response.status_code == 200:
            print('Lo recibió OK')
        else:
            print('No estuvo OK!')




# PRUEBAS DE CONEXION

uncliente = Client('1156512729')
url = "http://localhost:5000"

urlinvalid = "http://localhost:5000/invalidnumber"


# print('Desde cliente --> conexion: ', uncliente.conectar_x_get(url))
print('voy por post...')
uncliente.conectar_x_post(url)


uncliente.informar_invalido("114", urlinvalid)

otro_cliente = Client('2523')
print(otro_cliente.get_json_cliente())
