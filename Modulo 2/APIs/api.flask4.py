from flask import Flask,render_template
app = Flask(__name__)

@app.route('/portifolio')
def home():
    return render_template('port.html')

if __name__=="__main__":
    app.run(debug=True)