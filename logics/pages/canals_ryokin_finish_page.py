from logics.utils.page_base import PageBase
import sys


class CanalsRyokinFinishPage(PageBase):
    def __init__(self, selenium, config):
        super().__init__(selenium,
                         url=f'https://{config["CANALS_DOMAIN"]}/admin/FinishRyoukinEdit.jsp')

    def logout_button(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'body > table:nth-child(1) > tbody > tr:nth-child(2) > td.cls_honbun > div > a'
        )
