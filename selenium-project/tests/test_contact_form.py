from pages.home_page import HomePage
from pages.contact_form_page import ContactFormPage
import time


class TestContactFormPositive():

    def test_submit_contact_form_with_valid_data(self, pages): 
        home_page: HomePage = pages["home"]
        contact_form: ContactFormPage = pages["contact_form"]
          
        home_page.open(home_page.URL)
        home_page.accept_cookies()
        home_page.go_to_contact_form_page()
        
        contact_form.fill_name("ExampleName")
        contact_form.fill_email("Example@Email.com")
        contact_form.fill_subject("ExampleSubject")
        contact_form.fill_message("ExampleMessage")
        
        contact_form.upload_file("C:\\Users\\Miłosz Work\\Portfolio\\my-portfolio\\selenium-project\\data\\samplefile.jpg")
        
        contact_form.click_submit_button()
        
        contact_form.confirm_alert(accept=True)
        
        assert contact_form.is_contact_form_submitted()
        
        
        
        
        











class TestContactFormNegative():
    pass