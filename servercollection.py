
class Server():
    # activeToken is the user that is in the server we are scrapping from
    # proxyToken 
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
        'directedChannel': '955963680829341716',
        'chatChannel': False
    }, 
        #mrprada-alpha
    {
        'channel': '935774469740429352',
        'directedChannel' : '955963737863487569',
        'chatChannel': False
    },
        #friazzin-alpha
    {
        'channel': '955831993667584070',
        'directedChannel' : '955963760282042409',
        'chatChannel': False
    }
]





# <--------------Yuck Pass----------------->
yuckPass = Server()
yuckPass.activeToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
yuckPass.proxyToken = 'OTM2NTI2NjIyMjk3ODQ1Nzcy.YfOe0w._gnjg1tHO3bTrF-nHo8TjPTcfEI'
yuckPass.channelCollection = [
    {
        'channel': '951616970665635910',
        'directedChannel': '955977208390897744',
        'chatChannel': False
    },
    {
        'channel': '953375551219974165',
        'directedChannel': '955977641037529199',
        'chatChannel': False
    }
]