from flask import Flask, render_template,request,redirect,url_for,flash
import warnings
warnings.filterwarnings('ignore')
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask_login import login_required,LoginManager, UserMixin, login_user, logout_user, current_user
import numpy as np
import pandas as pd
from datetime import datetime
import crops
import time
import matplotlib.pyplot as plt
import io
import base64
import random
import pymongo
from pymongo import MongoClient
import os
from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from mlxtend.evaluate import bias_variance_decomp
from bson.objectid import ObjectId
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["TEMPLATES_AUTO_RELOAD"] = True
port = int(os.environ.get('PORT', 5000))
app.secret_key = "secret_key" # Change this to your own secret key
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flask_login'
mongo = PyMongo(app)
#connecting to db
client = MongoClient('localhost', 27017)
db = client.dataset
test_db = client["test_data"]
#getting data from db
def getDataFromDb(data,fileName):
    cursor = data.find()
    mongo_docs = list(cursor)
#print(mongo_docs)
    #print ("total docs:", len(mongo_docs))
    docs = pd.DataFrame(columns=[])
    for num, doc in enumerate(mongo_docs):
        doc["_id"] = str(doc["_id"])
        doc_id = doc["_id"]
        series_obj = pd.Series( doc, name=doc_id )
        docs = docs.append(series_obj)
    docs.to_csv(os.path.join('./static',fileName)) # CSV
    csv_export = docs.to_csv(sep=",",path_or_buf="../static")
    return csv_export

getDataFromDb(db.arhar,"Arhar.csv")
getDataFromDb(db.bajra,"Bajra.csv")
getDataFromDb(db.barley,"Barley.csv")
getDataFromDb(db.copra,"Copra.csv")
getDataFromDb(db.cotton,"Cotton.csv")
getDataFromDb(db.gram,"Gram.csv")
getDataFromDb(db.groundnut,"Groundnut.csv")
getDataFromDb(db.jowar,"Jowar.csv")
getDataFromDb(db.jute,"Jute.csv")
getDataFromDb(db.maize,"Maize.csv")
getDataFromDb(db.masoor,"Masoor.csv")
getDataFromDb(db.moong,"Moong.csv")
getDataFromDb(db.niger,"Niger.csv")
getDataFromDb(db.paddy,"Paddy.csv")
getDataFromDb(db.ragi,"Ragi.csv")
getDataFromDb(db.rape,"Rape.csv")
getDataFromDb(db.soyabean,"Soyabean.csv")
getDataFromDb(db.sugarcane,"Sugarcane.csv")
getDataFromDb(db.sunflower,"Sunflower.csv")
getDataFromDb(db.urad,"Urad.csv")
getDataFromDb(db.wheat,"Wheat.csv")

cors = CORS(app, resources={r"/ticker": {"origins": "http://localhost:port"}})

commodity_dict = {
    "arhar": "static/Arhar.csv",
    "bajra": "static/Bajra.csv",
    "barley": "static/Barley.csv",
    "copra": "static/Copra.csv",
    "cotton": "static/Cotton.csv",
    "gram": "static/Gram.csv",
    "groundnut": "static/Groundnut.csv",
    "jowar": "static/Jowar.csv",
    "maize": "static/Maize.csv",
    "masoor": "static/Masoor.csv",
    "moong": "static/Moong.csv",
    "niger": "static/Niger.csv",
    "paddy": "static/Paddy.csv",
    "ragi": "static/Ragi.csv",
    "rape": "static/Rape.csv",
    "jute": "static/Jute.csv",
    "soyabean": "static/Soyabean.csv",
    "sugarcane": "static/Sugarcane.csv",
    "sunflower": "static/Sunflower.csv",
    "urad": "static/Urad.csv",
    "wheat": "static/Wheat.csv"
}
annual_rainfall = [29, 21, 37.5, 30.7, 52.6, 150, 299, 251.7, 179.2, 70.5, 39.8, 10.9]
base = {
    "Paddy": 1245.5,
    "Arhar": 3200,
    "Bajra": 1175,
    "Barley": 980,
    "Copra": 5100,
    "Cotton": 3600,
    "Gram": 2800,
    "Groundnut": 3700,
    "Jowar": 1520,
    "Maize": 1175,
    "Masoor": 2800,
    "Moong": 3500,
    "Niger": 3500,
    "Ragi": 1500,
    "Rape": 2500,
    "Jute": 1675,
    "Soyabean": 2200,
    "Sugarcane": 2250,
    "Sunflower": 3700,
    "Urad": 4300,
    "Wheat": 1350

}
commodity_list = []

