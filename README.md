# Project Description
This repository contains code used to create the two classes as the first-semester data engineering project at AltSchool Africa. The project contains two classes - Expense and ExpenseDB.
The Expense class contains five (5) attributes (id, title, amount, created_at, updated_at) in which two (title, amount) are expected to be filled at the point of instantiation. The Expense class also has two methods, update (to update either title or amount, time of update is captured) and to_dict (which returns a list of dictionaries representing the expenses).

The ExpenseDB class manages a collection of expense objects. It has a single attribute which is the expense to be stored in the database, this is stored in a list and the list is empty at instantiation. It also has the add_expense, remove_expense, get_expense_by_id, get_expense_by_title, to_dict methods.

## How to Clone
You can clone this repository by running the code below.
git clone https://https://github.com/DanielSarumi/AltschoolProjectFS/.git

## How to Run
Below are examples of how to run the code.

expense_db = ExpenseDB()
expense_db.add_expense('Feeding', 50)
expense_db.add_expense('Flex', 30)
for expense in expense_db.expenses:
    print(expense.to_dict())
