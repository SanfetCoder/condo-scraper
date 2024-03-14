from flask import Flask, render_template, request, jsonify, abort
from utils.scrape import get_condo_detail
# Create a Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=["GET","POST"])
def root():
    if request.method == "GET":
        try:
            province = request.args.get('province')
            print(province)
            condos = get_condo_detail(province) if province is not None else []
            print(condos)
            return render_template('index.html', condos = condos)
        except Exception as e:
            return str(e), 400
        
      
