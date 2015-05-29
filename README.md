Imgur Upload
============
* Upload an image to an Imgur account
* Easy to integrate with Linux desktop usage
* Communicates with the Imgur API using the official 
  [Imgur python client library][1]

Configuration
-------------

See [The Imgur API - Authentication][2].

As this application is not official or in any way endorsed by Imgur (see
[imgur.com/apps][3]) you have to fix registration and authentication yourself. 
See [imgurpython - library usage][4] to get an idea how this is done. 

Once done, fill in your account properties in `.imgurrc` and copy it to your
`$HOME` directory. Designed to upload to an account, but could also be used for
anonymous uploads.

Simple usage
------------

1. Place `imgur.py` somewhere in your `$PATH`, e.g. `/home/user/bin/imgur.py`.
2. Run with path to an image as argument:

    $ imgur.py shot0001.png

Linux desktop usage
-------------------

1. Place `imgur.py` somewhere in your `$PATH`, e.g. `/home/user/bin/imgur.py`.
2. Update the paths in `Imgur.desktop`, optionally with an icon of choice. 
3. Copy `Imgur.desktop` to `$HOME/.local/share/applications` or similar
   depending on setup. Consult the documentation of your distro and the 
   [MIME application specification][5] on Freedesktop.org.
4. Update `mimeapps.list` with file associations to whatever file types you
   want, e.g:

    [Added Associations]
    image/gif=kde4-gwenview.desktop;gimp.desktop;Imgur.desktop;
    image/jpeg=kde4-gwenview.desktop;gimp.desktop;Imgur.desktop;
    image/png=kde4-gwenview.desktop;gimp.desktop;Imgur.desktop;

5. The Imgur Upload application should now be available on "Open With.." and
   any other menus using the MIME associations. 

![Open With...](http://i.imgur.com/DDuWQrd.png)

Demo
----

See [imgur_screenshot.ogv][6] for a demo using KDE's ksnapshot tool for taking
a screenshot, uploading it to Imgur using the PNG file association and finally
opening it in the default browser. 



[1]: https://github.com/Imgur/imgurpython
[2]: https://api.imgur.com/#authentication
[3]: https://imgur.com/apps
[4]: https://github.com/Imgur/imgurpython#library-usage
[5]: http://standards.freedesktop.org/mime-apps-spec/mime-apps-spec-1.0.1.html
[7]: https://github.com/timss/imgur-upload/blob/master/imgur_screenshot.ogv
