GitHub Webhook Wrapper
======================

The GitHub Webhook Wrapper allows one to maintain a single endpoint (web
URL) for all GitHub web hooks, as defined here:

 * https://help.github.com/articles/post-receive-hooks
 
The endpoint is a simple Python CGI script which parses the `payload` from 
the GitHub WebHook, and launches local scripts (if they exist) in the 
following order:

 * scripts/repo
 * scripts/repo-branch
 * scripts/all
 

For example, if your repo were named 'my-awesome-repo' and you committed data
to the 'master' branch, the following scripts would be executed (again, only 
if they exist):

 * scripts/my-awesome-repo
 * scripts/my-awesome-repo-master
 * scripts/all
 

Note that the 'all' script will be called for every commit, to any repo, and
any branch.


Installation and Setup
----------------------

First clone the repository:

```
$ git clone https://github.com/datafolklabs/github-webhook-wrapper.git
```


Create a script:

```

$ touch github-webhook-wrapper/scripts/my-repo

$ chmod +x github-webhook-wrapper/scripts/my-repo

```

Note that the script can be any scripting language you prefer, however it 
*must* have a #!shebang line at the top of the file, and must be executable
by the web server (i.e. www-root, apache, etc).

See the `examples` directory for usage help.

Configuring Apache
------------------

It is not required to use Apache, you simply need to configure whatever web
server to honor '.cgi' scripts.  The following is an example config, note that
we obscure the location by adding an MD5 sum to the Alias.  This is not
necessary, but will help prevent anyone randomly accessing your hook URL.  
You may consider adding HTTP Basic Authentication, SSL, and adding auth creds 
to the URL also, however that is beyond the scope of this example.

```
AddHandler cgi-script .cgi
Alias /5972d04b6930419baf200bcfab8ca71f /path/to/github-webhook-wrapper
```

And restart Apache. In this example, your URL endpoint would be:

```
http://example.com/5972d04b6930419baf200bcfab8ca71f/hook.cgi
```

Accessing The Payload Data
--------------------------

The entire `payload` is passed as a single JSON string argument to every
script.  The payload structure is outlined here:

 * https://help.github.com/articles/post-receive-hooks
