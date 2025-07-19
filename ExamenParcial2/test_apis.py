"""
Script de prueba para todas las APIs de Parra's Dev
Ejecutar: python test_apis.py
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/pendientes"

def test_api(endpoint, description):
    """Función para probar un endpoint de la API"""
    print(f"\n🔍 Probando: {description}")
    print(f"📡 Endpoint: {endpoint}")
    print("-" * 50)
    
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status: {response.status_code}")
            print(f"📊 Total elementos: {data.get('total', len(data.get('results', data.get('data', []))))}")
            
            # Mostrar primeros 2 elementos como ejemplo
            items = data.get('data', data.get('results', data))
            if items and len(items) > 0:
                print("📋 Primeros elementos:")
                for i, item in enumerate(items[:2]):
                    print(f"   {i+1}. {item}")
            
        else:
            print(f"❌ Error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

def main():
    print("🚀 TESTING DE APIS - PARRA'S DEV")
    print("=" * 60)
    
    # Lista de todas las APIs según los requerimientos
    apis_to_test = [
        (f"{BASE_URL}/solo-ids/", "Lista de todos los pendientes (solo IDs)"),
        (f"{BASE_URL}/ids-y-titulos/", "Lista de todos los pendientes (IDs y Titles)"),
        (f"{BASE_URL}/sin-resolver/", "Lista de pendientes sin resolver (ID y Title)"),
        (f"{BASE_URL}/resueltos/", "Lista de pendientes resueltos (ID y Title)"),
        (f"{BASE_URL}/ids-y-usuarios/", "Lista de todos los pendientes (IDs y userID)"),
        (f"{BASE_URL}/resueltos-usuarios/", "Lista de pendientes resueltos (ID y userID)"),
        (f"{BASE_URL}/sin-resolver-usuarios/", "Lista de pendientes sin resolver (ID y userID)"),
        (f"{BASE_URL}/", "CRUD Principal - Lista completa"),
    ]
    
    for endpoint, description in apis_to_test:
        test_api(endpoint, description)
    
    print("\n" + "=" * 60)
    print("✅ PRUEBAS COMPLETADAS")
    print("🌐 Dashboard: http://127.0.0.1:8000/")
    print("🔧 Admin: http://127.0.0.1:8000/admin/")
    print("📖 API Browser: http://127.0.0.1:8000/api/")

if __name__ == "__main__":
    main()
