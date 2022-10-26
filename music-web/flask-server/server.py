from flask import Flask

app = Flask(__name__)

# example route
@app.route('/api/members')
def members():
    return {'members': ['Jacob', 'Max', 'Daniel', 'David']}

if __name__ == '__main__':
    # run in development mode
    app.run(debug=True)