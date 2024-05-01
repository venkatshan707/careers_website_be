from flask import Flask, jsonify, render_template  # from flask Module importing Flask class

app = Flask(__name__)  # our app is just a object of the class Flask

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Chennai, India',
}, {
    'id': 2,
    'title': 'Data Scienist',
    'location': 'Bangalore, India',
    'salary': 'Rs. 20 LPA'
}, {
    'id': 3,
    'title': 'Machine learning Engineer',
    'location': 'Chennai, India',
    'salary': 'Rs. 15 LPA'
}, {
    'id': 4,
    'title': 'Tableau Developer',
    'location': 'Delhi, India',
    'salary': 'Rs. 10 LPA'
}]


@app.route('/')
def home():

  #Returning a HTML Endpoint
  return render_template(
      'home.html', jobs=JOBS, company_name="Thedal"
  )  # Sending jobs (dynamic content) to home.html using render_template as a argument


@app.route('/api/jobs')
def jobs():
  #Returning a json Endpoint
  return jsonify(JOBS)  # Webserver Returning jobs as a json


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
