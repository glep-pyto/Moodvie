from flask import Flask, render_template
from movie_data import 

app = Flask(__name__)

@app.route('/')
def home():
        # You can pass data to your HTML template
        title = "Moodvie"
        message = "Welcome to Moodvie, select a mood."
        return render_template('homepage.html', title=title, message=message)
@app.route('/select')
def select():
   return render_template('select_mood.html')  
@app.route('/results', methods=['GET','POST'])
def results():
   return render_template('results.html')  



if __name__ == '__main__':
        app.run(debug=True)

