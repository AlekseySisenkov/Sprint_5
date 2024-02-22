import secrets
import random

from selenium.webdriver.common.by import By


class Locator:
    INPUT_NAME = By.XPATH, '//label[text()="Имя"]/parent::div/input'  # Поле "Имя"
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/parent::div/input'  # Поле "Email"
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'  # Поле "Пароль"
    BUTTON_REGISTRATION = By.XPATH, '//button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться"
    MESSAGE_INVALID_PASSWORD = '//p[text()="Некорректный пароль"]'  # Подпись "Некорректный пароль"
    BUTTON_INPUT_ACCOUNT = By.XPATH, '//button[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт"
    BUTTON_PLACE_ORDER = '//button[text()="Оформить заказ"]'  # Кнопка "Оформить заказ"
    BUTTON_PERSONAL_CABINET = By.XPATH, '//p[text()="Личный Кабинет"]'  # Кнопка "Личный кабинет"
    BUTTON_INPUT = By.XPATH, '//button[text()="Войти"]'  # Кнопка "Войти"
    REF_INPUT = By.XPATH, '//a[@href="/login" and text()="Войти"]'  # Кнопка "Войти"
    FIELD_LOGIN = '//input[@value="alekseysisenkov5000@gmail.com"]'  # Поле "Логин" в Личном кабинете с
                                                                               # логином alekseysisenkov5000@gmail.com
    BUTTON_DESIGNER = By.XPATH, '//p[text()="Конструктор"]'  # Кнопка "Конструктор"
    BUTTON_OUTPUT = By.XPATH, '//button[@type="button" and text()="Выход"]'  # Кнопка "Выход"
    OUTPUT = '//button[text()="Выход"]'  # Локатор для ожидания кнопки "Выход"
    HEADER_ASSEMBLE_BURGER = '//h1[text()="Соберите бургер"]'  # Надпись "Соберите бургер"
    TAB_BREAD = By.XPATH, '//span[text()="Булки"]/parent::div'  # Вкладка "Булки"
    TAB_SAUSE = By.XPATH, '//span[text()="Соусы"]/parent::div'  # Вкладка "Соусы"
    TAB_STUFFING = By.XPATH, '//span[text()="Начинки"]/parent::div'  # Вкладка "Начинки"

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
    REGISTRATION_PAGE = 'https://stellarburgers.nomoreparties.site/register'  # ссылка на страницу Регистрации
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'  # ссылка на Главную страницу
    LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'  # ссылка на страницу Авторизации
    FORGOT_PASSWORD_PAGE = 'https://stellarburgers.nomoreparties.site/forgot-password'  # ссылка на страницу
                                                                                            # Восстановления пароля


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
