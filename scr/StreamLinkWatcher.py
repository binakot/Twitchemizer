import sys
from streamlink import Streamlink


def watch(url):
    streamlink = Streamlink()
    streamlink.set_loglevel("info")
    streamlink.set_logoutput(sys.stdout)

    streams = streamlink.streams(url)
    stream = streams['audio_only']

    fd = stream.open()  # read to nowhere
    while True:
        fd.read(1024)
