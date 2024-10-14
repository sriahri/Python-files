def cartesianProduct(a,b):
    x = list(a)
    y = list(b)
    result = []
    for i in range(len(x)):
        for j in range(len(y)):
            result.append([x[i],y[j]])
    print('The original sets are :')
    print('Set a: ',*x)
    print('Set b: ',*y)
    print('The cartesian product of the 2 sets is :')
    print(*result)

a = set([1,2,3,4,5])
b = set(['p','q','r','s','t','u'])
cartesianProduct(a, b)
print('Usecase scenarios are :')
print('The most important usecase is that it is used when a decision is to be made by combining more than one variable or input.')
print('For Example, consider we need to buy a car whose color is red, made by mercedes.')
print('In order to see the cars, we need to combine cars made by mercedes and color is red.')
print('So, we need to multiply two sets like manufacturer and color')