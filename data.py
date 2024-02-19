import secrets
import random


class Locator:
    @staticmethod
    def name_and_email():
        return ".//fieldset[1]/div/div/input"  # Поле "Имя" на странице Регистрации/
        # Поле "Email" на странице Авторизации

    @staticmethod
    def email_and_pass():
        return ".//fieldset[2]/div/div/input"  # Поле "Email" на странице Регистрации/
        # Поле "Пароль" на странице Авторизации

    @staticmethod
    def password():
        return ".//fieldset[3]/div/div/input"  # Поле "Пароль" на странице Регистрации

    @staticmethod
    def button_registration():
        return ".// *[ @ id = 'root'] / div / main / div / form / button"  # Кнопка "Зарегистрироваться"

    @staticmethod
    def message_invalid_password():
        return ".//fieldset[3] / div / p"  # Подпись "Некорректный пароль"

    @staticmethod
    def button_input():
        return ".//section[2]/div/button"  # Кнопка "Войти в аккаунт" на странице Регистрации/
        # Поле "Оформить заказ" на главной странице

    @staticmethod
    def button_personal_cabinet():
        return "//*[@id='root']/div/header/nav/a/p"  # Кнопка "Личный кабинет"

    @staticmethod
    def button_in():
        return "//*[@id='root']/div/main/div/div/p/a"  # Кнопка "Войти"

    @staticmethod
    def field_login():
        return "html/body/div/div/main/div/div/div/ul/li[2]/div/div/input"  # Поле "Логин" в Личном кабинете

    @staticmethod
    def button_designer():
        return "//*[@id='root']/div/header/nav/ul/li[1]/a/p"  # Кнопка "Конструктор"

    @staticmethod
    def header_assemble_burger():
        return ".//section[1]/h1"  # Надпись "Соберите бургер"

    @staticmethod
    def button_output():
        return ".// nav / ul / li[3] / button"  # Кнопка "Выход"

    @staticmethod
    def tab_bread():
        return ".//section[1]/div[1]/div[1]/span"  # Вкладка "Булки"

    @staticmethod
    def tab_sause():
        return ".//section[1]/div[1]/div[2]/span"  # Вкладка "Соусы"

    @staticmethod
    def tab_stuffing():
        return ".//section[1]/div[1]/div[3]/span"  # Вкладка "Начинки"

    @staticmethod
    def allocation_bread():
        return ".//section[1]/div[1]/div[1]"  # Выделение вкладки "Булки"

    @staticmethod
    def allocation_sause():
        return ".//section[1]/div[1]/div[2]"  # Выделение вкладки "Соусы"

    @staticmethod
    def allocation_stuffing():
        return ".//section[1]/div[1]/div[3]"  # Выделение вкладки "Начинки"


class Ref:
    @staticmethod
    def registration_page():
        return "https://stellarburgers.nomoreparties.site/register"  # ссылка на страницу Регистрации

    @staticmethod
    def main_page():
        return 'https://stellarburgers.nomoreparties.site/'  # ссылка на Главную страницу

    @staticmethod
    def login_page():
        return 'https://stellarburgers.nomoreparties.site/login'  # ссылка на страницу Авторизации

    @staticmethod
    def forgot_password_page():
        return 'https://stellarburgers.nomoreparties.site/forgot-password'  # ссылка на страницу Восстановления пароля


class New:
    def __init__(self):
        self.login = []
        self.password = []

    def generate_login(self):
        number = random.randint(100, 999)
        for i in range(len(self.login)):
            if self.login[i] != number:
                continue
            else:
                number = random.randint(100, 999)

        self.login.append(number)
        new_login = f'alekseysisenkov5{number}@gmail.com'
        return new_login

    def generate_password(self):
        new_password = secrets.token_urlsafe(4)
        for i in range(len(self.password)):
            if self.password[i] != new_password:
                continue
            else:
                new_password = secrets.token_urlsafe(4)

        self.password.append(new_password)
        return new_password
