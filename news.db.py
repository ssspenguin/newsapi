import sqlite3

# 連接到 SQLite 資料庫
conn = sqlite3.connect('news.db')
cursor = conn.cursor()

# 用三個引號包裹 SQL 語句，這樣可以寫多行的 SQL 指令
cursor.execute('''
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        url TEXT NOT NULL,
        category TEXT NOT NULL
    )
''')

# 連接到 SQLite 資料庫
conn = sqlite3.connect('news.db')
cursor = conn.cursor()

# 執行查詢語句，從 news 表中獲取所有數據
cursor.execute("SELECT * FROM news")

# 使用 fetchall() 獲取所有的查詢結果
rows = cursor.fetchall()

# 遍歷每一行結果，row 現在已經被定義了
for row in rows:
    print(row)  # 這裡可以用 row 變量處理每一行的數據

conn.close()





