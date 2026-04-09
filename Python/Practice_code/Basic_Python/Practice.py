import tkinter as tk
from tkinter import messagebox

def create_account():
    username = username_entry.get()
    password = password_entry.get()
    confirm = confirm_entry.get()

    if not username or not password or not confirm:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    if password != confirm:
        messagebox.showerror("Password Mismatch", "Passwords do not match.")
        return

    messagebox.showinfo("Success", f"Account created for '{username}'!")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Create Account")
root.geometry("320x220")
root.resizable(False, False)

tk.Label(root, text="Create Account", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Username:", width=12, anchor="w").grid(row=0, column=0, pady=5)
username_entry = tk.Entry(frame, width=20)
username_entry.grid(row=0, column=1)

tk.Label(frame, text="Password:", width=12, anchor="w").grid(row=1, column=0, pady=5)
password_entry = tk.Entry(frame, show="*", width=20)
password_entry.grid(row=1, column=1)

tk.Label(frame, text="Confirm:", width=12, anchor="w").grid(row=2, column=0, pady=5)
confirm_entry = tk.Entry(frame, show="*", width=20)
confirm_entry.grid(row=2, column=1)

tk.Button(root, text="Create Account", command=create_account, bg="#4CAF50", fg="white", width=20).pack(pady=15)

root.mainloop()