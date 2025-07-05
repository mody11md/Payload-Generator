from flask import Flask, render_template, request
from modules import xss, sqli, cmdi
from utils import encoder, obfuscator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    payloads = []

    if request.method == "POST":
        xss_type = request.form.get("xss")
        sqli_type = request.form.get("sqli")
        cmdi_os = request.form.get("cmdi")
        encode_type = request.form.get("encode")
        obfuscate_flag = request.form.get("obfuscate") == "on"
        append_file = request.form.get("appendfile") == "on"

        if xss_type and xss_type != "":
            xss_gen = xss.XSSPayloadGenerator()
            payloads += xss_gen.generate(xss_type, encode_type, obfuscate_flag)

        if sqli_type and sqli_type != "":
            sqli_gen = sqli.SQLiPayloadGenerator()
            payloads += sqli_gen.generate(sqli_type, encode_type, obfuscate_flag)

        if cmdi_os and cmdi_os != "":
            cmdi_gen = cmdi.OSCmdPayloadGenerator()
            payloads += cmdi_gen.generate(cmdi_os, encode_type, obfuscate_flag)

        if append_file:
            with open("output.txt", "a") as f:
                for p in payloads:
                    f.write(p + "\n")

    return render_template("index.html", payloads=payloads)

if __name__ == "__main__":
    app.run(debug=True)
