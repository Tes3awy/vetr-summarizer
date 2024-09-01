[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/Tes3awy/vetr-summarizer)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vetr-summarizer)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&labelColor=ef8336)](https://pycqa.github.io/isort/)
![PyPI - License](https://img.shields.io/pypi/l/vetr-summarizer)
![PyPI - Version](https://img.shields.io/pypi/v/vetr-summarizer)
![PyPI - Status](https://img.shields.io/pypi/status/vetr-summarizer)
![Pepy Total Downlods](https://img.shields.io/pepy/dt/vetr-summarizer)
![Commit Activity](https://img.shields.io/github/commit-activity/m/Tes3awy/vetr-summarizer/main?logo=github)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/Tes3awy)

## Table of Contents

1. [vetR Summarizer](#vetr-summarizer)
2. [Objective](#objective)
3. [Installation](#installation)
4. [Usage](#usage)

## vetR Summarizer

This tool summarizes data from any APIC collected by [vetr-collector](https://github.com/brightpuddle/vetr-collector).

## Objective

This tool processes data collected by [vetr-collector](https://github.com/brightpuddle/vetr-collector) for the ACI health check and displays it in a pretty HTML format. This tool can also be run from any computer having `aci-vetr-data` collected from any APIC.

The `aci-vetr-data` directory you get from `vetr-collector v3.3.0` includes **91** raw JSON files.

```bash
$ ls aci-vetr-data
apPlugin.json
bgpRRNodePEp.json
configRsRemotePath.json
coopPol.json
ctxClassCnt.json
datetimeNtpProv.json
datetimePol.json
epControlP.json
epIpAgingP.json
epLoopProtectP.json
...
<output_truncated>
```

_A sample preview of the output HTML_

![Preview](./assets/preview.jpg)

Almost all [MOs](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/policy-model-guide/b-Cisco-ACI-Policy-Model-Guide.html#id_107445__d54e1142) include unnecessary configuration properties. Some of these  properties: `extMngdBy`, `childAction`, `userdom`, etc. These unnecessary properties (key-value pairs) are excluded from the report for a neater representation of the output in the HTML file. _All excluded keys can be found in `config/excluded_keys` file._ You can also customize these keys-to-exclude according to your own case. _An empty excluded\_keys file will not exclude any keys_

> Raw JSON files with empty `imdata` and `totalCount` equal to `0` are not presented in the HTML `vetr-summary.html` summary report.

## Installation

> Install from PyPi

```bash
$ pip install --user vetr-summarizer
```

## Usage

> Both keyword arguments are optional. _Currently `html` is the only supported output format_.

```bash
$ vetr-summarizer --help
usage: vetr-summarizer [-h] [-f {html}] [-x EXCLUDE_FILE] [-v] directory  

Process and summarize aci-vetr-data JSON files into HTML reports.

positional arguments:
  directory             A path to the directory containing the JSON files.

options:
  -h, --help            show this help message and exit
  -f {html}, --format {html}
                        Output format (html).
  -x EXCLUDE_FILE, --exclude-file EXCLUDE_FILE
                        File containing keys to exclude from the summary HTML report.
  -v, --version         show program's version number and exit

Thanks for using vetr-summarizer! :)
```

```bash
$ vetr-summarizer "/path/to/aci-vetr-data"

HTML output is written to /path/to/vetr-summary.html
```

## Author

[Osama Abbas](https://www.linkedin.com/in/oabbas/)

## Contributions

As there is always a room for imporovment, you are welcome to contribute to `vetr-summarizer`.
