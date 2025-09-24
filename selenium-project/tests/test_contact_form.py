from pages.home_page import HomePage
from pages.contact_form_page import ContactFormPage


class TestContactFormPositive():

    def test_submit_contact_form_with_valid_data(self, pages): 
        home_page: HomePage = pages["home"]
        contact_form: ContactFormPage = pages["contact_form"]
          
        home_page.open(home_page.URL)
        home_page.go_to_contact_form_page()
        
        contact_form.fill_name()
        contact_form.fill_email()
        contact_form.fill_subject()
        contact_form.fill_message()
        contact_form.upload_file()
        
        
        
        











class TestContactFormNegative():
    pass