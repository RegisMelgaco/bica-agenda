import os
from dotenv import load_dotenv
import psycopg2

commands = [
    '''
    CREATE TABLE calendar (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50)
    )
    ''',
    '''
    CREATE TABLE client (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        phone VARCHAR(20)
    )
    ''',
    '''
    CREATE TABLE confirmation_configuration (
        id SERIAL PRIMARY KEY,
        calendar_id INT NOT NULL,
        advance_min INT,
        whatsapp_enabled BOOL,
        call_enabled BOOL,
        sms_enabled BOOL,
        FOREIGN KEY (calendar_id)
            REFERENCES calendar (id)
            ON UPDATE CASCADE ON DELETE CASCADE
    )
    ''',
    '''
    CREATE TABLE appointment (
        id SERIAL PRIMARY KEY,
        calendar_id INT NOT NULL,
        client_id INT NOT NULL,
        start TIMESTAMP,
        duration_min INT,
        notes VARCHAR(255),
        FOREIGN KEY (calendar_id)
            REFERENCES calendar (id)
            ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (client_id)
            REFERENCES client (id)
            ON UPDATE CASCADE ON DELETE CASCADE
    )
    ''',
    '''
    CREATE TABLE appointment_confirmation (
        id SERIAL PRIMARY KEY,
        appointment_id INT NOT NULL,
        done BOOL,
        FOREIGN KEY (appointment_id)
            REFERENCES appointment (id)
            ON UPDATE CASCADE ON DELETE CASCADE
    )
    ''',
    '''
    CREATE TABLE appointment_state (
        id SERIAL PRIMARY KEY,
        appointment_id INT NOT NULL,
        description VARCHAR(100),
        FOREIGN KEY (appointment_id)
            REFERENCES appointment (id)
            ON UPDATE CASCADE ON DELETE CASCADE
    )
    ''',
]

if __name__ == '__main__':
    load_dotenv()

    conn = psycopg2.connect(database=os.environ.get("DATABASE_NAME", "postgres"),
                            host=os.environ.get("DATABASE_HOST", "localhost"),
                            user=os.environ.get("DATABASE_USER", "postgres"),
                            password=os.environ.get("DATABASE_PASSWORD", "secr3t"),
                            port=os.environ.get("DATABASE_PORT", "5432"))

    cursor = conn.cursor()
    for command in commands:
        cursor.execute(command)
    conn.commit()

    print("migration done")
