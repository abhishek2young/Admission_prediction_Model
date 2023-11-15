from flask import Flask,redirect,render_template,request,url_for,jsonify
import pickle

app=Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict",methods=["POST"])
def predict_Chance_of_admit():
    
    with open("Admission model.pkl","rb") as f:
        ml_model=pickle.load(f)

    data = request.form
    print("Data is :",data)

    GRE_Score=int(data["GRE_Score"])
    TOEFL_Score=int(data["TOEFL_Score"])
    University_Rating=int(data["University_Rating"])
    SOP=float(data["SOP"])
    LOR=float(data["LOR"])
    CGPA=float(data["CGPA"])
    Research=int(data["Research"])

    result=ml_model.predict([[GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research]])

    return jsonify({"Result":f"Chances of Admission are {result}"})

if __name__=='__main__':
    app.run(debug=True)
