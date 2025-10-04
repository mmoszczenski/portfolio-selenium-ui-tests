from pages.home_page import HomePage
from pages.contact_form_page import ContactFormPage
import time
from utils.contact_form_factory import make_contact_form_data


class TestContactFormPositive():

    def test_submit_contact_form_with_valid_data(self, pages): 
        home_page: HomePage = pages["home"]
        contact_form: ContactFormPage = pages["contact_form"]
        contact_form_data = make_contact_form_data()
          
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        home_page.go_to_contact_form_page()
        
        contact_form.fill_name(contact_form_data.name)
        contact_form.fill_email(contact_form_data.email)
        contact_form.fill_subject(contact_form_data.subject)
        contact_form.fill_message(contact_form_data.message)
        contact_form.upload_file(contact_form_data.attachment)
        contact_form.click_submit_button()
        contact_form.confirm_alert(accept=True)
        
        assert contact_form.is_contact_form_submitted(), "Success message not displayed"
        
        
        
        
        











class TestContactFormNegative():
    pass