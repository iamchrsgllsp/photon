from flask import Flask, render_template, session, request,url_for, redirect
import config
from login import user_login

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        if user_login(user,password) == True:
            session['user'] = user
            return redirect(url_for('user',user=user))
        else:
            return render_template('home.html')
    else:
        return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    return "Register Here"

@app.route('/<user>')
def user(user):
    user = session['user']
    return render_template('user.html',user=user)



if __name__ == '__main__':
    app.run(debug=True)