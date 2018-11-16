# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="ivanov", middlename="vasya", lastname="ivanov", nickname="xhel",
                               title="contakt", company="xshel", address="rete, k-5", home="768867876", mobile="+79445",
                               work="546", fax="546774", email="teretr@ty.ty", email2="gfhf@hg.nb", email3="fggfh@.yu.tyu",
                               homepage="http://treet.rt", bday="2", bmonth="January", byear="1999", aday="6",
                               amonth="March", ayear="2000", address2="gddgdd, d-2. kv4", phone2="city",
                               notes="ghfgfhfhfhfghfghfhfhfg"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

def test_add_new_emty(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                               homepage="", bday="", bmonth="-", byear="", aday="-", amonth="-", ayear="", address2="",
                               phone2="", notes=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
