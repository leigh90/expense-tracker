import re
from decimal import Decimal
from datetime import datetime
from flask import Flask, render_template
from forms import ExpenseForm

pattern = r"\w+\s+Confirmed\.\s+Ksh(?P<amount_paid>[\d,|\d]+).00\s+\w+\s+\w+\s+(?P<vendor_name>[\w\s]+)[\s|\.]+on\s+(?P<date_paid>[0-9][0-9]/[0-9][0-9]/[0-9][0-9])\s+at\s+(?P<time>[0-9]+:[0-9][0-9]\s+\w+)[\.|\s]+New\s+M-PESA\s+balance\s+is\s+Ksh(?P<mpesa_balance>[\d|,]+\.[\d][\d]+)\.\s+Transaction\scost,\sKsh(?P<transaction_cost>[\d]+\.[0-9][0-9])\..+"

test_text = """THISCODE Confirmed. Ksh9,000.00 paid to THAT COMPANY LIMITED. on 12/12/22 at
12:25 AM.New M-PESA balance is Ksh10,508.68. Transaction cost, Ksh0.00. Amount
you can transact within the day is 215,786.00. Pay with M-PESA GlobalPay virtual
Visa card linked to MPESA wallet. More Promotional Stuff"""

def read_sms_file():
    """
    Read in SMS text file
    """
    all_texts = []
    with open("copy2.txt","r") as lines:
        data = lines.readlines()
        data = "".join(data)
        # print(data)
        return data


def parse_sms():
    """
    Parse SMS to create expenses payload
    """
    data = read_sms_file()
    all_expenses = []
    matches = re.finditer(pattern, data)
    for match in matches:
        payload = match.groupdict()
        all_expenses.append(payload)
        import pdb;pdb.set_trace()
    # print(all_expenses)
    return all_expenses

parse_sms()

def create_payload():
    """
    Sanitize sms payload and create payload to create expense record 
    """
    sms_payload = parse_sms()
    for num in range(len(sms_payload)):
        try:
            amount_paid = int(sms_payload[num]["amount_paid"])
        except ValueError:
            amount_paid = int(sms_payload[num]["amount_paid"].replace(",",""))
            print(amount_paid)

    transaction_cost = Decimal(sms_payload[num]["transaction_cost"])  
    date_obj = datetime.strptime(sms_payload[num]["date_paid"], '%d/%m/%y').date()
    time_str = sms_payload[num]["time"][0:4]
    time_obj = datetime.strptime(time_str,'%H:%M').time()
    expense_dict = dict(amount_spent=amount_paid, payee=sms_payload[num]["vendor_name"], date=date_obj, time=time_obj, transaction_cost=transaction_cost)
    # import pdb; pdb.set_trace()

    print(expense_dict)
    # commit record to DB 

    return(expense_dict)

# # def fill_expense_details():
# #     if request.method == "POST":
# #         item = request.form["item"]
# #         category = request.form["category"]
# #     else:
        

# #     pass

# def record_expense():
#     # {'amount_spent': 380, 'payee': '0782123604', 'date': datetime.date(2022, 11, 17), 'time': datetime.time(9, 38), 'transaction_cost': Decimal('45.00')}
#     new_expense = create_payload()
#     # Trigger a form that launches and asks you to fill certain holes or prefill in the db with the things and the user can call up the expenses later and fill in the missing info
#     # 1. Trigger a form that prefills known details and asks you to fill in the item and category

#     # 2. Create record that will be filled in later has notification in window pane
#     record = Expense(amount_spent=new_expense["amount_spent"],item="", payee=new_expense["payee"], date=new_expense["date"], time=new_expense["time"], transaction_cost=new_expense["transaction_cost"])
#     db.session.add(record)
#     try:
#         db.session.commit()
    
#     pass

# # calculate bank to mobile transfers
# # calculate transaction costs 

# def add_expense_prompt():
#     if request.method == "POST":
#         form = ExpenseForm()
#         amount = request.form["amount"]
#         item = request.form["item"]
#         payee = request.form["payee"]
#         date = request.form["date"]
#         time = request.form["time"]
#         transaction_cost = request.form["transaction_cost"]
#         category = request.form["category"]

#         new_expense = Expense(amount=amount,item=item,payee=payee, date=date, time=time, transaction_cost=transaction_cost, category=category)
#         db.session.add(new_expense)
#         try:
#             db.session.commit()
#         except Exception:
#             db.session.rollback()
#     else:
#         return render_template('new_expense_form.html')

     
   
# create_payload()








