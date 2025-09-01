FROM kong:3.6.0

WORKDIR /usr/local/kong

COPY kong.yml /usr/local/kong/kong.yml

EXPOSE 8000 8443 8001

CMD ["kong", "start", "-c", "/usr/local/kong/kong.yml"]
