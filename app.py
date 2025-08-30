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
        case "test3": return "SELECT * FROM employees"

        case "test4": return "SELECT name, salary FROM employees WHERE salary > 50000"
        case "test5": return "SELECT * FROM employees WHERE department = 'IT' AND (salary > 60000 OR title = 'Manager')"
        case "test6": return "SELECT name, hire_date FROM employees ORDER BY hire_date DESC"
        case "test7": return "SELECT * FROM employees LIMIT 10"
        case "test8": return "SELECT DISTINCT department FROM employees"
        case "test9": return "SELECT e.name, d.department_name FROM employees e INNER JOIN departments d ON e.department_id = d.id"
        case "test10": return "SELECT c.customer_name, o.order_id FROM customer c LEFT JOIN orders o ON c.id = o.customer_id"
        case "test11": return "SELECT p.product_name, s.supplier_name FROM product p RIGHT JOIN suppliers s ON p.supplier_id = s.id"
        case "test12": return "SELECT a.student_name, b.course_name FROM students a FULL OUTER JOIN courses b ON a.course_id = b.id"
        case "test13": return "SELECT department, COUNT(*) AS num_employees FROM employees GROUP BY department"
        case "test14": return "SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department HAVING AVG(salary) > 60000"
        case "test15": return "SELECT name FROM employees UNION SELECT name FROM contractors"
        case "test16": return "SELECT name FROM employees UNION ALL SELECT name FROM contractors"
        case "test17": return "SELECT anme FROM customers c WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id)"
        case "test18": return "SELECT name FROM employees WHERE department_id IN (1, 2, )"
        case "test19": return "SELECT name, hire_date FROM employees WHERE hire_date BETWEEN '2020-01-01' AND '2021-01-01'"
        case "test20": return "SELECT name FROM employees WHERE name LIKE 'A%'"
        case "test21": return "SELECT name, CASE WHEN salary > 100000 THEN 'High' WHEN salary > 50000 THEN 'Medium' ELSE 'Low' END AS salary_band FROM employees"
        case "test22": return "INSERT INTO employees (name, department, salary) VALUES ('Alice', 'HR', 55000)"
    return query

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
