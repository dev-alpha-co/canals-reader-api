from logics.utils.page_base import PageBase
import sys


class SamplePage(PageBase):
    def __init__(self, selenium):
        super().__init__(selenium,
                         url='https://www.yahoo.co.jp')

    def TopLink(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            '#TopLink > ul > li:nth-child(1) > a > span > span'
        )
