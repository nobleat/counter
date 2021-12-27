from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key="@ng#[@"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    return render_template("index.html")

@app.route('/increment')
def increment():
    session["count"]+=1
    return redirect('/')

# @app.route('/destroy_session')
# def reset():
#     return

if __name__=="__main__":
    app.run(debug=True)