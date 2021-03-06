import  re
from model.contact import Contact


def test_phones_on_home_page(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(contact)
    assert contact.all_phones_from_home_page == old_contacts


#def test_phones_on_contact_view_page(app, db):
#    contact_from_view_page = db.get_contact_from_view_page(0)
#    contact_from_edit_page = db.get_contact_info_from_edit_page()[0]
#    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[()-]", "",s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone, contact.secondaryphone]))))