import web
import model

urls = (
    '/', 'Index',
    '/phones/list', 'Phone_List',
    '/phone', 'Phone',
    '/phone/(\d+)', 'Phone',
    '/activity/list', 'Activity_List',
    '/activity', 'Activity',
    '/activity/(\d+)', 'Activity',
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

    form = web.form.Form(
        web.form.Textbox('name', web.form.notnull,
            description="Name:"),
    )

    def GET(self, phone_id):
        phone = model.get_phone(phone_id)
        form = self.form()
        return render.phone(phone, form)


    def GET(self):
        phone = {}
        form = self.form()
        return render.phone(phone, form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return web.seeother("/phones/list")
        phone_id = model.create_phone(form.d.name)
        web.ctx.status = '201 Created'
        web.header('Location', phone_id)
        return web.template.Template("""$def with (phone_id)
          <!doctype html>
          <html>
          <head>
            <meta charset=utf-8>
            <title>Phone Created</title>
          </head>
          <body>
            <p>Profile phone for $phone_id</p>
          </body>
          </html>""")(phone_id)

class Activity_List:

    def GET(self):
        activity = model.get_activity()
        return render.activity_list(activity)

class Activity:

    form = web.form.Form(
        web.form.Dropdown(name='phone_id',args=[]),
        web.form.Textbox('action', web.form.notnull, description="action:"),
        web.form.Textbox('category', web.form.notnull, description="category:"),
        web.form.Textbox('component', web.form.notnull, description="component:"),
        web.form.Textbox('details', web.form.notnull, description="details:"),
        web.form.Textbox('timestamp', web.form.notnull, description="timestamp:"),
        web.form.Button('Add Activity'),
    )

    """ Return an overview of activity"""
    def GET(self):
        entry = {}
        phones = model.get_phones()

        form = self.form()
        form.phone_id.args = [(o.ID, o.NAME) for o in phones]

        return render.activity(entry, form)

    #def GET(self, activty_id):
    #    return render.activity(activity)

    def POST(self):
        """ Add new Activity """
        form = self.form()
        if not form.validates():
            activity = model.get_activity()
            return render.activity(activity, form)
        model.create_activity(form.d.phone_id, form.d.action, form.d.category, form.d.component, form.d.details, form.d.timestamp)
        raise web.seeother('/activity/list')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
