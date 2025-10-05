from pages.home_page import HomePage
from pages.contact_form_page import ContactFormPage
from utils.contact_form_factory import make_contact_form_data


class TestContactFormPositive():

    def test_submit_contact_form_with_valid_data(self, pages): 
        home_page: HomePage = pages["home"]
        contact_form: ContactFormPage = pages["contact_form"]
        contact_form_data = make_contact_form_data()
          
        home_page.open_homepage()
        home_page.go_to_contact_form_page()
        
        contact_form.fill_contact_form(
            name = contact_form_data.name,
            email = contact_form_data.email,
            subject = contact_form_data.subject,
            message = contact_form_data.message,
            file = contact_form_data.attachment
        )
        
        contact_form.click_submit_button()
        contact_form.confirm_alert(accept=True)
        
        assert contact_form.is_contact_form_submitted(), "Success message not displayed"
        
        

class TestContactFormNegative():
    
    def test_submit_contact_form_with_empty_fields(self, pages):
        home_page: HomePage = pages["home"]
        contact_form: ContactFormPage = pages["contact_form"]
        
        home_page.open_homepage()
        home_page.go_to_contact_form_page()
        
        contact_form.click_submit_button()
        assert contact_form.is_email_error_type_value_missing(), "Validation error not displayed"
        