import sqlite3

def crear_db():
    '''
    Se conecta a la base de datos y ejecuta una query para crear una tabla.

    return:

    '''
    try:
        conexion = sqlite3.connect("../base_de_datos/database.db")
        cursor = conexion.cursor()
        # Crear una única tabla jugador con tres columnas: id, player y score
        cursor.execute("CREATE TABLE jugador (id INTEGER PRIMARY KEY AUTOINCREMENT, player VARCHAR(50), score INTEGER)")
        conexion.commit()
    except Exception as ex:
        print(ex)
    finally:
        if conexion:
            conexion.close()

def insertar_jugador(player, score):
    '''
    Ejecuta una query para insertar datos que llegan por parametro en una tabla
    
    args:
    - player: Nombre del jugador
    - score: Puntaje del jugador

    return:
    '''
    try:
        conexion = sqlite3.connect("../base_de_datos/database.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO jugador (player, score) VALUES (?, ?)", (player, score))
        conexion.commit()
    except Exception as ex:
        print(ex)
    finally:
        if conexion:
            conexion.close()
