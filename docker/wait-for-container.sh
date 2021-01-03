#!/bin/bash

set -e

host="$1"
shift
cmd=("$@")

sleep 45

>&2 echo "$host container is finished...starting container"
exec "${cmd[@]}"
