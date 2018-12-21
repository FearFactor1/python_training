from model.contact import Contact
import random
from model.group import Group


def test_add_contact_in_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.add_contact_in_group(contact.id, contact.group_id)
    new_contacts = db.get_contact_list(Group(id=group_id))
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)