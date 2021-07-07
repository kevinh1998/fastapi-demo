# Fastapi-demo
A fastapi demo

## Development guide

You can re-use the above container and simply mount your locally checked-out repository.

1. Build the containers.

    ```bash
    docker-compose up -d --build 
    ```

1. When that is done, enter the container with.

    ```bash
    docker-compose up
    ```

1. Get the name of the containers created.

    ```bash
    docker ps
    ```

1. Get into the container's shell.

    ```bash
    docker exec -it <container-name> bash
    ```

### Rebuilding the containers

1. To rebuild the containers run.

    ```bash
    docker-compose up --build
    ```