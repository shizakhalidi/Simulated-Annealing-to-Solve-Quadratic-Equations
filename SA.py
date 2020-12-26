import random
import numpy as np
import math
import sympy as sy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sympy import N, symbols, cos

def myformula(formula, **kwargs):
    expr = sy.sympify(formula)
    return expr.evalf(subs=kwargs)

def plot(x_values, y_values, i_values, f_values):
    fig, (ax1, ax2) = plt.subplots(2)   
    ax1.plot(i_values,f_values)
    ax1.set(xlabel='iteration', ylabel='function value')
    ax2.plot(i_values,x_values)
    ax2.plot(i_values,y_values)
    plt.xlabel('iteration')
    orange_patch = mpatches.Patch(color='orange', label='x value')
    plt.legend(handles=[orange_patch])
    blue_patch = mpatches.Patch(color='blue', label='y value')
    plt.legend(handles=[orange_patch,blue_patch])
    plt.tight_layout()
    plt.show()
    
def getInitialTemp(function,xmin, xmax,ymin,ymax): #initial temp is calculated by taking average of f values of 4 random x, y values
    x_1=np.random.uniform(xmin, xmax)
    y_1=np.random.uniform(ymin, ymax)
    f_1=myformula(x=x_1,y=y_1,formula=function)
    

    x_2=np.random.uniform(xmin, xmax)
    y_2=np.random.uniform(ymin, ymax)
    f_2=myformula(x=x_2,y=y_2,formula=function)

    x_3=np.random.uniform(xmin, xmax)
    y_3=np.random.uniform(ymin, ymax)
    f_3=myformula(x=x_3,y=y_3,formula=function)

    x_4=np.random.uniform(xmin, xmax)
    y_4=np.random.uniform(ymin, ymax)
    f_4=myformula(x=x_4,y=y_4,formula=function)

    f_avg = (f_1+f_2+f_3+f_4)/4
    return f_avg

def SimAnn(function,xmin, xmax,ymin,ymax,opt_type):#opt_type is either max or min
    
    x_list=[]
    y_list=[]
    f_list=[]
    i_list=[]
    x_curr=np.random.uniform(xmin, xmax) 
    y_curr=np.random.uniform(ymin, ymax)
    f_curr=myformula(x=x_curr,y=y_curr,formula=function)#f is calculated for random x, y values
    #initial temp average of function values
    temp=getInitialTemp(function,xmin, xmax,ymin,ymax)
    
    #print("temp", temp)
    for i in range(100): 
        #print("f_curr",f_curr)
        x_list.append(x_curr)
        y_list.append(y_curr)
        f_list.append(f_curr)
        i_list.append(i)
        temp_last=temp
        temp=temp_last*0.95 #cooling procedure
        x_next=np.random.uniform(xmin, xmax)
        y_next=np.random.uniform(ymin, ymax)
        f_next=myformula(x=x_next,y=y_next,formula=function)#another f val is calculated by taking random x, y values
        diff=f_next - f_curr
        if opt_type=="min" and diff < 0:  #for minimum, f_next should be less than f_curr
            x_curr=x_next
            y_curr=y_next
            f_curr=f_next
        elif opt_type=="max" and diff > 0:  #for maximum f_next should be more than f_curr
            x_curr=x_next
            y_curr=y_next
            f_curr=f_next
        else:
            #print(temp_last)
            #print(diff)
            p= math.exp(-(abs(diff)/temp_last))  
            number = random.uniform(0,1) #random number generated and checked if number is no greater than the prob 
            if number <= p:
                x_curr=x_next  #then make the change x, y values
                y_curr=y_next
                f_curr=f_next
    #print("list of f values:", f_list)
    #print("list of y values:", x_list)
    #print("list of x values:", y_list)
    print("global ", opt_type,"is ", round(f_list[-1],3))
    plot(x_list, y_list, i_list, f_list)


SimAnn("(x^2)+(y^2)", -5, 5, -5, 5, "min")
#SimAnn("((1-x)^2)+100*(((x^2)-y)^2)", -2, 2, -1, 3, "min")
#SimAnn("1+((x^2+y^2)/4000)-(cos(x)*cos(y/sqrt(2)))", -30, 30, -30, 30,"max")