class Commodity:

    def __init__(self, csv_name):
        #print(self)
        self.name = csv_name
        dataset = pd.read_csv(csv_name)
        self.X = dataset.iloc[:,2:-1].values
        self.Y = dataset.iloc[:, 5].values#wpi column
        from sklearn.model_selection import train_test_split
        X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y, 
        test_size=0.1, random_state=0)
        # Fitting decision tree regression to dataset
        from sklearn.tree import DecisionTreeRegressor
        depth = random.randrange(7,18)
        self.regressor = DecisionTreeRegressor(max_depth=depth)
        self.regressor.fit(self.X, self.Y)
        y_pred_tree = self.regressor.predict(X_test)
        # Compute the accuracy
        y_pred = self.regressor.predict(X_test)
        mse = mean_squared_error(Y_test, y_pred)
        print(mse)
        r2 = r2_score(Y_test, y_pred)
        print(r2)
        accuracy = f"MSE: {mse:.2f}, R2: {r2:.2f}"
        avg_expected_loss, avg_bias, avg_var = bias_variance_decomp(
        tree, X_train, y_train, X_test, y_test, 
        loss='0-1_loss',
        random_seed=123)
        print('Average expected loss: %.3f' % avg_expected_loss)
        print('Average bias: %.3f' % avg_bias)
        print('Average variance: %.3f' % avg_var)

    def evaluate_regression_model(Y_test, y_pred_tree):
        mse = mean_squared_error(Y_test, y_pred_tree)
        r2 = r2_score(Y_test, y_pred_tree)
        print("value is",r2)
        return mse
    def getPredictedValue(self, value):
        #print(self)
        if value[1]>=2019:
            fsa = np.array(value).reshape(1, 3)
            #print(" ",self.regressor.predict(fsa)[0])
            return self.regressor.predict(fsa)[0]
        else:
            c=self.X[:,0:2]
            x=[]
            for i in c:
                x.append(i.tolist())
            fsa = [value[0], value[1]]
            ind = 0
            for i in range(0,len(x)):
                if x[i]==fsa:
                    ind=i
                    break
            #print(index, " ",ind)
            #print(x[ind])
            #print(self.Y[i])
            return self.Y[i]

    def getCropName(self):
        a = self.name.split('.')
        return a[0]
@app.route('/')
def index():
    context = {
        "top5": TopSeverWinners(),
        "bottom5": TopSevenLosers(),
        "sixmonths": SixMonthsForecast(),
    }
    return render_template('index.html', context=context)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form values
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        existing_user = mongo.db.users.find_one({'email': email})
        if existing_user:
            return 'That email address is already in use'

        # Insert new user into database
        mongo.db.users.insert_one({'name': name, 'email': email, 'password': password})

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form values
        email = request.form['email']
        password = request.form['password']

        # Check if user exists and password is correct
        user = mongo.db.users.find_one({'email': email, 'password': password})
        if user:
            # User logged in successfully
            session['user'] = user['name']
            return redirect(url_for('dashboard'))

        # Invalid email or password
        return 'Invalid login credentials'

    return render_template('login.html')

@app.route('/dashboard')

def dashboard():
    message = request.args.get('message')  # Get the message parameter from the URL
    if 'user' in session:
        collections = test_db.list_collection_names()
        return render_template('dashboard.html', user=session['user'], message=message, collections=collections)
    # User not logged in
    return redirect(url_for('login'))

