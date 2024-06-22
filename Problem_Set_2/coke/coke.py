def main():
    coke_cost = 50
    coin_inserted = 0

    while coin_inserted < coke_cost:
        amount_due = coke_cost - coin_inserted
        print(f"Amount Due: {amount_due}")

        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            coin_inserted += coin
        else:
            print("Invalid coin. Please insert a coin of 25, 10, or 5 cents.")

    change_owed = coin_inserted - coke_cost
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
