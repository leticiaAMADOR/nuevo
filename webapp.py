import web
# @
from web import form
db = web.database(dbn='mysql', db='agendas', user='root', pw='toor')
render=web.template.render('templates')
urls = (
    
    '/','index',
    '/nuevo', 'nuevo',
    '/editar/(.+)','editar',
    '/ver/(.+)','ver',
    '/eliminar/(.+)','eliminar'
)



myformAgendas=form.Form(
    form.Textbox('Nombre'), 
    form.Textbox('Telefono'),
    form.Textbox('Email'),
    form.Textbox('Direccion'),
    
)
class index:
    def GET(self):
        
        result=db.select('datos')
        return render.index(result)
    def POST(self):           
        raise web.seeother("/nuevo")    
class nuevo:
    def GET(self):
        formNew=myformAgendas()
        return render.nuevo(formNew)
    def POST(self): 
        formNew = myformAgendas()
        if not formNew.validates(): 
            return render.nuevo(formNew)
        else:
            db.insert('datos', nombre=formNew.d.Nombre, 
            telefono=formNew.d.Telefono, email=formNew.d.Email,
             direccion=formNew.d.Direccion)
            result=db.select('datos')
            raise web.seeother('/')
            

class editar:
    def GET(self,id_dato):
        formEdit=myformAgendas()
        
        
        result=db.select('datos', where= "id_dato=%s"%(id_dato))
        
        for row in result:
            formEdit['Nombre'].value=row.nombre
            formEdit['Telefono'].value=row.telefono
            formEdit['Email'].value=row.email
            formEdit['Direccion'].value=row.direccion
            
        return render.editar(formEdit)        
    def POST(self,id_dato):
        formEdit=myformAgendas()
        if not formEdit.validates(): 
            return render.editar(formEdit)
        else:
            db.update('datos', where='id_dato=%s'%(id_dato), nombre=formEdit.d.Nombre,
             telefono=formEdit.d.Telefono, email=formEdit.d.Email,
              direccion=formEdit.d.Direccion)
            result=db.select('datos')
            raise web.seeother('/')
class eliminar:
    def GET(self,id_dato):
        formEdit=myformAgendas()
        
        result=db.select('datos', where='id_dato=%s'%(id_dato))
        
        for row in result:
            formEdit['Nombre'].value=row.nombre
            formEdit['Telefono'].value=row.telefono
            formEdit['Email'].value=row.email
            formEdit['Direccion'].value=row.direccion
            
        return render.eliminar(formEdit)        
    def POST(self,id_dato):
        formEdit=myformAgendas()
        if not formEdit.validates(): 
            return render.eliminar(formEdit)
        else:
            db.delete('datos', where="id_dato=%s"%(id_dato))
            raise web.seeother('/')


if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()
