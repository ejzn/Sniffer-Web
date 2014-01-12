import web, datetime


db = web.database(dbn="sqlite", db="db/sniffer.db")

def get_phones():
    return db.select('phone', order='id')

def create_phone(name):
    return db.insert('phone', name=name, last_com=datetime.datetime.utcnow())

def get_phone(id):
    try:
        return db.select('phone', where='id=$id')[0]
    except IndexError:
        return None

def get_activity():
    return db.select('activity', order='id')

def create_activity(phone_id, action, category, component, details, timestamp):
    db.insert('activity', action=action, category=category, component=component, details=details, phone=phone_id, timestamp=timestamp)

