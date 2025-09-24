from flask import Flask, render_template
from movie_data import happy_movies,sad_movies,fear_movies,suprised_movies 
#import a flask module and database from moviedata file
#flask is python module used to interact with internet files, mainly html similar to Django
app = Flask(__name__)

@app.route('/')
def home():
        # You can pass data to your HTML template
        title = "Moodvie"
        message = "Welcome to Moodvie, select a mood."
        return render_template('homepage.html', title=title, message=message)
@app.route('/select')#when the button is pressed in homepage, it redirects to selections
def select():
   return render_template('select_mood.html')  
@app.route('/results', methods=['GET','POST'])
#GET receives data from the server, in this case from selectmood html
#POST enables data to be sent over to server
def results():
   return render_template('results.html')  



if __name__ == '__main__':
        app.run(debug=True)

