
from surveygizmo.api import base


class SurveyTheme(base.Resource):
    resource_fmt_str = 'surveytheme/%(surveytheme_id)s'
    resource_id_keys = ['surveytheme_id']

    def list(self, **kwargs):
        return super(Survey, self).list(**kwargs)

    def get(self, surveytheme_id, **kwargs):
        kwargs.update({'surveytheme_id': surveytheme_id, })
        return super(SurveyTheme, self).get(**kwargs)

    def create(self, **kwargs):
        return super(SurveyTheme, self).create(**kwargs)

    def update(self, surveytheme_id, **kwargs):
        kwargs.update({'surveytheme_id': surveytheme_id, })
        return super(SurveyTheme, self).update(**kwargs)

    def copy(self, surveytheme_id, **kwargs):
        kwargs.update({
            'surveytheme_id': surveytheme_id,
        })
        return super(SurveyTheme, self).copy(**kwargs)

    def delete(self, surveytheme_id, **kwargs):
        kwargs.update({'surveytheme_id': surveytheme_id, })
        return super(SurveyTheme, self).delete(**kwargs)
