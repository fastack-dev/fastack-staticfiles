from typing import List, Tuple
from fastack import Fastack
from fastapi.staticfiles import StaticFiles

def setup(app: Fastack):
    staticfiles: List[Tuple] = app.get_setting("STATICFILES", [])
    try:
        for path, name, options in staticfiles:
            static_endpoint = StaticFiles(**options)
            app.mount(path, static_endpoint, name)

    except ValueError as e:
        if "not enough values to unpack" in e.args[0]:
            raise RuntimeError("Make sure your static file configuration is correct like this [(path, name, {options: value})]")
