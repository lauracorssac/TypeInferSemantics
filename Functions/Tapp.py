from Definitions.types import TYPE
import re


def isExpectingFunctionalParameter(s1):
    return s1[0] == '('

def isExpectingParameter(s1):
    return s1.find('->') > 0

def isFunctionalParameter(received_parameter):
    return received_parameter.find('->') > 0

def validParameters(environment, node):
    if node and "description" in node and "elements" in node and "e1" in node["elements"] and "e2" in node["elements"]:
        return True
    else:
        return False

def get_expected_parameter(term):
    lastIndex = 0
    pilha = []
    print(term)
    print()
    # changing index and printing separately
    for count,element in enumerate(term):
        print (count,element)
        if (element == '('):
            pilha.append(element)
        if(element == ')'):
            if (pilha[-1] == '('):
                pilha.pop()
                lastIndex = count
                if(len(pilha) ==0):
                    break
            else:
                raise Exception()

    print('last index = ', lastIndex)
    expected_parameter = term[1:lastIndex])
    return expected_parameter, lastIndex

def apply_parameter(term, lastIndex):
    result = term[lastIndex+3:] # the index indicates the closing ), so we have to remove the remaining ')->'
    return result

def t_app(environment, node):
    if not validParameters(environment, node):
        return TYPE.ERROR

    result = TYPE.ERROR
    term = infer_type(environment, node["elements"]["e1"])
    expected_parameter, ending_index = get_expected_parameter(term)
    received_parameter = infer_type(environment, node["elements"]["e2"])

    if expected_parameter == received_parameter:
        result = apply_parameter(term, lastIndex)

    return result

    # if isFunctionalParameter(received_parameter):
    #     if isExpectingFunctionalParameter(s1):
    #         expected_parameter = s1.split(')->',1)[0]
    #         expected_parameter = expected_parameter[1:] #Remove ( inicial da string
    #         if expected_parameter == received_parameter:
    #             result = s1.split(')->',1)[1]
    #
    # if isExpectingParameter(s1):
    #     expected_parameter = s1.split('->',1)[0]
    #     if expected_parameter == received_parameter:
    #         result = s1.split('->',1)[1]

    return result
