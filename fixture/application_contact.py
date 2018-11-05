from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session_contact import SessionHelperContact
from fixture.contact import ContactHelper

class ApplicationContact:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelperContact(self)
        self.contact = ContactHelper(self)




    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
