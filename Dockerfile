FROM python:3.7-alpine

RUN apk add --update alpine-sdk \
                     linux-headers \
                     pcre-dev \
                     postgresql-dev

# -h DIR          Home directory
# -D              Do not assign a password
RUN adduser -D -h /app app
USER app
ENV PATH=/app/.local/bin:$PATH

WORKDIR /app

RUN pip install --user uWSGI==2.0.18

COPY . .

RUN pip install --user -r requirements.txt

EXPOSE 8000

CMD ["uwsgi", "--ini", "uwsgi.ini"]

