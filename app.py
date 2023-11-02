from flask import Flask, render_template, request

app = Flask(__name__)

usersDB = [{'userid': 'admin', 'password': 'admin', 'name': 'Admin'},
           {'userid': 'pdelacruz', 'password': 'pass123', 'name': 'Pedro Dela Cruz'}]

@app.route("/")
def login():
    return render_template("login.html")

@app.route('/verify', methods=['POST', 'GET'])
def verify():
    if request.method == 'POST':
        userid = request.form['uid']
        password = request.form['password']

        valid = False
        logged_user = ''

        for user in usersDB:
            if user['userid'] == userid and user['password'] == password:
                valid = True
                logged_user = user['name']

        if valid:
            return f"Login Successful! Welcome {logged_user}!"
        else:
            return 'Login Failed!'

if __name__ == "__main__":
    app.run(debug=True)