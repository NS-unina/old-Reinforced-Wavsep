import os
import sys

from har_sender import send_from_har
HAR_FOLDER = "har_requests"



def usage():
    print("[-] Usage: run_crawler.py <category> <har_file> <host> <port>")
    sys.exit(-1)

host = None
port = None
if len(sys.argv) < 3:
    usage()
category = sys.argv[1]
filename = sys.argv[2]

if len(sys.argv) == 5:
    host = sys.argv[3]
    port = sys.argv[4]


filepath = os.path.join(HAR_FOLDER, category, filename)

print("[+] Scanning {} har file ".format(filepath))

send_from_har(filepath, "http://{}:{}".format(host, port) if host else None)
