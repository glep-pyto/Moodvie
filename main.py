from Flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
        # You can pass data to your HTML template
        title = "Moodvie"
        message = "Welcome to Moodvie, select a mood."
        return render_template('homepage.html', title=title, message=message)

if __name__ == '__main__':
        app.run(debug=True)