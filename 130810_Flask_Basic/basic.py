#!/usr/bin/env python
from flask import Flask;
from flask import Response;
import json;
from flask import request;
from flask import render_template;

# Create App
app = Flask(__name__, static_folder="./public", static_url_path="", template_folder="./template")

# Basic Page Route
@app.route("/a")
def a():
    return "Hello Page A"

@app.route("/b")
def b():
    return "Hello Page B"

@app.route("/c")
def c():
    return "Hello Page C"

# Response with Status Code
@app.route("/not_found")
def not_found():
    return "Not Found", 404

# Create Items
products_list = [{
    "id": 1,
    "name": "banana",
    "price": 300
}, {
    "id": 2,
    "name": "coconut",
    "price": 200
}, {
    "id": 3,
    "name": "apple",
    "price": 100
}]

# Basic Response Type
@app.route("/products.html")
def products_html():
    output = ''
    for item in products_list:
        output += '<div data-id="%s">' % item["id"]
        output += '  <h1>%s</h1>' % item["name"]
        output += '  <p>%s</p>' % item["price"]
        
        output += '</div>'
    return output

@app.route("/products.xml")
def products_xml():
    output = '<?xml version="1.0" encoding="UTF-8" ?>'
    output += '<products>'
    for item in products_list:
        output += '<product id="%s">' % item["id"]
        output += '  <name>%s</name>' % item["name"]
        output += '  <price>%s</price>' % item["price"]
        output += '</product>'
    output += '</products>'
    return Response(output, mimetype="text/xml")

@app.route("/products.json")
def products_json():
    return Response(json.dumps(products_list), mimetype="application/json")

# Basic Request Paramete
@app.route("/parameter")
def parameter():
    if request.method == "GET":
        """
        output = '<?xml version="1.0" encoding="UTF-8" ?>'
        output += '<args>'
        for key, value in request.args.getlist("a", "b"):
            output += '<args>'
            output += '  <name>%s</name>' % key
            output += '  <value>%s</value>' % value
            output += '</arg>'
        output += '</args>'
        return Response(output, mimetype="text/xml")
        """        
    elif request.method == "POST":
        pass

# RESTful Web Service
@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        return Response(json.dumps(products_list), mimetype="application/json")
    elif request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        data = {
            "id": len(products_list) + 1,
            "name": name,
            "price": int(price)
        }
        products_list.append(data)
        return Response(json.dumps({
            "message": "data is created",
            "data": data
        }), mimetype="application/json")

@app.route("/products/<int:product_id>", methods=["GET", "PUT", "DELETE"])
def product(product_id):
    if request.method == "GET":
        return Response(json.dumps(products_list[product_id]), mimetype="application/json")
    elif request.method == "PUT":
        products_list[product_id].name = request.form["name"]
        products_list[product_id].price = int(request.form["price"])
        return Response(json.dumps({
            "message": "data is updated",
            "data": products_list[product_id]
        }), mimetype="application/json")
    elif request.method == "DELETE":
        return Response(json.dumps({
            "message": "data is removed",
            "data": products_list.pop(product_id)
        }), mimetype="application/json")

@app.route("/products/<product_id>")
def product_item(user_id):
    return "User NameID %s" + user_id


@app.route("/template")
def template():
    return render_template("template.html", products=products_list)


# Basic Request Parameter

app.run(debug=True)










