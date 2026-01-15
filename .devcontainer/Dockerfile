FROM mcr.microsoft.com/devcontainers/python:3.13

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    zip \
    jq \
    tar \
    git \
    libglib2.0-0 \
    fonts-ipafont-gothic \
    && rm -rf /var/lib/apt/lists/*

    # Install Google Chrome
RUN mkdir /usr/local/share/keyrings \
    && curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/local/share/keyrings/chrome-archive-keyring.gpg \
    && echo "deb [signed-by=/usr/local/share/keyrings/chrome-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm /usr/local/share/keyrings/chrome-archive-keyring.gpg \
    && rm /etc/apt/sources.list.d/chrome.list

    # Install ChromeDriver
RUN LATEST_VERSION=$(wget -qO- https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json | jq -r '.channels.Stable.version') \
    && DOWNLOAD_URL=$(wget -qO- https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json | jq -r '.channels.Stable.downloads.chromedriver[] | select(.platform == "linux64").url') \
    && wget -O /tmp/chromedriver.zip $DOWNLOAD_URL \
    && unzip /tmp/chromedriver.zip -d /tmp/ \
    && rm /tmp/chromedriver.zip \
    && mv /tmp/chromedriver-linux64/chromedriver /opt/chromedriver \
    && rm -rf /tmp/chromedriver-linux64 \
    && chmod +x /opt/chromedriver

# Install Python packages
RUN pip install --upgrade pip && \
    pip install rope \
        flake8 \
        autopep8 \
        freezegun \
        pytest \
        pandas \
        boto3

# Install AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN rm awscliv2.zip
RUN ./aws/install

ENV PYTHONPATH="$PYTHONPATH:/workspace"