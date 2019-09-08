FROM python:3.7-alpine

RUN apk add --update alpine-sdk \
                     linux-headers \
                     pcre-dev

# -h DIR          Home directory
# -D              Do not assign a password
RUN adduser -D -h /app app
USER app
ENV PATH=/app/.local/bin:$PATH

WORKDIR /app

COPY . .

RUN pip install --user --no-cache-dir -r requirements.txt
RUN pip install --user --no-cache-dir uWSGI==2.0.18

EXPOSE 8000

CMD ["uwsgi", "--ini", "uwsgi.ini"]

