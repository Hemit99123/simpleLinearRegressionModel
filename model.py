import numpy as np
def simpleLinearRegression(x,y,target):
    # pearson R
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    x_sub = np.subtract(x,x_bar)
    y_sub = np.subtract(y,y_bar)
    mul = np.multiply(x_sub,y_sub)
    total = sum(mul)

    power = np.power(x_sub, 2)
    x_power = sum(power)
    power2 = np.power(y_sub, 2)
    y_power = sum(power2)
    mu = np.multiply(x_power,y_power)
    total2 = np.sqrt(mu)

    pearsonsR = np.divide(total,total2)

    # variable (b)
    number = len(y)
    n = (number - 1)
    statY = (y_power/n)
    sY = np.sqrt(statY)
    statX = (x_power/n)
    sX = np.sqrt(statX)
    s = (sY/sX)
    b = (pearsonsR*s)

    # variable (a)
    a = (y_bar-b*x_bar)

    
    # predicting the data given
    y = (a+b*target)
    print([y])    
