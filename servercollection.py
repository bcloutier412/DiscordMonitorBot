
class Server():
    # activeToken is the user that is in the server we are scrapping from
    # proxyToken 
    def __init__(self):
        self.serverName = ''
        self.activeToken = ''
        self.proxyToken = ''
        self.channelCollection = []
        self.isLive = False

# <--------------aquaHQ----------------->
aquaHQ = Server()
aquaHQ.serverName = 'aquaHQ'
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
        'directedChannel': '955963737863487569',
        'chatChannel': False
    },
        #friazzin-alpha
    {
        'channel': '955831993667584070',
        'directedChannel': '955963760282042409',
        'chatChannel': False
    },
    {
        'channel': '935772422517448725',
        'directedChannel': '955977663682580520',
        'chatChannel': True
    }
]





# <--------------Yuck Pass----------------->
yuckPass = Server()
yuckPass.serverName = 'yuckPass'
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
        'directedChannel': '957184545315233803',
        'chatChannel': False
    },
    {
        'channel': '928843551855489136',
        'directedChannel': '955977821602328636',
        'chatChannel': True
    }
]


# <--------------------Test----------------------->
test = Server()
test.serverName = 'test'
test.activeToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
test.proxyToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
test.channelCollection = [
    {
        'channel': '956827879591784518',
        'directedChannel': '956824883319414794',
        'chatChannel': False
    }
]


# <--------------------Alpha Oni----------------------->
oni = Server()
oni.serverName = 'Alpha Oni'
oni.activeToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
oni.proxyToken = 'OTM2NTMxOTAxNzI3MDE0OTgz.YfOjeA.V5COqMTZ-ql2eFM6FjJ9NIVl4Kk'
oni.channelCollection = [
    {
        'channel': '945551117411053578',
        'directedChannel': '957413862209093644',
        'chatChannel': False
    },
    {   
        'channel': '943990390942470144',
        'directedChannel': '957413902679965757',
        'chatChannel': True 
    },
    {   
        'channel': '952888290489540608',
        'directedChannel': '957414111262675025',
        'chatChannel': False
    },
    {   
        'channel': '944012876396511272',
        'directedChannel': '957414637454884864',
        'chatChannel': False
    },
    {   
        'channel': '944152306897805323',
        'directedChannel': '957414953256644698',
        'chatChannel': False
    }
]

servercollection = [aquaHQ, yuckPass, oni, test]