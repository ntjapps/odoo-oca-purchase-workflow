# Copyright 2026 NTJ (https://www.ntj.co.id)
# v19-incompat: Removed in v19: uom category model collapsed; uom.product_uom_categ_kgm xmlid no longer exists.
{
    "name": "Purchase Container",
    "summary": """Add containers to purchase orders and stock pickings.""",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "maintainers": ["nayatec"],
    "author": "Akretion, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/purchase-workflow",
    "depends": [
        "purchase_stock",
    ],
    "data": [
        "data/container.type.csv",
        "data/cron_data.xml",
        "views/container_type.xml",
        "views/purchase.xml",
        "views/purchase_container.xml",
        "views/stock_picking.xml",
        "security/ir.model.access.csv",
    ],    "installable": False,
}