# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class AccountMove(models.Model):
    _name = "account.move"
    _inherit = "account.move"

    def action_post(self):
        _super = super(AccountMove, self)
        _super.action_post()
        for record in self:
            self._event("on_account_move_post").notify(record)

    def button_cancel(self):
        _super = super(AccountMove, self)
        _super.button_cancel()
        for record in self:
            self._event("on_account_move_cancel").notify(record)

    def button_draft(self):
        _super = super(AccountMove, self)
        _super.button_draft()
        for record in self:
            self._event("on_account_move_draft").notify(record)
