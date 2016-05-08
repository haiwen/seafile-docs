java6와 java7을 함께 설치했다면 java 7이 기본이 아닐 수도 있습니다.

`java -version`을 입력하고, 출력 내용을 확인하십시오.

- 출력이 **"java version "1.7.0_xx"**와 같은 식이면, 기본 자바 버전은 7이며, 활용하기에 좋습니다.
- 출력이 **"java version "1.6.0_xx"**와 같은 식이면, 기본 자바 버전은 6이며, 7을 기본으로 사용하도록 설정해야합니다.

기본 자바 버전이 6일 경우,

데비안/우분투:
```
sudo update-alternatives --config java
```

CentOS/RHEL:
```
sudo alternatives --config java
```

위 명령을 실행하면 설치한 자바 중 하나를 기본으로 설정하도록 물어봅니다. 여기서 7을 선택해야합니다.

명령 처리가 끝나면 `java -version`을 다시 실행하여 바꾼 설정이 동작하는지 확인해야합니다.

[참고 링크](http://unix.stackexchange.com/questions/35185/installing-openjdk-7-jdk-does-not-update-java-which-is-still-version-1-6)

