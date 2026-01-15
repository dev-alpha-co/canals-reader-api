from logics.utils.page_base import PageBase
import sys


class CanalsRyokinListPage(PageBase):
    def __init__(self, selenium, config):
        super().__init__(selenium,
                         url=f'https://{config["CANALS_DOMAIN"]}/admin/RyoukinList.jsp')

    def new_registration_button(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=new]'
        )
