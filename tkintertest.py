import tkinter as tk

def send_data():
    date = date_entry.get()
    string = string_entry.get()
    data = (date, string)
    print("Data sent:", data)

root = tk.Tk()
root.title("Data Form")

date_label = tk.Label(root, text="Date:")
date_label.grid(row=0, column=0)

date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

string_label = tk.Label(root, text="Crypto Currency:")
string_label.grid(row=1, column=0)

string_entry = tk.Entry(root)
string_entry.grid(row=1, column=1)

send_button = tk.Button(root, text="Send", command=send_data)
send_button.grid(row=2, column=0, columnspan=2)

root.mainloop()