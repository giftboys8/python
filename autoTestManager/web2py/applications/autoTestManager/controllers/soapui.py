import suds
def index():
    url='http://127.0.0.1:8080/WebserviceSample-0.0.1-SNAPSHOT/ws/addServicePort?wsdl'
    client=suds.client.Client(url)
    methods=get_all_methods(client)

    methodArgs={}
    for method in methods:
        methodArgs[method]=get_methods_args(client,method)


    client.service.addService(1,2)

    requestxml=''
    a=[]

    for method in get_all_methods(client):
        requestxml=get_methods_args(client,method)
        a.append(requestxml)

    a=get_methods_args(client,'addService')
    # requestxml=client.last_sent()
    return dict(requestxml=a)



def get_all_methods(client):
    return [method for method in client.wsdl.services[0].ports[0].methods]

def get_methods_args(client,method_name):
    method=client.wsdl.services[0].ports[0].methods[method_name]
    input_params=method.binding.input
    return input_params.get_message(method, [], {})
    # return input_params.get_message()

def get_request_xml(client):
    methods = get_all_methods(client)
    d = {}
    for method in methods:
        d[method] = get_methods_args(client, method)
        pass
    pass