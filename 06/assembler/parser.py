import re
import code

def extractCommand(line):
    parts = line.split('//')
    cmd = parts[0]
    cmd = cmd.strip()

    if cmd == '':
        return None
    return cmd


def parseCommand(cmd):
    if commandType(cmd) == 'A_COMMAND':
        smb = int(symbol(cmd))
        return code.decimalToBinary(smb)
    if commandType(cmd) == 'C_COMMAND':
        cmdDest = dest(cmd)
        cmdComp = comp(cmd)
        cmdJump = jump(cmd)
        return '111'+ code.comp(cmdComp) + code.dest(cmdDest) + code.jump(cmdJump)
    return cmd


def commandType(cmd):
    """This is slightly too permissive in the identification of C_COMMANDS,
       but it gets the job done for now"""

    symbolPattern = '[^\d][\d\w\_\.\$\:]+'
    destPattern = '(A?M?D?=)?'
    compPattern = '[AMD]?[\-\!\+\&\|]?[AMD01]'
    jumpPattern = '(;(JGT|JLT|JGE|JLE|JNE|JEQ|JMP))?'

    patterns = [
        ('^\@[0-9]+$', 'A_COMMAND'), # @23
        ('^\@' + symbolPattern + '$', 'A_COMMAND'),
        ('^' + destPattern + compPattern + jumpPattern + '$', 'C_COMMAND'),
        ('^\(' + symbolPattern + '\)$', 'L_COMMAND'),
    ]

    for pattern, cmd_type in patterns:
        match = re.search(pattern, cmd)
        if match:
            return cmd_type

    raise ValueError(cmd)



def symbol(cmd):
    if (commandType(cmd) == 'A_COMMAND'):
        return cmd[1:]

    if (commandType(cmd) == 'L_COMMAND'):
        return cmd[1:-1]

    raise ValueError(cmd)


def dest(cmd):
    if (commandType(cmd) == 'C_COMMAND'):
        parts = cmd.split('=')
        if (len(parts) == 1):
            return None
        return parts[0]

    raise ValueError(cmd)


def comp(cmd):
    if (commandType(cmd) == 'C_COMMAND'):
        parts = cmd.split(';')
        rslt = parts[0]
        parts = rslt.split('=')
        if (len(parts) == 1):
            return parts[0]
        return parts[1]

    raise ValueError(cmd)


def jump(cmd):
    if (commandType(cmd) == 'C_COMMAND'):
        parts = cmd.split(';')
        try:
            return parts[1]
        except IndexError:
            return None

    raise ValueError(cmd)
