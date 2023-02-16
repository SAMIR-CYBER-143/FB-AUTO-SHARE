import os, sys
try:
    __import__("share2").rmx_share()
except Exception as e:
    exit(str(e))
