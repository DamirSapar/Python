import psycopg2
from config import load_config

def create_tables():
    commands = (
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            FOREIGN KEY (user_id)
                REFERENCES users (id)
                ON DELETE CASCADE
        )
        """
    )
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            for command in commands:
                cur.execute(command)
        conn.commit()

def get_or_create_user(username):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            if user:
                user_id = user[0]
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                user_id = cur.fetchone()[0]
            conn.commit()
    return user_id

def get_user_level(user_id):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT MAX(level) FROM user_scores WHERE user_id = %s", (user_id,))
            level = cur.fetchone()[0]
            if level is None:
                return 1
            else:
                return level

def save_score(user_id, score, level):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_scores (user_id, score, level)
                VALUES (%s, %s, %s)
            """, (user_id, score, level))
        conn.commit()

if __name__ == '__main__':
    create_tables()
    
    username = input("Введите ваше имя: ")
    user_id = get_or_create_user(username)
    user_level = get_user_level(user_id)

    print(f"Добро пожаловать, {username}! Ваш текущий уровень: {user_level}")

    pause = input("Нажмите 'p', чтобы поставить игру на паузу и сохранить результат: ")
    if pause.lower() == 'p':
        score = int(input("Введите ваш текущий счёт: "))
        save_score(user_id, score, user_level)
        print("Ваш прогресс сохранен!")
