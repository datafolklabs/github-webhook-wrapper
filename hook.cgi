#!/usr/bin/env python
print "Content-Type: text/html"
print

import os
import cgi
import json

form = cgi.FieldStorage()
payload = json.loads(form.getvalue('payload'))

script_dir = os.path.join(os.curdir, 'scripts')
repo = payload['repository']['name']
branch = payload['ref'].split('/')[2]

# Run all scripts that exist for either repo, repo-branch, or all
if os.path.exists(os.path.join(script_dir, repo)):
    os.system(os.path.join(script_dir, repo))

if os.path.exists(os.path.join(script_dir, "%s-%s" % (repo, branch))):
    os.system(os.path.join(script_dir, "%s-%s" % (repo, branch)))
  
if os.path.exists(os.path.join(script_dir, 'all'):
    os.system(os.path.join(script_dir, "all"))