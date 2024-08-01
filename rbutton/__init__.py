import os
import streamlit.components.v1 as components
from typing import Dict
import json

_USE_WEB_DEV_SERVER = True

if _USE_WEB_DEV_SERVER:
    _component_func = components.declare_component(
        "button", url="http://localhost:5173"
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "rbutton/web/dist")
    _component_func = components.declare_component("button", path=build_dir)


def rbutton_events(fig: Dict[str, str]):
    spec = json.dumps(fig)
    component_value = _component_func(spec=spec, default=None)
    return component_value