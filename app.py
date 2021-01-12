from flask import Flask, render_template, request
import joblib,pickle
import numpy as np


from flask import Flask,render_template

app=Flask(__name__,template_folder='template')

app = Flask(__name__)
# Load the Random Forest model
model = joblib.load('credit_card_approval.pkl' )


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Gender = (request.form['Gender'])
    Age = float(request.form['Age'])
    Debt = float(request.form['Debt'])
    Married = (request.form['Married'])
    BankCustomer = (request.form['BankCustomer'])
    EducationLevel = (request.form['EducationLevel'])
    Ethnicity = (request.form['Ethnicity'])
    YearsEmployed = float(request.form['YearsEmployed'])
    PriorDefault = (request.form['PriorDefault'])
    CreditScoreAge = (request.form['CreditScore'])
    DriversLicense = (request.form['DriversLicense'])
    Citizen = (request.form['Citizen'])
    Income = (request.form['Income'])


    data = [[Gender, Age, Debt, Married, BankCustomer, EducationLevel,Ethnicity, YearsEmployed,PriorDefault,CreditScoreAge,
    DriversLicense,Citizen,Income]]
    prediction = model.predict(data)
    
    prediction = model.predict(data)

    if prediction == 0:
        return render_template('index.html', prediction_text='Eligible for CC')

    else:
        return render_template('index.html', prediction_text='Not eligible for CC')


if __name__ == "__main__":
    app.run(debug=True)