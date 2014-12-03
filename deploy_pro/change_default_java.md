
When you have both java6 and java7 installed, the default java may not be java 7.

Do this by typing `java -version`, and check the output.

- If the output is like **"java version "1.7.0_xx"**, then the default java is java 7, which is good.
- If the output is like **"java version "1.6.0_xx"**, then the default java is java 6, we need to configure default java to java 7.

If the default java is java 6, then do

On Debian/Ubuntu:
```
sudo update-alternatives --config java
```

On CentOS/RHEL:
```
sudo alternatives --config java
```

The above command will ask you to choose one of the installed java as the default. You should choose java 7 here.

After that, you should re-run `java -version` to make sure the change has taken effect.

[Reference link](http://unix.stackexchange.com/questions/35185/installing-openjdk-7-jdk-does-not-update-java-which-is-still-version-1-6)
