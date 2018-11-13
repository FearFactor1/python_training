from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # click in submit add new
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # click Enter
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # add rows in form contacts company
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        # add rows in form contacts lichnie dannie
        self.change_field_value("homepage", contact.homepage)
        self.change_spisok_value("bday", contact.bday)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        self.change_spisok_value("bmonth", contact.bmonth)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_spisok_value("aday", contact.aday)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        self.change_spisok_value("amonth", contact.amonth)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)



    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



    def change_spisok_value(self, field_name, text):
        wd = self.app.wd
        if text is  None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).send_keys(text)
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("home").click()
        