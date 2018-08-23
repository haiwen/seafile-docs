# Configurable Options

**Note**: Since Seafile Server 5.0.0, all config files have been moved to the central **conf** folder. [Read More](../deploy/new_directory_layout_5_0_0.md).

In the file `seafevents.conf`:

```
[AUDIT]
## Audit log is disabled default.
## Leads to additional SQL tables being filled up, make sure your SQL server is able to handle it.
enabled = true

[STATISTICS]
## must be "true" to enable statistics
enabled = false

[INDEX FILES]
## must be "true" to enable search
enabled = true

## The interval the search index is updated. Can be s(seconds), m(minutes), h(hours), d(days)
interval=10m

## From Seafile 6.3.0 pro, in order to speed up the full-text search speed, you should setup
highlight = fvh

## If true, indexes the contents of office/pdf files while updating search index
## Note: If you change this option from "false" to "true", then you need to clear the search index and update the index again.
## Refer to file search manual for details.
index_office_pdf=false

## The default size limit for doc, docx, ppt, pptx, xls, xlsx and pdf files. Files larger than this will not be indexed.
## Since version 6.2.0
## Unit: MB
office_file_size_limit = 10

[SEAHUB EMAIL]

## must be "true" to enable user email notifications when there are new unread notifications
enabled = true

## interval of sending Seahub email. Can be s(seconds), m(minutes), h(hours), d(days)
interval = 30m


[OFFICE CONVERTER]

## must be "true" to enable office/pdf online preview
enabled = true

## how many libreoffice worker processes should run concurrenlty
workers = 1

## where to store the converted office/pdf files. Deafult is /tmp/.
outputdir = /tmp/

## how many pages are allowed to be previewed online. Default is 50 pages
max-pages = 50

## the max size of documents allowed to be previewed online, in MB. Default is 2 MB
## Previewing a large file (for example >30M) online is likely going to freeze the browser.
max-size = 2

[EVENTS PUBLISH]
## must be "true" to enable publish events messages
enabled = false
## message format: repo-update\t{{repo_id}}}\t{{commit_id}}
## Currently only support redis message queue
mq_type = redis

[REDIS]
## redis use the 0 database and "repo_update" channel
server = 192.168.1.1
port = 6379
password = q!1w@#123
```

### <a id="wiki-options-you-may-want-to-modify"></a>Options you may want to modify

The section above listed all the options in `seafevents.conf`. Most of the time you can use the default settings. But you may want to modify some of them to fit your own use case.

We list them in the following table, as well as why we choose the default value.

<table>
<tr>
<th>section</th>
<th>option</th>
<th>default value</th>
<th>description</th>
</tr>

<tr>
<td>INDEX FILES</td>
<td>index_office_pdf</td>
<td>false</td>
<td>
The full text search of office/pdf documents is not enabled by default. This is because it may consume quite some storage for the search index. To turn it on, set this value to "true" and recreate the search index. See [File Search Details](details_about_file_search.md) for details.
</td>
</tr>

<tr>
<td>OFFICE CONVERTER</td>
<td>max-size</td>
<td>2</td>
<td>
The max file size allowed to be previewed online is 2MB. The preview is converted for office/pdf files as HTML and display it in the browser. If the file size is too large, the conversion could take too much time and consume many resources.
</td>
</tr>

<tr>
<td>OFFICE CONVERTER</td>
<td>max-pages</td>
<td>50</td>
<td>
When previewing an office/pdf document online, the pages displayed are the first 50 pages. If the value is too large, the conversion may take too much time and consume too many resources. Furthermore the browser can crash.
</td>
</tr>

</table>
