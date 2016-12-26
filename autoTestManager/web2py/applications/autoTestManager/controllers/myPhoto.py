def index():
    list=photodb().select(photodb.photofile.photofile,orderby=photodb.photofile.name)
    return dict(list=list)

def show():
    return dict()

def createphoto():
    createphotoform=photodbcurd.create(photodb.photofile,next=URL(args=photodb.photofile.id),message='上传图片成功!')
    return dict(createphotoform=createphotoform)
