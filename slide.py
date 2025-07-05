import argparse
from modules import xss, sqli, cmdi
from utils import encoder, obfuscator
import json
import pyperclip


def print_banner():
    banner = r'''
   _____ _     ___ ____  _____  
  / ____| |   |_ _|  _ \| ____|
 | (___ | |    | || | | | |___
  \___ \| |___ | || |_| | |___
  |____/|_|___|___|____/|_____|


Modular Payload Generation Tool
    '''

    description = """
    Develop a modular payload generation tool capable of producing evasion-ready payloads for:
      - Cross-Site Scripting (XSS)
      - SQL Injection (SQLi)
      - Command Injection (CMDi)

    Features:
      - Bypass input validation
      - Evade Web Application Firewalls (WAFs)
      - Circumvent blacklist filters
      - Encode the Generated Payloads
      - Easy integration and customization
    """
    print(banner)
    print(description)


def main():
    parser = argparse.ArgumentParser(description="Modular Payload Generator Tool for XSS, SQLi, and CMDi")
    parser.add_argument('--xss', choices=["reflected", "stored", "dom","evasion","all",], help="Generate XSS Payloads")
    parser.add_argument('--sqli', choices=['error', 'union', 'blind','all'], help='Type of SQL injection payload to generate')
    parser.add_argument('--cmdi', choices=['linux','windows','all'])
    parser.add_argument('--encode', choices=['base64', 'url', 'hex', 'unicode'])
    parser.add_argument('--obfuscate', action='store_true')
    parser.add_argument('--output', choices=['cli', 'json', 'clipboard'], default='cli')
    parser.add_argument('--appendfile', action='store_true', help="Append payloads to 'output.txt'")

    args = parser.parse_args()
    payloads = []


    if args.xss: 
        print("XSS Payloads:\n")
        xss_gen = xss.XSSPayloadGenerator()
        xss_payloads = xss_gen.generate(args.xss, args.encode, args.obfuscate)
        payloads += xss_payloads

        if args.appendfile:
            with open('xss_payload.txt','a') as f:
                for p in payloads:
                    f.write(p + '\n')

    if args.sqli:
        print("SQLI Payloads:\n") 
        sqli_gen = sqli.SQLiPayloadGenerator()
        sqli_payloads = sqli_gen.generate(args.sqli, args.encode, args.obfuscate)
        payloads += sqli_payloads

        if args.appendfile:
            with open('sqli_payload.txt','a') as f:
                for p in payloads:
                    f.write(p + '\n')
    if args.cmdi: 
        print("CMDI Payloads:\n")
        cmdi_gen = cmdi.OSCmdPayloadGenerator()
        cmdi_payloads = cmdi_gen.generate(args.cmdi, args.encode, args.obfuscate)
        payloads += cmdi_payloads

        if args.appendfile:
            with open('cmdi_payload.txt','a') as f:
                for p in payloads:
                    f.write(p + '\n')



    if args.output == 'cli':
        for p in payloads:
            print(p)
    elif args.output == 'json':
        print(json.dumps(payloads, indent=2))
    elif args.output == 'clipboard':
        pyperclip.copy('\n'.join(payloads))
        print("=> Payloads copied to clipboard.")

if __name__ == "__main__":
    print_banner()
    main()
