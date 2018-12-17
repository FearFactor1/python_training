from model.contact import Contact
import random


def test_add_contact_in_group(app, db, check_ui, index):
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.id = old_contacts[index].id
    app.contact.add_contact_in_group(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)