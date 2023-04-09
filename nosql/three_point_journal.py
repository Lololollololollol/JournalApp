import mongoengine


class Journal(mongoengine.Document):
    # type = mongoengine.StringField()
    title = mongoengine.StringField()
    bad = mongoengine.StringField()
    good = mongoengine.StringField()
    tomorrow = mongoengine.StringField()
    date = mongoengine.DateField()

    meta = {
        'db_alias': 'core',
        'collection': 'three_point_journal',
    }
