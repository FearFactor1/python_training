from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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

    contact_cache=None

    def get_contact_list(self, text):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname=cells[1].text
                lastname=cells[2].text
                address=cells[3].text
                all_emails=cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page = all_phones,
                                                  all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)



    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # click in submit add new
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # click Enter
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        #wd.find_element_by_css_selector('input[type="submit"]').click()
        self.return_to_home_page()
        self.contact_cache = None


    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None


    def delete_contact_in_group(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[@value='35']").click()
        self.select_contact_by_id(id)
        wd.find_element_by_name("remove").click()
        self.return_to_home_page()
        self.contact_cache = None


    def modify_first_contact(self):
        self.modify_contact_by_index(0)


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


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


    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        #wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        #wd.find_element_by_css_selector('input[name="update"]').click()
        self.return_to_home_page()
        self.contact_cache = None


    def add_contact_in_group(self, id, group_id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath('//select[@name = "to_group"]').click()
        wd.find_elements_by_css_selector('select[name="to_group"] > option[value="%s"]' % group_id)[0].click()
        wd.find_element_by_xpath('//input[@name="add"]').click()
        self.return_to_home_page()
        self.contact_cache = None


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("home").click()


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        address2 = wd.find_element_by_name("address2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, address=address, address2=address2,
                       email= email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)