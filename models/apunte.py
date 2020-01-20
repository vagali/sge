# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields, api

class Apunte(models.Model):
    _name = 'verificaciones_de_productos.apunte'
    
    name = fields.Char(string="Titulo", required="True")
    description = fields.Text(string="Descripcion",required="True")
    codigo_apunte = fields.Integer(String="Codigo de apunte", required="True")
    es_profesional = fields.Boolean(string="Hecho por un profesional", default=False)
    revisiones_ids = fields.One2many('verificaciones_de_productos.revision','apunte_id', string ="Revisiones")
