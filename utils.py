def get_transactions(data):
    """Чтение json-файла"""
    items = [item for item in data if item.get('state') == 'EXECUTED']
    return items


def successful_actions(succ_items):
    """Создание списка успешных операций"""
    succ_items.sort(key=lambda x: x.get('data'), reverse=True)
    return succ_items


def chosen_actions(sort_items):
    """Выбор 5 необходимых операций"""
    items = sort_items[:5]
    return items


def date_correction(date):
    """Исправление формата даты"""
    corr_date = date.split('T')
    return corr_date[0][-2:] + corr_date[0][-6:-2] + corr_date[0][-10:-6]


def get_card(item):
    """Маскировка карты отправителя"""
    if item['description'] != 'Открытие вклада':
        card = item['from'].split()
        if card.count(' ') > 1:
            return card[0:3] + ' ' + card[4:5] + '** **** ' + card[-4:]


def get_account(item):
    """Маскировка счёта получателя"""
    if item['description'] != 'Открытие вклада':
        account = item['to'].split()
        if account.count(' ') > 0:
            return print ((len(account) - 4) * '*' + account[-4:])



