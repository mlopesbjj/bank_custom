{
    "name": "KHPS Custom BANK",
    "description": "ADD il campo x_acc_number tipo many2one",
    "summary": "ADD il campo x_acc_number tipo many2one",
    "author": "Marcio Lopes - KHPS",
    "depends": ['account', 
                'product'],
    "data": ['views/respartnerbank.xml',
             'views/product.xml',
             'views/company.xml',
             'reports/sale_report_inherit.xml']
}