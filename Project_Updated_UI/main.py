import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for, session
import db

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/categories")
def categories():
    return render_template("Categories.html")

@app.route("/contactus")
def contactus():
    return render_template("contact.html")

@app.route("/contactus", methods=['POST'])
def contactus_data():
    fullName = request.form.get('fullName')
    customer_email = request.form.get('customer_email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    connection_string = "mongodb+srv://Bhupesh:1234@cluster0.7at15.mongodb.net/eCommerce_Project?retryWrites=true&w" \
                        "=majority"
    my_client = pymongo.MongoClient(connection_string)
    dblist = my_client.list_database_names()
    db = my_client["eCommerce_Project"]  # database
    coll = db["queries"]  # collection
    coll.insert({'fullName': fullName, 'customer_email': customer_email, 'subject': subject, 'message': message})
    return redirect(url_for('home'))


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/login", methods=['GET', 'POST'])
def login_data():
    email = request.form.get('email')
    password = request.form.get('password')
    connection_string = "mongodb+srv://Bhupesh:1234@cluster0.7at15.mongodb.net/eCommerce_Project?retryWrites=true&w" \
                        "=majority"
    my_client = pymongo.MongoClient(connection_string)
    dblist = my_client.list_database_names()
    db = my_client["eCommerce_Project"]  # database
    coll = db["users"]  # collection
    # email_found = coll.find({"email": email})  # fetches one document
    user_found = coll.find({"email": email, "password": password})  # fetches
    length = user_found.count()
    if length == 0:
        return "<h1> login Failed, Please Try Again </h1>"
    else:
        return redirect(url_for('home'))


@app.route("/registerdata", methods=['POST'])
def register_data():
    fName = request.form.get('first_name')
    lName = request.form.get('last_name')
    country_code = request.form.get('code')
    phone_number = request.form.get('phone')
    alt_number = request.form.get('mobile')
    gender = request.form.get('gender')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    street = request.form.get('street')
    landmark = request.form.get('landmark')
    zip = request.form.get('zip')
    city = request.form.get('city')
    country = request.form.get('country')
    email = request.form.get('email')
    connection_string = "mongodb+srv://Bhupesh:1234@cluster0.7at15.mongodb.net/eCommerce_Project?retryWrites=true&w" \
                        "=majority"
    my_client = pymongo.MongoClient(connection_string)
    dblist = my_client.list_database_names()
    db = my_client["eCommerce_Project"]  # database
    coll = db["users"]  # collection
    coll.insert({'first_name': fName, 'last_name': lName, 'country_code': country_code, 'phone_number': phone_number,
                 'alt_number': alt_number, 'gender': gender, 'password': password,
                 'confirm_password': confirm_password, 'street': street, 'landmark': landmark, 'zip': zip, 'city': city,
                 'country': country, 'email': email})
    return redirect(url_for('login'))



# Connect to MongoDB
def connect_to_mongoDB():
    # connecting to DB
    connection_string = "mongodb+srv://Bhupesh:1234@cluster0.7at15.mongodb.net/eCommerce_Project?retryWrites=true&w" \
                        "=majority"
    my_client = pymongo.MongoClient(connection_string)
    dblist = my_client.list_database_names()
    db = my_client["eCommerce_Project"]  # database
    coll = db["users"]  # collection
    # if "users" in dblist:
    # print("The database exists.")


@app.route('/recordReport', methods=['POST'])
def recordReport():
    # connecting to DB
    connection_string = "mongodb+srv://Bhupesh:1234@cluster0.7at15.mongodb.net/eCommerce_Project?retryWrites=true&w" \
                        "=majority"
    my_client = pymongo.MongoClient(connection_string)
    dblist = my_client.list_database_names()
    db = my_client["eCommerce_Project"]  # database
    coll = db["users"]  # collection
    fName = request.form.get['first_name']
    lName = request.form.get['last_name']
    coll.insert({'first_name': fName, 'last_name': lName})
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
