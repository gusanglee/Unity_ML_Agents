from typing import NamedTuple, Any, Dict, Optional
# By lee. 2020.12.31

class ActionInfo(NamedTuple):
    action: Any
    memory: Any
    text: Any
    value: Any
    outputs: Optional[Dict[str, Any]]
