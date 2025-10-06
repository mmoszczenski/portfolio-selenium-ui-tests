from pages.products_page import ProductsPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.sign_up_step_2 import SignUpStep2
from pages.login_page import LoginPage
from pages.account_created_page import AccountCreatedPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.order_placed_page import OrderPlacedPage
from test_data.product_data import PRODUCTS
from utils.user_factory import make_user
from utils.card_payment_factory import make_payment_card

class TestCheckoutPositive:
    
    def test_basic_checkout_happy_path(self, pages):
        
        #Arrange 
        products_page: ProductsPage = pages["products_page"] 
        home_page: HomePage = pages["home"]
        cart_page: CartPage = pages["cart"]
        login_page: LoginPage = pages["login"]
        sign_up_step2_page: SignUpStep2 = pages["sign_up_step2"]
        account_created_page: AccountCreatedPage = pages["account_created_page"]
        checkout: CheckoutPage = pages["checkout"]
        payment_page: PaymentPage = pages["payment_page"]
        order_placed_page: OrderPlacedPage = pages["order_placed_page"]
        
        user = make_user()
        payment_card = make_payment_card()
        
        product_id = 1
        product = PRODUCTS[product_id]
        
        #Act
        home_page.open_homepage()
        home_page.go_to_login_page()
        
        login_page.sign_up(user.username, user.email)
        
        sign_up_step2_page.fill_account_information_form(
            password = user.password, 
            country = user.country,
            first_name = user.first_name,
            last_name = user.last_name,
            address = user.address,
            state = user.state,
            city = user.city,
            zipcode = user.zipcode,
            mobile_number = user.mobile_number
        )
        
        account_created_page.click_continue_button()
        
        home_page.go_to_products_page()
        
        products_page.remove_ads_banner_if_visible()
        products_page.add_to_cart_by_id(product_id)
        products_page.click_view_cart_btn()
        
        cart_page.click_proceed_to_checkout_button()
        
        #assercja czy wyświetlił się checkout
        assert checkout.is_checkout_page_displayd()
        
        #assercja czy adresy zgadzają się z tym co podczas rejestracji
        
        #assercja czy zgadza się total oraz ilość produktów
        
        #kliknięcie na place order
        checkout.click_place_order_button()
        
        #wypełnienie danych karty i kliknięcie potwierdzenia
        payment_page.provide_payment_form_data(
            name = payment_card.name,
            card_number = payment_card.card_number,
            cvc_number = payment_card.cvc_number,
            month = payment_card.expiration_month,
            year = payment_card.expiration_year
        )
        
        #asercja czy wyświetlił się page z "you order was placed and confirmed"
        
        order_placed_page.is_order_placed_page_displayed()
        order_placed_page.click_continue_button()
        
        assert home_page.is_on_homepage(), "Displayed page is not HomePage"
        
        #OPTIONAL - ściągnięcie faktury i weryfikacja czy dane się zgadzają