from database.connection import DatabaseConnection
from domain.expense import Expense
from services.utils import validate_amount, show_alert_if_needed

class ExpenseService:
    def __init__(self):
        self.db = DatabaseConnection()

    def add_expense(self, description, amount):
        if validate_amount(amount):
            expense = Expense(description, float(amount))
            self.db.execute_query("INSERT INTO expenses (description, amount) VALUES (?, ?)", (expense.description, expense.amount))
            show_alert_if_needed(expense.amount)
        else:
            raise ValueError("Importe inválido")

    def get_all_expenses(self):
        rows = self.db.fetch_all("SELECT description, amount FROM expenses")
        return [Expense(row[0], row[1]) for row in rows]
