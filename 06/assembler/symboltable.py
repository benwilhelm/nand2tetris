import parser

def buildTable(lines):
    labels = ((i, line) for i, line in enumerate(lines) if parser.commandType(line) == 'L_COMMAND')

    table = {}
    for idx, label in enumerate(labels):
        (lineNo, line) = label
        symbol = parser.symbol(line)
        lineNo = lineNo - idx # accounts for deletion of line
        table[symbol] = lineNo

    return table

def convertSymbol(cmd, table={}):
    if (parser.commandType(cmd) != 'A_COMMAND'):
        return cmd

    symbol = parser.symbol(cmd)
    predefined = {
        'SP'  : 0,
        'LCL' : 1,
        'ARG' : 2,
        'THIS': 3,
        'THAT': 4,
        'R0' :  0,
        'R1' :  1,
        'R2' :  2,
        'R3' :  3,
        'R4' :  4,
        'R5' :  5,
        'R6' :  6,
        'R7' :  7,
        'R8' :  8,
        'R9' :  9,
        'R10': 10,
        'R11': 11,
        'R12': 12,
        'R13': 13,
        'R14': 14,
        'R15': 15,
        'SCREEN': 16384,
        'KBD'   : 24576
    }
    table.update(predefined)

    try:
        return '@' + table[symbol]
    except KeyError:
        return cmd
