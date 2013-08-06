#!/usr/bin/env python
# Python Example for GitHub WebHook Wrapper

import os
import sys
import json
from tempfile import mkstemp

payload = json.loads(sys.argv[1])
_, tmpfile = mkstemp()

### Do something with the payload
if payload['repository']['name'] == 'my-repo-name':
    f = open(tmpfile, 'w')
    f.write(json.dumps(payload))
    f.close()