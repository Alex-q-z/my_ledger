import numpy as np
import datetime
import math
import csv
import sys

class Expense:
    def __init__(self, expense_date, expense_title, expense_place,
                 expense_amount, expense_approach):
        self.date = expense_date
        self.title = expense_title
        self.place = expense_place
        self.amount = expense_amount
        self.approach = expense_approach
    def description(self):
        system.separation_line_2()
        print("Expense Description")
        print("Date:", self.date)
        print("Title:", self.title)
        print("Place:", self.place)
        print("Amount:", self.amount)
        print("Approach:", self.approach)

class List:
    def __init__(self, list_title):
        self.title = list_title
        self.num_expense = 0
        self.list_expense = []
    def append_expense(self, new_expense):
        self.list_expense.append(new_expense)
        self.num_expense += 1
    def description(self):
        system.separation_line_1()
        print("List Description")
        print("Title:", self.title)
        print("Num of expenses:", self.num_expense)
        for single_expense in self.list_expense:
            single_expense.description()
        system.separation_line_1()
    def write_to_csv(self):
        with open('exp_ledger.csv', mode='w') as ledger:
            ledger_writer = csv.writer(ledger, delimiter=',', quotechar='"',
                                       quoting=csv.QUOTE_MINIMAL)
            ledger_writer.writerow(['expense_id','Date','Title','Place',
                                    'Amount','Approach'])
            for single_expense in self.list_expense:
                ledger_writer.writerow([self.list_expense.index(single_expense)+1,
                                        single_expense.date,
                                        single_expense.title,
                                        single_expense.place,
                                        single_expense.amount,
                                        single_expense.approach])
    # def read_from_csv(list_obj):

class User:
    def __init__(self):
        self.active_flag = 1
    def add_expense(self):
        '''
        # default expense for testing
        dinner = Expense("7/22","dinner","nella",20,"credit")
        # dinner.description()
        this_week = List("this week's expenses")
        #this_week.description()
        this_week.append_expense(dinner)
        #this_week.description()
        this_week.write_to_csv()
        '''

        system.separation_line_2()
        print("Where would you like to add the expense:",
              "1: to a new ledger 2: to an existing ledger",
              "b: back to last branch q: quit whole program", sep = '\n')
        op = input()
        if op == '1':
            print("new ledger initializing under progress ......")
        elif op == '2':
            system.under_construction()
        elif op == 'q':
            system.terminate()
        else:
            system.display_error(0)

        print("add_expense executed")

class System:
    def __init__(self):
        self.sys_active = 1
        self.time = str(datetime.datetime.now())
    def welcome(self):
        print("Welcome to my_ledger", "Current Version: 0.3",
              "Author: Qizheng Zhang", sep = '\n')
    def display_error(self,error_code):
        if error_code == 0: # invalid_input
            print("Invalid input. Please try again.")
    def under_construction(self):
        print("this function is under construction")
    def separation_line_1(self):
        print("========================================")
    def separation_line_2(self):
        print("----------------------------------------")
    def terminate(self):
        system.separation_line_1()
        print("my_ledger closed")
        sys.exit(0)
    def op_branch(self):
        # this might be modified using recursion
        loop_flag = 1
        while loop_flag:
            system.separation_line_1()
            print("Please choose what you would like to do:",
                  "1: add an expense 2: view a ledger q: exit", sep = '\n')
            op = input()
            if op == '1':
                user.add_expense()
            elif op == '2':
                system.under_construction()
                continue
            elif op == 'q':
                system.terminate()
            else:
                system.display_error(0)

def main():
    system.welcome()

    system.op_branch()

    system.terminate()
    # end of main

# Below for global contents
system = System()
user = User()
main()
