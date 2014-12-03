# Mac OS X

Setup homebrew environment
----------------------------
1. Install xcode

  - Download Xcode from [website](https://developer.apple.com/xcode/downloads/) or
    [App Store](http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12)
  - Xcode Command Line Utilities might be enough to build seafile, but it is left untested yet.

2. Install homebrew

  - Execute this from Terminal
  ``ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"``
  - Make sure you have a clean homebrew environment. You can double-check it
    by ``brew doctor``

Then install seafile from homebrew
  ```
  brew tap Chilledheart/seafile
  brew install seafile-client
  ```

If you face any installation issue, please report it with your homebrew logs
- [Homebrew Troubleshooting](https://github.com/Homebrew/homebrew/wiki/Troubleshooting)

If it is an issue while using homebrewed seafile, please report it with your seafile logs
- [Seafile FAQ](../faq.md)

Setup macports environment
-----------------------------

1. Install xcode
  - Download Xcode from [website](https://developer.apple.com/xcode/downloads/) or
  [App Store](http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12)

2. Install macports
  - Visit macports [website](https://www.macports.org/)

3. Install following libraries and tools using `port`

        sudo port install autoconf automake pkgconfig libtool glib2 \
        libevent vala openssl git qt4-mac python27 jansson

4. Install python

        sudo port select --set python python27
        sudo port install py27-pip

5. Set pkg config environment

        export PKG_CONFIG_PATH=/opt/local/lib/pkgconfig:/usr/local/lib/pkgconfig
        export LIBTOOL=glibtool
        export LIBTOOLIZE=glibtoolize
        export CFLAGS="-I/opt/local/include"
        export LDFLAGS="-L/opt/local/lib -L/usr/local/lib -Wl,-headerpad_max_install_names"


Compiling libsearpc
------------------

Download [libsearpc](https://github.com/haiwen/libsearpc), then:

        ./autogen.sh
        ./configure
        make
        sudo make install

Compiling ccnet
---------------

Download [ccnet](https://github.com/haiwen/ccnet), then:

        ./autogen.sh
        ./configure
        make
        sudo make install

Compiling seafile
-----------------

1. Download [seafile](https://github.com/haiwen/seafile)
2. Compile

        ./autogen.sh
        ./configure
        make
        sudo make install

Compiling seafile-client and packaging it
---------

1. prepare for building:

        ./genapp.sh xcode

    Generate xcode project from cmake

2. Compile seafile-applet.app：

        ./genapp.sh build

3. Package seafile-applet.app:

        ./genapp.sh otool
        ./genapp.sh package

    This will copy ccnet, seaf-daemon and other libraries to seafile-client, and use `install_name_tool` to modify the library paths in ccnet, seaf-daemon.
    After compiling, it will copy seafile.app to `${top_dir}/../seafile-${VERSION}`. You can also compiling seafile.app in xcode.

4. Go to seafile-applet.app and see if it can run correctly.

Problem you may encounter
-------------------------
1. If `install_name_tool` reports "malformed object" "unknown load command", It may be the version of xcode command line tools incompatible with `install_name_tool`.
2. If xcode can't find glib, Corrects xcode's "build settings/search paths/header search".
