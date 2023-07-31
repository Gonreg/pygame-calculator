numbers = '0123456789'
operands = {
    '=': 'equals',
    '+': 'plus',
    '-': 'minus',
    '%': 'percent',
    '÷': 'digit',
    'x': 'X'
}
methods = {
    ',': 'add_comma',
    'AC': 'reset',
    '+/-': 'change_sign'
}


def getTypeCommand(text):
    if text in numbers:
        return 'number'
    if text in methods.keys():
        return 'method'
    if text in operands.keys():
        return 'operand'
