from mongoengine import connect


def global_init():
    # mongoengine.register_connection(alias='core', name='journal_app')
    connect(host="mongodb+srv://admin01:1q2w3e@cluster0.ehepg.mongodb.net", alias='core', name='journal_app')
