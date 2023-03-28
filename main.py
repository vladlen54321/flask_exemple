from flask import Flask, request
from ut import get_password, get_requirements, get_generate_users, get_space
import sqlite3

app = Flask(__name__)

#  /dt -> dt
@app.route('/password')
def password():
    length = request.args.get('length') or '10'

    if length.isdigit():
        length = int(length)
        max_length = 200

        if length > max_length:
            return f"Max length sould be less that {max_length}"
    else:
        return f"Invalid parametr length{length}"
    
    length = int(length)
    result = get_password(length)
    return result


@app.route('/requirements/')
def requirements():
    reg = get_requirements()
    return reg


@app.route('/generate_users')
def generate_users():
    users = request.args.get('users') or '50'
    print(3424)
    if users.isdigit():
        users = int(users)
        max_user = 200
        if users > max_user:
            return f"The maximum number of users has been exceeded '{max_user}'"
    
    else:
        return f'Invalid parametr users "{users}"'
    
    users = int(users)
    result = get_generate_users(users)
    return result

@app.route('/space/')
def space():
    result = get_space()
    return f'Number cosmonaft: {str(result)}'


@app.route('/emails/create/')
def email_create():
    email = request.args['email']
    name = request.args['name']
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        INSERT INTO emails
        VALUES ('{name}', '{email}')
        '''
        cur.execute(sql)

        conn.commit()
    finally:
        conn.close()

    return 'Emails Create'

@app.route('/emails/read/')
def email_read():
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = '''
        SELECT * FROM emails;
        '''
        cur.execute(sql)
        emails = cur.fetchall()

    finally:
        conn.close()

    return str(emails)

@app.route('/emails/delete/')
def email_create_delete():
    email = request.args['email']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        DELETE FROM emails WHERE Email == '{email}';
        '''
        cur.execute(sql)

        conn.commit()
    finally:
        conn.close()

    return 'Emails Create'

@app.route('/emails/update/')
def email_create_update():
    email = request.args['email']
    name = request.args['name']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        UPDATE emails
        SET UserName = '{name}'
        WHERE Email == '{email}';
        '''
        cur.execute(sql)

        conn.commit()
    finally:
        conn.close()

    return 'Emails Create'


@app.route('/phones/create/')
def phones_create():
    phone = request.args['phone']
    name = request.args['name']
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        INSERT INTO phones
        VALUES ('{name}', '{phone}');
        '''
        cur.execute(sql)

        conn.commit()
    finally:
        conn.close()

    return 'Number Create'

@app.route('/phones/read/')
def phones_read():
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = '''
        SELECT * FROM phones;
        '''
        cur.execute(sql)
        emails = cur.fetchall()

    finally:
        conn.close()

    return str(emails)



@app.route('/phones/update/')
def phones_create_update():
    phone = request.args['phone']
    name = request.args['name']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        UPDATE phones
        SET ContactName = '{name}'
        WHERE phone == '{phone}';
        '''
        cur.execute(sql)

        conn.commit()
    finally:
        conn.close()

    return 'Name Update'


@app.route('/phones/delete/')
def phones_create_delete():
    phone = request.args['phone']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        DELETE FROM phones WHERE phone == '{phone}';
        '''
        cur.execute(sql)

        conn.commit()
    finally:
        conn.close()

    return 'phone delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)


'''

http://192.168.1.5:5000/  ?length=20&name=Dima&age=30
1      2            3   4

1. protocol
    http:// https:// ftp:// (filezilla) smtp:// amqp:// 


2. Destination. Domain, IPv4, IPv6
IPv4 
0-255.0-255.0-255.0-255
0.0.0.0 - yes
254.0.0.1 - yes
254.0.1 - no
254.0.0.0.1 - no


localhost - 127.0.0.1


3. Port - 0-65_535
0 - root
80 - http
443 - https


4. Path


Stateless
Stateful 

==
!=
>=
<=
>
<


AND
OR
NOT


CRUD

C - CREATE
R- READ
U - UPDATE
D - DELETE

'''