from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    # Run the app on localhost:5000
    app.run(debug=True)