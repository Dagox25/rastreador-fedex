from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Ruta principal: muestra el formulario de búsqueda
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el número de rastreo
@app.route('/track', methods=['POST'])
def track():
    tracking_number = request.form['tracking_number']
    
    # Conexión a la base de datos
    conn = sqlite3.connect('paquetes.db')
    cursor = conn.cursor()
    
    # Consulta el paquete
    cursor.execute("SELECT * FROM paquetes WHERE numero_seguimiento = ?", (tracking_number,))
    paquete = cursor.fetchone()
    
    conn.close()

    if paquete:
        return render_template('result.html', paquete=paquete)
    else:
        return render_template('result.html', error="No se encontró ningún paquete con ese número.")

# Ejecuta la aplicación localmente (solo para pruebas)
if __name__ == '__main__':
    app.run(debug=True)