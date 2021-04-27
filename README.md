# bcfm_db_flaskapi

# Docker 

# Build base image :

    Docker image build -f Dockerfile.base -t ahmetucan/flask_api:base-image  .

 Build image from base image :

    Docker image build -t ahmetucan/flask_api_con  .
    
# Run a Container:

    Dockercontainer run -p 80:5000 ahmetucan/flask_api_con

# Push an Image:
    Docker push ahmetucan/flask_api:base-image
    
    Docker push ahmetucan/flask_api_con
