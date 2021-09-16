FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

# Update repository listings and upgrade packages
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Install Python 3
RUN apt-get -qq -y install python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Install tesseract and other tools
RUN apt-get -qq -y install \
    wget \
    curl \
    git \
    make \
    sudo \
    software-properties-common \
    tesseract-ocr-eng \
    poppler-utils \
    graphviz \
    libgraphviz-dev 

# Install jupyter and jupyterlab
RUN pip install jupyter -U && pip install jupyterlab

# Install python dependencies
RUN pip install numpy \
    beautifulsoup4 \
    matplotlib \
    pandas \
    scikit-learn \
    scipy \
    pytesseract \
    requests \
    regex \
    imdbpy \
    networkx \
    pygraphviz \
    opencv-python \
    seaborn

# Create user "docker" with sudo powers. 
# WARNING: THIS MAY POSE A SERIOUS SECURITY RISK!
# DO NOT USE THIS ON A SERVER WITH SENSITIVE DATA 
# AND RESEARCH HOW TO "DEPRIVILEGE" THE USER CORRECTLY.

RUN useradd -m docker && \
    usermod -aG sudo docker && \
    echo '%sudo ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \
    cp /root/.bashrc /home/docker/ && \
    mkdir /home/docker/data && \
    chown -R --from=root docker /home/docker

# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Create working directory
WORKDIR /home/docker/data
ENV HOME /home/docker
ENV USER docker
USER docker
ENV PATH /home/docker/.local/bin:$PATH
# Avoid first use of sudo warning. c.f. https://askubuntu.com/a/22614/781671
RUN touch $HOME/.sudo_as_admin_successful

# Expose the port for communication and start jupyterlab
EXPOSE 8888
ENTRYPOINT ["jupyter", "lab","--no-browser","--ip=0.0.0.0","--NotebookApp.token='data-science'"]