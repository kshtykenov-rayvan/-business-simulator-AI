import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            print(f"Подключено к базе данных: {db_file}")
            return conn
        except sqlite3.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
            return None

    def list_tables(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            return [table[0] for table in tables]
        except sqlite3.Error as e:
            print(f"Ошибка получения списка таблиц: {e}")
            return []

    def search_in_table(self, table_name):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"Ошибка поиска в таблице {table_name}: {e}")

    def terminal_menu(self):
        while True:
            print("\nМеню:")
            print("1. Найти данные в таблице")
            print("2. Показать список таблиц")
            print("3. Выход")

            choice = input("Введите номер команды: ")

            if choice == "1":
                tables = self.list_tables()
                if tables:
                    print("Доступные таблицы:")
                    for i, table in enumerate(tables, start=1):
                        print(f"{i}. {table}")

                    table_choice = input("Введите имя таблицы: ")
                    if table_choice in tables:
                        self.search_in_table(table_choice)
                    else:
                        print("Таблица не найдена.")
                else:
                    print("Нет доступных таблиц.")
            elif choice == "2":
                tables = self.list_tables()
                if tables:
                    print("Список таблиц:")
                    for table in tables:
                        print(table)
                else:
                    print("Нет доступных таблиц.")
            elif choice == "3":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    def close_connection(self):
        if self.conn:
            self.conn.close()


def main():
    database = "/home/harris/Документы/GitHub/-business-simulator-AI/BusinessSimulatorAI/db.sqlite3"
    db_manager = DatabaseManager(database)

    if db_manager.conn:
        db_manager.terminal_menu()
        db_manager.close_connection()

if __name__ == '__main__':
    main()
