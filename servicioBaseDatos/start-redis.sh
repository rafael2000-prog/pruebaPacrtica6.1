#!/bin/sh
set -e

if [ -z "$REDIS_PASSWORD" ]; then
  echo "ERROR: REDIS_PASSWORD environment variable is required"
  exit 1
fi

mkdir -p /data
chown redis:redis /data || true

exec redis-server --appendonly yes --appendfilename appendonly.aof --dir /data --requirepass "$REDIS_PASSWORD" --bind 0.0.0.0
