FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl gnupg2 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EB3E94ADBE1229CF && apt-get update && apt-get install -y unixodbc-dev libgssapi-krb5-2
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18 && ACCEPT_EULA=Y apt-get install -y mssql-tools18
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc && source ~/.bashrc && 
