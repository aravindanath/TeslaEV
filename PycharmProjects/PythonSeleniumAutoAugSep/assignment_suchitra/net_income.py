def net_income(gross_income,state_tax_pct,central_tax_pct):
    v_state_tax = gross_income * (state_tax_pct/100)
    v_central_tax = gross_income * (central_tax_pct/100)
    net_income_after_tax = gross_income - (v_state_tax + v_central_tax)
    return net_income_after_tax
print(net_income(100000,8,5))
