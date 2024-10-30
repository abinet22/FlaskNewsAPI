from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual NewsAPI key
NEWS_API_KEY = '93246a58a2c54ed7adbc7dea37e8cc3a'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

@app.route('/')
def index():
    query = request.args.get('query', '')
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'us',  # Change to your preferred country code
        'q': query
    }
    response = requests.get(NEWS_API_URL, params=params)
    articles = response.json().get('articles', [])
    return render_template('index.html', articles=articles, query=query)

if __name__ == '__main__':
    app.run(debug=True)
