FROM python:3.11-slim

WORKDIR /app

RUN pip install sigma-cli && \
    sigma plugin install elasticsearch

COPY convert_all.sh .
RUN chmod +x convert_all.sh

ENTRYPOINT ["./convert_all.sh"]
