from browser import Browser


class ResultsPage(Browser):

    def get_text_title(self):
        return self.driver.find_element_by_css_selector('.main-content h2').text