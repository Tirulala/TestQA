import pytest


@pytest.fixture()
def set_ep():
    print("Вход в систему выполнен")
    yield
    print('Выход из системы')

def test_sending_mail_1(set_ep):
    print('Письмо отправлено')

def test_sending_mail_2(set_ep):
    print('Письмо отправлено')