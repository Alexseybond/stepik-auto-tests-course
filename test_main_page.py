from ..pages.main_page import MainPage
from ..pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    """ Make sure go to login page from main page works fine. """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                        # открываем страницу
    page.go_to_login_page()            # выполняем метод страницы — переходим на страницу логина
    time.sleep(4)
    page.should_be_login_link()        #
    time.sleep(4)


def test_login_page(browser):
    """ Make sure we at login page. """
    link = "http://selenium1py.pythonanywhere.com/"
    login_page = LoginPage(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    login_page.open()                        # открываем страницу
    login_page.go_to_login_page()            # переходим на страницу с авторизацией
    login_page.should_be_login_page()        # проверяем на наличии форм авторизации и регистрации. присутствие "login" в URL
    time.sleep(4)




