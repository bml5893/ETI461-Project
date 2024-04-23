from flask import Flask, redirect, render_template, request, url_for

from flask_sqlalchemy import SQLAlchemy

from db import DB


app = Flask(__name__)

db = DB(username = "bml5893", password = "H0d3sk@lL3", hostname = "bml5893.mysql.pythonanywhere-services.com", dbtype = "mysql", dbname = "bml5893$USPS")

#db.tables.set_option('display.max_cols', 15)

df1 = db.query("select * from shopitems where itemID = 1;")
df2 = db.query("select * from shopitems where itemID = 2;")
df3 = db.query("select * from shopitems where itemID = 3;")
df4 = db.query("select * from shopitems where itemID = 4;")
df5 = db.query("select * from shopitems where itemID = 5;")
df6 = db.query("select * from shopitems where itemID = 6;")
df7 = db.query("select * from shopitems where itemID = 7;")
df8 = db.query("select * from shopitems where itemID = 8;")
df9 = db.query("select * from shopitems where itemID = 9;")
df10 = db.query("select * from shopitems where itemID = 10;")
df11 = db.query("select * from shopitems where itemID = 11;")

zip = db.query("select * from zipcodes;")

addr1 = db.query("select * from addresses where addressNo = 1;")
addr2 = db.query("select * from addresses where addressNo = 2;")

tr1 = db.query("select * from tracking where contents like 'Apple%';")
tr2 = db.query("select * from tracking where trackingNumber = '51H5135IO0LM5438789K';")

df1.rename(columns={"itemID": "","ItemName": "","ItemPrice": "" ,"itemType": ""})

print(db.query("select * from tracking where contents like 'Apple%'"))

@app.route('/')
def home():
    return render_template("mainpag.html", content1 = df1, content2 = df2, content3 = df3, content4 = df4, content5 = df5,
    content6 = df6, content7 = df7, content8 = df8, content9 = df9, content10 = df10, content11 = df11, zipcodes = zip,
    address1 = addr1, address2 = addr2, tracking1 = tr1, tracking2 = tr2)