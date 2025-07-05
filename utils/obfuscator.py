import re
import random
import binascii

def hex_encode_string(s):
    return ''.join(f"\\x{ord(c):02x}" for c in s)

def obfuscate(payload):
    keywords = ['select', 'union', 'from', 'where', 'and', 'or', 'insert', 'update', 'delete', 'join', 'user', 'version']
    whitespace_chars = ['\t', '\n', '\r', '\x0b', '\x0c', '/**/']

    for kw in keywords:
        mixed = ''.join(c.upper() if random.choice([True, False]) else c.lower() for c in kw)
        payload = re.sub(r'\b' + kw + r'\b', mixed, payload, flags=re.IGNORECASE)

    payload = re.sub(r'\s+', lambda m: f"/**/{' ' if random.random() > 0.5 else ''}", payload)

    payload = payload.replace("=1", "LIKE 1") if "1" in payload else payload

    for _ in range(random.randint(1, 3)):
        payload = payload.replace(' ', random.choice(whitespace_chars), 1)

    if random.random() > 0.2:
        payload = payload.replace("alert", hex_encode_string("alert"))

    if random.random() > 0.5:
        payload += random.choice(["--", "#", "/*abc*/"])


    return payload
