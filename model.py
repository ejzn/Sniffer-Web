import web, datetime


db = web.database(dbn="sqlite", db="db/sniffer")

def get_phones():
    return db.select('phone', order='id')

def get_phone(id):
    try:
        return db.select('phone', where='id=$id')[0]
    except IndexError:
        return None

def get_activity():
    return sdb.select('activity', order='id')

def create_activity(phone_id, act_type, details):
    db.insert('activity', activity_type=act_type, details=details, phone=phone_id, timestamp=datetime.datetime.utcnow())


