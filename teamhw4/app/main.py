from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        student_number = request.form['student_number']
        major = request.form['major']
        email = request.form['email']
        gender = request.form['gender']
        languages = request.form.getlist('languages')
        return redirect(url_for('result', name=name, student_number=student_number, major=major, email=email, gender=gender, languages=",".join(languages)))
    return render_template('input_info.html')

@app.route('/result')
def result():
    return render_template('result.html', 
                           name=request.args['name'],
                           student_number=request.args['student_number'],
                           major=request.args['major'],
                           email=request.args['email'],
                           gender=request.args['gender'],
                           languages=request.args['languages'].split(","))
                           
if __name__ == "__main__":
    app.run(debug=True)
