# https://www.codewars.com/kata/526c7b931666d07889000a3c/train/python
def makecodearray(code):
    codearray = code.split('\n')
    for i in codearray:
        x = []
        for j in range(len(i)):
            x.append(i[j])
        codearray[codearray.index(i)] = x
    return codearray


outputarray = []
output=''


def interpretor(codearray, mov, pos=[0, 0]):
    global output,outputarray
    if pos == [0,0]:
        output,outputarray = '',[]
    testvalue = codearray[pos[0]][pos[1]]
    if mov == '>':
        pos_new = [pos[0], pos[1]+1]
    elif mov == '<':
        pos_new = [pos[0], pos[1]-1]
    elif mov == '^':
        pos_new = [pos[0]-1, pos[1]]
    elif mov == 'v':
        pos_new = [pos[0]+1, pos[1]]
    #print(pos, pos_new, output)

    if testvalue == '>':
        interpretor(codearray, '>', [pos[0], pos[1]+1])
    elif testvalue == '<':
        interpretor(codearray, '<', [pos[0], pos[1]-1])
    elif testvalue == '^':
        interpretor(codearray, '^', [pos[0]-1, pos[1]])
    elif testvalue == 'v':
        interpretor(codearray, 'v', [pos[0]+1, pos[1]])
    elif testvalue == '@':
        pass
    elif testvalue.isalpha():
        outputarray.append(testvalue)
        interpretor(codearray, mov, [pos_new[0], pos_new[1]])
    elif testvalue == '.':
        for i in range(len(outputarray)):
            output += outputarray.pop()
        interpretor(codearray, mov, [pos_new[0], pos_new[1]])
    elif testvalue == ':':
        if outputarray == []:
            outputarray.append('0')
        else:
            outputarray.append(outputarray[-1])
        interpretor(codearray, mov, [pos_new[0], pos_new[1]])
    elif testvalue == '|':
        value = outputarray.pop()
        if value == '0':
            interpretor(codearray, 'v', [pos[0]+1, pos[1]])
        else:
            interpretor(codearray, '^', [pos[0]-1, pos[1]])
    elif testvalue == '_':
        value = outputarray.pop()
        if value == '0':
            interpretor(codearray, '>', [pos[0], pos[1]+1])
        else:
            interpretor(codearray, '<', [pos[0], pos[1]-1])
    else:
        interpretor(codearray, mov, [pos_new[0], pos_new[1]])
    

    return output


def interpret(code):
    codelist = makecodearray(code)
    for i in codelist:
        print(i, end='\n')
    mov = codelist[0][0]
    print(interpretor(codelist, mov))


interpret('>987v>.v\nv456<  :\n>321 ^ _@')
interpret('>              v\nv  ,,,,,"Hello"<\n>48*.          v\nv,,,,,,"World!"<\n>25*.@')
