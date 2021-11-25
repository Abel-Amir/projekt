import sqlite3
database = sqlite3.connect("notes_lessons.db")
sql = database.cursor()

# sql.execute(
#     """
#     CREATE TABLE schedule(
#     name TEXT,
#     day_of_the_month TEXT,
#     time TEXT,
#     lesson_plan TEXT
#     )
#     """
# )
database.commit()
def objective():
    global name, day_of_the_month, time, lesson_plan
    name = input("Введите имя:")
    day_of_the_month = input("Введите число месяца:")
    time = input("Введите время:")
    lesson_plan = input("План урока?")

    sql.execute(f"SELECT lesson_plan FROM schedule WHERE lesson_plan = '{lesson_plan}' ")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO schedule VALUES (?, ?, ?, ?)",(name,day_of_the_month,time,lesson_plan))
        database.commit()
        print("График заполнен!")

    else:
        print("График записан")
        for value in sql.execute("SELECT*FROM schedule"):
            print(value)

objective()