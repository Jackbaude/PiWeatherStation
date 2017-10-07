from flask import Flask, render_template, session, request


app = Flask(__name__)
# This is a test to verify that falsk works
@app.route('/hello')
def hello_flask():
    return 'Hello from flask\n'
    

    




















if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")
