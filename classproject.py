from uuid import uuid4
from datetime import datetime

class Expense():
    def __init__(self, title, amount):
        self.id = str(uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.created_at.isoformat()
        }
    
    def __repr__(self) -> str:
        return f'{self.id}_{self.amount}'


class ExpenseDB():
    def __init__(self):
        self.DB = []

    def add_expense(self, expense):
        self.DB.append(expense)
        print(f'{expense} added successfully')
        return expense.id
    
    def remove_expense(self, expense_id):
        self.DB = [x for x in self.DB if x.id != expense_id]
        print(f'expense with id {id} has been successfuly removed')

    def get_expense_by_id(self, expense_id):
        expense = [x for x in self.DB if x.id == expense_id]
        if len(expense) == 0:
            return None
        return expense[0]
    
    def get_expense_by_title(self, expense_title):
        expense = [x for x in self.DB if x.id == expense_title]
        if len(expense) == 0:
            return None
        return expense[0]
    
    def to_dict(self):
        return [expense.to_dict() for expense in self.DB]


    