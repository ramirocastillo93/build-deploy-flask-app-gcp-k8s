import psycopg2
from psycopg2 import Error
from datetime import datetime

class PostgreSQL:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host 
        self.port = port 
        self.conn = None
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to database.")
        except Error as e:
            print(f"Error connecting to db: {e}")
            self.conn = None
    
    def createUpdateUser(self, username, dateOfBirth):
        try:
            with self.conn.cursor() as cur:
                cur.execute(f"SELECT 1 FROM usuarios WHERE username='{username.lower()}'")
                user_exists = cur.fetchone()

                if user_exists:
                    cur.execute(f"UPDATE usuarios SET dateOfBirth='{dateOfBirth}' WHERE username='{username.lower()}'")
                    self.conn.commit()
                    return {"status": 204, "message": f"User '{username.lower()}' updated successfully."}, 204
                else:
                    cur.execute(f"INSERT INTO usuarios (username, dateOfBirth) VALUES ('{username.lower()}', '{dateOfBirth}')")
                    self.conn.commit()
                    return {"status": 204, "message": f"User '{username.lower()}' created successfully."}, 204
        
        except Error as e:
            print(f"Error creating user: {e}")
            self.conn.rollback()
            return {"status": 400, "message": str(e)}, 400

    def isBirthday(self, username):
        date_format = '%Y-%m-%d'
        today = datetime.today()
        try:
            with self.conn.cursor() as cur:
                cur.execute(f"SELECT dateOfBirth FROM usuarios WHERE username='{username.lower()}'")
                birthday = cur.fetchone()
                if birthday == None:
                    return None
                else:
                    birthday = datetime.strptime(str(birthday[0]), date_format) 
                    birthday = birthday.replace(year=today.year)
                    delta = abs(birthday - today)
                    if today > birthday:
                        return 365 - delta.days
                    if today == birthday:
                        return 0
                    else:
                        return delta.days
        except Error as e:
            print(f"Error fetching birthday: {e}")
        # except NoneType as e:
        #     print(f"Error, no user: {e}")
    def disconnect(self):
        self.conn.close()
        print("Disconnected from database")
