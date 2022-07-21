import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt 


# x = np.arange(-2, 3, 0.1)

# def f(x):
#     return 2*x + 5
# y = f(x)
# plt.plot(x,y,color = 'g',linewidth = 3)
# plt.xlabel('x')
# plt.xlabel('y')
# plt.show()


# x = np.arange(-2, 3, 0.1)

# def f(x):
#     return -3*x + 5
# y = f(x)
# plt.plot(x,y,color = 'g',linewidth = 3)
# plt.xlabel('x')
# plt.xlabel('y')
# plt.show()


# x = np.arange(0, 7, 0.2)

# def f(x):
#     return 4 / (2 + (3 * (2**x)))  
# y = f(x)
# plt.plot(x,y,color = 'g',linewidth = 3)
# plt.xlabel('x')
# plt.xlabel('y')
# plt.show()


# a = 1
# b = -4
# c = 5
# delta = b**2 - 4*a*c
# if delta < 0:
#     print("não possui raiz real")
# else:
#     x1 = (-b + np.sqrt(delta)) / (2 * a)
#     x2 = (-b - np.sqrt(delta)) / (2 * a)
#     print("x’=", x1)
#     print("x’’=", x2)

# x = np.arange(1, 100, 0.1)

# def f(x):
#     return np.exp(x)
# y = f(x)
# plt.plot(x,y,color = 'g',linewidth = 3)
# plt.xlabel('x')
# plt.xlabel('y')
# plt.grid(True)
# plt.show()

# sy.init_printing()
# x = sy.symbols('x')
# f = 1/(1 + sy.exp(-x))
# p = sy.plot(f, xlim=(-5, 5), ylim=(-0.5, 2), show=True)
# plt.show()


# sy.init_printing()
# x = sy.symbols('x')
# f = sy.tanh(x)
# p = sy.plot(f, xlim=(-5, 5), ylim=(-2, 2), show=True)
# plt.show()


# sy.init_printing()
# x = sy.symbols('x')
# f = sy.tanh(x)
# p = sy.plot(f, xlim=(-5, 5), ylim=(-2, 2), show=True)
# plt.show()

# sy.init_printing()
# x = sy.symbols('x')
# f = sy.tanh(x)
# p = sy.plot(f, xlim=(-5, 5), ylim=(-2, 2), show=True)
# plt.show()


# x=np.arange(-4,4,0.1) #intervalo [A, B] com 0.1 é o passodef f(x):
# n=x.shape[0]
# y=np.ones(n)
# for i in range(n):
#     if x[i]<-2:
#         y[i]=-2
#     if x[i]>=-2 and x[i]<2:
#         y[i]=x[i]
#     if x[i]>2:
#         y[i]=2
# plt.plot(x,y,color='green',linewidth=3)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.show()

# a = np.array([[1,2,3,4],[5,6,7,8]])
# b = np.array([[10,20,-3,5],[8,9,-7,80]])
# soma = a + b
# print(soma)



# a = np.array([[1,4,7],[4,2,-1],[7,1/2,np.sqrt(5)]])
# c = 5 * a
# print(c)

# a = np.array([[2,3,8],[1,-4,0]])
# c = np.array([[2,0],[8,6],[-4,-10]])
# s = 3 * a-1/2 * c.T
# print(s)



# a = np.array([[1,3,2],[0,5,-1]])
# c = np.array([[3,0],[4,-2],[1,6]])

# k = c @ a

# print(k)

# a = np.array([[1,1],[3,4]])
# b = np.array([[4,-1],[-3,4]])
# p1 = a@b
# p2 = b@a
# c = p2 - p1

# print(c)

# x = 0
# A = np.array([[1,-1,x],[2,-9,-7],[0,5,5]])
# detA = np.linalg.det(A)
# print(round(detA,2))

# iris = load_iris()
# x = iris.data[:, 0:5]
# feature_names = ['sepal length (cm)' , 'sepal width (cm)', 'petal length (cm)','petal width (cm)']
# x = pd.DataFrame(x,columns=feature_names)
# # print(x)
# x.hist()
# plt.show()

# dataset = pd.read_csv('Iris.csv', sep=',')
# dataset = pd.DataFrame(dataset)


# a = dataset.describe()
# # print(a)

# media = x['sepal length (cm)'].mean()
# print('Media: ', media)

# mediana =  x['sepal length (cm)'].median()
# # print('Mediana', mediana)

# q1 = x['sepal length (cm)'].quantile(0.25)
# q2 = x['sepal length (cm)'].quantile(0.50)
# q3 = x['sepal length (cm)'].quantile(0.75)
# print('q1',q1)
# print('q2',q2)
# print('q3',q3)

# sns.boxplot(y='petal width (cm)', data=x)
# plt.show()

# print('Frequência ds_categoria:')
# a=pd.value_counts(dataset['Species'])
# a = pd.DataFrame(data=a)
# a.rename(columns={'Species' : 'fi'}, inplace=True)
# soma=a['fi'].sum()
# a['fri %']=a['fi']/soma*100
# a['fri %']=a['fri %'].round(2)
# print(a)


# A = np.array([[0,2,1,2,5],[2,1,2,1,-1],[0,3,4,2,2],[0,0,0,3,1],[0,1,-1,0,1]])
# detA = np.linalg.det(A)
# print(round(detA))

# x = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', ' Sab']
# y = [33,34,35,35,34.5,34,33]   


    
# fig, ax = plt.subplots()
# plt.plot(x,y,color='green',linewidth=3)
# plt.xlabel('Dia')
# plt.ylabel('Temperatura')
# plt.title(f'Temperatura da semana 3')
# plt.show()

a = [30,32,31.5,31,33,34,33]
media = sum(a) / len(a)
print('Media: ', media)