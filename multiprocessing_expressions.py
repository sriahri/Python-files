import multiprocessing  # For creating the processes

expressions_queue = []  # Queue containing the expressions


# Function that is used to create and store expressions in a queue
def getQueue():
    global expressions_queue
    for i in range(5):
        expression = input("Enter the simple mathematical expression {}: ".format(i + 1))
        expressions_queue.append(expression)


# Function to calculate the result of expressions present in the queue
def solveExpressions():
    while expressions_queue:
        expr = expressions_queue.pop(0)
        result = eval(expr)
        print("Expression: {} = {}".format(expr, result))


# Creating the 2 processes containing the targets as the respective functionalities
process1 = multiprocessing.Process(target=getQueue())
process2 = multiprocessing.Process(target=solveExpressions())

# Start the processes
process1.start()
process2.start()

process1.join()  # Wait till the process1 is complete
process2.join()  # Wait till the process2 is complete

print("Completed")
