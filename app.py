from flask import Flask,render_template

# create an instance of the class
app =Flask(__name__)

# routes/
@app.route('/')
def index():
    return render_template('index.html')
# other routes 

# about route 
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/portfolio')
def portfolio():
    projects = [
        {
            'id': 'Project-1',
            'title': 'Project One',
            'description': 'My first Project built with Bootstrap',
            'image': 'p1.jpg'
        },
        {
            'id': 'Project-2',
            'title': 'Project Two',
            'description': 'My second Project built with Flask',
            'image': 'p2.jpg'
        },
        {
            'id': 'Project-3',
            'title': 'Project Three',
            'description': 'My third Project built with Vue.js',
            'image': 'p3.jpg'
        }
    ]
    return render_template('portfolio.html',projects=projects)

if __name__ == '__main__':
    app.run(debug=True)