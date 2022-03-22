
class Server():
    # activeToken is the user that is in the server we are scrapping from
    def __init__(self):
        self.activeToken = ''
        self.proxyToken = ''
        self.channelCollection = []

# <--------------aquaHQ----------------->
aquaHQ = Server()
aquaHQ.activeToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
aquaHQ.proxyToken = 'ODg0NjU0MDYyODcwNjAxNzM5.YTbocQ.DWod2UZqL50hkuUcC0Hw0P9mSLo'
aquaHQ.channelCollection = [
    {
        #mg-alpha
        'channel': '953866553135353856',
        'directedChannel': '955943446550573137',
    }, 
        #mrprada-alpha
    {
        'channel': '935774469740429352',
        'directedChannel' : '955943475608703066',
    },
        #friazzin-alpha
    {
        'channel': '955831993667584070',
        'directedChannel' : '955943512329842818',
    }
]
# <--------------aquaHQ----------------->