@app.route('/delete/<collection_name>', methods=['POST'])
def delete_collection(collection_name):
    # Check if collection exists
    if collection_name not in test_db.list_collection_names():
        return f"Collection '{collection_name}' does not exist in the database"

    # Delete collection
    test_db[collection_name].drop()

    # Redirect back to dashboard
    flash(f"Collection '{collection_name}' deleted successfully!", "success")
    return redirect(url_for('dashboard'))

@app.route('/upload', methods=['POST'])
def upload_csv():
    # Get the uploaded file from the request object
    file = request.files["file"]

    # Read CSV data into a pandas DataFrame
    df = pd.read_csv(file)

    # Extract collection name from file name
    collection_name = file.filename.split(".")[0]

     # Check if collection already exists
    if collection_name in test_db.list_collection_names():
        return redirect(url_for('dashboard',message=f"Collection '{collection_name}' already exists in the database"))

    # Insert data into MongoDB
    collection = test_db[collection_name]
    collection.insert_many(df.to_dict("records"))
    # Return a success message
    # return "Data uploaded successfully!"
    # Redirect to dashboard
    return redirect(url_for('dashboard',message=f"{collection_name} uploaded successfully"))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/commodity/<name>')
def crop_profile(name):
    max_crop, min_crop, forecast_crop_values = TwelveMonthsForecast(name)
    prev_crop_values = TwelveMonthPrevious(name)
    two_prev_values = year2021(name)
    year2020Predic = year2020Predict(name)
    forecast_x = [i[0] for i in forecast_crop_values]
    forecast_y = [i[1] for i in forecast_crop_values]
    previous_x = [i[0] for i in prev_crop_values]
    previous_y = [i[1] for i in prev_crop_values]
    current_price = CurrentMonth(name)
    #print(max_crop)
    #print(min_crop)
    #print(forecast_crop_values)
    #print(prev_crop_values)
    #print(str(forecast_x))
    crop_data = crops.crop(name)
    context = {
        "name":name,
        "max_crop": max_crop,
        "min_crop": min_crop,
        "forecast_values": forecast_crop_values,
        "forecast_x": str(forecast_x),
        "forecast_y":forecast_y,
        "previous_values": prev_crop_values,
        "twoyear_prev_values":two_prev_values,
        "predict2020":year2020Predic,
        "previous_x":previous_x,
        "previous_y":previous_y,
        "current_price": current_price,
        "image_url":crop_data[0],
        "prime_loc":crop_data[1],
        "type_c":crop_data[2],
        "export":crop_data[3]
    }
    return render_template('commodity.html', context=context)
TEMPLATES_AUTO_RELOAD = True
@app.route('/ticker/<item>/<number>')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def ticker(item, number):
    n = int(number)
    i = int(item)
    data = SixMonthsForecast()
    context = str(data[n][i])

    if i == 2 or i == 5:
        context = 'TK' + context
    elif i == 3 or i == 6:

        context = (context/100) + '%'

    #print('context: ', context)
    return context


def TopSeverWinners():
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    prev_month = current_month - 1
    prev_rainfall = annual_rainfall[prev_month - 1]
    current_month_prediction = []
    prev_month_prediction = []
    change = []
    for i in commodity_list:
        current_predict = i.getPredictedValue([float(current_month),
         current_year, current_rainfall])
        current_month_prediction.append(current_predict)
        prev_predict = i.getPredictedValue([float(prev_month),
         current_year, prev_rainfall])
        prev_month_prediction.append(prev_predict)
        change.append((((current_predict - prev_predict) * 100 / prev_predict),
         commodity_list.index(i)))
    sorted_change = change
    sorted_change.sort(reverse=True)
    # print(sorted_change)
    to_send = []
    for j in range(0, 7):
        perc, i = sorted_change[j]
        name = commodity_list[i].getCropName().split('/')[1]
        to_send.append([name, round((current_month_prediction[i] 
        * base[name]) / 100, 2), round(perc, 2)])
    print(to_send)
    return to_send
