import web
urls= (
    '/hello(.*)','hellow',
    '/(.*)','index',
    )
app= web.application(urls,globals())
class index:
    def GET(self,name):
        if not name:
            name= 'world'
            web.header('Content-Type','text/html;charset=UTF-8')
            return 'www.zhaokeli.com'
class hellow:
    def GET(self,name):
        if not name:
            name= 'world'
            web.header('Content-Type','text/html;charset=UTF-8')
            return 'hellow world'
if __name__== "__main__":
    app.run()