from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'paquetes.db'

# Función para conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear base de datos y tabla si no existen
def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE paquetes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero_guia TEXT NOT NULL,
                estado TEXT NOT NULL,
                ubicacion TEXT NOT NULL,
                fecha TEXT NOT NULL
            )
        ''')
        conn.commit()
        print("✅ Base de datos y tabla creada.")

    # Verificar si hay datos. Si no, insertar uno de prueba
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM paquetes")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute('''
            INSERT INTO paquetes (numero_guia, estado, ubicacion, fecha)
            VALUES (?, ?, ?, ?)
        ''', ('ABC123456789', 'En tránsito', 'Santo Domingo', '2025-05-14'))
        conn.commit()
        print("📦 Paquete de prueba insertado.")
    conn.close()

# Inicializar DB al iniciar
init_db()

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario
@app.route('/resultado', methods=['POST'])
def resultado():
    numero_guia = request.form['numero_guia']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM paquetes WHERE numero_guia = ?', (numero_guia,))
    paquete = cursor.fetchone()
    conn.close()

    if paquete:
        return render_template('result.html', paquete=paquete)
    else:
        return render_template('result.html', paquete=None, numero_guia=numero_guia)

# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)