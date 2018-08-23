# Access log and auditing

In the Pro Edition, Seafile offers four audit logs in system admin panel:

* Login log
* File access log (including access to shared files)
* File update log
* Permission change log

![Seafile Auditing Log](../images/admin-audit-log.png)

The logging feature is turned off by default before version 6.0. Add the following option to `seafevents.conf` to turn it on:

```
[Audit]
## Audit log is disabled default.
## Leads to additional SQL tables being filled up, make sure your SQL server is able to handle it.
enabled = true
```


The audit log data is being saved in `seahub-db`.
