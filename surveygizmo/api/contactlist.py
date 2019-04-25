
from surveygizmo.api import base


class ContactList(base.Resource):
    resource_fmt_str = 'contactlist/%(contactlist_id)s'
    resource_id_keys = ['contactlist_id']

    def list(self, **kwargs):
        return super(ContactList, self).list(**kwargs)

    def get(self, contactlist_id, **kwargs):
        kwargs.update({'contactlist_id': contactlist_id, })
        return super(ContactList, self).get(**kwargs)

    def create(self, contactlist_name, **kwargs):
        kwargs.update({
            'listname': contactlist_name,
        })
        return super(ContactList, self).create(**kwargs)

    def update(self, contactlist_id, **kwargs):
        kwargs.update({
            'contactlist_id': contactlist_id,
        })
        return super(ContactList, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, contactlist_id, **kwargs):
        kwargs.update({
            'contactlist_id': contactlist_id,
        })
        return super(ContactList, self).delete(**kwargs)
