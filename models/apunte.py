# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields, api, exceptions

class Apunte(models.Model):
    _name = 'verificaciones_de_productos.apunte'
    
    name = fields.Char(string="Titulo", required="True")
    frase_es_profesional = fields.Char(string="Tipo de apunte")
    description = fields.Text(string="Descripcion",required="True")
    codigo_apunte = fields.Integer(String="Codigo de apunte", required="True")
    es_profesional = fields.Boolean(string="Hecho por un profesional", default=False)
    revisiones_ids = fields.One2many('verificaciones_de_productos.revision','apunte_id', string ="Revisiones")
    
    @api.depends('es_profesional')
    def _escribir_el_tipo(self):
        for a in self:
            if a.es_profesional == True:
                a.frase_es_profesinal="Creado por profesinal"
            else:
                a.frase_es_profesinal="Creado por cliente"
    
   

    