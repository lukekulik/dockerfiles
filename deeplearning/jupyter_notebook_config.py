import os
from IPython.lib import passwd

c = get_config()

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False
c.MultiKernelManager.default_kernel_name = 'python3'
# Password to use for web authentication
c.NotebookApp.password = u'sha1:95672cd645aa:73778711ea91d19230826efd2644f6e0f0cb466e'
# The full path to an SSL/TLS certificate file.
c.NotebookApp.certfile = u'/etc/ssl/cert.pem'
# The full path to a private key file for usage with SSL/TLS.
c.NotebookApp.keyfile = u'/etc/ssl/key.pem'

_default_scrub = False
_default_save_script = False

_save_script = _default_save_script
_script_exporter = None

def scrub_output_hook(model, path, contents_manager, **kwargs):
    """scrub output before saving notebooks"""

    # only run on notebooks
    if model['type'] != 'notebook':
        return
    # only run on nbformat v4
    if model['content']['nbformat'] != 4:
        return

    # Check for user-specified options for scrubbing and script saving. Example:
    # -*- scrub-output: false; save-script: True -*-
    scrub = _default_scrub
    global _save_script
    _save_script = _default_save_script
    for cell in model['content']['cells']:
        for line in cell['source'].split('\n'):
            if line.count('-*-') == 2:
                line = line.split('-*-')[1].strip()
                for item in line.split(';'):
                    key, value = [s.strip() for s in item.split(':')]
                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    else:
                        contents_manager.log.warn(
                            'Unknown value for option {!r}: {!r}'.format(key, value))
                    if key == 'scrub-output':
                        scrub = value
                    elif key == 'save-script':
                        _save_script = value
                    else:
                        contents_manager.log.warn(
                            'Unknown option in "-*-" config: {!r}'.format(key))

    if not scrub:
        return

    for cell in model['content']['cells']:
        if cell['cell_type'] != 'code':
            continue
        cell['outputs'] = []
        cell['execution_count'] = None

c.FileContentsManager.pre_save_hook = scrub_output_hook

def save_script_hook(model, os_path, contents_manager, **kwargs):
    """convert notebooks to Python script after save with nbconvert

    replaces `ipython notebook --script`
    """
    from nbconvert.exporters.script import ScriptExporter

    if model['type'] != 'notebook':
        return

    if not _save_script:
        return

    global _script_exporter

    if _script_exporter is None:
        _script_exporter = ScriptExporter(parent=contents_manager)

    log = contents_manager.log

    base, ext = os.path.splitext(os_path)
    py_fname = base + '.py'
    script, resources = _script_exporter.from_filename(os_path)
    script_fname = base + resources.get('output_extension', '.txt')
    log.info("Saving script /%s", to_api_path(script_fname, contents_manager.root_dir))

    with io.open(script_fname, 'w', encoding='utf-8') as f:
        f.write(script)

c.FileContentsManager.post_save_hook = save_script_hook
