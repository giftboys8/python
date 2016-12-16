def index():
    '''
    response.flash = T("Hello World")
    :return:
    '''
    if not session.counter:
        session.counter = 1
    else:
        session.counter += 1
    return dict(message=T('自动化测试管理系统'), counter=session.counter)


def user():
    return dict(form=auth())


@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()

def addCase():
    grid=SQLFORM.grid(casedb.testCase,user_signature=False)
    return locals()

def addWsdl():
    if (request.vars.wsdl_url=='a'):
        session.counter=1000
    session.counter=(session.counter or 0) + 1
    return dict(message='Counter The Welcom count',counter=session.counter)

def first():
    return dict()

def second():
    return dict()
