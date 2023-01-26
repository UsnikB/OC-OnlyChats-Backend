# Video Chatting App

This is a Flask-based video chatting app that uses WebSockets to enable real-time communication.

## Deployment

To deploy the app, you will need to have Docker installed on your machine. Follow these steps:

1. Clone the repository:
git clone https://github.com/<your-username>/video-chat-app.git

2. Build the Docker image:
docker build -t video-chat-app .


3. Run the container:
docker run -p 5000:5000 video-chat-app


4. Open your browser and go to `http://localhost:5000` to access the app.

Note: If you are running on windows or mac you will have to use `http://<docker-machine-ip>:5000` to access the app.

## Additional Note

* Make sure you have the correct version of python specified in your `Dockerfile` as well as in your `requirement.txt` file.

* You can also use the `docker-compose` to deploy the app which is easier and more efficient.

* If you want to run the app in the background you can use the `-d` flag in the `docker run` command.

* If you want to see the logs of your container you can use the `docker logs <container-id>` command.

* If you want to stop the container you can use the `docker stop <container-id>` command.

* This is a basic app and you can add more functionality to it.

* Feel free to reach out to me if you have any questions or issues.
