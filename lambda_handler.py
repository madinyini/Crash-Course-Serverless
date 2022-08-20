import datetime


def suma(event, context):
    operando_a = event['num1']
    operando_b = event['num2']
    if not isinstance(operando_a, int) or not isinstance(operando_b, int):
        raise Exception('Parametros no son numeros enteros')
    return {
        "status": 200,
        "message": "ok",
        "suma": operando_b + operando_a
    }

def resta(event, context):
    operando_a = event['num1']
    operando_b = event['num2']
    if not isinstance(operando_a, int) or not isinstance(operando_b, int):
        raise Exception('Parametros no son numeros enteros')
    return {
        "status": 200,
        "message": "ok",
        "suma": operando_b - operando_a
    }


def fecha_actual(event, context):
    return {
        "status": 200,
        "message": "ok",
        "suma": datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%s')
    }

