from flask import Flask
app = Flask(__name__)

@app.route('/bemvindo')
def home():
    return'bemvindo'

@app.route('/calculadora/soma/<int:num1>/<int:num2>')
def calculadora_soma(num1,num2):
    soma =  num1 + num2
    return f'resultado é: {soma}'

@app.route('/calculadora/subtrair/<int:num1>/<int:num2>')
def calculadora_subtrair(num1,num2):
    subtrair =  num1 -  num2
    return f'resultado é: {subtrair}'

@app.route('/calculadora/multiplicar/<int:num1>/<int:num2>')
def calculadora_multiplicar(num1,num2):
    multiplicar =  num1 *  num2
    return f'resultado é: {multiplicar}'

@app.route('/calculadora/divisão/<int:num1>/<int:num2>')
def calculadora_dividir(num1,num2):
    dividir =  num1 / num2
    return f'resultado é: {dividir}' 

if calculadora_dividir == 0:
    print ("erro")
else:
    print("divisão feita")    


if __name__=="__main__":
    app.run(debug=True)
  