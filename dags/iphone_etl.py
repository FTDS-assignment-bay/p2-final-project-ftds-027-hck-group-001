from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.models import Variable
import pandas as pd
import psycopg2 as pg

default_args= {
    'owner': 'Dwi',
    'start_date': datetime(2025, 6, 17),
}

with DAG(
    'Final_Project',
    description='from postgres to clean data',
    schedule_interval='10-30/10 9 * * 6',
    default_args=default_args, 
    catchup=False) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    @task()
    def preprocess_data():
        # Method ini digunakan untuk cleaning data mentah yang diambil dari table_m3

        df = pd.read_csv('/opt/airflow/data/iphone_extract.csv')
        
        # Remove missing value if any
        df = df.dropna()
        
        # Remove duplicates if any
        df = df.drop_duplicates()
        
        # column productVariant
        # list jenis warna, size storage, nama provider, dan id untuk iphone 13, 14, 15
        colors_list = ['blue', 'starlight', 'purple', 'midnight', 'red', 'yellow', 'pink', 'green','black']
        size_list = [128, 256, 512]
        provider_list = ['Verizon', 'Unlocked', 'AT&T', 'T-Mobile', 'GSM Carriers']
        iphone_13 = ['B09P82T3PZ','B09G9J5JZX','B09G9D8KRQ','B09G9BL5CP']
        iphone_14 = ['B0BDK8LKPJ','B0BN72MLT2']
        iphone_15 = ['B0CHX1W1XY']

        clean_texts = []
        for variant, asin in zip(df['variant'], df['product_asin']):
            variant_lower = variant.lower()
            colour = None
            size = None
            provider = None
            model = None

            # pengecekan jenis Iphone 13, 14 atau 15 bedasarkan id di productAsin
            if asin in iphone_13:
                model = '13'
            elif asin in iphone_14:
                model = '14'
            elif asin in iphone_15:
                model = '15'
            else:
                model = 'Unknown'
            # pengecekan jenis warna Iphone
            for c in colors_list:
                if c in variant_lower:
                    colour = c.capitalize()
                    break
            # pengecekan size storage Iphone
            for s in size_list:
                if str(s) in variant_lower:
                    size = s
                    break
            # pengecekan jenis provider Iphone
            for p in provider_list:
                if p.lower() in variant_lower:
                    provider = p
                    break
            if provider:
                clean_text = f'Apple Iphone {model} ({size} GB) - {colour} for {provider}'
            else:
                clean_text = f'Apple Iphone {model} ({size} GB) - {colour}'
            clean_texts.append(clean_text)

        df['product_variant'] = clean_texts     

        df['product_type'] = df['product_variant'].str.slice(0,16)

        df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce').dt.date
        
        df.drop(columns=['parsed_date'], errors='ignore')

        print("Preprocessed data is Success")
        print(df.head())
        df.to_csv('/opt/airflow/data/iphone_clean.csv', index=False)

    @task()
    def fetch_from_postgre():
        # Method ini digunakan untuk mengambil data dari database dan membuat csv baru.
        database = "final_project"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

        engine = create_engine(postgres_url)
        conn = engine.connect()
        # ganti isi table_m3 dengan data dari kaggle 
        df = pd.read_sql('select * from raw_data_iphone',conn)
        df.to_csv('/opt/airflow/data/iphone_extract.csv',index=False)
        print("Success FETCH")

    @task()
    def load_to_postgre():
        pgConn = pg.connect(
        dbname="final_project",
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432"
     )
        cur = pgConn.cursor()
        cur.execute(
        '''
            CREATE TABLE IF NOT EXISTS iphone_clean (
            review_id SERIAL PRIMARY KEY,
            product_asin VARCHAR(20),
            country VARCHAR(20),
            date DATE,
            is_verified BOOLEAN,
            rating_score INTEGER,
            review_title TEXT,
            review_description TEXT,
            review_url TEXT,
            reviewed_in TEXT,
            variant TEXT,
            variant_asin VARCHAR(15),
            product_variant TEXT,
            product_type VARCHAR(15)
            );
        '''
        )
        df = pd.read_csv('/opt/airflow/data/iphone_clean.csv')
        for row in df.to_dict(orient='reconds'):
            cur.execute(
                '''
                INSERT INTO iphone_clean (
                product_asin, country, date, is_verified, rating_score, 
                review_title, review_description, review_url, reviewed_in, 
                variant, variant_asin, product_variant, product_type
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''',
                (
                    row['product_asin'],
                    row['country'],
                    row['date'],
                    row['is_verified'],
                    row['rating_score'],
                    row['review_title'],
                    row['review_description'],
                    row['review_url'],
                    row['reviewed_in'],
                    row['variant'],
                    row['variant_asin'],
                    row['product_variant'],
                    row['product_type']
                )
            )
        pgConn.commit()
        cur.close()
        pgConn.close()
            
    start >> fetch_from_postgre() >> preprocess_data() >> load_to_postgre() >> end