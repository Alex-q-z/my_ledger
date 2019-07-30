import numpy as np
import datetime
import math
import csv
import sys
import os

class Record:
    def __init__(self, record_date, record_type, record_title, record_place,
                 record_amount, record_approach, record_remark = ' '):
        self.date = record_date
        self.type = record_type
        self.title = record_title
        self.place = record_place
        self.amount = record_amount
        self.approach = record_approach
        self.remark = record_remark
    def description(self):
        system.separation_line_2()
        if self.type == "exp":
            print("Expense Description")
            print("Date:", self.date)
            print("Title:", self.title)
            print("To:", self.place)
            print("Amount:", self.amount)
            print("Approach:", self.approach)
            print("Remark:", self.remark)
        elif self.type == "inc":
            print("Income Description")
            print("Date:", self.date)
            print("Title:", self.title)
            print("From:", self.place)
            print("Amount:", self.amount)
            print("Approach:", self.approach)
            print("Remark:", self.remark)

class Ledger:
    def __init__(self, Ledger_title):
        self.title = Ledger_title
        self.num_record = 0
        self.list_record = []
        self.total_exp = 0.0
        self.total_inc = 0.0
        self.net_spending = 0.0
    def description(self):
        system.separation_line_1()
        print("Ledger Description")
        print("Title:", self.title)
        print("Num of records:", self.num_record)
        print("Total expense:", round(self.total_exp,2))
        print("Total income:", round(self.total_inc,2))
        print("Net spending:", round(self.net_spending,2))
        for single_record in self.list_record:
            single_record.description()
    def append_record(self, new_record):
        self.list_record.append(new_record)
        self.num_record += 1
        if new_record.type == "exp":
            self.total_exp += float(new_record.amount)
            self.net_spending += float(new_record.amount)
        elif new_record.type == "inc":
            self.total_inc += float(new_record.amount)
            self.net_spending -= float(new_record.amount)
    def write_to_csv(self, name_csv):
        # write the info in the Ledger object into a .csv file
        with open(name_csv, mode='w') as ledger_csv:
            ledger_writer = csv.writer(ledger_csv, delimiter=',', quotechar='"',
                                       quoting=csv.QUOTE_MINIMAL)
            ledger_writer.writerow(['record_id','Date','Type','Title','To/From',
                                    'Amount','Approach','Remark'])
            for single_record in self.list_record:
                ledger_writer.writerow([self.list_record.index(single_record)+1,
                                        single_record.date,
                                        single_record.type,
                                        single_record.title,
                                        single_record.place,
                                        single_record.amount,
                                        single_record.approach,
                                        single_record.remark])
    def read_from_csv(self, name_csv):
        # read the info in a .csv file into a Ledger object
        with open(name_csv, mode='r') as ledger_csv:
            ledger_reader = csv.reader(ledger_csv, delimiter=',')
            line_count = 0
            for row in ledger_reader:
                if line_count == 0: # skip header
                    line_count += 1
                else:
                    date, type, title, place = row[1], row[2], row[3], row[4]
                    amount, approach, remark = row[5], row[6], row[7]
                    self.append_record(Record(date,type,title,place,amount,approach,remark))
                    line_count += 1

