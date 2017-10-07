PAGE_SIZES = {
    'a4': (210, 297),
    'a3': (297, 420)
}

class PageGeometry(object):
    def __init__(self, page_size, margins=10, portait=True):
        page_size = page_size.lower()

        if page_size not in PAGE_SIZES.keys():
            raise f'Unknown page size {page_size}'
        
        self._page_size = PAGE_SIZES[page_size]
        self._margins = margins
        self.portait = portait
        super(PageGeometry, self).__init__()
    
    def max_printable_dimensions(self):
        return [
            (min(self._page_size) if self.portait else max(self._page_size)) - self._margins,
            (max(self._page_size) if self.portait else min(self._page_size)) - self._margins
        ]
