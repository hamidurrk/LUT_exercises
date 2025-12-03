from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate")
def calculate():
    a = request.args.get("a", "").strip()
    b = request.args.get("b", "").strip()
    op = request.args.get("op", "").strip()

    
    try:
        a_val = float(a)
        b_val = float(b)
    except ValueError:
        return jsonify(result="Error")

    
    if op == "add":
        result = a_val + b_val
    elif op == "sub":
        result = a_val - b_val
    elif op == "mul":
        result = a_val * b_val
    elif op == "div":
        if b_val == 0:
            return jsonify(result="Error")
        result = a_val / b_val
    else:
        return jsonify(result="Error")

    return jsonify(result=result)


if __name__ == "__main__":
    app.run()