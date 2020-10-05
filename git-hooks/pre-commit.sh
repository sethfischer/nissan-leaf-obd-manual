#!/usr/bin/env bash

set -o errexit -o noclobber -o nounset

make linkcheck
make spelling
make lint-prose
