{
    "name": "Tags",
    "version": "0.0.3",
    "author": "JBM",
    "website": "",
    "summary": "Tags",
    'category': 'Hidden/Dependency',
    "depends": [
        "base",
        "base_action_rule",
    ],
    "description": """
        Provides generic tags logic and basic views.
        Integration with other modules should be implemented as sparate modules
    """,
    "init_xml": [
    ],
    "data": [
        'security/base_security.xml',
        'security/ir.model.access.csv',
        'views/res_tag_view.xml',
        'views/base_action_rule_view.xml',
    ],
    "installable": True,
}
