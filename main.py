from flask import Flask
from flask import request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)
@app.route('/callback', methods = ['POST'])
def user():
   data = request.data
   print(data)
   return data


if __name__ == "__main__":
  app.run()