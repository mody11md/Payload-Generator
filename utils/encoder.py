import urllib.parse
import base64

def encode(payload, method):
    if method == 'base64':
        return base64.b64encode(payload.encode()).decode()
    elif method == 'url':
        return urllib.parse.quote(payload)
    elif method == 'hex':
        return ''.join(['\\x{:02x}'.format(ord(c)) for c in payload])
    elif method == 'unicode':
        return ''.join(['\\u{:04x}'.format(ord(c)) for c in payload])
    return payload