import os
from dotenv import load_dotenv
import psycopg2


if __name__ == '__main__':
    load_dotenv()

    conn = psycopg2.connect(database=os.environ.get("DATABASE_NAME", "postgres"),
                            host=os.environ.get("DATABASE_HOST", "localhost"),
                            user=os.environ.get("DATABASE_USER", "postgres"),
                            password=os.environ.get("DATABASE_PASSWORD", "secr3t"),
                            port=os.environ.get("DATABASE_PORT", "5432"))

    cursor = conn.cursor()
    cursor.execute('''
         CREATE TABLE cars (
            brand VARCHAR(255),
            model VARCHAR(255),
            year INT
        );  
''')
    
    conn.commit()

    print("migration done")
