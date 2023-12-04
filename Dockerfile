FROM registry.fedoraproject.org/fedora:latest
RUN dnf install -y python3-faker.noarch python3-pandas.x86_64
COPY app.py /opt/app.py
CMD ["python3", "/opt/app.py"]
