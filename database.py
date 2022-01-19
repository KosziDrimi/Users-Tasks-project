def create_database(name):
    Path(name).touch()

    conn = connect(name)
    c = conn.cursor()

    c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT,
              username TEXT, email TEXT, city TEXT, phone TEXT, company TEXT)''')

    c.execute('''CREATE TABLE todos (id INTEGER PRIMARY KEY, userId INTEGER, 
              title TEXT, completed BOOL, FOREIGN KEY(userId) REFERENCES users(id))''')

    conn.close()


def load_data(url):
    return requests.get(url).json()


def prepare_users_data():
    users = load_data('https://jsonplaceholder.typicode.com/users')

    entries = []
    for user in users:
        entry = (user['id'], user['name'], user['username'], user['email'],
                 user['address']['city'], user['phone'], user['company']['name'])
        entries.append(entry)

    query = '''INSERT INTO users (id, name, username, email, city, phone, company) 
            VALUES (?, ?, ?, ?, ?, ?, ?)'''

    return entries, query


def prepare_todos_data():
    todos = load_data('https://jsonplaceholder.typicode.com/todos')

    entries = []
    for todo in todos:
        entry = (todo['id'], todo['userId'], todo['title'], todo['completed'])
        entries.append(entry)

    query = '''INSERT INTO todos (id, userId, title, completed) VALUES (?, ?, ?, ?)'''

    return entries, query


def add_data_to_database(data, db_name):
    conn = connect(db_name)
    c = conn.cursor()
    entries = data[0]
    query = data[1]

    for entry in entries:
        c.execute(query, entry)
        conn.commit()

    conn.close()


if __name__ == "__main__":
    from pathlib import Path
    from sqlite3 import connect
    import requests

    create_database('database.sqlite')
    add_data_to_database(prepare_users_data(), 'database.sqlite')
    add_data_to_database(prepare_todos_data(), 'database.sqlite')
