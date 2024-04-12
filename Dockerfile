FROM ubuntu:20.04
RUN apt-get update && apt-get install -y \
    python3.8 \
    python \
    python3-pip

RUN pip install django
COPY . .
ENTRYPOINT ["bash","execute_commands.sh"]