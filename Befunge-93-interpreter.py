# https://www.codewars.com/kata/526c7b931666d07889000a3c/train/python
def makecodearray(code):
    codearray = code.split('\n')
    for i in codearray:
        x = []
        for j in range(len(i)):
            x.append(i[j])
        codearray[codearray.index(i)] = x
    return codearray

def interpretor(codelist):
    import random
    fwd = True
    pos = [0,0]
    mov = '>'
    mode = 'normal'
    outputlist = []
    output = ''
    skip = False

    while fwd:
        if skip:
            skip = False
            if mov == '>':
                pos = [pos[0], pos[1]+1]
            elif mov == '<':
                pos = [pos[0], pos[1]-1]
            elif mov == '^':
                pos = [pos[0]-1, pos[1]]
            elif mov == 'v':
                pos = [pos[0]+1, pos[1]]
            continue
        else:
            pass

        testvalue = codelist[pos[0]][pos[1]]
        print(outputlist,pos)

        if mode == 'string':
            if testvalue == '"':
                mode = 'normal'
            elif testvalue == ' ':
                pass
            else:
                outputlist.append(testvalue)
        else:
            if testvalue == '@':
                fwd = False
            elif testvalue == '>':
                mov = '>'
            elif testvalue == '<':
                mov = '<'
            elif testvalue == '^':
                mov = '^'
            elif testvalue == 'v':
                mov = 'v'
            elif testvalue == '"':
                mode = 'string'
            elif testvalue == '#':
                skip = True
            elif testvalue == '+':
                a = int(outputlist.pop())
                if outputlist == []:
                    b = 0
                else:
                    b = int(outputlist.pop())
                outputlist.append(str(a+b))
            elif testvalue == '-':
                a = outputlist.pop()
                if not a.isnumeric():
                    outputlist.append(a)
                else:
                    if not outputlist == []:
                        b = outputlist.pop()
                        if not b.isnumeric():
                            outputlist.append(b)
                    else:
                        b = '0'
                    outputlist.append(str(int(b)-int(a)))
            elif testvalue == '*':
                a = int(outputlist.pop())
                b = int(outputlist.pop())
                outputlist.append(str(b*a))
            elif testvalue == '/':
                a = int(outputlist.pop())
                b = int(outputlist.pop())
                if a == 0:
                    outputlist.append(0)
                else:
                    outputlist.append(str(b//a))
            elif testvalue == '%':
                a = int(outputlist.pop())
                b = int(outputlist.pop())
                if a == 0:
                    outputlist.append('0')
                else:
                    outputlist.append(str(b % a))
            elif testvalue == '!':
                a = outputlist.pop()
                if a == '0':
                    outputlist.append('1')
                else:
                    outputlist.append('0')
            elif testvalue == '`':
                a = outputlist.pop()
                b = outputlist.pop()
                if not a.isnumeric():
                    a = ord(a)
                if not b.isnumeric():
                    b = ord(b)
                if int(b) > int(a):
                    outputlist.append('1')
                else:
                    outputlist.append('0')
            elif testvalue == '_':
                a = outputlist.pop()
                if a == '0':
                    mov = '>'
                else:
                    mov = '<'
            elif testvalue == '|':
                a = outputlist.pop()
                if a == '0':
                    mov = 'v'
                else:
                    mov = '^'
            elif testvalue == ':':
                if outputlist == []:
                    outputlist.append('0')
                else:
                    outputlist.append(outputlist[-1])
            elif testvalue == '\\':
                a = outputlist.pop()
                if outputlist == []:
                    b = '0'
                else:
                    b = outputlist.pop()
                outputlist.append(a)
                outputlist.append(b)
            elif testvalue == '$':
                outputlist.pop()
            elif testvalue == '.':
                a = outputlist.pop()
                if a.isnumeric():
                    output += a
            elif testvalue == ',':
                if not outputlist == []:
                    a = outputlist.pop()
                    if a.isnumeric():
                        output += chr(int(a))
                    else:
                        output += a
                else:
                    pass
            elif testvalue == 'p':
                y = int(outputlist.pop())
                x = int(outputlist.pop())
                codelist[x][y] = chr(int(outputlist.pop()))
            elif testvalue == 'g':
                y = int(outputlist.pop())
                x = int(outputlist.pop())
                temp = codelist[y][x]
                outputlist.append(str(ord(temp)))
            elif testvalue =='?':
                mov = random.choice(['>', '<', '^', 'v'])
            elif testvalue.isalnum():
                outputlist.append(testvalue)
        
        if mov == '>':
            pos = [pos[0], pos[1]+1]
        elif mov == '<':
            pos = [pos[0], pos[1]-1]
        elif mov == '^':
            pos = [pos[0]-1, pos[1]]
        elif mov == 'v':
            pos = [pos[0]+1, pos[1]]

    return output


def interpret(code):
    codelist = makecodearray(code)
    for i in codelist:
        print(i, end='\n')
    print(interpretor(codelist))


interpret('>987v>.v\nv456<  :\n>321 ^ _@')
interpret(    '>              v\nv  ,,,,,"Hello"<\n>48*,          v\nv,,,,,,"World!"<\n>25*,@')
interpret('08>:1-:v v *_$.@ \n  ^    _$>\:^')# output and input are same
interpret('01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@')
interpret('v@.<\n >1^\n>?<^\n >2^')
