from logics.utils.page_base import PageBase
import sys


class CanalsLoginPage(PageBase):
    def __init__(self, selenium, config):
        super().__init__(selenium,
                         url=f'https://{config["CANALS_DOMAIN"]}/admin/Login.jsp')

    def login_id(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=AdminID]'
        )

    def password(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=Password]'
        )

    def login_button(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'body > div > form > table:nth-child(2) > tbody > tr:nth-child(2) > td > input[type=submit]'
        )
