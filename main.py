from flask import Flask, render_template, request, jsonify, abort
from utils.scrape import get_condo_detail
# Create a Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=["GET","POST"])
async def root():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        try:
            get_condo_detail()
            return jsonify({
                "message" : "hello"
            })
            # return jsonify({
            #     "message" : get_condo_detail()
            # })
        except Exception as e:
            return str(e), 400
if __name__ == '__main__':
    # Run the app on localhost:5000
    app.run(debug=True)