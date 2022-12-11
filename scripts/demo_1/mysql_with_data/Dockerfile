FROM mysql

EXPOSE 3306 33060

WORKDIR /

ADD create_table.sql .
ADD load_data_into_db.sh .

RUN chmod 700 /load_data_into_db.sh

CMD ["mysqld"]
