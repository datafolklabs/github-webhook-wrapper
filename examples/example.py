#!/usr/bin/env python

import os
import sys
import json
from tempfile import mkstemp

payload = json.loads(sys.argv[0])
tmpfile = mkstemp()

### Do something with the payload
if payload['repository']['name'] == 'my-repo':
    f = open(os.path.join(tmpfile, 'my-repo.commit', 'w')
    f.write(json.dumps(payload))
    f.close()