import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123' - ##OWASP A02 – Cryptographic Failures.
}

def get_user_input():
    user_input = input('Enter your name: ') ##OWASP A04 – Insecure Design
    return user_input

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}') ##OWASP A03 – Injection

def get_data():
    url = 'http://insecure-api.com/get-data' ##OWASP A02 – Cryptographic Failures
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')" ##OWASP A03 – Injection
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
