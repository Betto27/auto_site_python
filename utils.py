from browser import Browser


class Utils(Browser):

    def navegar(self, url):
        self.driver.get(url)