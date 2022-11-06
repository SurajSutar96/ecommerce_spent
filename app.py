
from flask import Flask,render_template,request,jsonify,url_for
import pickle 

app=Flask(__name__)
with open("Ecommerce.pkl",'rb') as f:
    model=pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    array=[float(x) for x in request.form.values()]
    pred=model.predict([array])[0].round(2)
    return render_template("home.html", prediction_text=f"Predicted Spent of Customer is {pred} $")
if __name__ == "__main__":
    app.run(debug=True)