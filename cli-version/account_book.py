import json
import os
from datetime import datetime

DATA_FILE = "data.json"

class AccountBook:
    def __init__(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.bill_list = json.load(f)
        else:
            self.bill_list = []

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.bill_list, f, ensure_ascii=False, indent=2)

    def add_bill(self):
        print("\n===== Add New Bill =====")
        kind = input("Type: Income(1) / Expense(2), enter number: ")
        if kind == "1":
            bill_type = "Income"
        elif kind == "2":
            bill_type = "Expense"
        else:
            print("Invalid input, back to menu")
            return

        try:
            money = float(input("Enter amount: "))
        except:
            print("Invalid amount, back to menu")
            return

        category = input("Category: ")
        remark = input("Remark: ")
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        bill = {
            "time": now_time,
            "type": bill_type,
            "money": money,
            "category": category,
            "remark": remark
        }
        self.bill_list.append(bill)
        self.save_data()
        print("Bill added successfully!")

    def show_all(self):
        print("\n======== All Bills ========")
        if len(self.bill_list) == 0:
            print("No bill records")
            return
        for index, item in enumerate(self.bill_list):
            print(f"{index+1} | {item['time']} | {item['type']} | {item['money']} | {item['category']} | {item['remark']}")

    def month_statistics(self):
        print("\n===== Monthly Statistics =====")
        now_month = datetime.now().strftime("%Y-%m")
        income = 0.0
        pay = 0.0
        for item in self.bill_list:
            if item["time"].startswith(now_month):
                if item["type"] == "Income":
                    income += item["money"]
                else:
                    pay += item["money"]
        balance = income - pay
        print(f"Total Income: {income:.2f}")
        print(f"Total Expense: {pay:.2f}")
        print(f"Balance: {balance:.2f}")

    def delete_bill(self):
        self.show_all()
        try:
            idx = int(input("\nEnter index to delete: ")) - 1
            if 0 <= idx < len(self.bill_list):
                del self.bill_list[idx]
                self.save_data()
                print("Deleted successfully")
            else:
                print("Wrong index")
        except:
            print("Invalid input")

    def run(self):
        while True:
            print("\n======== Personal Account Book ========")
            print("1 Add Bill")
            print("2 Show All Bills")
            print("3 Monthly Statistics")
            print("4 Delete Bill")
            print("0 Exit")
            choice = input("Select function: ")
            if choice == "1":
                self.add_bill()
            elif choice == "2":
                self.show_all()
            elif choice == "3":
                self.month_statistics()
            elif choice == "4":
                self.delete_bill()
            elif choice == "0":
                print("Exit, data saved automatically")
                break
            else:
                print("Invalid option")

if __name__ == "__main__":
    app = AccountBook()
    app.run()

