# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models

class Apunte(models.Model):
    _name = 'verificaciones_de_productos.apunte'
    
    name = fields.Char(string="Titulo", required="True")
    description = fields.Text(string="Descripcion")
    codigo_apunte = fields.Integer(String="Codigo de apunte")
    
    

