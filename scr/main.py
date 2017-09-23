import thread

import StreamLinkWatcher

STREAM_URL = 'http://www.twitch.tv/blizzakot'
WATCHER_COUNT = 5
PROXY_FILE = '../resources/proxy.txt'

with open(PROXY_FILE) as f:
    proxies = f.readlines()
proxies = [x.strip() for x in proxies]

for x in range(0, min(WATCHER_COUNT, len(proxies))):
    thread.start_new_thread(StreamLinkWatcher.watch, (STREAM_URL, proxies[x]))

raw_input('Press Enter to quit...\r\n')
