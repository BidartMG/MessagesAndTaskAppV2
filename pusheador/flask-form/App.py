from flask import Flask, redirect, url_for, render_template, request, flash
from flask_mysqldb import MySQL
from datetime import datetime
import json
from myLibrary.my_functions import find_task

app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'flaskmessages'

mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'


@app.route('/', methods=['GET', 'POST'])
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from messages')
    data = cur.fetchall()

    if request.method == 'POST':
        # Guardo en la variable el identificador de la línea telefónica que trabajará
        recibo = request.json['SOY']  # TODO: Comparar con el tipo de dato que va a enviar Nelson

        # Tomo la fecha actual y la parseo a string
        date_now = datetime.now()

        # Consulto a la BBDD por lista para el sender recibido
        myquery = "SELECT * FROM messages WHERE sender = " + recibo  # si agrego el date rompe!
        cur.execute(myquery)
        find_sender = cur.fetchall()

        # Evalúo que la lista filtrada para el sender no esté vacía
        if len(find_sender) > 0:
            print('------------------------------------------------------------------------------------------------')
            print('*** **** **** Dentro de post con find_sender mayor a cero: ')
            print('**** **** Muestro el find_sender')
            print(find_sender)

            print(date_now.date() == (find_sender[0][4]).date(), '** comparacion date **', date_now.hour == (find_sender[0][4]).hour, ' ** comparacion hora **', date_now.minute == (find_sender[0][4]).minute, ' compare por ultimo los minutos')
            print('Muestro el tipo de dato de time', type(find_sender[0][5]), 'valor del time: ', find_sender[0][5])
            print('------------------------------------------------------------------------------------------------')
            print("SE VIENE EL PRINT MAS IMPORTANTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            # acá llamo a la función find_task
            cadena = find_task(find_sender, recibo,date_now)# cadena es una tupla con el json y el status OJO como accederla
            print('print de cadena..........', cadena)

            if cadena[1] == 200:
                print('El status es 201')
                # Tomo el id que es la primary key autoincremental para eliminarlo mediante query
                id = find_sender[0][0]
                # LO SACO DE LA TABLA MESSAGES PARA CARGARLO EN LA TABLA ASSIGNED-MESSAGES
                cur.execute('DELETE from messages WHERE id = {0}'.format(id))
                mysql.connection.commit()

                # LO INSERTO EN LA TABLA ASIGNADOS
                cur.execute('INSERT INTO assigned_messages (id, message, sender, receiver, date, time, estado) VALUES ('
                            '%s, %s, %s, %s, %s, %s, %s)', (find_sender[0][0], find_sender[0][1], find_sender[0][2],
                                                            find_sender[0][3], find_sender[0][4], find_sender[0][5],
                                                            "OCUPADO"))
                mysql.connection.commit()
                print('OK inserté en mensajes asignados... ')
            else:
                print('El status de cadena NO ES 201')

            return cadena # cadena es una tupla que contiene el json(indice 0) y el status(indice 1)
        # Este else pertenece a no encontrar en la BBDD mensajes para el sender
        else:
            return json.dumps(
                {"message": "", "receiver": ""}), 204

    cur.close()
    # cerrar el curl ESTE RETORNO ES DEL GET
    return render_template('index.html', messages=data)  # GET RETURN


@app.route('/add_message', methods=['POST'])
def add_message():
    if request.method == 'POST':
        message = request.form['message']
        sender = request.form['sender']
        receivers = request.form['receiver']
        date = request.form['date']
        time = request.form['time']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO messages (message, sender, receiver, date, time) VALUES (%s, %s, %s, %s, %s)',
                    (message, sender, receivers, date, time))
        mysql.connection.commit()
        flash("Contact Added Successfully")
    return redirect(url_for('index'))


@app.route('/edit/<id>')
def edit_message(id):
    cur = mysql.connection.cursor()
    cur.execute(f'SELECT * FROM messages WHERE id = {id}')
    data = cur.fetchall()
    # TODO: Conviene darle formato DDMMYYYY a la fecha recibida desde la BBDD porque queda al reves
    fecha = data[0][4]
    return render_template('edit_task.html', message=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_message(id):
    if request.method == 'POST':
        message = request.form['message']
        sender = request.form['sender']
        receivers = request.form['receiver']
        date = request.form['date']
        time = request.form['time']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE messages SET message = %s, sender = %s,receiver = %s, date = %s, time = %s WHERE id =%s',
                    (message, sender, receivers, date, time, id))
        mysql.connection.commit()
        flash('Message Updated Successfully')
        return redirect(url_for('index'))


@app.route('/delete/<string:id>')
def delete_message(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE from messages WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('index'))


@app.route('/invalidnumber', methods=['GET', 'POST'])
def delete_invalid():
    """
    Este método va a recibir un numero que es invalido para recorrer los registros que lo contengan y eliminarlo de ahí
    Hace la consulta a la BBDD buscando coincidencia dentro de los receiver de la tabla message y editarlos
    """
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM assigned_messages")
    data = cur.fetchall()
    print("---Muestro la data: -- ", data) #TODO borrar el print
    if request.method == 'POST':
        invnum = request.json['NumInv']
        print('RECIBI EN EL POST EL NUMERO INVALIDO: ' + invnum + '------------------------------------!♥♥♥')# TODO borrar el print

        query = "SELECT * FROM messages WHERE (receiver LIKE '%" + invnum + "%')"
        cur.execute(query)
        mysql.connection.commit()
        listacontiene = cur.fetchall()

        # ya consulté la BBDD, ahora a ver si hubo coincidencias, las tengo que eliminar
        print('SE ELIMINÓ de las listas el numero: ' + invnum)# TODO borrar este print de referencia
        print(listacontiene) # TODO borrar este print de referencia
        if len(listacontiene) > 0:
            print('HUBO REGISTROS QUE LO CONTIENEN...')
        return 'NO RETORNA NADA'

    else:
        return 'NO RECIBI UN POST!'



if __name__ == '__main__':
    app.run(port=5000, debug=True)
