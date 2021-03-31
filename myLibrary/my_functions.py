import json


def find_task(lista, sender, date):
    """
    Método que recibe una lista con todas las tareas obtenidas de la BBDD a través del GET del inicio/conexión
    :param lista: Contiene todas las tareas a revisar
    :param sender: Es el cliente que realiza el POST a la api
    :param date: Es la fecha actual que busca coincidir con la fecha de la tarea
    :param time: Es la hora actual que busca coincidir con la hora de la tarea
    :return: Un json con dos atributos, el mensaje a enviar y los destinatarios del mismo en caso de haber coincidencia.
            Y en caso contrario un json con los valores vacíos
    """
    encontre = False
    index = 0
    while not encontre and index < len(lista):
        date_lista = (lista[index][4]).date()
        hour_lista = (lista[index][4]).hour
        minute_lista = (lista[index][4]).minute

        if lista[index][2] == sender and date_lista == date.date() and hour_lista == date.hour and minute_lista == date.minute:
            encontre = True
            print('ESTOY EN EL HAPPY ROAD!')
            return json.dumps({"message": lista[index][1], "receiver": lista[index][3]}), 200
        index += 1

    else:
        return json.dumps({"task": "", "receivers": ""}), 204