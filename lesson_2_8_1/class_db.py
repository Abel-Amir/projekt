import random
import sqlite3

database = sqlite3.connect("server_user.sqlite3")
sql = database.cursor()

# sql.execute(
#     """
#     CREATE TABLE users(
#     login TEXT,
#     password TEXT,
#     email TEXT,
#     cash INT
#     )
#     """
# )
#
# database.commit()
def register():
    global user_login, user_password, email
    user_login = input("Login: ")
    user_password = input("Password: ")
    email = input("Email: ")
    sql.execute("SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?,?)",
                (user_login, user_password, email, 0))

        database.commit()
        print("User Registered ! Congrats!")
    else:
        print("User already exists!")
        for value in sql.execute("SELECT * FROM users"):
            print(value)

def black_jack():
    user_login = input("Log in: ")
    number = random.randint(1,2)
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print("User is not exists< register please")
        register()
    else:
        if number == 1:
            sql.execute(f"UPDATE users SET cash = {120} WHERE login = '{user_login}'")
            print("You win!")
        else:
            print("You lose monye")
black_jack()