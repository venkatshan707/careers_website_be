from flask import Flask, render_template  # from flask Module importing Flask class

app = Flask(__name__)  # our app is just a object of the class Flask


@app.route('/')
def home():
  return render_template('home.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
