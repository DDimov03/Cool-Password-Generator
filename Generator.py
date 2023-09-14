import string
import secrets
import tkinter as tk
from tkinter import messagebox, END, ttk, filedialog
from ttkthemes import ThemedStyle
import pyperclip  # Added library for clipboard functionality

def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_password(password, filename):
    if filename:
        try:
            with open(filename, 'w') as file:
                file.write(password)
            messagebox.showinfo("Password Saved", f"Password saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def validate_password_length():
    length = password_length.get()
    try:
        length = int(length)
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        elif length > 128:
            messagebox.showwarning("Password Length Warning", "Generating passwords longer than 128 characters may not be secure.")
        return True
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for the password length.")
        return False

def generate_password_clicked(text_widget, window, save_checkbox):
    if validate_password_length():
        length = int(password_length.get())
        strong_password = generate_strong_password(length)
        text_widget.delete(1.0, END)  # Clear previous text
        text_widget.insert(tk.END, f"Your Super Strong Password:\n{strong_password}")
        pyperclip.copy(strong_password)  # Copy the password to clipboard
        
        if save_checkbox.get():
            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            save_password(strong_password, filename)

def main():
    global password_length
    window = tk.Tk()
    window.title("Cool Password Generator")
    window.geometry("720x480")
    window.resizable(False, False)  # Make the window non-resizable

    style = ThemedStyle(window)
    style.set_theme("arc")

    title_label = ttk.Label(window, text="Cool Password Generator", font=("Helvetica", 24), padding=20)
    title_label.pack()

    content_frame = ttk.Frame(window, padding=20)
    content_frame.pack(fill=tk.BOTH, expand=True)

    password_length_label = ttk.Label(content_frame, text="Password Length:", font=("Helvetica", 12))
    password_length_label.pack()

    password_length = ttk.Entry(content_frame, font=("Helvetica", 12))
    password_length.insert(0, "Enter password length (1-128)")
    password_length.bind("<FocusIn>", lambda event: password_length.delete(0, END))
    password_length.pack(fill=tk.BOTH, expand=True, pady=5)
    
    # Bind Enter key to the password length entry field
    password_length.bind("<Return>", lambda event: generate_password_clicked(password_text_widget, window, save_checkbox))

    save_checkbox = tk.BooleanVar()
    save_checkbox.set(False)
    save_checkbox_button = ttk.Checkbutton(content_frame, text="Save as Text File", variable=save_checkbox)
    save_checkbox_button.pack(fill=tk.BOTH, expand=True)

    generate_button = ttk.Button(content_frame, text="Generate Super Password 🚀", command=lambda: generate_password_clicked(password_text_widget, window, save_checkbox))
    generate_button.pack(fill=tk.BOTH, expand=True, pady=20)

    password_text_widget = tk.Text(content_frame, wrap=tk.WORD, height=5, font=("Helvetica", 12))
    password_text_widget.pack(fill=tk.BOTH, expand=True)
    password_text_widget.configure(bg="#F0F0F0", fg="#333333", highlightbackground="#4CAF50", highlightcolor="#4CAF50")

    watermark_label = ttk.Label(window, text="Created by Denis Dimov", font=("Helvetica", 10, "italic"), foreground="#999999")
    watermark_label.place(relx=0.01, rely=0.95)

    window.mainloop()

if __name__ == "__main__":
    main()
