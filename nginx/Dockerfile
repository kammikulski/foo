FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY certs/ /etc/ssl/certs/
RUN mkdir -p /data/nginx/cache

CMD ["nginx","-g", "daemon off;"]

