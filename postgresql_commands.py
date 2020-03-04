import psycopg2

conn = psycopg2.connect(dbname='ENTER DB NAME', host='ENTER HOST', user='USER', password='PASSWORD')
cur = conn.cursor()


def fetch_data():
    cur.execute('SELECT * FROM employee_id')
    rows = cur.fetchall()
    return rows


def insert_data(first_name,last_name, gender, birth_date, job, email, salary,hired_date, warning_strike):
    cur.execute('INSERT INTO employee_id (first_name,last_name, gender, birth_date, job, email, salary,hired_date, '
                'warning_strike) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (first_name, last_name, gender, birth_date, job, email, salary, hired_date, warning_strike))
    conn.commit()


def remove_data(id):
    cur.execute('DELETE FROM employee_id WHERE id=%s', (id,))
    conn.commit()


def update_data(first_name, last_name, gender, birth_date, job, email, salary, hired_date, warning_strike, id):
    cur.execute('UPDATE employee_id SET first_name=%s, last_name=%s, gender=%s, birth_date=%s, job=%s, email=%s,'
                'salary=%s, hired_date=%s, warning_strike=%s WHERE id=%s',
                (first_name, last_name, gender, birth_date, job, email, salary, hired_date, warning_strike, id))
    conn.commit()


def close_connection():
    conn.close()


fetch_data()
