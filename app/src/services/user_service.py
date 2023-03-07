from flask import make_response
from utils.VerifyDate import VerifyDate
from utils.DbConnection import PostgreSQL
import os

db_user = os.environ["POSTGRES_USER"]
db_pass = os.environ["POSTGRES_PASSWORD"]
db_host = os.environ["POSTGRES_HOST"]
db_name = os.environ["POSTGRES_DB"]
db_port = os.environ["POSTGRES_PORT"]

db_conn = PostgreSQL(
    dbname = db_name, 
    password = db_pass, 
    host = db_host, 
    user = db_user,
    port = db_port
    )

def put_user_service(username, request):
    if request.is_json:
        json_data = request.get_json()
        if 'dateOfBirth' in json_data:
            dob = json_data['dateOfBirth']
            if VerifyDate.verifyDate(dob):
                db_conn.connect()
                try:
                    db_conn.createUpdateUser(username, dob)
                    return make_response({}, 204)
                except:
                    return make_response({}, 400)
                finally:
                    db_conn.disconnect()
            else:
                return make_response({"message" : "dateOfBirth format isn't YYYY-MM-DD", "status": 400}, 400)
        else:
            return make_response({"message":"Missing required attribute \"dateOfBirth\"", "status": 400}, 400)
    else:
        return make_response({"message":f"Request not in json format {type(request)}", "status": 400}, 400)
    
def get_user_service(username):
    db_conn.connect()
    try:
        if db_conn.isBirthday(username) == 0:
            return make_response({"message":f"Hello, {username.capitalize()}! Happy birthday!"}, 200)
        if db_conn.isBirthday(username) != 0 and db_conn.isBirthday(username) is not None:
            return make_response({"message":f"Hello, {username.capitalize()}! Your birthday is in {db_conn.isBirthday(username)} day(s)!"}, 200)
        elif db_conn.isBirthday(username) == None:
            return make_response({"message":f"Error: User {username.capitalize()} doesn't exist."}, 400)
    except Exception as e:
        return make_response({"message":f"Error occurred {e}"}, 400)
    finally:
        db_conn.disconnect()