from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input_info.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        student_number = request.form['student_number']
        gender = request.form.get('gender', 'Not specified')  # Default to 'Not specified' if not provided
        major = request.form['major']
        languages = request.form.getlist('languages')
        return render_template('result.html', name=name, student_number=student_number,
                               gender=gender, major=major, languages=languages)

if __name__ == '__main__':
    app.run(debug=True)