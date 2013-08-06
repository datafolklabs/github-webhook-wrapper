#!/usr/bin/env python
print "Content-Type: text/html"
print

import os
import cgi
import json

form = cgi.FieldStorage()
json_payload = form.getvalue('payload')
payload = json.loads(json_payload)

script_dir = os.path.join(os.curdir, 'scripts')
repo = payload['repository']['name']
branch = payload['ref'].split('/')[2]

possible_scripts = [
    os.path.join(script_dir, repo), 
    os.path.join(script_dir, '%s-%s' % (repo, branch)),
    os.path.join(script_dir, "all"),
    ]
    
# Run all scripts that exist for either repo, repo-branch, or all
for script in possible_scripts:
    if os.path.exists(script):
        os.system('%s \"%s\"' % (script, json_payload)
