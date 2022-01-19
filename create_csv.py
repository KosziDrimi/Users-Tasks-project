def create_tasks_data(db_name):

    conn = connect(db_name)
    c = conn.cursor()
    c.execute('''SELECT u.name, u.city, t.title, t.completed FROM users AS u JOIN todos AS t ON u.id = t.userId''')
    tasks = c.fetchall()
    tasks = [list(task) for task in tasks]
    fields = ['name', 'city', 'title', 'completed']
    conn.close()

    return tasks, fields


def create_csv_file(data, filename):
    todos = data[0]
    fields = data[1]

    tasks = []
    for task in todos:
        task[3] = bool(task[3])
        tasks.append(task)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows(tasks)


if __name__ == "__main__":
    from sqlite3 import connect
    import csv

    create_csv_file(create_tasks_data('database.sqlite'), 'users_tasks.csv')
