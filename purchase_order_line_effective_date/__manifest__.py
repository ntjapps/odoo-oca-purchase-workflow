# Copyright (C) 2026  Renato Lima - Akretion
# Copyright 2026 NTJ (https://www.ntj.co.id)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Purchase Order Line Effective Date",
    "summary": "Calculated effective dates in Purchase Order Lines",
    "category": "Inventory/Purchase",
    "license": "AGPL-3",
    "author": "Akretion, Odoo Community Association (OCA)",
    "maintainers": ["renatonlima"],
    "website": "https://github.com/OCA/purchase-workflow",
    "development_status": "Production/Stable",
    "version": "19.0.1.0.0",
    "depends": [
        "purchase_stock",
    ],
    "data": [
        # Views
        "views/purchase_order.xml",
        "views/purchase_order_line.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
