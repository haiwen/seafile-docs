# FAQ
## <a id="wiki-search-faq"></a>FAQ about Search ##

- Q: However I tried, files in an encrypted library aren't listed in the search results

  A: This is because the server can't index encrypted files, since, they are encrypted.

- Q: I switched to Professional Server from Community Server, but whatever I search, I get no results

  A: The search index is updated every 10 minutes by default. So before the first index update is performed, you get nothing no matter what you search.

  To be able to search immediately,

  - Make sure you have started seafile server
  - Update the search index manually:
  ```
  cd haiwen/seafile-pro-server-1.7.0
  ./pro/pro.py search --update
  ```

  If you have lots of files, this process may take quite a while.

- Q: I want to enable full text search for office/pdf documents, so I set `index_office_pdf` to `true` in the configuration file, but it doesn't work.

  A: In this case, you need to:
  1. Edit the value of `index_office_pdf` option in `seafevents.conf` to `true`
  2. Restart seafile server
  ```
  cd /data/haiwen/seafile-pro-server-1.7.0/
  ./seafile.sh restart
  ```
  3. Delete the existing search index
  ```
  ./pro/pro.py search --clear
  ```
  4. Create and update the search index again
  ```
  ./pro/pro.py search --update
  ```


## <a id="wiki-office-preview-faq"></a>FAQ about libreoffice-based office documents preview ##

- Q: The browser displays "document conversion failed", and in the logs I see messages like `[WARNING] failed to convert xxx to ...`, what should I do?

  A: Sometimes the libreoffice process need to be restarted, especially if it's the first time seafile server is running on the server.

  Try to kill the libreoffice process:
  ```sh
  pkill -f soffice.bin
  ```
  Now try re-opening the preview page in the brower again.

  Also if you are deploying seafile in cluster mode, make sure memcached is working on each server.

- Q: The above solution does not solve my problem.

  A: Please check whether the user you run Seafile can correctly start the libreoffice process. There may be permission problems.
