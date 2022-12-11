#!/bin/bash
base_url='https://tassidicambio.bancaditalia.it/terzevalute-wf-web/rest/v1.0'
base_file_path='/var/lib/mysql-files'

function getParams() {
  y=$1
  m=$2
  echo "year=$y&month=$m&currencyIsoCode=EUR"
}
function getDataFromBDI() {
  for Y in {2021..2022}
  do
    for M in {1..12}
    do
      curl -H "Content-Type: application/json" $base_url/monthlyAverageRates?$(getParams $Y $M) > "${base_file_path}/data/avg_rates_${Y}_${M}.csv" &2>/dev/null
    done
  done
}

function generateLoadSql() {
  for Y in {2021..2022}
  do
    for M in {1..12}
    do
      echo "START TRANSACTION;"
      echo "LOAD DATA INFILE '${base_file_path}/data/avg_rates_${Y}_${M}.csv'"  >> "${base_file_path}/loadData.sql"
      echo "INTO TABLE avg_rates FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES"  >> "${base_file_path}/loadData.sql"
      echo "(@col1, @col2, @col3, @col4, @col5, @col6, @col7, @col8) SET "  >> "${base_file_path}/loadData.sql"
      echo " Paese=@col1, Valuta=@col2, ~CodiceISO~=@col3, ~CodiceUIC~=@col4, ~Quotazionemedia~=@col5, ~Convenzionedicambio~=@col6, Anno=@col7 , Mese=@col8;"| sed -e 's/~/`/g' >> "${base_file_path}/loadData.sql"
      echo "COMMIT;"
    done
  done
}

echo "Creating table"
mysql --password=lejwelfkjhFjkhwefkjwejwF be_db < /create_table.sql

echo "Get data from Banca D'Italia"
mkdir "${base_file_path}/data"
$(getDataFromBDI)

echo "Generate db scripts"
echo "USE be_db;" > "${base_file_path}/loadData.sql"
$(generateLoadSql)
echo "Load db data"
mysql --password=lejwelfkjhFjkhwefkjwejwF be_db < "${base_file_path}/loadData.sql"

mysqld