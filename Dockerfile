# Docker crash course: https://www.youtube.com/watch?v=XQNv0SRB0OM
# Docker images with github acitons for ci: https://www.youtube.com/watch?v=x7f9x30W_dI

FROM python:3.13-slim-bookworm

SHELL ["/bin/bash", "-c"] 

WORKDIR /

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

RUN uv sync --locked

COPY . .

EXPOSE 5000

ENV DEBUG=False
ENV PORT=5000
ENV LOG_FILE=/data/logs/logs.txt

CMD ["uv", "python", "main.py"]