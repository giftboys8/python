

import suds.metrics as metrics
from cookielib import CookieJar
from suds import *
from suds.reader import DefinitionsReader
from suds.transport import TransportError, Request
from suds.transport.https import HttpAuthenticated
from suds.servicedefinition import ServiceDefinition
from suds import sudsobject
from suds.resolver import PathResolver
from suds.builder import Builder
from suds.wsdl import Definitions
from suds.cache import ObjectCache
from suds.sax.document import Document
from suds.sax.parser import Parser
from suds.options import Options
from suds.properties import Unskin
from urlparse import urlparse
from copy import deepcopy
from suds.plugin import PluginContainer
from logging import getLogger

def index():
    '''
    response.flash = T("Hello World")
    :return:
    '''
    host="127.0.0.1:8000"
    if not session.counter:
        session.counter = 1
    else:
        session.counter += 1

    return dict(message=T('自动化测试管理系统'), counter=session.counter,host=host)


def user():
    return dict(form=auth())


def download():
    return response.download(request, db)


def call():
    return service()

def addcase():
    if session.wsdlStr or not '':
        grid=SQLFORM.grid(casedb.testCase,user_signature=False)
        return locals()

def addwsdl():
    wsdlform=FORM(INPUT(_name='wsdlStrl',requires=IS_NOT_EMPTY()),INPUT(_type='submit'))
    if wsdlform.process().accepted:
        session.wsdlStr=wsdlform.vars.wsdlStr
        redirect(URL('addcase'))

    return dict(wsdlform=wsdlform)


def showbug():
    images=bugdb().select(bugdb.image.ALL,orderby=bugdb.image.title)
    return dict(images=images)

@auth.requires_login()
def show():
        image = bugdb.image(request.args(0)) or redirect(URL('show'))
        bugdb.bugdetail.image_id.default = image.id
        bugform = curd.create(bugdb.bugdetail,next=URL(args=image.id),message='you are ok')
            #SQLFORM(bugdb.bugdetail)
        #if bugform.process().accepted:
        #    response.flash = '问题单详情'
        # bugform=crud.create(bugdb.bugdetail,message='your comment is post',next=URL(args=image.id))
        bugdetails = bugdb(bugdb.bugdetail.image_id==image.id).select()
        return dict(image=image,bugdetails=bugdetails,bugform=bugform)
        # return dict(image=image)

def download():
    return response.download(request,bugdb)

# @auth.requires_membership('manager')
def manager():
    grid=SQLFORM.smartgrid(bugdb.image)
    return dict(grid=grid)



def testsoap():
    import suds
    from suds.client import SoapClient
    url='http://127.0.0.1:8080/WebserviceSample-0.0.1-SNAPSHOT/ws/addServicePort?wsdl'
    client=suds.client.Client(url)
        


    # e=suds.client.Method(client,'addService').__call__
    # a=suds.client.Method(client,'addService')

    # xmlresult=client.service.addService(41,25)
    xmlresult=''
    # soapclient =client.last_received()
    # soapclient=client.last_sent()


    soapclienta=client.sd
    # a=soapclienta[0]
    # a=client.dict(client.wsdl.imports.count())

    #取得URL地址
    # a=client.wsdl.url

    #取得binding地址
    # a=dict(client.wsdl.bindings).keys()



    # a='a'
    # a = dict(dict(client.wsdl.bindings).values()[0]).get('root')
    # for a in soapclienta:
    #     a
    # pass

    # soapclientb=client.service.checkFileExist('a')
    b=client.last_sent()
    # for b in soapclientb:
    #     b
    # pass
    #soapclient=client.service.types()
    # soapclient=client.service.__getitem__(addService)
    #soapclient=client.service.__getattr__('portType')
    return dict(client=client,xmlresult=xmlresult,soapclient=soapclienta,a=e,b=b)
