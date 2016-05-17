# 所用端口说明

Seafile 服务器由两个组件组成，默认情况下用到 8000, 8082 两个端口号 (TCP)。

## 配置文件

所有端口的相关配置都记录在`ccnet.conf`文件和`seafile.conf`文件中

#### 如何打开 ccnet.conf 文件

- 右击 Seafile 服务器托盘图标，选择"打开 seafile-server 文件夹"选项
- 打开`seafile-server`目录下的`ccnet`文件夹。`ccnet.conf`文件就在此文件夹下。

#### 如何打开 seafile.conf 文件

- 右击 Seafile 服务器托盘图标，选择"打开 seafile-server 文件夹"选项
- 打开`seafile-server`目录下的`seafile-data`文件夹。`seafile.conf`文件就在此文件夹下。


在接下来的部分，我们分别列举了 Seafile 服务器各个组件用到的TCP端口以及如何改变它们（比如，一些端口很有可能已经被其他应用程序占用）。 

**注意**：如果您改变了以下任何端口，请重启 Seafile 服务器。  

## seahub

`seahub` 是 Seafile 服务器的 Web 端。

**注意**：如果您改变了 Seahub 的端口号，`ccnet.conf`文件中的`SERVICE_URL`也应该随之改变。

- 默认端口： 8000
- 如何设置端口号： 编辑`seafile.conf`文件。 设置在`seahub`段下`port`的值.

```
[seahub]
port=8000
```
- 编辑`ccnet.conf`文件，改变`SERVICE_URL`的值。比如， 如果您将端口号重新设置为 8001 ，那么更改`SERVICE_URL`的值如下：
```
[General]
SERVICE_URL = <您的 IP 或者域名>:8001
```

## seafile fileserver

`seafile fileserver` 负责为 Seahub 处理文件的上传和下载

- 默认端口： 8082
- 如何设置端口号： 桌面客户端会连接这个端口来同步文件，所以不要修改这个端口。

