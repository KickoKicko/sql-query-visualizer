from flask import Flask, render_template, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods = ["POST"])
def test():
    print("hey")
    query = {"rows": ["Row 1"], "query":"SELECT * FROM test;"}
    print(jsonify(query))
    return jsonify(query)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