def TopSevenLosers():
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    prev_month = current_month - 1
    prev_rainfall = annual_rainfall[prev_month - 1]
    current_month_prediction = []
    prev_month_prediction = []
    change = []

    for i in commodity_list:
        current_predict = i.getPredictedValue([float(current_month),
         current_year, current_rainfall])
        current_month_prediction.append(current_predict)
        prev_predict = i.getPredictedValue([float(prev_month), 
        current_year, prev_rainfall])
        prev_month_prediction.append(prev_predict)
        change.append((((current_predict - prev_predict) * 100 / prev_predict),
         commodity_list.index(i)))
    sorted_change = change
    sorted_change.sort()
    to_send = []
    for j in range(0, 7):
        perc, i = sorted_change[j]
        name = commodity_list[i].getCropName().split('/')[1]
        to_send.append([name, round((current_month_prediction[i] 
        * base[name]) / 100, 2), round(perc, 2)])
   # print(to_send)
    return to_send



def SixMonthsForecast():
    month1=[]
    month2=[]
    month3=[]
    month4=[]
    month5=[]
    month6=[]
    for i in commodity_list:
        crop=SixMonthsForecastHelper(i.getCropName())
        k=0
        for j in crop:
            time = j[0]
            price = j[1]
            change = j[2]
            if k==0:
                month1.append((price,change,i.getCropName().split("/")[1],time))
            elif k==1:
                month2.append((price,change,i.getCropName().split("/")[1],time))
            elif k==2:
                month3.append((price,change,i.getCropName().split("/")[1],time))
            elif k==3:
                month4.append((price,change,i.getCropName().split("/")[1],time))
            elif k==4:
                month5.append((price,change,i.getCropName().split("/")[1],time))
            elif k==5:
                month6.append((price,change,i.getCropName().split("/")[1],time))
            k+=1
    month1.sort()
    month2.sort()
    month3.sort()
    month4.sort()
    month5.sort()
    month6.sort()
    crop_month_wise=[]
    crop_month_wise.append([month1[0][3],month1[len(month1)-1][2],month1[len(month1)-1][0],month1[len(month1)-1][1],month1[0][2],month1[0][0],month1[0][1]])
    crop_month_wise.append([month2[0][3],month2[len(month2)-1][2],month2[len(month2)-1][0],month2[len(month2)-1][1],month2[0][2],month2[0][0],month2[0][1]])
    crop_month_wise.append([month3[0][3],month3[len(month3)-1][2],month3[len(month3)-1][0],month3[len(month3)-1][1],month3[0][2],month3[0][0],month3[0][1]])
    crop_month_wise.append([month4[0][3],month4[len(month4)-1][2],month4[len(month4)-1][0],month4[len(month4)-1][1],month4[0][2],month4[0][0],month4[0][1]])
    crop_month_wise.append([month5[0][3],month5[len(month5)-1][2],month5[len(month5)-1][0],month5[len(month5)-1][1],month5[0][2],month5[0][0],month5[0][1]])
    crop_month_wise.append([month6[0][3],month6[len(month6)-1][2],month6[len(month6)-1][0],month6[len(month6)-1][1],month6[0][2],month6[0][0],month6[0][1]])

   # print(crop_month_wise)
    return crop_month_wise

