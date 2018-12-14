from model.contact import Contact
from random import randrange


def test_add_contact_in_group(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname="New name", title="New title")
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.create(contact)
    contact.id = old_contacts[index].id
    app.contact.add_contact_in_group(index, contact)
    new_contacts = db.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)