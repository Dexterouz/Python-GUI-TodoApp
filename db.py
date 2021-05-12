import sqlite3

class Database:
    '''Todo App Database'''

    def __init__(self, db) -> None:
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, todo_item text, created_at text, updated_at text)")
        self.conn.commit()

    def fetch(self):
        '''Fetch todo item list'''
        self.cur.execute("SELECT * FROM todos")
        rows = self.cur.fetchall()
        return rows

    def insert(self, todo):
        '''Insert new todo item'''
        self.cur.execute("INSERT INTO todos VALUES (NULL, ?, datetime('now'), datetime('now'))", (todo,))
        self.conn.commit()

    def update(self, id,todo_item):
        '''Update a todo list'''
        self.cur.execute("UPDATE todos SET todo_item = ?, updated_at = datetime('now') WHERE id = ?", (todo_item, id))
        self.conn.commit()

    def delete(self, id):
        '''Delete a todo list'''
        self.cur.execute("DELETE FROM todos WHERE id = ?", (id,))
        self.conn.commit()

    def __delattr__(self) -> None:
        '''Destructor'''
        self.conn.close()

# db = Database('store.db')
# db.insert('My programming lesson')
# print(db.fetch())