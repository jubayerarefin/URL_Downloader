import urllib
import sys

__name__ = 'Parser'
__author__ = 'Jubayer Arefin'


class Parser(object):
    container = 'list.txt'

    # Parse a text file containing urls separated by new lines
    def parse(self):
        fonts = open(self.container, 'r')
        fonts.tell()
        lines = fonts.read()
        separator = '\n'
        return lines.split(separator, lines.count(separator))

    # Download parsed urls and save to disk
    def download(self, argv):
        print argv
        if not argv:
            if len(argv) > 1:
                print "Pass only one text file name."
                exit()
            elif 0 < len(argv) < 2:
                self.container = argv[0]
        opener = urllib.URLopener()
        urls = self.parse()
        for url in urls:
            # Strip of spaces if there is any
            url.strip(' ')
            # Check if the line of text starts with `http://` or `https://`
            if url.startswith('http://', 0, 7) or url.startswith('https://', 0, 8):
                print url.split('/')[-1]
                # opener.retrieve(url, url.split('/')[-1])


parser = Parser()
sys.argv.append('asdasd')
sys.argv.append('dlist.txt')
parser.download(sys.argv[1:])
