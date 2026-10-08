def exclusive_to_include(amount, vat):
    return amount * (1 + vat / 100)


excl_vat = float(input("What is the amount excluding VAT?"))
vat_percentage = float(input("What is the percentage of VAT?"))

incl_vat = exclusive_to_include(excl_vat, vat_percentage)

print(f"The inclusive amount you have to pay is: {incl_vat}")
