import thread
import StreamLinkWatcher

WATCHER_COUNT = 10

for x in range(0, WATCHER_COUNT):
    thread.start_new_thread(StreamLinkWatcher.watch, ('https://www.twitch.tv/blizzakot',))

raw_input("Press Enter to quit...")
