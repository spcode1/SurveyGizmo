
from surveygizmo.api import base


class ContactListContact(base.Resource):
    resource_fmt_str = 'contactlist/%(contactlist_id)s/contactlistcontact/%(contactlistcontact_id)s'
    resource_id_keys = ['contactlist_id', 'contactlistcontact_id']

    def list(self, contactlist_id, **kwargs):
        kwargs.update({
            'contactlist_id': contactlist_id,
        })
        return super(ContactListContact, self).list(**kwargs)

    def get(self, contactlist_id, contactlistcontact_id, **kwargs):
        kwargs.update({
            'contactlist_id': contactlist_id,
            'contactlistcontact_id': contactlistcontact_id,
        })
        return super(ContactListContact, self).get(**kwargs)

    def create(self, contactlist_id, email_address, **kwargs):
        kwargs.update({
            'contactlist_id': contactlist_id,
            'email_address': email_address,
        })
        return super(ContactListContact, self).create(**kwargs)

    def update(self, contactlist_id, contactlistcontact_id, email_address, **kwargs):
        kwargs.update({
            'contactlist_id': contactlist_id,
            'contactlistcontact_id': contactlistcontact_id,
            'email_address': email_address,
        })
        return super(ContactListContact, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, contactlist_id, contactlistcontact_id, **kwargs):
        kwargs.update({
            'contactlist_id': contactlist_id,
            'contactlistcontact_id': contactlistcontact_id,
        })
        return super(ContactListContact, self).delete(**kwargs)
