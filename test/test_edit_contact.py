

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact()
    app.session.logout()
