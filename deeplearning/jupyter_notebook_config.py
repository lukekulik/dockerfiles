import os
from IPython.lib import passwd

c = get_config()

c.NotebookApp.ip = '*'
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False
c.MultiKernelManager.default_kernel_name = 'python3'
# Password to use for web authentication
c.NotebookApp.password = u'sha1:95672cd645aa:73778711ea91d19230826efd2644f6e0f0cb466e'
# The full path to an SSL/TLS certificate file.
c.NotebookApp.certfile = u'/mycert.crt'
# The full path to a private key file for usage with SSL/TLS.
c.NotebookApp.keyfile = u'/mycert.key'
