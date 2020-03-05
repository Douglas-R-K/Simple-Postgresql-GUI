import psycopg2

conn = psycopg2.connect(dbname='', host='', user='', password='')
cur = conn.cursor()


def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS employees ( id BIGSERIAL PRIMARY KEY, first_name VARCHAR(50),'
                ' last_name VARCHAR(50), gender VARCHAR(50), birth_date DATE, job VARCHAR(50), email VARCHAR(50), '
                'salary VARCHAR(50), hired_date DATE, warning_strike INT )')

def fetch_data():
    cur.execute('SELECT * FROM employee_id')
    rows = cur.fetchall()
    return rows


def insert_data(first_name,last_name, gender, birth_date, job, email, salary,hired_date, warning_strike):
    cur.execute('INSERT INTO employee_id (first_name,last_name, gender, birth_date, job, email, salary,hired_date,'
                ' warning_strike) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (first_name, last_name, gender,
                birth_date, job, email, salary, hired_date, warning_strike))
    conn.commit()


def remove_data(id):
    cur.execute('DELETE FROM employee_id WHERE id=%s', (id,))
    conn.commit()


def update_data(first_name, last_name, gender, birth_date, job, email, salary, hired_date, warning_strike, id):
    cur.execute('UPDATE employee_id SET first_name=%s, last_name=%s, gender=%s, birth_date=%s, job=%s, email=%s,'
                'salary=%s, hired_date=%s, warning_strike=%s WHERE id=%s',
                (first_name, last_name, gender, birth_date, job, email, salary, hired_date, warning_strike, id))
    conn.commit()


def order_by_id():
    cur.execute('SELECT * FROM employee_id ORDER BY id')
    rows = cur.fetchall()
    return rows


def order_by_name():
    cur.execute('SELECT * FROM employee_id ORDER BY first_name')
    rows = cur.fetchall()
    return rows


def order_by_salary():
    cur.execute('SELECT * FROM employee_id ORDER BY salary DESC')
    rows = cur.fetchall()
    return rows


def order_by_job():
    cur.execute('SELECT * FROM employee_id ORDER BY job')
    rows = cur.fetchall()
    return rows


def search_by_name(first_name_entry, last_name_entry):
    cur.execute('SELECT * FROM employee_id WHERE first_name ILIKE %s AND last_name ILIKE %s',
                (first_name_entry, last_name_entry))
    rows = cur.fetchall()
    return rows


def close_connection():
    conn.close()


fetch_data()
