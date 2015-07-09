import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
from lxml import html


class Render(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()

url = 'https://impythonist.wordpress.com'
url = 'http://pycoders.com/archive/'
r = Render(url)
result = r.frame.toHtml()
formatted_result = str(result.toAscii())
#Next build lxml tree from formatted_result
tree = html.fromstring(formatted_result)

#Now using correct Xpath we are fetching URL of archives
archive_links = tree.xpath('//div[@class="campaign"]/a/@href')
print archive_links
# This step is important.Converting QString to Ascii for lxml to process
# archive_links = html.fromstring(str(result.toAscii()))
# print archive_links
