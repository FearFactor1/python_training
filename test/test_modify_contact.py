
from model.contact import Contact


def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New name", title="New title"))
    app.session.logout()


def test_modify_contact_title(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(title="New title"))
    app.session.logout()


def test_modify_contact_spisok(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(bday="9", bmonth="May", byear="2023", aday="7", amonth="April",
                                ayear="1988"))
    app.session.logout()

