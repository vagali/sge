# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields, api, exceptions 

class Nivel(models.Model):
    _name = 'verificaciones_de_productos.nivel'
    
    nivel_academico = fields.Char(string = "Nivel academico", required=True)
    espeificacion = fields.Char(string = "Especificacion", required=True)
    descripcion = fields.Text( required=True)

    #profesional_id = fields.One2many('verificaciones_de_productos.profesional',string = "Profesional" )
    profesional_id = fields.One2many('res.partner','id',string = "Profesional" )
    
    @api.constrains('nivel_academico')
    def _verificar_nivel_academico(self):
        if (len(self.nivel_academico) < 3):
            raise exceptions.ValidationError("Nivel academico minimo longitud 4 caracteres.")
    
    
    @api.constrains('espeificacion')
    def _verificar_espeificacion(self):
        if len(self.espeificacion) < 3:
            raise exceptions.ValidationError("Especificacion minimo longitud 4 caracteres.")
        
    @api.constrains('descripcion')
    def _verificar_descripcion_nivel(self):
        if self.descripcion and (len(self.descripcion) < 3):
            raise exceptions.ValidationError("Descripcion minimo longitud 4 caracteres.")
        
    