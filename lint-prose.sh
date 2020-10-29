#!/usr/bin/env bash

set -o errexit -o noclobber -o nounset

directory="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

ci_alert_level=""

if [ -n "${CI+x}" ]; then
    ci_alert_level="--minAlertLevel=error"
fi

vale --config "${directory}/.vale.ini" ${ci_alert_level} "${directory}/source/"
