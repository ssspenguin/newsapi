from flask import Flask, request, jsonify
import sqlite3
import requests

app = Flask(__name__)

@app.route('/fetch-news')
def fetch_news():
    category = request.args.get('category')
    apiKey = ''  # Your News API key
    url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={apiKey}'
    response = requests.get(url)
    data = response.json()
    print(data)  # check API return data
    if data['status'] == 'ok':
        # connect to SQLite database
        conn = sqlite3.connect('news.db')
        cursor = conn.cursor()
        
        # put every news into the database
        for article in data['articles']:
            title = article['title']
            description = article.get('description', '沒有描述')
            url = article['url']
            category = category  # choose category into the news database
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
