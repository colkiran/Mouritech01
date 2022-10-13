
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass


class Manager(Employee):

    def doJob(self):
        print("Manager's Job......")


class Developer(Employee):

    def doJob(self):
        print("Developer's Job......")


def BankJob(emp):
    print("Bankjob started.......")
    emp.doJob()
    print("Bankjob ended........")
    print("-" * 40)

Mike = Manager()
Dave = Developer()


BankJob(Mike)
BankJob(Dave)