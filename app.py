import web
import model

urls = (
    '/', 'Index',
    '/phones/list', 'Phone_List',
    '/phones/info/(\d+)', 'Phone_Info',
    '/activity/list', 'Activity_List',
    '/activity/info/(\d+)', 'Activity_Info',
    '/test/activity/', 'Activity_Test',
)

### Templates
render = web.template.render('templates', base='base')


class Index:

    def GET(self):
        return render.index()

class Phone_List:

    def GET(self):
        """ Return a listing of the phones or phone """
        return render.phone_list(model.get_phones())

class Phone:

    def GET(self, phone_id):
        phone = model.get_phone(phone_id)
        return render.phone(phone)

    def POST(self):
        """ Return a listing of the phones or phone """

class Activity_List:

    def GET(self):
        activity = model.get_activity()
        return render.activity_list(activity)

class Activity:

    """ Return an overview of activity"""
    def GET(self, activty_id):
        return render.activity(activity)

    def POST(self):
        """ Add new Activity """
        form = self.form()
        if not form.validates():
            activity = model.get_activity()
            return render.index(activity, form)
        model.create_activity(form.d.activity_type, form.d.details, form.d.phone_id)
        raise web.seeother('/')



class Test_Activity:
    form = web.form.Form(
        web.form.Textbox('phone_id', web.form.notnull,
            description="Phone Id:"),
        web.form.Textbox('activity_type', web.form.notnull,
            description="Activity Type:"),
        web.form.Textbox('details', web.form.notnull,
            description="details:"),
        web.form.Button('Add Activity'),
    )

    def POST(self):
        """ Add new Activity """
        form = self.form()
        if not form.validates():
            activity = model.get_activity()
            return render.index(activity, form)
        model.create_activity(form.d.activity_type, form.d.details, form.d.phone_id)
        raise web.seeother('/')


    def GET(self):
        """ Show page """
        activity = model.get_activity()
        form = self.form()
        return render.index(activity, form)



app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
