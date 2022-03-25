import time
from servercollection import test
from requestsfunc import retrieve_messages, send_message

recent_messages = []
for value in test.channelCollection:
    recent_messages.append('')
def testrun():
    try:
        while test.isLive:
            print("online")
            counter = 0
            for value in test.channelCollection:
                json_obj = retrieve_messages(test.activeToken ,value['channel'])
                try:
                    payload_content_0 = json_obj[0]['id']
                except KeyError:
                    print('KeyError 0')

                if payload_content_0 != recent_messages[counter]:
                    send_message(value['directedChannel'], json_obj[0]['content'], test.proxyToken)
                    recent_messages[counter] = payload_content_0

                counter += 1
            time.sleep(1)
            counter = 0
    except:
        test.isLive = False
if __name__ == '__main__':
    testrun()