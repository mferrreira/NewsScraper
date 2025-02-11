from flask import Flask, jsonify, request
from scraper import scrape_news
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/api/news', methods=['GET'])
def get_news():
    # Pega a lista de notícias do scraper
    news = scrape_news()
    return jsonify(news)

@app.route('/api/search', methods=['GET'])
def search_news():
    query = request.args.get('query', '')
    if not query:
        return jsonify({"message": "No query provided!"}), 400

    # Filtra as notícias com base na consulta
    news = scrape_news()
    filtered_news = [item for item in news if query.lower() in item['title'].lower() or query.lower() in item['description'].lower()]

    return jsonify(filtered_news)

if __name__ == '__main__':
    app.run(debug=True)
