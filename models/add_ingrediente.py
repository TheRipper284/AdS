import mysql.connector

def agregar_ingrediente(itemId, categoryId, itemName, supplier):
    """Agrega un nuevo ingrediente a la tabla ingredientes."""
    try:
        # Conexión a la base de datos
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='miyh2'
        )
        cursor = db.cursor()
        print("Conexión a la base de datos establecida.")
        
        # Verificar si la categoría existe
        cursor.execute("SELECT categoria_ing FROM catego_ing WHERE categoria_id = %s", (categoryId,))
        result = cursor.fetchone()
        print(result)

        if result is None:
            raise ValueError(f"La categoría con ID {categoryId} no existe.")  # Lanzar una excepción si no existe

        # Insertar el nuevo ingrediente en la base de datos
        query = "INSERT INTO ingredientes (id_ing, categoria_ing, nombre, proveedor) VALUES (%s, %s, %s, %s)"
        values = (itemId, result[0], itemName, supplier)
        cursor.execute(query, values)
        db.commit()  # Confirmar los cambios
        print("Ingrediente agregado exitosamente.")

    except mysql.connector.Error as err:
        print(f"Error al interactuar con la base de datos: {err}")
        raise  # Propagar el error para que Flask pueda manejarlo
    except ValueError as ve:
        print(ve)
        raise  # Propagar el error para que Flask pueda manejarlo
    finally:
        # Cerrar la conexión a la base de datos
        if cursor:
            cursor.close()
        if db:
            db.close()
        print("Conexión a la base de datos cerrada.")

def editar_ingrediente(itemId, categoryId, itemName, supplier):
    """Edita un ingrediente existente en la tabla ingredientes."""
    try:
        # Conexión a la base de datos
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='miyh2'
        )
        cursor = db.cursor()
        print("Conexión a la base de datos establecida.")

        # Verificar si la categoría existe
        cursor.execute("SELECT categoria_ing FROM catego_ing WHERE categoria_id = %s", (categoryId,))
        result = cursor.fetchone()
        print(result)

        if result is None:
            raise ValueError(f"La categoría con ID {categoryId} no existe.")  # Lanzar una excepción si no existe

        # Actualizar el ingrediente en la base de datos
        query = "UPDATE ingredientes SET categoria_ing = %s, nombre = %s, proveedor = %s WHERE id_ing = %s"
        values = (result[0], itemName, supplier, itemId)
        cursor.execute(query, values)
        db.commit()  # Confirmar los cambios
        print("Ingrediente actualizado exitosamente.")

    except mysql.connector.Error as err:
        print(f"Error al interactuar con la base de datos: {err}")
        raise  # Propagar el error para que Flask pueda manejarlo
    except ValueError as ve:
        print(ve)
        raise  # Propagar el error para que Flask pueda manejarlo
    finally:
        # Cerrar la conexión a la base de datos
        if cursor:
            cursor.close()
        if db:
            db.close()
        print("Conexión a la base de datos cerrada.")

def eliminar_ingrediente(itemId):
    """Elimina un ingrediente de la tabla ingredientes."""
    try:
        # Conexión a la base de datos
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='miyh2'
        )
        cursor = db.cursor()
        print("Conexión a la base de datos establecida.")

        # Eliminar el ingrediente de la base de datos
        query = "DELETE FROM ingredientes WHERE id_ing = %s"
        cursor.execute(query, (itemId,))
        db.commit()  # Confirmar los cambios
        print("Ingrediente eliminado exitosamente.")

    except mysql.connector.Error as err:
        print(f"Error al interactuar con la base de datos: {err}")
        raise  # Propagar el error para que Flask pueda manejarlo
    finally:
        # Cerrar la conexión a la base de datos
        if cursor:
            cursor.close()
        if db:
            db.close()
        print(" Conexión a la base de datos cerrada.")