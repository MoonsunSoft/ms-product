{
    'name': 'Service Charges POS',
    'version': '17.0.1.0.0',
    'category': 'Point Of Sale',
    'summary': 'Allows you to set service charges.',
    'description': 'Allows you to set service charges for an order by globally'
                   ' and session wise.',
    'author': 'ceo@moonsun.au (MoonSun)',
    'website': 'https://www.MoonSun.au',
    'depends': ['point_of_sale'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/pos_config_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'service_charges_pos/static/src/js/pos_load_data.js',
            'service_charges_pos/static/src/js/service_charge_button.js',
            'service_charges_pos/static/src/xml/ServiceChargeButton.xml',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
