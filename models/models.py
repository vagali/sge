# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class verificaciones_de_productos(models.Model):
#     _name = 'verificaciones_de_productos.verificaciones_de_productos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Revision(models.Model):
    _name = 'verificaciones_de_productos.revision'
    
    apunte_id = fields.Many2one('verificaciones_de_productos.apunte', ondelete='cascade', string="Apunte", index=True)
    profesional_id = fields.Many2one('verificaciones_de_productos.profesional', string="Profesional")
    anotacion = fields.Text(string="Anotacions sobre el apunte")
    
class Nivel(models.Model):
    _name = 'verificaciones_de_productos.nivel'
    
    nivel_academico = fields.Char(string = "Nivel academico")
    espeificacion = fields.har(string = "Especificacion")
    descripcion = fields.Text()
    
    profesional_id = fields.One2many('verificaciones_de_productos.profesional', ondelete = 'cascade', string = "Profesional" )
    
class Apunte(models.Model):
    _name = 'verificaciones_de_productos.apunte'
    
    name = fields.Char(string="Titulo", required="True")
    description = fields.Text(string="Descripcion",required="True")
    codigo_apunte = fields.Integer(String="Codigo de apunte", required="True")
    
class Profesional(models.Model):
    _name = 'verificaciones_de_productos.profesional'
    _inherit = 'res.users'
    
    description = fields.Text(required="True",string="Descripcion")
    contacto = fields.Char(required="True", string="Contacto")