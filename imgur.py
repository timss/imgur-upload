#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dbus
import ConfigParser
import sys
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from os.path import expanduser, isfile
from subprocess import call, Popen, PIPE

def clipboard(link):
    """Copy image link to system clipboard if xclip exists"""
    try:
        p = Popen(['xclip', '-selection', 'c'], stdin=PIPE)
        p.communicate(input=link)
        return True
    except OSError:
        notify("xclip not found, not able to use system clipboard")
        return False
    except:
        notify("Unknown clipboard error")
        return False

def get_config(path='~/.imgurrc'):
    """Get and validate configuration"""
    realpath = expanduser(path)

    if not isfile(realpath):
        notify("No configuration found")
        return False

    config = ConfigParser.ConfigParser()
    config.read(realpath)

    if 'auth' and 'general' not in config.sections():
        notify("Invalid '%s' configuration" % (section))
        return False

    return config

def notify(body, summary="Imgur", app_name="Imgur", app_icon="~/.icons/imgur.png"):
    """Shows a desktop notification using D-Bus.

    Using the freedesktop.org and D-Bus standards to display a desktop
    notification using the same code on most popular desktop environments.
    http://mueller.panopticdev.com/2011/06/create-notification-bubbles-in-python.html
    """
    try:
        app_icon = expanduser(app_icon)
        bus_name = "org.freedesktop.Notifications"
        object_path = "/org/freedesktop/Notifications"
        session_bus = dbus.SessionBus()
        obj = session_bus.get_object(bus_name, object_path)
        interface = dbus.Interface(obj, bus_name)

        interface.Notify(app_name, 0, app_icon, summary, body, [], [], 5000)

        return True
    except:
        # TODO: catch this more elegantly
        return False

def upload(client, image, anon):
    """Upload image to Imgur using the Imgur API"""
    try:
        return client.upload_from_path(image, anon=anon)
    except IOError as e:
        notify("I/O error(%d): %s" % (e.errno, e.strerror))
    except ImgurClientError as e:
        notify("Imgur error(%d): %s" (e.status_code, e.error_message))
    except:
        notify("Unknown error")
    else:
        return False

def main():
    # somewhat shit and hard to read, should fix a better solution
    config = get_config() or sys.exit(1)
    client = ImgurClient(**dict(config.items('auth'))) or sys.exit(1)
    result = upload(client, sys.argv[1], anon=not hasattr(client, 'auth')) or sys.exit(1)
    link = result['link']

    if config.getboolean('general', 'clipboard'): clipboard(link)
    if config.getboolean('general', 'notify'): notify("Image link: %s" % (link))
    if config.getboolean('general', 'browser'): call(['xdg-open', link])

    sys.exit(0)

if __name__ == '__main__':
    main()
