FROM apache/airflow:2.6.3
RUN python -m pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install tensorflow
RUN pip install keras
RUN pip install scikit-learn
