from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)
api = Api(app)

# Load environment variables from a .env file
load_dotenv()

class News(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('source', type=str, help='News source name')
        args = parser.parse_args()
        source = args['source']
        if not source:
            return {'message': 'Please provide a news source name'}, 400
        
        # Fetching news
        api_key = os.getenv("NEWS_API_KEY")
        if not api_key:
            return {'message': 'API key is missing'}, 500
        
        url = f'https://newsapi.org/v2/top-headlines?sources={source}&apiKey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get('articles', [])
            return {'articles': articles}
        else:
            return {'message': 'Failed to fetch news from News API'}, 500

api.add_resource(News, '/news')

if __name__ == '__main__':
    app.run(debug=True)
