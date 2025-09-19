def calculate_finances(monthly_expenses: float, monthly_income: float, tax_rate: float, currency: str) -> None:
    monthly_tax = monthly_income * (tax_rate / 100)
    monthly_net_income = monthly_income - monthly_tax
    money_used_monthly = monthly_expenses
    money_left_monthly = monthly_net_income - money_used_monthly
    yearly_salary = monthly_income * 12
    yearly_tax = monthly_tax * 12
    yearly_net_income = yearly_salary - yearly_tax
    money_used_yearly = money_used_monthly * 12
    money_left_yearly = money_left_monthly * 12

    print('\n---------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Money used monthly: {currency}{money_used_monthly:,.2f}')
    print(f'Money left monthly: {currency}{money_left_monthly:,.2f}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print(f'Money used yearly: {currency}{money_used_yearly:,.2f}')
    print(f'Money left yearly: {currency}{money_left_yearly:,.2f}')
    print('---------------------------')


def main() -> None:
    while True:
        try:
            monthly_income = float(input('Enter your monthly salary: '))
            if monthly_income < 0:
                print("Income must be a positive number.")
                continue
            break
        except ValueError:
            print('Invalid input, please input a number.')

    while True:
        try:
            tax_rate = float(input('Enter your tax rate (%): '))
            if tax_rate < 0:
                print("Tax rate cannot be negative.")
                continue
            break
        except ValueError:
            print('Invalid input, please input a number.')

    while True:
        try:
            monthly_expenses = float(input('Enter your monthly expenses: '))
            if monthly_expenses < 0:
                print("Expenses must be positive.")
                continue
            break
        except ValueError:
            print('Invalid input, please input a number.')

    calculate_finances(monthly_expenses, monthly_income, tax_rate, currency='MYR')


if __name__ == '__main__':
    main()
