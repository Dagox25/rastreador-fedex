import sqlite3

# Conectar a la base de datos (la crea si no existe)
conn = sqlite3.connect('tracking.db')
c = conn.cursor()

# Crear tabla
c.execute('''
    CREATE TABLE IF NOT EXISTS packages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tracking_number TEXT NOT NULL,
        status TEXT NOT NULL,
        location TEXT NOT NULL,
        last_updated TEXT NOT NULL
    )
''')

# Insertar datos de prueba
c.execute('''
    INSERT INTO packages (tracking_number, status, location, last_updated)
    VALUES
    ('ABC123456', 'En tránsito', 'Santo Domingo', '2025-05-14 15:00'),
    ('XYZ789012', 'Entregado', 'Santiago', '2025-05-13 11:45')
''')

conn.commit()
conn.close()

print("Base de datos inicializada.")