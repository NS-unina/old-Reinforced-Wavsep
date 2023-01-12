import os
import sys

from har_sender import send_from_har




def usage():
    print("[-] Usage: run_crawler.py <host> <port>")
    sys.exit(-1)

if len(sys.argv) == 3:
    host = sys.argv[1]
    port = sys.argv[2]

elif len(sys.argv) == 1:
    host = None 
    port = None

else: 
    usage()


# WAVSEP_TARGET = "http://127.0.0.1:18080/wavsep"

# request = HttpRequest.get(WAVSEP_TARGET)
# resp = request.send()
# print(resp.text)

send_from_har(os.path.join("har_requests", "xss", "RXSS-Detection-Evaluation-POST.har"), "http://{}:{}".format(host, port))