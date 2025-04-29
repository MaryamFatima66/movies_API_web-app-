from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OMDB_API_KEY = "ff249c2e"
OMDB_URL = "http://www.omdbapi.com/"

@app.route('/', methods=['GET', 'POST'])
def index():
    movie_data = None
    error = None

    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            params = {
                'apikey': OMDB_API_KEY,
                't': title
            }
            response = requests.get(OMDB_URL, params=params)
            data = response.json()
            if data.get("Response") == "True":
                movie_data = data
            else:
                error = "Movie not found. Try another title."
        else:
            error = "Please enter a movie title."

    return render_template('index.html', movie=movie_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
