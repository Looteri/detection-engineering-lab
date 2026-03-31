FROM python:3.11-slim

WORKDIR /app

RUN pip install sigma-cli && \
    sigma plugin install elasticsearch

COPY tools/sigma-converter/convert_all.sh .
COPY detections/sigma /rules/sigma

RUN chmod +x convert_all.sh
RUN mkdir -p /rules/elastic

ENTRYPOINT ["./convert_all.sh"]
