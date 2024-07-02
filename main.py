import tkinter as tk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.books = []

        
        self.title_label = tk.Label(root, text="Title")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.author_label = tk.Label(root, text="Author")
        self.author_label.grid(row=1, column=0, padx=10, pady=10)
        self.author_entry = tk.Entry(root)
        self.author_entry.grid(row=1, column=1, padx=10, pady=10)

        self.year_label = tk.Label(root, text="Year")
        self.year_label.grid(row=2, column=0, padx=10, pady=10)
        self.year_entry = tk.Entry(root)
        self.year_entry.grid(row=2, column=1, padx=10, pady=10)

        
        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(root, text="Update Book", command=self.update_book)
        self.update_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(root, text="Delete Book", command=self.delete_book)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(root, text="View Books", command=self.view_books)
        self.view_button.grid(row=6, column=0, columnspan=2, pady=10)

        
        self.book_listbox = tk.Listbox(root, width=50)
        self.book_listbox.grid(row=7, column=0, columnspan=2, pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        if title and author and year:
            self.books.append({"title": title, "author": author, "year": year})
            messagebox.showinfo("Success", "Book added successfully!")
            self.clear_entries()
            self.view_books()
        else:
            messagebox.showwarning("Warning", "Please enter title, author, and year")

    def update_book(self):
        selected_book = self.book_listbox.get(tk.ACTIVE)
        if selected_book:
            index = self.book_listbox.curselection()[0]
            new_title = self.title_entry.get()
            new_author = self.author_entry.get()
            new_year = self.year_entry.get()
            if new_title and new_author and new_year:
                self.books[index] = {"title": new_title, "author": new_author, "year": new_year}
                messagebox.showinfo("Success", "Book updated successfully!")
                self.clear_entries()
                self.view_books()
            else:
                messagebox.showwarning("Warning", "Please enter title, author, and year")
        else:
            messagebox.showwarning("Warning", "Please select a book to update")

    def delete_book(self):
        selected_book = self.book_listbox.get(tk.ACTIVE)
        if selected_book:
            index = self.book_listbox.curselection()[0]
            del self.books[index]
            messagebox.showinfo("Success", "Book deleted successfully!")
            self.view_books()
        else:
            messagebox.showwarning("Warning", "Please select a book to delete")

    def view_books(self):
        self.book_listbox.delete(0, tk.END)
        for book in self.books:
            self.book_listbox.insert(tk.END, f"{book['title']} by {book['author']} ({book['year']})")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
