from servercollection import yuckPass
from requestsfunc import retrieve_messages, send_message
import time
import multiprocessing

recent_messages = []
for value in yuckPass.channelCollection:
    recent_messages.append('')
def run():
    while True:
        counter = 0
        for value in yuckPass.channelCollection:
            json_obj = retrieve_messages(yuckPass.activeToken ,value['channel'])
            try:
                payload_content_0 = json_obj[0]['content']
            except KeyError:
                print('KeyError 0')

            if payload_content_0 != recent_messages[counter]:
                send_message(value['directedChannel'], payload_content_0, yuckPass.proxyToken)
                recent_messages[counter] = payload_content_0
            counter += 1
        counter = 0
run()