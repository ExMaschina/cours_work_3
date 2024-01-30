from utils import get_transactions, successful_actions, chosen_actions, date_correction
from utils import get_card, get_account, get_money
from read_json import load_json

def main():
    data = load_json()

    succ_items = get_transactions(data)
    sort_items = successful_actions(succ_items)
    items = chosen_actions(sort_items)
    for item in items:
        print(date_correction(item['date']), item['description'])
        print(get_card(item), get_account(item))
        print(get_money(item))
        print()


if __name__ == '__main__':
    main()