import re
from decimal import Decimal
from datetime import datetime



pattern = r"\w+\s+Confirmed\.\s+Ksh(?P<amount_paid>[\d,|\d]+).00\s+\w+\s+\w+\s+(?P<vendor_name>[\w\s]+)[\s|\.]+on\s+(?P<date_paid>[0-9][0-9]/[0-9][0-9]/[0-9][0-9])\s+at\s+(?P<time>[0-9]+:[0-9][0-9]\s+\w+)[\.|\s]+New\s+M-PESA\s+balance\s+is\s+Ksh(?P<mpesa_balance>[\d|,]+\.[\d][\d]+)\.\s+Transaction\scost,\sKsh(?P<transaction_cost>[\d]+\.[0-9][0-9])\..+"
test_text = """THISCODE Confirmed. Ksh9,000.00 paid to THAT COMPANY LIMITED. on 12/12/22 at
12:25 AM.New M-PESA balance is Ksh10,508.68. Transaction cost, Ksh0.00. Amount
you can transact within the day is 290,960.00. Pay with M-PESA GlobalPay virtual
Visa card linked to MPESA wallet. More Promotional Stuff"""
# 1. Read in text file
def read_sms_file():
    all_texts = []
    with open("copy2.txt","r") as lines:
        data = lines.readlines()
        data = "".join(data)
        # print(data)
        return data


# 2. Parse SMS
def parse_sms():
    data = read_sms_file()
    all_amounts = []
    matches = re.finditer(pattern, data)
    for match in matches:
        payload = match.groupdict()
        print(payload)
    return payload

# 3. Create Payload to create Expense Record
def create_payload():
    # data = read_sms_file()
    sms_payload = parse_sms()
    # amount_paid = sms_payload["amount_paid"]
    try:
        amount_paid = int(sms_payload["amount_paid"])
    except ValueError:
        amount_paid = amount.replace(",","")
        print(amount_paid)
    transaction_cost = Decimal(sms_payload["transaction_cost"])  
    date_obj = datetime.strptime(sms_payload["date_paid"], '%d/%m/%y').date()
    time_str = sms_payload["time"][0:4]
    time_obj = datetime.strptime(time_str,'%H:%M').time()
    expense_dict = dict(amount_spent=amount_paid, payee=sms_payload["vendor_name"], date=date_obj, time=time_obj, transaction_cost=transaction_cost)
    print(expense_dict)
    # commit record to DB 

    # return(expense_dict)
     
   
create_payload()









