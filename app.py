from flask import Flask, render_template, request, redirect

app = Flask(__name__)

applicants = []

class Candidate:
    def __init__(self, name, email, resume):
        self.name = name
        self.email = email
        self.resume = resume

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply', methods=['POST'])
def apply():
    name = request.form['name']
    email = request.form['email']
    resume = request.files['resume'].read().decode('utf-8')
    candidate = Candidate(name, email, resume)
    applicants.append(candidate)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)