def SixMonthsForecastHelper(name):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    name = name.split("/")[1]
    name = name.lower()
    commodity = commodity_list[0]
    for i in commodity_list:
        if name == str(i):
            commodity = i
            break
    month_with_year = []
    for i in range(1, 7):
        if current_month + i <= 12:
            month_with_year.append((current_month + i, current_year, annual_rainfall[current_month + i - 1]))
        else:
            month_with_year.append((current_month + i - 12, current_year + 1, annual_rainfall[current_month + i - 13]))
    wpis = []
    current_wpi = commodity.getPredictedValue([float(current_month), current_year, current_rainfall])
    change = []

    for m, y, r in month_with_year:
        current_predict = commodity.getPredictedValue([float(m), y, r])
        wpis.append(current_predict)
        change.append(((current_predict - current_wpi) * 100) / current_wpi)

    crop_price = []
    for i in range(0, len(wpis)):
        m, y, r = month_with_year[i]
        x = datetime(y, m, 1)
        x = x.strftime("%b %y")
        crop_price.append([x, round((wpis[i]* base[name.capitalize()]) / 100, 2) , round(change[i], 2)])

   # print("Crop_Price: ", crop_price)
    return crop_price

def CurrentMonth(name):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    name = name.lower()
    commodity = commodity_list[0]
    for i in commodity_list:
        if name == str(i):
            commodity = i
            break
    current_wpi = commodity.getPredictedValue([float(current_month), current_year, current_rainfall])
    current_price = (base[name.capitalize()]*current_wpi)/100
    return current_price

def TwelveMonthsForecast(name):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    name = name.lower()
    commodity = commodity_list[0]
    for i in commodity_list:
        if name == str(i):
            commodity = i
            break
    month_with_year = []
    for i in range(1, 13):
        if current_month + i <= 12:
            month_with_year.append((current_month + i, current_year, annual_rainfall[current_month + i - 1]))
        else:
            month_with_year.append((current_month + i - 12, current_year + 1, annual_rainfall[current_month + i - 13]))
    max_index = 0
    min_index = 0
    max_value = 0
    min_value = 9999
    wpis = []
    current_wpi = commodity.getPredictedValue([float(current_month), current_year, current_rainfall])
    change = []

    for m, y, r in month_with_year:
        current_predict = commodity.getPredictedValue([float(m), y, r])
        if current_predict > max_value:
            max_value = current_predict
            max_index = month_with_year.index((m, y, r))
        if current_predict < min_value:
            min_value = current_predict
            min_index = month_with_year.index((m, y, r))
        wpis.append(current_predict)
        change.append(((current_predict - current_wpi) * 100) / current_wpi)

    max_month, max_year, r1 = month_with_year[max_index]
    min_month, min_year, r2 = month_with_year[min_index]
    min_value = min_value * base[name.capitalize()] / 100
    max_value = max_value * base[name.capitalize()] / 100
    crop_price = []
    for i in range(0, len(wpis)):
        m, y, r = month_with_year[i]
        x = datetime(y, m, 1)
        x = x.strftime("%b %y")
        crop_price.append([x, round((wpis[i]* base[name.capitalize()]) / 100, 2) , round(change[i], 2)])
   # print("forecasr", wpis)
    x = datetime(max_year,max_month,1)
    x = x.strftime("%b %y")
    max_crop = [x, round(max_value,2)]
    x = datetime(min_year, min_month, 1)
    x = x.strftime("%b %y")
    min_crop = [x, round(min_value,2)]

    return max_crop, min_crop, crop_price


def TwelveMonthPrevious(name):
    name = name.lower()
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    commodity = commodity_list[0]
    wpis = []
    crop_price = []
    for i in commodity_list:
        if name == str(i):
            commodity = i
            break
    month_with_year = []
    for i in range(1, 13):
        if current_month - i >= 1:
            month_with_year.append((current_month - i, current_year, annual_rainfall[current_month - i - 1]))
        else:
            month_with_year.append((current_month - i + 12, current_year - 1, annual_rainfall[current_month - i + 11]))

    for m, y, r in month_with_year:
        current_predict = commodity.getPredictedValue([float(m), 2013, r])
        wpis.append(current_predict)

    for i in range(0, len(wpis)):
        m, y, r = month_with_year[i]
        x = datetime(y,m,1)
        x = x.strftime("%b %y")
        crop_price.append([x, round((wpis[i]* base[name.capitalize()]) / 100, 2)])
   # print("previous ", wpis)
    new_crop_price =[]
    for i in range(len(crop_price)-1,-1,-1):
        new_crop_price.append(crop_price[i])
    return new_crop_price
