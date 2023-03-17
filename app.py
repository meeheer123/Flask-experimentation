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
    signInEmail = request.form.get('signInEmail')
    signInPassword = request.form.get('signInPassword')
    signInEmail = str(signInEmail)
    signInPassword = str(signInPassword)
    with engine.connect() as conn:
      conn.execute(
        text(
          f"INSERT INTO Data (email,password) VALUES ('{signInEmail}','{signInPassword}')"
        ))
      conn.commit()
  return render_template('registration_page.html')


def signUp():
  if request.method == 'POST':
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
      conn.commit()
  return render_template('registration_page.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug="True")
