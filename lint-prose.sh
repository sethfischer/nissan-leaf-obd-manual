#!/usr/bin/env bash

set -o errexit -o noclobber -o nounset

directory="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

vale --config "${directory}/.vale.ini" "${directory}/source/"
