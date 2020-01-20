# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields, api

class Profesional(models.Model):
    _name = 'verificaciones_de_productos.profesional'
    _inherit = 'res.users'
    
    description = fields.Text(required="True",string="Descripcion")
    contacto = fields.Char(required="True", string="Contacto")
    
    #revision_id = fields.One2many('verificaciones_de_productos.revision', string = "Revision" )
    nivel_id = fields.Many2one('verificaciones_de_productos.nivel', ondelete='cascade', string="Nivel")

