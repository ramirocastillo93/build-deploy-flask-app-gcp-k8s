export FLASK_IMAGE_NAME=flask-api
export GCP_PROJECT_NAME=developing-stuff 
export FLASK_IMAGE_TAG=v0.0.1

docker build --platform=linux/amd64 -t $FLASK_IMAGE_NAME .
docker tag $FLASK_IMAGE_NAME gcr.io/$GCP_PROJECT_NAME/$FLASK_IMAGE_NAME:$FLASK_IMAGE_TAG
docker push gcr.io/$PROJECT_ID/$FLASK_IMAGE_NAME:$FLASK_IMAGE_TAG