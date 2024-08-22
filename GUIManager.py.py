import tkinter as tk
from tkinter import messagebox
from OperationsManager import OperationsManager

class GUIManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.operations_manager = OperationsManager()

        # Create and arrange widgets
        self.create_widgets()

    def create_widgets(self):
        # Label for instructions
        self.label = tk.Label(self.root, text="Choose an option:")
        self.label.pack(pady=10)

        # Buttons for each option
        tk.Button(self.root, text="Add Book", command=self.add_book).pack(pady=5)
        tk.Button(self.root, text="Print Library Books", command=self.print_library_books).pack(pady=5)
        tk.Button(self.root, text="Search Books by Prefix", command=self.search_books_by_prefix).pack(pady=5)
        tk.Button(self.root, text="Add User", command=self.add_user).pack(pady=5)
        tk.Button(self.root, text="Borrow Book", command=self.borrow_book).pack(pady=5)
        tk.Button(self.root, text="Return Book", command=self.return_book).pack(pady=5)
        tk.Button(self.root, text="Print Users Who Borrowed Books", command=self.print_users_borrowed).pack(pady=5)
        tk.Button(self.root, text="Print All Users", command=self.print_all_users).pack(pady=5)

    def add_book(self):
        def submit():
            book_id = entry_id.get()
            book_name = entry_name.get()
            book_quantity = entry_quantity.get()
            self.operations_manager.admin.add_book(book_id, book_name, book_quantity)
            add_book_window.destroy()

        add_book_window = tk.Toplevel(self.root)
        add_book_window.title("Add Book")

        tk.Label(add_book_window, text="Book ID").pack(pady=5)
        entry_id = tk.Entry(add_book_window)
        entry_id.pack(pady=5)

        tk.Label(add_book_window, text="Book Name").pack(pady=5)
        entry_name = tk.Entry(add_book_window)
        entry_name.pack(pady=5)

        tk.Label(add_book_window, text="Book Quantity").pack(pady=5)
        entry_quantity = tk.Entry(add_book_window)
        entry_quantity.pack(pady=5)

        tk.Button(add_book_window, text="Add", command=submit).pack(pady=20)

    def print_library_books(self):
        books = self.operations_manager.admin.print_all_books()
        messagebox.showinfo("Library Books", books)

    def search_books_by_prefix(self):
        def search():
            query = entry_query.get()
            found_books = self.operations_manager.admin.search_for_book(query)
            if found_books:
                messagebox.showinfo("Search Results", ", ".join(found_books))
            else:
                messagebox.showinfo("Search Results", "No books found")
            search_window.destroy()

        search_window = tk.Toplevel(self.root)
        search_window.title("Search Books by Prefix")

        tk.Label(search_window, text="Enter prefix").pack(pady=5)
        entry_query = tk.Entry(search_window)
        entry_query.pack(pady=5)

        tk.Button(search_window, text="Search", command=search).pack(pady=20)

    def add_user(self):
        def submit():
            user_id = entry_id.get()
            user_name = entry_name.get()
            self.operations_manager.admin.add_user(user_id, user_name)
            add_user_window.destroy()

        add_user_window = tk.Toplevel(self.root)
        add_user_window.title("Add User")

        tk.Label(add_user_window, text="User ID").pack(pady=5)
        entry_id = tk.Entry(add_user_window)
        entry_id.pack(pady=5)

        tk.Label(add_user_window, text="User Name").pack(pady=5)
        entry_name = tk.Entry(add_user_window)
        entry_name.pack(pady=5)

        tk.Button(add_user_window, text="Add", command=submit).pack(pady=20)

    def borrow_book(self):
        def submit():
            user_name = entry_user_name.get()
            book_name = entry_book_name.get()
            self.operations_manager.admin.borrow_book(user_name, book_name)
            borrow_book_window.destroy()

        borrow_book_window = tk.Toplevel(self.root)
        borrow_book_window.title("Borrow Book")

        tk.Label(borrow_book_window, text="User Name").pack(pady=5)
        entry_user_name = tk.Entry(borrow_book_window)
        entry_user_name.pack(pady=5)

        tk.Label(borrow_book_window, text="Book Name").pack(pady=5)
        entry_book_name = tk.Entry(borrow_book_window)
        entry_book_name.pack(pady=5)

        tk.Button(borrow_book_window, text="Borrow", command=submit).pack(pady=20)

    def return_book(self):
        def submit():
            user_name = entry_user_name.get()
            book_name = entry_book_name.get()
            self.operations_manager.admin.return_book(user_name, book_name)
            return_book_window.destroy()

        return_book_window = tk.Toplevel(self.root)
        return_book_window.title("Return Book")

        tk.Label(return_book_window, text="User Name").pack(pady=5)
        entry_user_name = tk.Entry(return_book_window)
        entry_user_name.pack(pady=5)

        tk.Label(return_book_window, text="Book Name").pack(pady=5)
        entry_book_name = tk.Entry(return_book_window)
        entry_book_name.pack(pady=5)

        tk.Button(return_book_window, text="Return", command=submit).pack(pady=20)

    def print_users_borrowed(self):
        users_borrowed = "\n".join(
            f"The user {user.name} borrowed the books {', '.join(books)}"
            for user, books in self.operations_manager.admin.users.items() if books is not None
        )
        if not users_borrowed:
            users_borrowed = "No users have borrowed books"
        messagebox.showinfo("Users Borrowed Books", users_borrowed)

    def print_all_users(self):
        users = "\n".join(user.name for user in self.operations_manager.admin.users)
        if not users:
            users = "No users available"
        messagebox.showinfo("All Users", users)

if __name__ == "__main__":
    root = tk.Tk()
    gui_manager = GUIManager(root)
    root.mainloop()
