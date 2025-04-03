from app import application
from flask import *
from app.models import *
import numpy as np
from flask_bcrypt import Bcrypt
from Loan_APP.pipeline.prediction import PredictionPipeline
import os

# model = pickle.load(open('model.pkl', 'rb')) ## rb :- read binary

bcrypt = Bcrypt(application)

@application.route('/')
def home():
    return render_template('home.html')

@application.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
            
        isUserPresent = User.query.with_entities(User.email).filter_by(email=email).first()

        if isUserPresent:
            try:
                user = User.query.filter_by(email=email).first()
                
                if bcrypt.check_password_hash(user.password, password):  # If user exists
                    session['user_id'] = user.user_id
                    return redirect(url_for('predict'))
                else:
                    return render_template('login.html', message = 'notValid')  
            except Exception as e:
                print(f"Error during login: {e}")
                return render_template('login.html', message='An error occurred. Please try again.')
        else:
            return render_template('login.html', message = 'notRegistered')

@application.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':    
        return render_template('register.html')
    
    elif request.method == 'POST':
        try:
            full_name = request.form['full_name']
            email = request.form['email']
            password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            
            user = User(full_name, email, password)
            
            isUserPresent = User.query.filter_by(email=user.email).first()
            
            if isUserPresent:  # If user exists
                return render_template('login.html', message='error')
            else:
                db.session.add(user)
                db.session.commit()
                return render_template('login.html', message = 'success')
        except:
            return render_template('500.html')
            
@application.route('/train', methods = ['GET'])
def training():
    os.system("python main.py")
    return "Training Successfull!"


@application.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        if session.get('user_id'):
            return render_template('predict.html')
        else:
            return render_template('401.html')
    
    elif request.method == 'POST':
        if session.get('user_id'):
            try:
                data1 = request.form['gender']
                data2 = request.form['married']
                data3 = request.form['dependents']
                data4 = request.form['education']
                data5 = request.form['self_employed']
                data6 = request.form['applicant_income']
                data7 = request.form['coapplicant_income']
                data8 = request.form['loan_amount']
                data9 = request.form['loan_amount_tenure']
                data10 = request.form['credit_history']
                data11 = request.form['property_area']
                
                if not all([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]):
                    raise ValueError("All fields must be filled out.")
                
                arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]], dtype=float)
                # print(arr)
                obj = PredictionPipeline()
                pred = obj.predict(arr)
                # print("Output value is", pred)
                # pred = model.predict(arr)
                return render_template('predict.html', data=pred)
            
            except ValueError as e:
                return render_template('400.html', error_message="Invalid input type. Please enter valid numbers."), 400
        else:
            return render_template('401.html')

@application.route('/logout')
def logout():
    try:
        if session.get('user_id'):
            session.pop('user_id', None)
            return redirect(url_for('home'))
        else:
            return render_template('500.html') 
    except Exception as e:
        return render_template('500.html')

@application.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@application.errorhandler(400)
def bad_request_error(e):
    return render_template('400.html', error_message="Bad Request: Please check your input."), 400
