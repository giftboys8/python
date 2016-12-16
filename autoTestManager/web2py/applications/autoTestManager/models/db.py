if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

from gluon.contrib.appconfig import AppConfig

myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
else:
    db = DAL('google:datastore+ndb')
    session.connect(request, response, db=db)

response.generic_patterns = ['*'] if request.is_local else []
response.formstyle = myconf.get('forms.formstyle')
response.form_label_separator = myconf.get('forms.separator') or ''



from gluon.tools import Auth, Service, PluginManager

auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

auth.define_tables(username=False, signature=False)

mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True


casedb=DAL('sqlite://storage.sqlite')
casedb.define_table('testCase',Field('id'),Field('caseName'),Field('elecementId'))