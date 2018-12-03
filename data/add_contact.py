from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"),
    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=firstname, middlename="fghjjf", lastname=lastname, nickname="xhel",
                               title="contakt", company="xshel", address=address, home="768867876", mobile="+79445",
                               work="546", fax="546774", email="teretr@ty.ty", email2="gfhf@hg.nb", email3="fggfh@.yu.tyu",
                               homepage="http://treet.rt", bday="2", bmonth="January", byear="1999", aday="6",
                               amonth="March", ayear="2000", address2="gddgdd, d-2. kv4", phone2="city",
                               notes="ghfgfhfhfhfghfghfhfhfg")
    for firstname in ["", random_string("firstname", 5)]
    for address in ["", random_string("address", 7)]
    for lastname in ["", random_string("lastname", 9)]
]