from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods = ["POST"])
def query():
    #print(request.data.decode("utf-8"))
    query = request.data.decode("utf-8")
    query = query[10:len(query)-2]
    query =query =  tests(query)
    words = query.split()
    table_part = []
    for i in range(len(words)):
        if words[i] == "FROM":
            table_part = words[i+1:]
    print(query)
    print(words)
    print(table_part)
    query_test = {"rows": ["Row 1"], "query":"SELECT * FROM test;"}
    return jsonify(query_test)



def tests(query):
    match query:
        case "test1": return "SELECT * FROM table"
        case "test2": return "SELCET Id,Name,Password FROM Users"
    return query

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
