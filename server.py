from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Secret Secrets'

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
        print('The index route was hit: Add 1 to count')
    return render_template("index.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)