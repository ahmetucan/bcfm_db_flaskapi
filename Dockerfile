FROM ahmetucan/mysqldb_flask_api:base-image
WORKDIR /app
COPY . .
EXPOSE 5000
ENTRYPOINT ["python3", "odev.py"]