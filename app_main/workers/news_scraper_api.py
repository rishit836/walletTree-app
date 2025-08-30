from flask import Flask,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    response={
        "message":"the api is working perfectly fine."
    }
    return jsonify(response)

def _execute_api_():
    app.run(port=1232,debug=True)

    

        
        
