from pycoingecko import CoinGeckoAPI
import tkinter as tk


cg = CoinGeckoAPI()

def send_data():

    # dd-mm-yyyy
    date = date_entry.get()
    string = string_entry.get()

    data = cg.get_coin_history_by_id(id=f'{string}', date=f'{date}', localization='false')
    price = data["market_data"]["current_price"]["usd"]
    crypto_name = data["id"]
    message_label.config(text=f"{crypto_name}: ${price}")
    print("Data sent:",data["id"], data["market_data"]["current_price"]["usd"])

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


message_label = tk.Label(root, text="")
message_label.grid(row=3, column=0, columnspan=2)

root.mainloop()