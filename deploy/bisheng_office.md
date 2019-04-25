# BiSheng Office

From version 7.0.0 on (including CE), Seafile supports [BiSheng Office](https://ibisheng.cn/) to view/edit office files online. In order to use BiSheng Office, you must first deploy an BiSheng Office server.

## Deployment of BiSheng Office Server

Please refer to the official document of BiSheng Office: https://ibisheng.cn/apps/blog/free/

### Configure Seafile

Add the following config option to ```seahub_settings.py```.

```python
# Enable BiSheng Office
ENABLE_BISHENG_OFFICE = True
BISHENG_OFFICE_API_KEY = 'your bisheng office server api key'
BISHENG_OFFICE_HOST_DOMAIN = 'http://your-bisheng-office-server-domain'
```

Then restart the Seafile Server

```
./seafile.sh restart
./seahub.sh restart
```

When you click on a document you should see the new preview page.
