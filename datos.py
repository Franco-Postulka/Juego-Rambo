import sqlite3

with sqlite3.connect("score.db") as conexion:
    try:
        cursor = conexion.cursor() #cursor es un objeto que permite ejecutar comandos SQL y manejar los resultados
        # Verificar si la tabla 'Jugadores' existe en sqlite_master
        cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='Jugadores' ''')
        tabla_existe = cursor.fetchone() ## fetchone devuelve None si no enu¿cuentra la table 
        if tabla_existe:
            print("La tabla 'Jugadores' ya existe en la base de datos")
        else:
            # Si la tabla no existe, se crea
            sentencia = '''
                create table Jugadores
                (
                    id integer primary key autoincrement,
                    nombre text,
                    score integer
                )
                '''
            conexion.execute(sentencia)
            print("Tabla 'Jugadores' creada con éxito")
    except Exception as e:
        print("Error:", e)
        
    # try:
    #     sentencia = '''
    #     insert into Jugadores(nombre,score) values (?,?)
    #     '''
    #     conexion.execute(sentencia,("Franco", 615))
    #     print("tabla completada")
    # except Exception as e:
    #     print("Error:", e)

    # try:
    #     sentencia = '''
    #     select nombre, score from Jugadores order by score desc limit 3
    #     '''
    #     cursor = conexion.execute(sentencia)
    #     for fila in cursor:
    #         print(fila)
    # except Exception as e:
    #     print("Error:", e)

    # try:
    #     score = 730
    #     id =2 
    #     sentencia = '''
    #     update Jugadores set score = ? where id = ?
    #     '''
    #     cursor = conexion.execute(sentencia,(score,id))
    #     for fila in cursor:
    #         print(fila)
    #     print("tabla modificada")
    # except Exception as e:
    #     print("Error:", e)

    try:
        score = 730
        id =2 
        sentencia = '''
        delete from Jugadores where score <= 500
        '''
        cursor = conexion.execute(sentencia)
        for fila in cursor:
            print(fila)
        print("tabla modificada")
    except Exception as e:
        print("Error:", e)