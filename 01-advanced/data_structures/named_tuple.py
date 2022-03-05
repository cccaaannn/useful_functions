from collections import namedtuple
from pprint import pprint

scientist = namedtuple("scientist", [
    "name",
    "field",
    "born",
    "nobel"
])

scientists = (
    scientist(name="can", field="computer", born="1997", nobel=False),
    scientist(name="not can", field="not computer", born="1997", nobel=False),
    scientist(name="person", field="physics", born="1951", nobel=True),
    scientist(name="another person", field="math", born="1951", nobel=True)
)


pprint(scientists)
