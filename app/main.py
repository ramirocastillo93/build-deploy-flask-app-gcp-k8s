from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from db import PostgreSQL
import re, os


# db_user = os.environ["DB_USER"]
# db_pass = os.environ["DB_PASS"]
# db_host = os.environ["DB_HOST"]
# db_name = os.environ["DB_NAME"]

db_user, db_pass, db_host, db_name, db_port= "admin", "admin", "localhost", "suppliers", "5432"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'
db = SQLAlchemy(app)

db_conn = PostgreSQL(db_name, db_user, db_pass, db_host, db_port)

def verifyDate(date=str):
    pattern = "(?:19\d{2}|20[01][0-9]|2023)[-/.](?:0[1-9]|1[012])[-/.](?:0[1-9]|[12][0-9]|3[01])\b"
    try:
        re.match(pattern, date)
        return True
    except:
        return False

@app.route('/hello/<username>', methods=['GET','PUT'])
def hello_world(username):
    if request.method == 'PUT':
        if request.is_json:
            json_data = request.get_json()
            if 'dateOfBirth' in json_data:
                dob = json_data['dateOfBirth']
                if verifyDate(dob):
                    db_conn.connect()
                    try:
                        db_conn.createUpdateUser(username, dob)
                        return {}, 204
                    except:
                        return {}, 400
                    finally:
                        db_conn.disconnect()
                else:
                    return jsonify({"message":"dateOfBirth format isn't YYYY-MM-DD", "status": 400}), 400
            else:
                return jsonify({"message":"Missing required attribute \"dateOfBirth\"", "status": 400}), 400
        else:
            return jsonify({"message":f"Request not in json format {type(request)}", "status": 400}), 400
    else:
        db_conn.connect()
        try:
            if db_conn.isBirthday(username) == 0:
                return {
                    "message":f"Hello, {username.capitalize()}! Happy birthday!"
                }, 200
            if db_conn.isBirthday(username) != 0 and db_conn.isBirthday(username) is not None:
                return {
                    "message":f"Hello, {username.capitalize()}! Your birthday is in {db_conn.isBirthday(username)} day(s)!"
                }, 200
            elif db_conn.isBirthday(username) == None:
                return {
                    "message":f"Error: User {username.capitalize()} doesn't exist."
                }, 400
        except IndexError as e:
            return {
                "message":f"Error occurred {e}"
            }, 400
        finally:
            db_conn.disconnect()
    

if __name__ == "__main__":
    app.run(debug='False')
