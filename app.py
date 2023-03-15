from flask import Flask, render_template, request
import pymysql


def sqlConnector():
  conn = pymysql.connect(
    user='8sevrae90cwiz17mpil5',
    password='pscale_pw_P7H8NoHsW6xToDrIYTp3ai0PwIWVx905B61PYeLcI2c',
    db='python_flask_website',
    host='ap-south.connect.psdb.cloud')
  c = conn.cursor()
  return conn, c


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    Name = request.form.get('batsman')
    Runs = request.form.get('runs')
    conn, c = sqlConnector()
    c.execute("INSERT INTO Data VALUES ('{}',{})".format(Name, int(Runs)))
    conn.commit()
    conn.close()
    c.close()
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug="True")
