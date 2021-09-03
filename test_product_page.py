from .pages.product_page import ProductPage
import time
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=offer"

@pytest.mark.parametrize('links', 
                                [
                                    link+'0',
                                    # link+'1',
                                    # link+'2',
                                    # link+'3',
                                    # link+'4',
                                    # link+'5',
                                    # link+'6',
                                    # pytest.param(link+'7',
                                    #              marks=pytest.mark.xfail),
                                    # link+'8',
                                    # link+'9'
                                ]
                        )   
def test_guest_can_add_product_to_basket(browser, links):
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_product_to_basket()
    time.sleep(5)