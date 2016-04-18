# Details about File Search

**Note**: Since Seafile Server 5.0.0, all config files are moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

## <a id="search-opt"></a>Search Options

Following options should be set in file **seafevents.conf**, and need to restart seafile and seahub to take effect.

```
[INDEX FILES]
...
# Enable full-text search for PDF/Word/PPT
index_office_pdf = false

```

## Use existing ElasticSearch server

The search module use an elasticsearch server bundled within the seafile pro server tarball. However, you may have an existing ElasticSearch server or cluster running in your company. In this situation, you can change the config file to use your existing ES server or cluster.

This feature is added since `Seafile Professional Server 2.0.5`.

### Notes

- Your ES cluster must have thrift transport plugin installed. If not, install it:

```
bin/plugin -install elasticsearch/elasticsearch-transport-thrift/1.6.0
```

Restart your ES server after this.

- Currently the seafile search module use the default analyzer in your ES server settings. 


### Change the config file

- Edit `seafevents.conf`, add settings in the section **[INDEX FILES]** to specify your ES server host and port:

```
vim seafevents.conf
```

```
[INDEX FILES]
...
es_host = 192.168.1.101
es_port = 9500
```

- `es_host`: The ip address of your ES server
- `es_port`: The listening port of the Thrift transport module. By default it should be `9500`

## <a id="wiki-faq"></a>Common problems

### <a id="how-to-rebuild-search-index"></a>How to rebuild index if something goes wrong

You can rebuild search index by:

```
./pro/pro.py search --clear
./pro/pro.py search --update
```

If this not work, you can try the following steps:

1. Stop Seafile
2. Remove old search index `rm -rf pro-data/search`
3. Restart Seafile
4. Wait one minute then run `./pro/pro.py search --update`


### <a id="wiki-search-no-result"></a>I get no result when I search a keyword

The search index is updated every 10 minutes by default. So before the first index update is performed, you get nothing no matter what you search.

  To be able to search immediately,

  - Make sure you have started seafile server
  - Update the search index manually:
```
      cd haiwen/seafile-pro-server-2.0.4
     ./pro/pro.py search --update
```

### <a id="wiki-cannot-search-encrypted-files"></a>Encrypted files cannot be searched

This is because the server can't index encrypted files, since, they are encrypted.





