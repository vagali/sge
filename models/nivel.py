class Nivel(models.model):
    _name = 'verificaciones_de_productos.nivel'
    
    nivel_academico = fields.char(string = "Nivel academico")
    espeificacion = fields.char(string = "Especificacion")
    descripcion = fields.Text()
    
    profesional_id = fields.One2many('verificaciones_de_productos.profesional', ondelete = 'cascade', string = "Profesional" )