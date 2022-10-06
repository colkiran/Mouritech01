
def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def log_details(fnc):               # HOF
    loginfo = "Logging into the service...."

    def innerFun(*args):
        print(loginfo)
        print(fnc(*args))
        print("-" * 40)
    
    return innerFun

sum_logger = log_details(sum)
diff_logger = log_details(diff)

# calling the innerfun which indirectly calls the sum or diff functions
sum_logger(10, 20)
diff_logger(30, 8)
