import time
from servercollection import aquaHQ
from requestsfunc import retrieve_messages, send_message

recent_messages = []
for value in aquaHQ.channelCollection:
    recent_messages.append('')
def aquaHQrun():
    while True:
        counter = 0
        for value in aquaHQ.channelCollection:
            json_obj = retrieve_messages(aquaHQ.activeToken ,value['channel'])
            try:
                payload_content_0 = json_obj[0]['id']
            except KeyError:
                print('KeyError 0')

            if payload_content_0 != recent_messages[counter]:
                send_message(value['directedChannel'], json_obj[0]['content'], aquaHQ.proxyToken)
                recent_messages[counter] = payload_content_0
            counter += 1
        time.sleep(1)
        counter = 0

if __name__ == '__main__':
    aquaHQrun()