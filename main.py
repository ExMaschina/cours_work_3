import utils

def main():
    data = load_data()
    succ_items = get_trasactions(data)
    sort_items = successful_actions(succ_items)
    items = chosen_actions(sort_items)
    for item in items:
        print(date_correction['date'], item['description'])
        print(get_card(item), get_account(item))
        print(get_money(item))
        print()


if __name__ == '__main__':
    main()