def year2021(name):
    name = name.lower()
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    commodity = commodity_list[0]
    wpis = []
    crop_price = []
    for i in commodity_list:
        if name == str(i):
            commodity = i
            break
    month_with_year = []
    for i in range(1, 13):
        month_with_year.append((i, 2021, annual_rainfall[i - 1]))
    for m, y, r in month_with_year:
        current_predict = commodity.getPredictedValue([float(m), y, r])
        wpis.append(current_predict)

    for i in range(0, len(wpis)):
        m, y, r = month_with_year[i]
        x = datetime(y,m,1)
        x = x.strftime("%b %y")
        crop_price.append([x, round((wpis[i]* base[name.capitalize()]) / 100, 2)])
    new_crop_price =[]
    for i in range(len(crop_price)-1,-1,-1):
        new_crop_price.append(crop_price[i])
    return new_crop_price[::-1]
def year2020Predict(name):
    name = name.lower()
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    commodity = commodity_list[0]
    wpis = []
    crop_price_2020 = []
    for i in commodity_list:
        if name == str(i):
            commodity = i
            break
    month_with_year = []
    for i in range(1, 13):
        month_with_year.append((i, 2020, annual_rainfall[i - 1]))

    for m, y, r in month_with_year:
        current_predict = commodity.getPredictedValue([float(m), y, r])
        wpis.append(current_predict)

    for i in range(len(wpis)):
        m, y, r = month_with_year[i]
        x = datetime(y,m,1)
        x = x.strftime("%b %y")
        crop_price_2020.append([x, round((wpis[i]* base[name.capitalize()]) / 100, 2)])
    crop_price_20 =[]
    for i in range(len(crop_price_2020)-1,-1,-1):
        crop_price_20.append(crop_price_2020[i])
    return crop_price_20[::-1]

if __name__ == "__main__":
    arhar = Commodity(commodity_dict["arhar"])
    commodity_list.append(arhar)
    bajra = Commodity(commodity_dict["bajra"])
    commodity_list.append(bajra)
    barley = Commodity(commodity_dict["barley"])
    commodity_list.append(barley)
    copra = Commodity(commodity_dict["copra"])
    commodity_list.append(copra)
    cotton = Commodity(commodity_dict["cotton"])
    commodity_list.append(cotton)
    gram = Commodity(commodity_dict["gram"])
    commodity_list.append(gram)
    groundnut = Commodity(commodity_dict["groundnut"])
    commodity_list.append(groundnut)
    jowar = Commodity(commodity_dict["jowar"])
    commodity_list.append(jowar)
    maize = Commodity(commodity_dict["maize"])
    commodity_list.append(maize)
    masoor = Commodity(commodity_dict["masoor"])
    commodity_list.append(masoor)
    moong = Commodity(commodity_dict["moong"])
    commodity_list.append(moong)
    niger = Commodity(commodity_dict["niger"])
    commodity_list.append(niger)
    paddy = Commodity(commodity_dict["paddy"])
    commodity_list.append(paddy)
    ragi = Commodity(commodity_dict["ragi"])
    commodity_list.append(ragi)
    rape = Commodity(commodity_dict["rape"])
    commodity_list.append(rape)
    jute = Commodity(commodity_dict["jute"])
    commodity_list.append(jute)
    soyabean = Commodity(commodity_dict["soyabean"])
    commodity_list.append(soyabean)
    sugarcane = Commodity(commodity_dict["sugarcane"])
    commodity_list.append(sugarcane)
    sunflower = Commodity(commodity_dict["sunflower"])
    commodity_list.append(sunflower)
    urad = Commodity(commodity_dict["urad"])
    commodity_list.append(urad)
    wheat = Commodity(commodity_dict["wheat"])
    commodity_list.append(wheat)

app.run(host='0.0.0.0', port=port, debug=True)




