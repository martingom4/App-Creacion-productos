from flask import Blueprint


operations = Blueprint('operations', __name__)


@operations.route('/suma/<num1>/<num2>')
def suma(num1, num2):
    return {'resultado': int(num1) + int(num2)}

@operations.route('/resta/<num1>/<num2>')
def resta(num1,num2):
    return {"resultado": int(num1) - int(num2)}



@operations.route('/division/<num1>/<num2>')
def division(num1,num2):
    if num1 or num2 == 0:
        return {"resultado": "No se puede dividir entre 0"}
    else:
        return {"resultado": int(num1) / int(num2)}

