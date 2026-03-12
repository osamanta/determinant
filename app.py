from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import math

app = Flask(__name__)
app.secret_key = "supersecretkey"

def det(A):
    A = np.array(A, dtype=float)
    n = A[0].size
    swaps = 0

    for j in range(n - 1):
        r = j
        while r < n and A[r][j] == 0 :
            r += 1
        if r == n:
            return 0
        if r > j:
            for k in range(n):
                temp = A[r][k]
                A[r][k] = A[j][k]
                A[j][k] = temp
            swaps += 1
        for i in range(j + 1, n):
            if A[i][j] != 0:
                m = A[i][j] / A[j][j]
                for k in range(n):
                    A[i][k] -= m * A[j][k]

    det = (-1) ** swaps
    for i in range(n):
        det *= A[i][i]
    return det

@app.route('/')
def index():
    result = session.pop("result", None)
    inputs = session.pop("inputs", None)

    if session.pop("from_post", False):
        n = session.get("n", 3)
    else:
        n = 3

    if inputs is None or len(inputs) != n:
        inputs = [[None for _ in range(n)] for _ in range(n)]

    return render_template("index.html", result=result, inputs=inputs, n=n)

@app.route('/dimension', methods=['POST'])
def dimension():
    try:
        n = int(request.form["n"])
        session["n"] = n
        session["from_post"] = True
    except:
        session["n"] = 3

    return redirect(url_for("index"))


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        n = session.get("n", 3)
        session["from_post"] = True
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i][j] = float(request.form[f"a_{i}_{j}"])
        d = det(A)
        if d.is_integer():
            d = int(d)
        else:
            d = round(d, 10)
        session["result"] = d
        A_python = []
        for row in A.tolist():
            new_row = []
            for x in row:
                if float(x).is_integer():
                    new_row.append(int(x))
                else:
                    new_row.append(float(x))
            A_python.append(new_row)
        session["inputs"] = A_python
    except Exception as e:
        session["result"] = "Invalid input"
        session["n"] = n
        print(f"An error occurred: {e}")


    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
