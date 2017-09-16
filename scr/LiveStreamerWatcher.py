import sys
from livestreamer import Livestreamer


def watch(url):
    session = Livestreamer()
    session.set_loglevel("info")
    session.set_logoutput(sys.stdout)
    session.set_option("http-headers", "Client-ID=jzkbprff40iqj646a697cyrvl0zt2m6")

    streams = session.streams(url)
    stream = streams['audio_only']

    fd = stream.open()  # read to nowhere
    while True:
        fd.read(1024)
