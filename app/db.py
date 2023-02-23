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
                cur.execute("SELECT 1 FROM users WHERE username=%s", (username.lower(),))
                user_exists = cur.fetchone()

                if user_exists:
                    cur.execute("UPDATE users SET dateOfBirth=%s WHERE username=%s", (dateOfBirth, username.lower()))
                    self.conn.commit()
                    return {"status": 204, "message": f"User {username.lower()} updated successfully."}
                else:
                    cur.execute("INSERT INTO users (username, dateOfBirth) VALUES (%s, %s)", (username.lower(), dateOfBirth))
                    self.conn.commit()
                    return {"status": 204, "message": f"User '{username.lower()}' created successfully."}
        
        except Error as e:
            print(f"Error creating user: {e}")
            self.conn.rollback()
            return {"status": 400, "message": str(e)}

    def isBirthday(self, username):
        date_format = '%Y-%m-%d'
        today = datetime.today()
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT dateOfBirth FROM users WHERE username=%s", (username.lower(),))
                birthday = cur.fetchone()
                birthday = datetime.strptime(birthday[0], date_format) 
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
    
    def disconnect(self):
        self.conn.close()
        print("Disconnected from database")
