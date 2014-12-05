{
    "name": "Tags",
    "version": "0.0.3",
    "author": "JBM",
    "website": "",
    "summary": "Tags",
    'category': 'Hidden/Dependency',
    "depends": [
        "base",
    ],
    "description": """
        Provides generic tags logic and basic views.
        Integration with other modules should be implemented as sparate modules
    """,
    "init_xml": [
    ],
    "update_xml": [
        'security/base_security.xml',
        'security/ir.model.access.csv',
        'views/res_tag_view.xml',
    ],
    "installable": True,
    "active": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
