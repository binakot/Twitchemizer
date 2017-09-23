import sys

from streamlink import Streamlink


def watch(url, proxy):
    print 'Run watcher of ' + url + ' from ' + proxy + '\r\n'

    streamlink = Streamlink()
    streamlink.set_loglevel('info')
    streamlink.set_logoutput(sys.stdout)
    streamlink.set_option('http-proxy', 'http://' + proxy)
    #streamlink.set_option('https-proxy', 'https://' + proxy)
    #streamlink.set_option('rtmp-proxy', 'http://' + proxy)

    streams = streamlink.streams(url)
    stream = streams['audio_only']

    fd = stream.open()  # read to nowhere
    while True:
        fd.read(1024)
