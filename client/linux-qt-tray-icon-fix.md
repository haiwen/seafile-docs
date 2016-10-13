## Fix the Tray Icon of Seafile Client on Ubuntu 14.04

If you're using ubuntu desktop 14.04, there is a known problem in the seafile linux client 5.1 and later: The tray icon of seafile client would appear on the top-left corner of the screen.

This is a bug that exists in Qt versions earlier than qt 5.5. And lots of other software are also affected by it. Ubuntu 16.04 is not affected by this bug because it ships with Qt 5.5 (while ubuntu 14.04 ships Qt 5.2).

Here we provide a workaround for this bug.

### The Workaround

First install the `opt-qt561-trusty` ppa and Qt 5.6 packages. The packages are installed to `/opt/` so your system won't be affected.

```
sudo add-apt-repository ppa:beineri/opt-qt561-trusty
sudo apt-get update
sudo apt-get install qt56base qt56translations qt56webengine
```

Download the wrapper script, which tells seafile-applet to use the Qt 5.6 libs we installed just now.

```
wget -O seafile-applet-qt56 https://gist.githubusercontent.com/lins05/6468059d8130ad50464b1b3b43ec46dc/raw/c23e84c435b60c528d06e40be239689f9947b9ed/seafile-applet-qt56
chmod +x seafile-applet-qt56
sudo mv seafile-applet-qt56 /usr/local/bin/
```

Then download the updated seafile client desktop file, which launchs seafile client through the wrapper scripts you downloaded just now:

```
wget -O seafile.desktop https://gist.githubusercontent.com/lins05/6468059d8130ad50464b1b3b43ec46dc/raw/c23e84c435b60c528d06e40be239689f9947b9ed/seafile.desktop
sudo cp seafile.desktop /usr/share/applications/seafile.desktop
```

Now you can launch seafile-applet from the ubuntu dashboard (quit the client first if it's running). The tray icon of seafile client should appear in the correct position.

Finally, tell apt not to override the seafile.desktop file when you upgrade seafile client in the future:

```
sudo dpkg-divert --add /usr/share/applications/seafile.desktop
```
