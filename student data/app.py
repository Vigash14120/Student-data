from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory data storage: {reg_no: [marks]}
students = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_student():
    reg_no = request.form['reg_no']
    marks = request.form['marks']

    try:
        mark_list = list(map(int, marks.split(',')))  # "78,89,90" → [78, 89, 90]
        students[reg_no] = mark_list
    except:
        return "Invalid input format. Please enter comma-separated integers."

    return redirect(url_for('view_students'))

@app.route('/delete/<reg_no>')
def delete_student(reg_no):
    students.pop(reg_no, None)
    return redirect(url_for('view_students'))

@app.route('/view')
def view_students():
    student_data = [
        {
            'reg_no': reg_no,
            'marks': marks,
            'total': sum(marks)
        }
        for reg_no, marks in students.items()
    ]
    return render_template('view.html', students=student_data)

if __name__ == '__main__':
    app.run(debug=True)
