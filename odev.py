from mysql.connector import errorcode
import mysql.connector
import os
import configparser
import logging
from flask import Flask,jsonify,request, make_response



dir_path = os.path.dirname(os.path.realpath(__file__))
config =configparser.ConfigParser()
config.read(f'{dir_path}/odev.cfg')
logging.basicConfig(filename=config['LOGGING']['log_file'], level = config['LOGGING']['log_level'])

app = Flask(__name__)


def connect():
    return mysql.connector.connect(
        user = config['MYSQL']['mysql_user'],
        password = config['MYSQL']['mysql_password'],
        host = config['MYSQL']['mysql_host'],
        database = config['MYSQL']['mysql_database'],
        auth_plugin='mysql_native_password'
    )

@app.route("/Select", methods=['GET'])
def select():
    try:
        mysqldb = connect()
        cursor = mysqldb.cursor(buffered=True)
        query = f"SELECT * FROM {config['MYSQL']['mysql_database']}.{config['MYSQL']['mysql_table']};"
        cursor.execute(query)
        response= jsonify(cursor.fetchall())
        mysqldb.close()
    except mysql.connector.Error as e:
        if(e.errno == errorcode.ER_ACCESS_DENIED_ERROR):
            logging.error(str(e))
            return make_response(("AUTH ERROR! PLEASE CHECK LOG FILE."),401)

        elif(e.errno == errorcode.ER_BAD_DB_ERROR):
            logging.error(str(e))
            return make_response(("DB NOT EXIST! PLEASE CHECK LOG FILE."),404)

        else:
            logging.error(str(e))
            return make_response(("SOME ERROR OCCURED! PLEASE CHECK LOG FILE."),400)

    return (response)



@app.route("/Insert", methods=['POST','PUT'])
def insert ():
    json_object = request.get_json()
    name =json_object["name"]
    surname =json_object["surname"]
    email =json_object["email"]
    
    try:
        mysqldb = connect()
        cursor = mysqldb.cursor(buffered=True)
        query = f'''INSERT INTO {config['MYSQL']['mysql_database']}.{config['MYSQL']['mysql_table']}
        (name, surname, email) VALUES ('{name}','{surname}','{email}');'''
        cursor.execute(query)
        mysqldb.commit()
        mysqldb.close()
    except mysql.connector.Error as e:
        if(e.errno == errorcode.ER_ACCESS_DENIED_ERROR):
            logging.error(str(e))
            return make_response(("AUTH ERROR! PLEASE CHECK LOG FILE."),401)
            
        elif(e.errno == errorcode.ER_BAD_DB_ERROR):
            logging.error(str(e))
            return make_response(("DB NOT EXIST! PLEASE CHECK LOG FILE."),404)

            
        else:
            logging.error(str(e))
            return make_response(("SOME ERROR OCCURED! PLEASE CHECK LOG FILE."),400)

        
    return('SUCCES!')

@app.route("/Delete", methods=['DELETE'])
def delete():
    json_object = request.get_json()
    number =json_object["number"]
    try:
        mysqldb = connect()
        cursor = mysqldb.cursor(buffered=True)
        query = f'''DELETE FROM {config['MYSQL']['mysql_database']}.{config['MYSQL']['mysql_table']} WHERE id = {number};'''
        cursor.execute(query)
        mysqldb.commit()
        mysqldb.close()
    except mysql.connector.Error as e:
        if(e.errno == errorcode.ER_ACCESS_DENIED_ERROR):
            logging.error(str(e))
            return make_response(("AUTH ERROR! PLEASE CHECK LOG FILE."),401)
            
        elif(e.errno == errorcode.ER_BAD_DB_ERROR):
            logging.error(str(e))
            return make_response(("DB NOT EXIST! PLEASE CHECK LOG FILE."),404)

            
        else:
            logging.error(str(e))
            return make_response(("SOME ERROR OCCURED! PLEASE CHECK LOG FILE."),400)


    return('SUCCES!')

if __name__ == "__main__":
    app.run(host=config['API SERVER']['odev_host'], port=config['API SERVER']['odev_port'], debug=False)












