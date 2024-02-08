from utils import sort_date, chosen_actions, date_correction, get_card, get_account, get_money

def test_date_correction():
    assert date_correction("2018-08-17T03:57:28.607101") == '17.08.2018'

def test_get_card():
    assert get_card({'description': '', "from": "Maestro 7810841234565568"}) == 'Maestro 7810 84** **** 5568'
    assert get_card({'description': '', "from": "Visa Platinum 3530191547567121"}) == ('Visa Platinum 3530 19** **** '
                                                                                       '7121')
    assert get_card({'description': 'Открытие вклада', "from": "Visa Platinum 1813166339376336"}) == ''



def test_get_account():
    assert get_account({'to': "Счет 35383033474447895560"}) == '-> Счёт: **5560'

def test_chosen_actions():
    assert chosen_actions("") == ""

# def get_money():
#     assert get_money({'operationAmount''amount': "6004.00", 'operationAmount''currency''name': "RUB"}) == "6004.00 RUB"



