# Details about File Search

**Note**: Since Seafile Professional Server 5.0.0, all config files are moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

## <a id="search-opt"></a>Search Options

The following options can be set in **seafevents.conf** to control the behaviors of file search. You need to restart seafile and seahub to make them take effect.

```
[INDEX FILES]
## must be "true" to enable search
enabled = true

## The interval the search index is updated. Can be s(seconds), m(minutes), h(hours), d(days)
interval=10m

## If true, indexes the contents of office/pdf files while updating search index
## Note: If you change this option from "false" to "true", then you need to clear the search index and update the index again.
index_office_pdf=false
```

## Enable full text search for Office/PDF files

Full text search is not enabled by default to save system resources. If you want to enable it, you need to follow the instructions below.

First you have to set the value of `index_office_pdf` option in `seafevents.conf` to `true`.

Then restart seafile server

```
  cd /data/haiwen/seafile-pro-server-1.7.0/
  ./seafile.sh restart
```

You need to delete the existing search index and recreate it.

```
  ./pro/pro.py search --clear
  ./pro/pro.py search --update
```

## Use existing ElasticSearch server

The search module uses an Elasticsearch server bundled with the Seafile Professional Server. However, you may have an existing Elasticsearch server or cluster running in your company. In this situation, you can change the config file to use your existing ES server or cluster.

This feature was added in Seafile Professional Server 2.0.5.


### Modify the config file

- Edit `seafevents.conf`, add settings in the section **[INDEX FILES]** to specify your ES server host and port:

```
[INDEX FILES]
...
external_es_server = true
es_host = 192.168.1.101
es_port = 9200
```

- `external_es_server`: set to `true` so seafile would not start its own elasticsearch server
- `es_host`: The ip address of your ES server
- `es_port`: The listening port of ES server RESTful API. By default it should be `9200`

## <a id="wiki-faq"></a>Common problems

### <a id="how-to-rebuild-search-index"></a>How to rebuild the index if something went wrong

You can rebuild search index by running:

```
./pro/pro.py search --clear
./pro/pro.py search --update
```

If this does not work, you can try the following steps:

1. Stop Seafile
2. Remove the old search index `rm -rf pro-data/search`
3. Restart Seafile
4. Wait one minute then run `./pro/pro.py search --update`


### <a id="wiki-search-no-result"></a>I get no result when I search a keyword

The search index is updated every 10 minutes by default. So before the first index update is performed, you get nothing no matter what you search.

  To be able to search immediately,

  - Make sure you have started Seafile Server
  - Update the search index manually:

```
cd haiwen/seafile-pro-server-2.0.4
./pro/pro.py search --update
```

### <a id="wiki-cannot-search-encrypted-files"></a>Encrypted files cannot be searched

This is because the server cannot index encrypted files, since they are encrypted.

### <a id="how-to-increase-search-process-memory"></a>Increase the heap size for the java search process

The search functionality is based on elasticsearch, which is a java process. To increase the java heap size, you can use the `ES_HEAP_SIZE` environment variable, e.g.:

```sh
export ES_HEAP_SIZE=4g # default is 1g
./seafile.sh restart
```
