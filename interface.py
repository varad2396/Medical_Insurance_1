from flask import Flask, jsonify, render_template, request
from utils import Medical_Insurance

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Medicle Insurance Charges Prediction")
    return render_template("home.html")
   
@app.route('/predict_charges', methods = ["POST", "GET"])
def get_insurance_charges():

    if request.method == "GET":
        print("We are using GET Method")

        age = eval(request.args.get("age"))
        gender = request.args.get("gender")
        bmi = eval(request.args.get("bmi"))
        children = eval(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        print("age, gender, bmi, children, smoker, region\n",age, gender, bmi, children, smoker, region)

        med_ins = Medical_Insurance(age, gender, bmi, children, smoker, region)
        charges = med_ins.get_predicted_price()

        return render_template("home.html", prediction = charges)
        # return jsonify({"Result" : f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})

    else:
        print("We are using POST Method")

        age = eval(request.form.get("age"))
        # age = int(request.form["age"])

        gender = request.form.get("gender")
        bmi = eval(request.form.get("bmi"))
        children = eval(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("region")

        print("age, gender, bmi, children, smoker, region\n",age, gender, bmi, children, smoker, region)

        med_ins = Medical_Insurance(age, gender, bmi, children, smoker, region)
        charges = med_ins.get_predicted_price()

        return render_template("home.html", prediction = charges)
        # return jsonify({"Result" : f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= 5005)
