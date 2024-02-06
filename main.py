from utils import get_transactions, sort_date, chosen_actions, date_correction
from utils import get_card, get_account, get_money
from read_json import load_json

def main():
    data = load_json()

    sorted_date = get_transactions(data)
    sort_items = sort_date(sorted_date)
    items = chosen_actions(sort_items)
    for item in items:
          print(date_correction(item['date']), item['description'])
          print(get_card(item), get_account(item))
          print(get_money(item))
          print()


if __name__ == '__main__':
    main()