import numpy as np
import math
import csv

class Expense:
    def __init__(self, expense_date, expense_title, expense_place,
                 expense_amount, expense_approach):
        self.date = expense_date
        self.title = expense_title
        self.place = expense_place
        self.amount = expense_amount
        self.approach = expense_approach
    def description(self):
        print("----------------------------------------")
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
        print("========================================")
        print("List Description")
        print("Title:", self.title)
        print("Num of expenses:", self.num_expense)
        for single_expense in self.list_expense:
            single_expense.description()
        print("========================================")

def write_to_csv(list_obj):
    with open('exp_ledger.csv', mode='w') as ledger:
        ledger_writer = csv.writer(ledger, delimiter=',', quotechar='"',
                                   quoting=csv.QUOTE_MINIMAL)
        ledger_writer.writerow(['expense_id','Date','Title','Place',
                                'Amount','Approach'])
        for single_expense in list_obj.list_expense:
            ledger_writer.writerow([list_obj.list_expense.index(single_expense)+1,
                                    single_expense.date,
                                    single_expense.title,
                                    single_expense.place,
                                    single_expense.amount,
                                    single_expense.approach])

def main():
    dinner = Expense("7/22","dinner","nella",20,"credit")
    # dinner.description()

    this_week = List("this week's expenses")
    #this_week.description()
    this_week.append_expense(dinner)
    #this_week.description()

    write_to_csv(this_week)

main()
