FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf

ARG ENV
COPY nginx_${ENV}.conf /etc/nginx/conf.d

