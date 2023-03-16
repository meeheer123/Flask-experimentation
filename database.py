from sqlalchemy import create_engine

connectionString = "mysql+pymysql://8sevrae90cwiz17mpil5:pscale_pw_P7H8NoHsW6xToDrIYTp3ai0PwIWVx905B61PYeLcI2c@ap-south.connect.psdb.cloud/python_flask_website?charset=utf8mb4"

engine = create_engine(connectionString,connect_args= {
  "ssl" : {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

with engine.connect() as conn:
  result = conn.execute(text(""))