from flask import Flask, jsonify, render_template  # from flask Module importing Flask class
from database import load_jobs_from_db, load_job_from_db # from database
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

@app.route('/job/<id>')# It will accept dynamic value for job id and will create route dynamically. 
def sho_job(id):
  JOB=load_job_from_db(id)
  if not JOB:
    return "Not Found", 404
  return render_template('jobpage.html',job=JOB)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
