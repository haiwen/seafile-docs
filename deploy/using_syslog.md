## Configure Seafile to Use Syslog

Since community edition 5.1.2 and professional edition 5.1.4, Seafile support using Syslog.

### Configure Syslog for Seafile Controller and Server

Add following configuration to `general` section in `seafile.conf`:
```
[general]
enable_syslog = true
```

Restart seafile server, you will find follow logs in `/var/log/syslog`:
```
May 10 23:45:19 ubuntu seafile-controller[16385]: seafile-controller.c(154): starting ccnet-server ...
May 10 23:45:19 ubuntu seafile-controller[16385]: seafile-controller.c(73): spawn_process: ccnet-server -F /home/plt/haiwen/conf -c /home/plt/haiwen/ccnet -f /home/plt/haiwen/logs/ccnet.log -d -P /home/plt/haiwen/pids/ccnet.pid
```
```
May 12 01:00:51 ubuntu seaf-server[21552]: ../common/mq-mgr.c(60): [mq client] mq cilent is started
May 12 01:00:51 ubuntu seaf-server[21552]: ../common/mq-mgr.c(106): [mq mgr] publish to hearbeat mq: seaf_server.heartbeat
```

### Configure Syslog For Seafevents (Professional Edition only)

Add following configuration to `seafevents.conf`:
```
[Syslog]
enabled = true
```

Restart seafile server, you will find follow logs in `/var/log/syslog`
```
May 12 01:00:52 ubuntu seafevents[21542]: [seafevents] database: mysql, name: seahub-pro
May 12 01:00:52 ubuntu seafevents[21542]: seafes enabled: True
May 12 01:00:52 ubuntu seafevents[21542]: seafes dir: /home/plt/pro-haiwen/seafile-pro-server-5.1.4/pro/python/seafes
```

### Configure Syslog For Seahub

Add following configurations to `seahub_settings.py`:

```
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(process)-5d %(thread)d %(name)-50s %(levelname)-8s %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)s %(funcName)s %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(name)s %(levelname)s %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'syslog': {
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'formatter': 'standard'
        },
    },
    'loggers': {
        # root logger
        '': {
            'handlers': ['console', 'syslog'],
            'level': 'INFO', # Logs when log level is higher than info. Level can be any one of DEBUG, INFO, WARNING, ERROR, CRITICAL.
            'disabled': False
        },
        'django.request': {
            'handlers': ['console', 'syslog'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
```
