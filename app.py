from flask import Flask, jsonify, render_template  # from flask Module importing Flask class
from database import load_jobs_from_db # from database
from sqlalchemy import  text


app = Flask(__name__)  # our app is just a object of the class Flask







@app.route('/')
def home():
  JOBS=load_jobs_from_db()
  #Returning a HTML Endpoint
  return render_template(
      'home.html', jobs=JOBS, company_name="Thedal"
  )  # Sending jobs (dynamic content) to home.html using render_template as a argument


@app.route('/api/jobs')
def jobs():
  JOBS=load_jobs_from_db()
  #Returning a json Endpoint
  return jsonify(JOBS)  # Webserver Returning jobs as a json


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
