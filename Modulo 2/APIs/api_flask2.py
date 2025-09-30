from flask import Flask
app = Flask(__name__)

@app.route('/bemvindo')
def home():
    return'bem vindo'

@app.route('/bemvindo/<nome>')
def bemvindo(nome):
    seu_nome =  nome
    return f'bemvindo(a): {seu_nome}'


if __name__=="__main__":
    app.run(debug=True)