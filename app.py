from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <html><body>
        Hellssssso.
        </body></html>
        '''

app.run(debug=True)
