from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

products = [
    {"id": 1, "name": "Teddy Bear", "price": 500},
    {"id": 2, "name": "Gift Mug", "price": 300}
]

@app.route("/")
def home():
    return "Tapas Stores API is LIVE 🚀"

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    users.append(data)
    return jsonify({"message": "User registered successfully"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    for u in users:
        if u["username"] == data["username"] and u["password"] == data["password"]:
            return jsonify({"message": "Login success"})
    return jsonify({"message": "Invalid login"}), 401

if __name__ == "__main__":
    app.run()