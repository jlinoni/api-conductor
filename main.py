from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "100.27.62.167"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_conductor"

# Get all conductors
@app.get("/conductor")
def get_conductor():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM conductor")
    result = cursor.fetchall()
    mydb.close()
    return {"conductor": result}

# Get a conductor by ID
@app.get("/conductor/{id}")
def get_conductor(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM conductor WHERE id = %s", (id,))
    result = cursor.fetchone()
    mydb.close()
    return {"conductor": result}

# Add a new conductor
@app.post("/conductor")
def add_conductor(item: schemas.Conductor):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    nombres = item.nombres
    edad = item.edad
    direccion = item.direccion
    licencia = item.licencia
    cursor = mydb.cursor()
    sql = "INSERT INTO conductor (nombres, edad, direccion, licencia) VALUES (%s, %s, %s, %s)"
    val = (nombres, edad, direccion, licencia)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Conductor agregado con éxito"}

# Modify a conductor
@app.put("/conductor/{id}")
def update_conductor(id: int, item: schemas.Conductor):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    nombres = item.nombres
    edad = item.edad
    direccion = item.direccion
    licencia = item.licencia
    cursor = mydb.cursor()
    sql = "UPDATE conductor SET nombres=%s, edad=%s, direccion=%s, licencia=%s WHERE id=%s"
    val = (nombres, edad, direccion, licencia, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Datos del conductor actualizados con éxito"}

# Delete a conductor by ID
@app.delete("/conductor/{id}")
def delete_conductor(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM conductor WHERE id = %s", (id,))
    mydb.commit()
    mydb.close()
    return {"message": "Conductor eliminado con éxito"}

# Get vehicles by conductor ID
@app.get("/conductor/{id}/vehiculos")
def get_vehiculos_by_conductor(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM vehiculo WHERE conductor_id = %s", (id,))
    result = cursor.fetchall()
    mydb.close()
    return {"vehiculos": result}