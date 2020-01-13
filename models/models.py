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
class Profesional(models.Model):
    #_name = 'verificaciones_de_productos.profesional'
    _inherit = 'res.users'
    
    description = fields.Text(required="True",string="Descripcion")
    contacto = fields.Char(required="True", string="Contacto")
    
    revision_id = fields.One2many('verificaciones_de_productos.revision', string = "Revision" )
    #nivel_id = fields.Many2one('verificaciones_de_productos.nivel', ondelete='cascade', string="Nivel", index=True)

class Revision(models.Model):
    _name = 'verificaciones_de_productos.revision'
    
    apunte_id = fields.Many2one('verificaciones_de_productos.apunte', ondelete='cascade', string="Apunte", index=True)
    profesional_id = fields.Many2one('res.profesional', string="Profesional")
    anotacion = fields.Text(string="Anotacions sobre el apunte")
    

    
