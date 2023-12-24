#!/bin/bash
py=${PY_EXEC:-"python"}
$py -m pip install selenium --quiet && curl https://raw.githubusercontent.com/hUwUtao/facoar/main/index.py -L -o.tmp.py && python .tmp.py && rm .tmp.py