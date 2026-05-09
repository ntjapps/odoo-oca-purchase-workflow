# Copyright 2025 Moduon Team S.L.
# Copyright 2026 NTJ (https://www.ntj.co.id)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
# v19-incompat: Removed in v19: depends on stock.valuation.layer model not available without account/stock_account; install fails out of the box.
{
    "name": "Update costs from purchase",
    "summary": "Allows to update valuation layers once the purchase is received",
    "version": "19.0.1.0.0",
    "category": "Purchase Management",
    "author": "Moduon, Odoo Community Association (OCA)",
    "maintainers": ["chienandalu", "rafaelbn"],
    "website": "https://github.com/OCA/purchase-workflow",
    "license": "LGPL-3",
    "depends": ["purchase_stock"],
    "data": [
        "views/purchase_order_form_views.xml",
        "views/stock_valuation_layer_views.xml",
    ],    "installable": False,
}