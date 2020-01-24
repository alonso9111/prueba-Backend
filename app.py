'''
Tipo de usuario
    1 - Maestro
    2 - Estudiante
'''
import pymysql
import json
import ast
from flask import Flask , jsonify, request

app=Flask(__name__)
'''
CRUD CURSO
'''
#CRATE CURSP
@app.route('/addCurso',methods=['POST']) 
def addCurso():
    msg=""
    tipo_usuario=request.json['tusuario']
    curso_nombre=request.json['nombre']
    id_prerrequisito=int(request.json['prerrequisito'])

    if tipo_usuario==1:
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='educdb')
            try:
                with conexion.cursor() as cursor:
                    consulta = "INSERT INTO curso(id_curso_prerrequisito, nombre) VALUES (%s, %s);"
                    if(id_prerrequisito>1):
                        cursor.execute(consulta, (id_prerrequisito, curso_nombre))
                    else:
                        cursor.execute(consulta, (0, curso_nombre))
                conexion.commit()
            finally:
                conexion.close()
                msg="ok"
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            msg="error"
    else:
        msg="Usted es alumno no puede realizar esta operacion"

    return jsonify({
        "message":msg
    })
#LIST ALL CURSO
@app.route('/getCurso',methods=['GET']) 
def getCursos(): 
    cursos =""
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM Curso;")
                cursos = cursor.fetchall()
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    
    return json.dumps(cursos)
#LIST CURSO BY ID
@app.route('/getCurso/<id_curso>',methods=['GET']) 
def getCurso(id_curso):
    curso=""
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM Curso where id="+str(id_curso)+";")
                curso = cursor.fetchall()
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    
    return json.dumps(curso)
#EDIT CURSO
@app.route('/editCurso',methods=['PUT'])
def editCurso():
    tipo_usuario=request.json['tusuario']
    id_curso=request.json['id']
    curso_nombre=request.json['nombre']
    id_prerrequisito=int(request.json['prerrequisito'])
    if tipo_usuario==1:
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='educdb')
            try:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE curso SET id_curso_prerrequisito=%s,nombre=%s WHERE id =%s;"
                    if(id_prerrequisito>1):
                        cursor.execute(consulta, (id_prerrequisito, curso_nombre,id_curso))
                    else:
                        cursor.execute(consulta, (0, curso_nombre,id_curso))
                conexion.commit()
            finally:
                conexion.close()
                msg="ok"
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            msg="error"
    else:
        msg="Usted es alumno no puede realizar esta operacion"
    return jsonify({
        "message":msg
    })
#DELETE CURSO
@app.route('/delCurso/<id_curso>/<tipo_usuario>',methods=['DELETE'])
def delCurso(id_curso,tipo_usuario):
    print(type(tipo_usuario))
    if int(tipo_usuario) ==1 :
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='educdb')
            try:
                with conexion.cursor() as cursor:
                    consulta = "DELETE FROM curso WHERE id ="+id_curso+";"
                    cursor.execute(consulta)
                conexion.commit()
            finally:
                conexion.close()
                msg="ok"
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            msg="error"
    else:
        msg="Usted es alumno no puede realizar esta operacion"
    return jsonify({
        "message":msg
    })

'''
CRUD LECCIONES
'''
#CRATE LECCION
@app.route('/addLeccion',methods=['POST']) 
def addLeccion():
    msg=""
    tipo_usuario=request.json['tusuario']
    id_curso=request.json['id_curso']
    id_prerrequisito=int(request.json['prerrequisito'])
    nombre=request.json['nombre']
    puntaje=request.json['puntaje']

    if tipo_usuario==1:
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='educdb')
            try:
                with conexion.cursor() as cursor:
                    consulta = "INSERT INTO leccion(id_curso, id_leccion_prerrequisito, nombre, puntaje_aprobacion) VALUES (%s, %s, %s, %s);"
                    cursor.execute(consulta, (id_curso, id_prerrequisito,nombre,puntaje))
                conexion.commit()
            finally:
                conexion.close()
                msg="ok"
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            msg="error"
    else:
        msg="Usted es alumno no puede realizar esta operacion"

    return jsonify({
        "message":msg
    })
#LIST ALL LECCION
@app.route('/getLeccion',methods=['GET']) 
def getLecciones():
    lecciones =""
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM leccion;")
                lecciones = cursor.fetchall()
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    
    return json.dumps(lecciones)
