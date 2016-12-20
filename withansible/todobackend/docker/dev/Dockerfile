FROM todobackend-base:latest

MAINTAINER Ivan Ka <tanzwud.work@gmail.com>

# Install dev/build dependencies
RUN apt-get upate && \
    apt-get install -qy python-dev

# Activate virtual environmnet and isntall wheel support
RUN . /appenv/bin/activate &&
    pip install wheel --upgrade

# PIP environmnet variables (NOTE: must be set after installing wheel)
ENV WHEELHOUSE=/whellhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# OUTPUT: Build artefacts (Wheels) are output here
VOLUME /wheelhouse

# OUTPUT: Test reports are output here
VOLUME /reports

# Add test entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set default for entrypoint and command string
ENTRYPOINT ["test.sh"]
CMD ["python", "manage.py", "test", "--noinput"]

# Add application source
COPY src /application
WORKDIR /application