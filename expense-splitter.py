def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError('Number of people must be at least 1.')

    print(f'\n--- Summary ---')
    print(f'Total expense: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')


def main() -> None:
    try:
        # Get the total amount
        while True:
            total_amount_input = input('Enter the total amount of the expense: ')
            try:
                total_amount = float(total_amount_input)
                if total_amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
                break
            except ValueError:
                print('Please enter a valid number.')

        # Get a number of people
        while True:
            number_input = input('Enter the number of people: ')
            if number_input.isdigit():
                number_of_people = int(number_input)
                if number_of_people < 1:
                    print('Must be at least 1 person.')
                    continue
                break
            else:
                print('Please enter a valid whole number.')

        # Show summary
        calculate_split(total_amount, number_of_people, currency='$')

        # Get split percentages
        split_total = 0.0
        for person in range(1, number_of_people + 1):
            while True:
                try:
                    split_rate = float(input(f'Enter the splitting rate of person {person} (%): '))
                    if split_rate < 0 or split_rate > 100:
                        print("Rate must be between 0 and 100.")
                        continue
                    split_total += split_rate
                    amount_to_pay = split_rate * total_amount / 100
                    print(f'Person {person} should pay: $ {amount_to_pay:.2f}')
                    break
                except ValueError:
                    print('Please enter a valid number.')

        # Optional: validate total %
        if abs(split_total - 100) > 0.01:
            print(f"\n Warning: Total split is {split_total:.2f}%, not 100%. You may want to review.")

    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