#LIST LECCION BY ID
@app.route('/getLeccion/<id_leccion>',methods=['GET']) 
def getLeccion(id_leccion):
    leccion=""
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM leccion where id="+id_leccion+";")
                leccion = cursor.fetchall()
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    
    return json.dumps(leccion)
#EDIT LECCION
@app.route('/editLeccion',methods=['PUT'])
def editLeccion():
    tipo_usuario=request.json['tusuario']
    id_leccion=request.json['id']
    id_curso=request.json['id_curso']
    id_prerrequisito=int(request.json['prerrequisito'])
    nombre=request.json['nombre']
    puntaje=request.json['puntaje']
    if tipo_usuario==1:
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='educdb')
            try:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE leccion SET id_curso=%s,id_leccion_prerrequisito=%s,nombre=%s,puntaje_aprobacion=%s WHERE id=%s;"
                    cursor.execute(consulta, (id_curso,id_prerrequisito, nombre,puntaje,id_leccion))
                conexion.commit()
            finally:
                conexion.close()
                msg="ok"
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            msg="error"
    else:
        msg="Usted es alumno no puede realizar esta operacion"
    return jsonify({
        "message":msg
    })
#DELETE LECCION
@app.route('/delLeccion/<id_leccion>/<tipo_usuario>',methods=['DELETE'])
def delLeccion(id_leccion,tipo_usuario):
    if int(tipo_usuario) ==1 :
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='educdb')
            try:
                with conexion.cursor() as cursor:
                    consulta = "DELETE FROM leccion WHERE id ="+id_leccion+";"
                    cursor.execute(consulta)
                conexion.commit()
            finally:
                conexion.close()
                msg="ok"
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            msg="error"
    else:
        msg="Usted es alumno no puede realizar esta operacion"
    return jsonify({
        "message":msg
    })

'''
CRUD PREGUNTAS
    
    TIPO PREGUNTA
        1 - Booleana
        2 - Opción múltiple donde solo una respuesta es correcta
        3 - Opción múltiple donde más de una respuesta es correcta
        4 - Opción múltiple donde más de una respuesta es correcta y 
            todas deben responderse correctamente
'''
#CRATE PREGUNTA
@app.route('/addPregunta',methods=['POST']) 
def addPregunta():
    msg=""
    tipo_usuario=request.json['tusuario']
    id_leccion=request.json['id_leccion']
    id_tipo=request.json['tipo']
    pregunta=request.json['pregunta']
    respuesta=request.json['respuesta']
    puntaje=request.json['puntaje']

    if tipo_usuario==1:
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='educdb')
            try:
                with conexion.cursor() as cursor:
                    consulta = "INSERT INTO pregunta(id_leccion, id_tipo, pregunta, respuesta, puntaje) VALUES (%s, %s, %s, %s, %s);"
                    cursor.execute(consulta, (id_leccion, id_tipo,pregunta,respuesta,puntaje))
                conexion.commit()
            finally:
                conexion.close()
                msg="ok"
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            msg="error"
    else:
        msg="Usted es alumno no puede realizar esta operacion"

    return jsonify({
        "message":msg
    })
#LIST ALL PREGUNTA
@app.route('/getPregunta',methods=['GET']) 
def getPreguntas():
    preguntas =""
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM pregunta;")
                preguntas = cursor.fetchall()
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    
    return json.dumps(preguntas)
#LIST PREGUNTA BY ID
@app.route('/getPregunta/<id_pregunta>',methods=['GET']) 
def getPregunta(id_pregunta):
    pregunta=""
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM pregunta where id="+id_pregunta+";")
                pregunta = cursor.fetchall()
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    
    return json.dumps(pregunta)
#EDIT PREGUNTA
@app.route('/editPregunta',methods=['PUT'])
def editPregunta():
    msg=""
    tipo_usuario=request.json['tusuario']
    id_pregunta=request.json['id']
    id_leccio=request.json['id_leccion']
    id_tipo=request.json['tipo']
    pregunta=request.json['pregunta']
    respuesta=request.json['respuesta']
    puntaje=request.json['puntaje']
    if tipo_usuario==1:
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='educdb')
            try:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE pregunta SET id_leccion=%s,id_tipo=%s,pregunta=%s,respuesta=%s,puntaje=%s  WHERE id=%s;"
                    cursor.execute(consulta, (id_leccio,id_tipo, pregunta,respuesta,puntaje,id_pregunta))
                conexion.commit()
            finally:
                conexion.close()
                msg="ok"
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            msg="error"
    else:
        msg="Usted es alumno no puede realizar esta operacion"
    return jsonify({
        "message":msg
    })
