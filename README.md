# bcfm_db_flaskapi

# Docker 

# Build base image :

    Docker image build -t ahmetucan/mysqldb_flask_api  .

 Build image from base image :

    Docker image build -t ahmetucan/mysql-flask-api  .
    
# Run a Container:

    Dockercontainer run -p 80:5000 ahmetucan/mysql-flask-api

# Push an Image:
    Docker push ahmetucan/mysqldb_flask_api
    
    Docker push ahmetucan/mysql-flask-api
