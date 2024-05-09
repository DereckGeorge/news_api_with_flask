from flask import Flask
from flask_restful import Api, Resource, reqparse
import requests

app = Flask(__name__)
api = Api(app)

class News(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('source', type=str, help='News source name')
        args = parser.parse_args()
        source = args['source']
        if not source:
            return {'message': 'Please provide a news source name'}, 400
        
        # Fetching news
        url = f'https://newsapi.org/v2/top-headlines?sources={source}&apiKey=YOUR_API_KEY'
        response = requests.get(url)
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get('articles', [])
            return {'articles': articles}
        else:
            return {'message': 'Failed to fetch news'}, 500

api.add_resource(News, '/news')

if __name__ == '__main__':
    app.run(debug=True)
