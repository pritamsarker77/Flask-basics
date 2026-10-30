from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "About Page"\

@app.route('/contact')
def contact():
    return "Contact Page"  

# Dynamic route example:
@app.route('/user/<username>')
def username(username):
    return f"Hello Mr. {username}!"

@app.route('/student/<username>/<course>')
def student(username, course):
    return f"{username} is learning {course}!"

if __name__ == '__main__':
    app.run(debug=True)