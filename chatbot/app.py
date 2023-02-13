from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from bot import response_from_user

#app = Flask(__name__, template_folder='/Users/sn/Desktop/ChatBot/frontend')
app = Flask(__name__)
CORS(app)

#@app.route("/")
#def home():
#    return 'home'

#@app.route('/') # Homepage
#def home():
    #return render_template('/Users/sn/Desktop/ChatBot/frontend')

# simple API which allows user input to be carried on to NN
#@app.post("/predict")
#@app.post('/')
#@app.route('/home')
#@app.route('/predict')
@app.route("/", methods=['GET',"POST"])
def predict():
    text = request.get_json().get('message')
    if text is None:     
        print("request returned None") 
    else:   
        print("doing somethings")
    print('message')
    #text = request.data.get('message')
    response = response_from_user(text)
    msg = {"answer": response}
    return jsonify(msg)

if __name__ == "__main__":
    #app.run(debug=True ,port=5000,use_reloader=False)
    #app.run(port=5000, debug=True)
    app.run(debug=True)