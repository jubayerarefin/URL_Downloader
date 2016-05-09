import urllib
import sys
import platform
from subprocess import call

# __name__ = 'Parser'
__author__ = 'Jubayer Arefin'
__email__ = 'dipu2005 at gmail.com'


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
        if argv:
            if len(argv) > 1:
                print "Pass only one text file name as parameter."
                exit()
            elif 0 < len(argv) < 2:
                self.container = argv[0]
                print 'I will now try to download the contents of this file: ' + argv[0]
        opener = urllib.URLopener()
        urls = self.parse()
        for url in urls:
            # Strip of spaces if there is any
            url.strip(' ')
            # Check if the line of text starts with `http://` or `https://`
            print 'Checking url(s)...\n'
            if url == "\n" or url is None:
                print 'url(s) are not valid.'
                exit()
            elif url.startswith('http://', 0, 7) or url.startswith('https://', 0, 8):
                print url.split('/')[-1]
                opener.retrieve(url, url.split('/')[-1])
                print "is downloaded"
                if platform.system().lower() is 'linux':
                    call(["notify-send", url + " is downloaded."])
            else:
                print "url(s) are not valid. Please provide valid url that starts with http: or https:"


if __name__ == '__main__':
    parser = Parser()
    parser.download(sys.argv[1:])
else:
    print 'Sorry, can\'t run'
