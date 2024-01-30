def get_transactions(data):
    """Чтение json-файла"""
    items = [item for item in data if item.get('state') == 'EXECUTED']
    return items


def successful_actions(succ_items):
    """Создание списка успешных операций"""
    succ_items.sort(key=lambda x: x.get('date'), reverse=True)
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
        if len(card) == 3:
            return card[0] + card[1] + ' ' + card[2][-16:-12] + ' ' + card[2][-12:-10] + '** ****' + ' ' + card[2][-4:]
        if len(card) == 2:
            return card[0] + ' ' + card[1][-16:-12] + ' ' + card[1][-12:-10] + '** ****' + ' ' + card[1][-4:]
    else:
        return ""


def get_account(item):
    """Маскировка счёта получателя"""
    account = item['to'].split()
    return f"-> Счёт: **{account[1][-4:]}"


def get_money(item):
    """Вывод количества денег"""
    return f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}"






