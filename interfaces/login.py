import tkinter as tk
from tkinter import messagebox
from services.database_service import DatabaseService
from interfaces.gui import ExpenseApp

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.db_service = DatabaseService("database/expenses.db")
        self.root.bind('<Return>', lambda event: self.login())

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Usuario").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Contraseña").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Ingresar", command=self.login).grid(row=2, column=0, columnspan=2)

        self.forgot_password_label = tk.Label(self.root, text="Olvidé mi contraseña", fg="blue", cursor="hand2")
        self.forgot_password_label.grid(row=3, column=0, columnspan=2)
        self.forgot_password_label.bind("<Button-1>", lambda e: self.forgot_password())

        tk.Button(self.root, text="Registrar", command=self.open_register_window).grid(row=4, column=0, columnspan=2)

    def open_register_window(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Registra usuario nuevo")
        RegisterApp(register_window)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("input Error", "Por favor complete correctamente los campos Usuario y Contraseña")
            return

        if self.db_service.validate_user(username, password):
            messagebox.showinfo("Logueo exitoso", "Bienvenido!")
            self.root.destroy()
            expense_app = ExpenseApp()
            expense_app.run()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrecta, intente nuevamente")

    def forgot_password(self):
        messagebox.showinfo("Forgot Password", "La recuperación de contraseña aun no se ha realizado.")

    def run(self):
        self.root.mainloop()



class RegisterApp:
    def __init__(self, root):
        self.root = root
        self.db_service = DatabaseService("database/expenses.db")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Usuario").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Contraseña").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Registrar", command=self.register).grid(row=2, column=0, columnspan=2)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            self.db_service.register_user(username, password)
            messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente")
            self.root.destroy()
        else:
            messagebox.showwarning("Error", "Por favor complete todos los campos.")
