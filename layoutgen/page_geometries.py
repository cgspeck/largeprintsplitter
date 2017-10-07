from sys import exit

from reportlab.lib import pagesizes

class PageGeometry(object):
    def __init__(self, page_size, margins=10, portait=True):
        page_size = page_size.upper()

        try:
            page_size_imperial = getattr(pagesizes, page_size)
        except AttributeError as e:
            print(f'Unknown page size "{page_size}"!')
            exit(1)
        
        self._page_size_imperial = page_size_imperial
        self._page_size = (
            self.convert_fractional_inch_to_mm(page_size_imperial[0]),
            self.convert_fractional_inch_to_mm(page_size_imperial[1]),
        )
        self._margins = margins
        self.portait = portait
        super(PageGeometry, self).__init__()


    @staticmethod
    def convert_fractional_inch_to_mm(value):
        return (value / 72) * 25.4


    def max_printable_dimensions(self):
        return [
            (min(self._page_size) if self.portait else max(self._page_size)) - self._margins,
            (max(self._page_size) if self.portait else min(self._page_size)) - self._margins
        ]
