from flask import Flask, render_template, request
from sqlalchemy import create_engine, text

connectionString = "mysql+pymysql://8sevrae90cwiz17mpil5:pscale_pw_P7H8NoHsW6xToDrIYTp3ai0PwIWVx905B61PYeLcI2c@ap-south.connect.psdb.cloud/python_flask_website?charset=utf8mb4"

engine = create_engine(connectionString,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def signIn():
    if request.method == 'POST':
        if 'signInEmail' in request.form:
            signInEmail = request.form.get('signInEmail')
            signInPassword = request.form.get('signInPassword')
            signInEmail = str(signInEmail)
            signInPassword = str(signInPassword)
            with engine.connect() as conn:
              result = conn.execute(
        text(
          f"SELECT * FROM signUpDetails WHERE email='{signInEmail}' AND password='{signInPassword}'"
        ))
              user = result.fetchone()
              if user is None:
                return render_template('registration_page.html',
                               error_message="Invalid Email or Password")

            conn.commit()
        elif 'signUpName' in request.form:
            signUpName = request.form.get('signUpName')
            signUpEmail = request.form.get('signUpEmail')
            signUpPassword = request.form.get('signUpPassword')
            signUpName = str(signUpName)
            signUpEmail = str(signUpEmail)
            signUpPassword = str(signUpPassword)
            with engine.connect() as conn:
                conn.execute(
                    text(
                        f"INSERT INTO python_flask_website.signUpDetails (name,email,password) VALUES ('{signUpName}','{signUpEmail}','{signUpPassword}')"
                    ))
    return render_template('registration_page.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug="True")
