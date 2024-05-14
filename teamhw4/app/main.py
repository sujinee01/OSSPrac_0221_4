from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input_info.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = dict()
        result['Name'] = request.form.get('name')
        result['Student Number'] = request.form.get('student_number')
        result['Gender'] = request.form.get('gender', 'Not specified')  # Default to 'Not specified' if not provided
        result['Major'] = request.form.get('major')
        selected_languages = request.form.getlist('languages[]')
        languages_str = ', '.join(selected_languages)
        result['Languages'] = languages_str
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
