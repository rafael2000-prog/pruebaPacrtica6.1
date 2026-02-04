FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends redis-server ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY start-redis.sh /usr/local/bin/start-redis.sh
RUN chmod +x /usr/local/bin/start-redis.sh

VOLUME ["/data"]
EXPOSE 6379
CMD ["/usr/local/bin/start-redis.sh"]
