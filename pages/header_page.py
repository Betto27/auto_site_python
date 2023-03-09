from browser import Browser

class HeaderPageElements(object):

    INPUT_BUSCA = '#id-search-field'


class HeaderPage(Browser):

    def preencher_input_busca(self, texto):
        self.driver.find_element_by_css_selector('#id-search-field').send_keys(texto)

    def click_btn_go(self):
        self.driver.find_element_by_css_selector('#submit').click()