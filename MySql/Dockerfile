FROM mysql
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=receipts
COPY ./data /docker-entrypoint-initdb.d

EXPOSE 3306
