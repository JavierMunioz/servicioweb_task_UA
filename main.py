import requests

# URL base del servicio Flask desplegado en Render
BASE_URL = "https://servicioweb-task-ua.onrender.com/items"

def get_items():
    """Obtiene todos los elementos de la lista."""
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print("Lista de items:", response.json())
        else:
            print(f"Error al obtener items: {response.status_code}")
    except Exception as e:
        print(f"Excepción al obtener items: {e}")

def create_item(item):
    """Crea un nuevo elemento."""
    try:
        response = requests.post(BASE_URL, json={"name": item})
        if response.status_code == 201:
            print(f"Item creado: {response.json()}")
        else:
            print(f"Error al crear item: {response.status_code}")
    except Exception as e:
        print(f"Excepción al crear item: {e}")

def update_item(item_id, new_name):
    """Actualiza un elemento existente."""
    try:
        url = f"{BASE_URL}/{item_id}"
        response = requests.put(url, json={"name": new_name})
        if response.status_code == 200:
            print(f"Item actualizado: {response.json()}")
        else:
            print(f"Error al actualizar item: {response.status_code}")
    except Exception as e:
        print(f"Excepción al actualizar item: {e}")

def delete_item(item_id):
    """Elimina un elemento."""
    try:
        url = f"{BASE_URL}/{item_id}"
        response = requests.delete(url)
        if response.status_code == 200:
            print(f"Item eliminado: {response.json()}")
        else:
            print(f"Error al eliminar item: {response.status_code}")
    except Exception as e:
        print(f"Excepción al eliminar item: {e}")

# Operaciones CRUD
if __name__ == "__main__":
    # Obtener todos los items
    print("=== Obtener Items ===")
    get_items()
    
    # Crear un nuevo item
    print("\n=== Crear Item ===")
    create_item("Tarea 1")
    
    # Crear otro item
    create_item("Tarea 2")

    # Obtener todos los items nuevamente
    print("\n=== Obtener Items Después de Crear ===")
    get_items()
    
    # Actualizar un item existente
    print("\n=== Actualizar Item ===")
    update_item(1, "Tarea Actualizada")

    # Obtener todos los items después de la actualización
    print("\n=== Obtener Items Después de Actualizar ===")
    get_items()
    
    # Eliminar un item
    print("\n=== Eliminar Item ===")
    delete_item(2)
    
    # Obtener todos los items después de eliminar
    print("\n=== Obtener Items Después de Eliminar ===")
    get_items()
