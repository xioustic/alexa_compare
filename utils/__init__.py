import json

def jsonPretty(obj, indent=2):
  """Return a "pretty-printed" JSON string from an object.

  Keyword arguments:
  indent -- number of spaces to indent (default 2)

  Per https://docs.python.org/2.7/library/json.html
  """
  return json.dumps(obj, sort_keys=True, indent=indent, separators=(',',':'))