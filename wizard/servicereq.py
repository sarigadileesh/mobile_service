from odoo import models, fields, api

class service_request(models.TransientModel):
    _name = 'servicereq.report'

    startdate1 = fields.Date()
    enddate1 = fields.Date()


    def mob_pdf_report(self):
        store1 = {
            'ids': self.ids,
            'model': self._name,
            'form': {'start_d': self.startdate1,
                     'end_d': self.enddate1,
                     }, }
        return self.env.ref('mobile_service.mob_pdf_report').report_action(self, data=store1)
                            # ^ * module name.id from <report tag in xml file in report folder

class servicereq_wizard(models.AbstractModel):
    _name = 'report.mobile_service.doc_rep'
             # * report. name from <report tag in xml file in report folder
    @api.model
    def _get_report_values(self, docids, data=None):
        start = data['form']['start_d']
        end = data['form']['end_d']


        filter = "mobile_service_service_request.date1::date>='" + str(start) + "' and mobile_service_service_request.date1::date<='"+ str(
            end) + "'"
                     # ^ id is from models _ id in security folder
        qry = """select name,num,email,brname,model,tech from mobile_service_service_request where """ + str(filter) + """"""
        print(qry)

        docss = []
        self.env.cr.execute(qry)
        for d in self.env.cr.dictfetchall():
            docss.append({
                'name': d['name'],
                'num': d['num'],
                'email': d['email'],
                'brname': d['brname'],
                'model': d['model'],
                'tech': d['tech'],
            })
        return {
            'res_id': 1,
            'res_model': 'servicereq.report',
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'startdate1': start,
            'enddate1': end,
            'data': docss,
        }
