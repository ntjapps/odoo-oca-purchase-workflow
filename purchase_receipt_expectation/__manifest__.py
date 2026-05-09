# Copyright 2022 Camptocamp SA
# Copyright 2026 NTJ (https://www.ntj.co.id)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Purchase Receipt Expectation",
    "version": "19.0.1.0.0",
    "category": "Purchase Management",
    "author": "Camptocamp SA, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/purchase-workflow",
    "license": "AGPL-3",
    "data": [
        "views/purchase_order.xml",
    ],
    "depends": [
        "purchase_stock",
    ],
    "installable": True,
}
