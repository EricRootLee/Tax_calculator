def calc_tax(gross_pay, tax) -> int:
    income_tax = gross_pay * (tax / 100)
    net_pay = gross_pay - income_tax
    return net_pay


def total_calc_tax(gross_pay, age) -> int:
    if 0 < age <= 45:
        return calc_tax(gross_pay, 9)
    elif 46 <= age <= 65:
        return calc_tax(gross_pay, 5)
    else:
        return calc_tax(gross_pay, 3)
