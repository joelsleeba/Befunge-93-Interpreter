# https://www.codewars.com/kata/526c7b931666d07889000a3c/train/python
def makecodearray(code):
    codearray = code.split('\n')
    for i in codearray:
        x = []
        for j in range(len(i)):
            x.append(i[j])
        codearray[codearray.index(i)] = x
    return codearray


output = ''


def interpretor(codearray, mov, pos=[0, 0]):
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
        return interpretor(codearray, '>', [pos[0], pos[1]+1])
    elif testvalue == '<':
        return interpretor(codearray, '<', [pos[0], pos[1]-1])
    elif testvalue == '^':
        return interpretor(codearray, '^', [pos[0]-1, pos[1]])
    elif testvalue == 'v':
        return interpretor(codearray, 'v', [pos[0]+1, pos[1]])
    elif testvalue == '@':
        return ''
    elif testvalue.isalnum():
        return testvalue+interpretor(codearray, mov, [pos_new[0], pos_new[1]])
    else:
        return interpretor(codearray, mov, [pos_new[0], pos_new[1]])


def interpret(code):
    codelist = makecodearray(code)
    for i in codelist:
        print(i, end='\n')
    mov = codelist[0][0]
    print(interpretor(codelist, mov))


interpret('>987v> v\nv456<   \n>321 ^ @')