#DELETE PREGUNTA
@app.route('/delPregunta/<id_pregunta>/<tipo_usuario>',methods=['DELETE'])
def delPregunta(id_pregunta,tipo_usuario):
    if int(tipo_usuario) ==1 :
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='educdb')
            try:
                with conexion.cursor() as cursor:
                    consulta = "DELETE FROM pregunta WHERE id ="+id_pregunta+";"
                    cursor.execute(consulta)
                conexion.commit()
            finally:
                conexion.close()
                msg="ok"
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
            msg="error"
    else:
        msg="Usted es alumno no puede realizar esta operacion"
    return jsonify({
        "message":msg
    })

########################### TIPO PREGUNTA #################################

#LIST ALL TIPO PREGUNTAA
@app.route('/getTipoPregunta',methods=['GET']) 
def getTipoPreguntas():
    tipos =""
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM tipo_pregunta;")
                tipos = cursor.fetchall()
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    
    return json.dumps(tipos)
#LIST TIPO PREGUNTA BY ID
@app.route('/getTipoPregunta/<id_tipo>',methods=['GET']) 
def getTipoPregunta(id_tipo):
    tipo=""
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM tipo_pregunta where id="+id_tipo+";")
                tipo = cursor.fetchall()
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    
    return json.dumps(tipo)

'''
FUNCIONES
'''
def getCursoEstudiante(id_estudiante,id_curso):
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                consulta="SELECT * FROM cursoestudiante where id_estudiante=%s and id_curso=%s;"
                cursor.execute(consulta,(id_estudiante,id_curso))
                records = cursor.fetchmany()
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    return records

#Funcion que valida y asigna curso a alumno si
#cumple con las condiciones y prerrequisitos
@app.route('/asignaCurso',methods=['POST']) 
def asignaCurso():
    msg=""
    aux=False
    id_estudiante=request.json['estudiante']
    id_curso=request.json['curso']
    curso=  ast.literal_eval(getCurso(id_curso))
    curso_prerrequisito = getCursoEstudiante(id_estudiante,curso[0][1])
    if curso[0][1]==0:
        aux=True
    elif len(curso_prerrequisito)>0 and curso_prerrequisito[0][3]>0:
        curso_solisita = getCursoEstudiante(id_estudiante,id_curso)
        if len(curso_solisita)==0:
            aux=True
        else:
            msg="Ya tienes tomado este curso"
    else:
        msg="No puedes tomar este curso, Faltan prerrequisitos"

    if aux:
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='educdb')
            print("Conexión correcta")
        
            try:
                with conexion.cursor() as cursor:
                    consulta="INSERT INTO cursoestudiante(id_estudiante, id_curso) VALUES (%s, %s);"
                    rs=cursor.execute(consulta,(id_estudiante,id_curso))
                    msg="Curso asignado correctamente"
                conexion.commit()
            finally:
                conexion.close()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
    
    return jsonify({
        "message":msg
    })

#Funcion que obtiene el listado de preguntas
#por leccion con la finalidad de responderlas
@app.route('/listarPregunta/<id_leccion>',methods=['GET']) 
def listarPregunta(id_leccion):
    preguntas =""
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM vwpreguntasbyleccion WHERE id_leccion="+str(id_leccion)+";")
                preguntas = cursor.fetchall()
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    
    return json.dumps(preguntas)

#Funcion que obtiene el listado de Cursos
#por los que puede tomarel alumno
@app.route('/listaCurso/<id_estudiante>',methods=['GET']) 
def listaCurso(id_estudiante):
    cursos =""
    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='educdb')
        print("Conexión correcta")
       
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM educdb.vwlistacurso where id_estudiante is null or id_estudiante = "+str(id_estudiante)+";")
                cursos = cursor.fetchall()
        finally:
            conexion.close()
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
    
    return json.dumps(cursos)

'''
RUN APP
'''
if __name__=='__main__':
    app.run(debug=True,port=4000)