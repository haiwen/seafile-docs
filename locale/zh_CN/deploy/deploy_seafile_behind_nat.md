# 防火墙 / NAT 设置

通过广域网(WAN)访问部署在局域网(LAN)的 Seafile 服务器

需要:

- 一台支持端口转发的路由器
- 使用动态域名解析服务
- 配置 Seafile 服务器

### Table of Contents

- [Setup the server](deploy_Seafile_behind_NAT.md#setup-the-server)
- [Setup port forwarding in your router](deploy_Seafile_behind_NAT.md#setup-port-forwarding-in-your-router)
- [Use a dynamic dns serivce](deploy_Seafile_behind_NAT.md#use-a-dynamic-dns-serivce)
- [Modify your seafile configuration](deploy_Seafile_behind_NAT.md#modify-your-seafile-configuration)


## Setup the server

First, you should follow the guide on [Download and Setup Seafile Server](using_sqlite.md) to setup your Seafile server.

Before you continue, make sure:

- You can visit your seahub website
- You can download/sync a library through your seafile client

## 在路由器中设置端口转发

### 确保路由器支持端口转发功能

首先, 确保你的路由器支持端口转发功能：

- Login to the web adminstration page of your router. If you don't know how to do this, you should find the instructions on the manual of the router. If you have no maunal, just google **"XXX router administration page"** where `XXX` is your router's brand.

- 找到包含 "转发" 或者 "高级" 等关键词的页面, 说明此路由器支持端口转发功能。

### 设置路由转发规则

Seafile 服务器包含两个组件， 请根据以下规则为 Seafile 组件设置端口转发。

<table>
<tr>
  <th>组件</th>
  <th>默认端口</th>
</tr>
<tr>
  <td>fileserver</td>
  <td>8082</td>
</tr>
<tr>
  <td>seahub</td>
  <td>8000</td>
</tr>
</table>

* You don't need to open port 8000 and 8082 if you deploy Seafile behind Apache/Nginx.
* If you're not using the default ports, you should adjust the table accroding to your own customiztion.

### 端口转发测试

设置端口转发后，可按以下步骤测试是否成功:

- 打开一个命令行终端
- 访问 http://who.is 得到本机的IP
- 通过以下命令连接 Seahub
````
telnet <Your WAN IP> 8000
```

如果端口转发配置成功，命令行会提示连接成功。否则, 会显示 *connection refused* 或者 *connection timeout*， 提示连接不成功。

若未成功，原因可能如下:

- 端口转发配置错误
- 需要重启路由器
- 网络不可用

### 设置 SERVICE_URL

服务器依赖于 `ccnet.conf` 中的 "SERVICE_URL" 来生成文件的上传/下载链接。如果使用内置的 web 服务器，改为

```
SERVICE_URL = http://<Your WAN IP>:8000
```

大部分路由器都支持 NAT loopback. 当你通过内网访问 Seafile 时, 即使使用外部 IP ，流量仍然会直接通过内网走。

## Use a Dynamic DNS Serivce

### Why use a Dynamic DNS(DDNS) Service?

完成以上端口转发配置工作后，就可以通过外网 IP 访问部署在局域网内的 Seafile 服务器了。但是对于大多数人来说， 外网 IP 会被 ISP (互联网服务提供商)定期更改, 这就使得，需要不断的进行重新配置.

可以使用动态域名解析服务来解决这个问题。通过使用域名解析服务，你可以通过域名（而不是 IP）来访问 Seahub，即使 IP 会不断变化，但是域名始终会指向当前 IP。

There are a dozen of dynamic DNS service providers on the internet. If you don't know what service to choose We recommend using [www.noip.com](http://www.noip.com) since it performs well in our testing.

怎样使用域名解析服务，不在本手册说明范围之内，但是基本上，你需要遵循以下步骤:

1. 选择一个域名解析服务提供商。
2. 注册成为此服务商的一个用户。
3. Download a client from your DDNS service provider to keep your domain name always mapped to your WAN IP

## 更改 Seafile 配置

当你配置好域名解析服务之后，需要对 `ccnet.conf` 进行更改:

```
SERVICE_URL = http://<Your dynamic DNS domain>:8000
```

然后重新 Seafile 服务.

