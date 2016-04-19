# Mac OS X

## 선택지 1: Homebrew (macports와 겹침)

### homebrew 환경 설정

1. xcode를 설치하십시오

  - [웹 사이트](https://developer.apple.com/xcode/downloads/) 또는 [App Store](http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12)에서 Xcode를 다운로드하십시오
  - Seafile을 빌드할 때 Xcode 명령행 유틸리티로 충분할 수 있지만, 아직 시험해보진 않았습니다. :P

2. homebrew를 설치하십시오

  - 아래 명령을 터미널에서 실행하십시오
  ``ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
  - 초기 homebrew 환경을 갖췄는지 확인하십시오. ``brew doctor``명령으로 다시 확인해볼 수 있습니다

> 기타 정보는 http://brew.sh/ 주소를 방문하십시오

그 다음 homebrew로 Seafile을 설치하십시오
  ```
  brew tap Chilledheart/seafile
  brew install seafile-client
  ```

설치상 문제가 있다면 homebrew 로그를 보내주십시오.
- [Homebrew 문제 해결](https://github.com/Homebrew/homebrew/wiki/Troubleshooting)

homebrew로 설치한 Seafile에 문제가 있다면 Seafile 로그를 보내주십시오.
- [Seafile 자주 묻는 질문](../faq.md)

## 선택지 2: Macports (homebrew와 겹침)

### macports 환경 설정

1. xcode를 설치하십시오
  - [웹 사이트](https://developer.apple.com/xcode/downloads/) 또는 [App Store](http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12)에서 Xcode를 다운로드하십시오

2. macports를 설치하십시오

  - https://www.macports.org/install.php에서 간단하게 시작

> 더 많은 내용은 https://www.macports.org/ 주소에 있습니다

3. `port`로 다음 라이브러리 및 도구를 설치하십시오

        sudo port install autoconf automake pkgconfig libtool glib2 \
        libevent vala openssl git qt4-mac jansson

4. 파이썬을 설치하십시오

        sudo port install python27
        sudo port select --set python python27

        sudo port install py27-pip
        sudo port select --set pip pip27

5. pkg config 환경을 설정하십시오

        export PKG_CONFIG_PATH=/opt/local/lib/pkgconfig:/usr/local/lib/pkgconfig
        export LIBTOOL=glibtool
        export LIBTOOLIZE=glibtoolize
        export CPPFLAGS="-I/opt/local/include"
        export LDFLAGS="-L/opt/local/lib -L/usr/local/lib -Wl,-headerpad_max_install_names"


libsearpc 컴파일
------------------

[libsearpc](https://github.com/haiwen/libsearpc)를 다운로드한 후:

        ./autogen.sh
        ./configure
        make
        sudo make install

ccnet 컴파일
---------------

[ccnet](https://github.com/haiwen/ccnet)을 다운로드한 후:

        ./autogen.sh
        ./configure
        make
        sudo make install

seafile 컴파일
-----------------

1. [seafile](https://github.com/haiwen/seafile)을 다운로드하십시오
2. 컴파일 하십시오

        ./autogen.sh
        ./configure --disable-fuse
        make
        sudo make install

seafile-client 컴파일 및 꾸러미 생성
---------

1. 빌드 스크립트를 실행하십시오:

        ./scripts/build.py

2. Go to Release directory and see if `seafile-applet.app` can run correctly.

직면할 수 있는 문제
-------------------------
1. `install_name_tool`에서 "malformed object" "unknown load command" 메시지를 출력했다면, xcode 명령행 도구의 해당 버전이 `install_name_tool`와 맞지 않기 때문일 수도 있습니다.
2. xcode에서 glib를 찾지 못했다면, xcode의 "build settings/search paths/header search" 설정을 올바르게 고치십시오.

