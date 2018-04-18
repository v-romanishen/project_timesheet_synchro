# -*- coding: utf-8 -*-

from openerp import http
import logging

_logger = logging.getLogger(__name__)

class UrlControllers(http.Controller):
    @http.route('/web/test/test/', type='json', auth='none')
    def test_rpc_request(self, **kw):
        _logger.info("__________CONNECT SUCCESS__________")

        response = ""
        arr = ["H", "i", " ", "V", "a", "s", "y", "a"]

        for el in arr:
            response += el

        return response
