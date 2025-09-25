from flask import Flask, render_template, request
from movie_data import happy_movies, sad_movies, fear_movies, surprised_movies

app = Flask(__name__)

@app.route('/')
def home():
    title = "Moodvie"
    message = "Welcome to Moodvie, select a mood."
    return render_template('homepage.html', title=title, message=message)

@app.route('/select')
def select():
    return render_template('select_mood.html')

@app.route('/results', methods=['POST'])
def results():
    # get mood from the hidden input in select_mood.html
    mood = request.form.get("mood")

    if mood == "happy":
        movies = happy_movies
    elif mood == "sad":
        movies = sad_movies
    elif mood == "fear":
        movies = fear_movies
    elif mood == "surprised":   # careful: HTML button has "surprised"
        movies = surprised_movies
    else:
        movies = []

    return render_template('result.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
