import random
import tkinter as tk
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            output_label["text"] = "Error: Length must be at least 4"
            strength_label["text"] = ""
            return
    except:
        output_label["text"] = "Error: Enter a number"
        strength_label["text"] = ""
        return
    chars = ""
    if upper_entry.get().lower() == "y": chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower_entry.get().lower() == "y": chars += "abcdefghijklmnopqrstuvwxyz"
    if digits_entry.get().lower() == "y": chars += "0123456789"
    if symbols_entry.get().lower() == "y": chars += "!@#$%"

    if not chars:
        output_label["text"] = "Error: Select at least one type"
        strength_label["text"] = ""
        return

    password = "".join(random.choice(chars) for _ in range(length))

    types = 0
    if any(c.isupper() for c in password): types += 1
    if any(c.islower() for c in password): types += 1
    if any(c.isdigit() for c in password): types += 1
    if any(c in "!@#$%" for c in password): types += 1

    if types == 1:
        strength = "Weak"
    elif types == 2:
        strength = "Medium"
    elif types == 3:
        strength = "Strong"
    else:  
        if length >= 6:
            strength = "Very Strong"
        else:
            strength = "Strong"

    output_label["text"] = "Password: " + password
    strength_label["text"] = "Strength: " + strength

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")

tk.Label(root, text="Password Generator", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Preferred Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

tk.Label(root, text="Include Uppercase? (y/n)").pack()
upper_entry = tk.Entry(root)
upper_entry.pack()

tk.Label(root, text="Include Lowercase? (y/n)").pack()
lower_entry = tk.Entry(root)
lower_entry.pack()

tk.Label(root, text="Include Digits? (y/n)").pack()
digits_entry = tk.Entry(root)
digits_entry.pack()

tk.Label(root, text="Include Symbols? (y/n)").pack()
symbols_entry = tk.Entry(root)
symbols_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
output_label.pack(pady=5)

strength_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
strength_label.pack(pady=5)

root.mainloop()
