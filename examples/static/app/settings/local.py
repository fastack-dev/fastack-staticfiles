DEBUG = True
PLUGINS = [
    "fastack_staticfiles"
]

COMMANDS = []
STATICFILES = [
    ("/static", "static", {
        "directory": "assets",
        "packages": [],
        "html": False,
        "check_dir": True
    })
]
