from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = {
    'id' : 1,
    'title': 'data analyst',
    'location': 'Bengaluru, India',
    'Salary': 'Rs. 1,00,000'
}
{
    'id' : 2,
    'title': 'Back end engineer',
    'location': 'Dilhi, India',
    'Salary': 'Rs. 10,00,000'
}
{
    'id' : 3,
    'title': 'Front End engineer',
    'location': 'Remote',
    'Salary': 'Rs. 5,00,000'
}
{
    'id' : 4,
    'title': 'Front End engineer',
    'location': 'San Farncisco, usa',
    'Salary': '$5,000'
}

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS, company_name='Jobs')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)