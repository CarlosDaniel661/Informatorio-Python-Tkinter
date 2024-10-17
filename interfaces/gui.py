import tkinter as tk
from tkinter import messagebox
from services.expense_service import ExpenseService

class ExpenseApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Control de gastos")
        self.expense_service = ExpenseService()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Descripción").grid(row=0, column=0)
        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Importe").grid(row=1, column=0)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Agregar Gastos", command=self.add_expense).grid(row=2, column=0)
        tk.Button(self.root, text="Ver Gastos", command=self.view_expenses).grid(row=2, column=1)

    def add_expense(self):
        description = self.description_entry.get()
        amount = self.amount_entry.get()

        if description and amount:
            try:
                self.expense_service.add_expense(description, amount)
                messagebox.showinfo("Exitoso", "Nuevo gasto agregado correctamente")
            except ValueError as e:
                messagebox.showwarning("Error", str(e))
        else:
            messagebox.showwarning("Error", "Verifica los datos ingresados para descripción e importe")

    def view_expenses(self):
        expenses = self.expense_service.get_all_expenses()
        view_window = tk.Toplevel(self.root)
        view_window.title("Lista de Gastos")

        listbox = tk.Listbox(view_window, width=50)
        listbox.pack()

        for expense in expenses:
            listbox.insert(tk.END, f"Descripción: {expense.description}, Importe: {expense.amount}")

    def run(self):
        self.root.mainloop()

        