class User:
    def __init__(self):
        self.active_flag = 1
    def op_branch(self):
        # this might be modified using recursion
        while 1:
            system.separation_line_1()
            print("Please choose what you would like to do:",
                  "1: add a record 2: view a ledger q: exit", sep = '\n')
            op = input().strip()
            if op == '1':
                user.add_record_branch()
            elif op == '2':
                user.view_ledger()
            elif op == 'q':
                system.terminate()
            else:
                system.display_error(0)

    # def_record_branch starts
    def add_record_branch(self):
        '''
        # default record for testing
        dinner = Record("7/22","exp","dinner","nella",20,"credit")
        # dinner.description()
        this_week = Ledger("this week's records")
        #this_week.description()
        this_week.append_record(dinner)
        #this_week.description()
        this_week.write_to_csv()
        '''
        system.separation_line_2()
        print("Enter info of the record:")
        input_date = input("Date:").strip()
        input_type = input("'exp':expense/'inc':income?:").strip()
        input_title = input("Title:").strip()
        input_place = input("Place:").strip()
        input_amount = input("Amount:").strip()
        input_approach = input("Approach:").strip()
        input_remark = input("Remark:").strip()

        while 1:
            system.separation_line_2()
            print("Where would you like to add the record:",
                "1: to a new ledger 2: to an existing ledger",
                "n: I don't want to add a record",
                "q: give up and quit whole program", sep = '\n')
            op = input().strip()
            if op == '1':
                # create a new .csv file and write the record & ledger
                print("Please enter the title of the ledger to create below.",
                      "Note: you may go back to the main branch by entering exit().", sep = '\n')
                ledger_title = input().strip()
                if ledger_title == "exit()":
                    user.op_branch()
                    break
                name_csv = ledger_title + '.csv'
                new_ledger = Ledger(ledger_title)
                new_ledger.append_record(Record(input_date, input_type, input_title,
                        input_place, input_amount, input_approach, input_remark))
                new_ledger.write_to_csv(name_csv)
                break
            elif op == '2':
                # append a record to an existing .csv file
                while 1:
                    system.separation_line_1()
                    print("Please enter the title of the ledger to open below.",
                          "Note: you may go back to the main branch by entering exit().", sep = '\n')
                    ledger_title = input().strip()
                    if ledger_title == "exit()":
                        user.op_branch()
                        break
                    name_csv = ledger_title + ".csv"
                    exist_flag = os.path.isfile(name_csv)
                    if exist_flag:
                        # continue only when the input ledger exists
                        curr_ledger = Ledger(ledger_title)
                        curr_ledger.read_from_csv(name_csv)
                        curr_ledger.append_record(Record(input_date, input_type, input_title,
                            input_place, input_amount, input_approach, input_remark))
                        curr_ledger.write_to_csv(name_csv)
                        break
                    else:
                        system.display_error(1)
                break
            elif op == 'n':
                user.op_branch()
                break
            elif op == 'q':
                system.terminate() # directly exit the program
            else:
                system.display_error(0)

    # view_ledger starts
    def view_ledger(self):
        while 1:
            system.separation_line_1()
            print("Please enter the title of the ledger to view below.",
                  "Note: you may go back to the main branch by entering exit().", sep = '\n')
            ledger_title = input().strip()
            if ledger_title == "exit()":
                user.op_branch()
                break
            name_csv = ledger_title + '.csv'
            exist_flag = os.path.isfile(name_csv)
            if exist_flag:
                # continue only when the input ledger exists
                curr_ledger = Ledger(ledger_title)
                curr_ledger.read_from_csv(name_csv)
                curr_ledger.description()
                break
            else:
                system.display_error(1)

class System:
    def __init__(self):
        self.sys_active = 1
        self.time = str(datetime.datetime.now())
    def welcome(self):
        system.separation_line_1()
        print("Welcome to my_ledger", "Current Version: 1.2",
              "Author: Qizheng Zhang", sep = '\n')
    def display_error(self,error_code):
        system.separation_line_1()
        if error_code == 0: # invalid_input
            print("Invalid input: please try again.")
        elif error_code == 1: #non-existing_ledger
            print("The indicated ledger doesn't exist, please check again.")
    def under_construction(self):
        system.separation_line_1()
        print("this function is under construction")
    def separation_line_1(self):
        print("========================================")
    def separation_line_2(self):
        print("----------------------------------------")
    def terminate(self):
        system.separation_line_1()
        print("my_ledger closed")
        sys.exit(0)

def main():
    system.welcome()

    user.op_branch()

    system.terminate()
    # end of main

if __name__== "__main__":
    # Below for global contents
    system = System()
    user = User()
    main()
