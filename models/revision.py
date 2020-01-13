# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models

class Revision(models.Model):
    _name = 'verificaciones_de_productos.revision'
    
    apunte_id = fields.Many2one('verificaciones_de_productos.apunte', string="Apunte")
    profesional_id = fields.Many2one('verificaciones_de_productos.profesional', string="Profesional")
    
    
    
