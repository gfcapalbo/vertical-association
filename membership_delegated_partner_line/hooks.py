# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID
from odoo.exceptions import UserError

def check_incompatibilities(env):
    #env = api.Environment(cr, SUPERUSER_ID, {})
    mod = env["ir.module.module"].search([
        ("name", "=", "membership_delegated_partner"),
        ("state", "=", "installed"),
    ], limit=1)
    if mod:
        raise UserError(
            "The module 'membership_delegated_partner' is installed and incompatible "
            "with this module.\n\n"
            "Please follow the instructions in this module's 'scripts' folder before continuing."
        )
