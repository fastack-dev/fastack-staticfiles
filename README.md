# fastack-staticfiles

Easy to add static files

# Usage

```
pip install fastack-staticfiles
```

Add the plugin to your project configuration

```py
PLUGINS = [
    "fastack_staticfiles",
    ...
]
```

Plugin configuration example

```py
STATICFILES = [
    (
        "/static",
        "static",
        {"directory": "assets", "packages": [], "html": False, "check_dir": True},
    )
]
```

Configuration format like this `(path: str, name: str, options: dict)`
The options here will be passed to `starlette.staticfiles.StaticFiles`.
