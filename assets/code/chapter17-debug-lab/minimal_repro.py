"""No environment, network or files: isolate the text conversion mistake."""
raw_debug = "false"
print(repr(raw_debug), bool(raw_debug), raw_debug == "true")
