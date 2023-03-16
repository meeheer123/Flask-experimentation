from flask import Flask, render_template, request
from sqlalchemy import create_engine

connectionString = "mysql+pymysql://8sevrae90cwiz17mpil5:pscale_pw_P7H8NoHsW6xToDrIYTp3ai0PwIWVx905B61PYeLcI2c@ap-south.connect.psdb.cloud/python_flask_website?charset=utf8mb4"

engine = create_engine(connectionString,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    Name = request.form.get('batsman')
    Runs = request.form.get('runs')
    Runs = int(Runs)
    with engine.connect() as conn:
      statement = f"INSERT INTO data (Name, Runs) VALUES ({Name}, {Runs})"
      print(statement)
      conn.execute(statement)
      conn.commit()
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug="True")
