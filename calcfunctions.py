# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 10:05:40 2022

@author: ASUS
"""


OPERS = 'Del C + - x / % ='.split()

def trying(function, arguments, exception=None):
    """
    Try execute function with its arguments, if error it results the exception
    """
    try:
        result = function(*arguments)
    except:
        if exception is not None:
            result = exception
        else:
            result = ''
            
    return result

def numerize(text):
    """
    Convert text from display to readable mathematical expression or number
    """
    if len(text.split('.')) > 1:
        convert = float
    else:
        convert = int
        
    num = trying(convert, [text], 0.)
    
    return num

def negation(text):
    """
    Negating the number given
    """
    num = -numerize(text)
    
    return num

def getmultiply(text):
    """
    Convert 'x' to '*' as readable by python for multiplication
    """
    expression = ''
    if 'x' in text:
        split = text.split('x')
        for i in range(len(split)):
            if i == len(split)-1:
                nt = split[i]
            else:
                nt = split[i] + '*'
            expression = expression + nt
    else:
        expression = text
        
    return expression

def getpercent(text):
    """
    Convert '%' to '/100' as readable by python for percentage operation
    """
    expression = '' 
    if '%' in text:
        split = text.split('%')
        for i in range(len(split)):
            if i == len(split)-1:
                nt = split[i]
            else:
                subtext = split[i]
                for char in subtext:
                    if char in OPERS[2:-2]:
                        t = subtext.split(char)
                        subtext = ' '.join(t)
                subtext = subtext.split()
                nt = split[i].strip(subtext[-1]) + '(%s/100)'%subtext[-1]
            expression = expression + nt
    else:
        expression = text
    
    return expression

def equalto(text, maxdec=5):
    """
    Execute the mathematical expression given
    """
    newtext = getmultiply(text)
    newtext = getpercent(newtext)
    expression = 'num = %s'%newtext
    
    result = {}
    exec(expression, globals(), result)
    num = result['num']
    
    if len(str(num)) > maxdec:
        num = round(num, 5)
    
    return num
    