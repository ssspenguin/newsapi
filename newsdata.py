from flask import Flask, request, jsonify
import sqlite3
import requests

app = Flask(__name__)

@app.route('/fetch-news')
def fetch_news():
    category = request.args.get('category')
    apiKey = 'f446cbb0c08f4b33b48317e568e702fb'  # 替換為你的 News API 金鑰
    url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={apiKey}'
    response = requests.get(url)
    data = response.json()
    print(data)  # 檢查 API 返回的完整數據
    if data['status'] == 'ok':
        # 連接到 SQLite 資料庫
        conn = sqlite3.connect('news.db')
        cursor = conn.cursor()
        
        # 將每篇新聞插入資料庫
        for article in data['articles']:
            title = article['title']
            description = article.get('description', '沒有描述')
            url = article['url']
            category = category  # 將選擇的類型也存入資料庫
            print(title, description, url, category)
            try:
                cursor.execute('''INSERT INTO news (title, description, url, category) VALUES (?, ?, ?, ?)''', (title, description, url, category))
                print(f'Inserted article: {title}')
            except sqlite3.Error as e:
                print(f'An error occurred while inserting article: {e}')
    
        conn.commit()
        print('News successfully committed to the database')
        conn.close()
        return jsonify(success=True, articles=data['articles'])
    else:
        return jsonify(success=False, message=data.get('message', '未知錯誤'))

if __name__ == '__main__':
    app.run(debug=True)
