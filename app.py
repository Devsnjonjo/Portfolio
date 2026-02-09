from flask import Flask, render_template
# <!-- creat an instance of the class -->
app = Flask(__name__)
# <!-- routes -->
@app.route('/')
def index():
    return render_template('index.html')
    # <!-- other routes -->
if __name__ == '__main__':
    app.run(debug=True)