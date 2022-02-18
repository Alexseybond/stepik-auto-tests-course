from ..pages.product_page import ProductPages



def test_guest_can_add_product_to_basket(browser):
    """ Make sure that cart method works fine. """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPages(browser, link)
    product_page.product_add_to_cart()
    product_page.solve_quiz_and_get_code()
    print('123')

