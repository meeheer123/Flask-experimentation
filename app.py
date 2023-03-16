from flask import Flask, render_template, request
from sqlalchemy import create_engine, text

connectionString = "mysql+pymysql://8sevrae90cwiz17mpil5:pscale_pw_P7H8NoHsW6xToDrIYTp3ai0PwIWVx905B61PYeLcI2c@ap-south.connect.psdb.cloud/python_flask_website?charset=utf8mb4"

engine = create_engine(connectionString,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    Name = request.form.get('name')
    Runs = request.form.get('id')
    Name = str(Name)
    Runs = int(Runs)
    with engine.connect() as conn:
      conn.execute(text(
        f"INSERT INTO Data (Name,Runs) VALUES ('{Name}',{Runs})"))
      conn.commit()
  return render_template('registration.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug="True")

