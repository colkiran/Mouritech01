



class Manager():

    def doJob(self):
        print("Manager's Job......")


class Developer():

    def doJob(self):
        print("Developer's Job......")


Mike = Manager()
Dave = Developer()

def BankJob(emps):
    print("Bankjob started.......")
    for emp in emps:
        emp.doJob()
    print("Bankjob ended........")
    print("-" * 40)

BankJob([Mike, Dave])
