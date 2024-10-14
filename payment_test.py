def get_payment(to_pay: float) -> float:
    cash_or_card = ""
    if float(to_pay) > 100.00:
        change_amount = "0.00"
        rounding_amount = "-0.00"
        print("Payment by credit card only.")
        return to_pay
    while True:
        try:
            cash_or_card = str(input("Pay by cash or credit card: ")).strip().lower()
            if cash_or_card != 'cash' and cash_or_card != "card":
                continue
            else:
                break
        except Exception:
            pass  # Place the required messages or logic

    if cash_or_card == 'cash':
        received = get_cash(int(to_pay))
        return received
    if cash_or_card == 'card':
        change_amount = '0.00'
        rounding_amount = '-0.00'
        return to_pay


def get_cash(minimum_cash: int) -> int:
    cash_value_sum = 0
    while True:
        try:
            cash_value = float(input("Enter cash: "))
            if not (is_cash(cash_value)):
                print("Invalid banknote!")
                continue
            cash_value_sum = cash_value_sum + cash_value
            print(f'Payment received: ${cash_value_sum:.2f}')
            if float(cash_value_sum) >= float(minimum_cash):
                break
            return cash_value_sum
        except Exception:
            pass  # Place the required messages or logic
