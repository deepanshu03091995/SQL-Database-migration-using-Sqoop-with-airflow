from datetime import datetime, timedelta

from airflow import DAG

from airflow.contrib.operators.ssh_operator import SSHOperator





default_args = {

    'owner': 'deepanshu',

    'start_date': datetime(2024,2,28),

    'retries': 5,

    'retry_delay': timedelta(minutes=5)

    # Add any other desired default arguments

}



#Defining the dags



dag = DAG('SQL-SQOOP-DATA-INGESTION-ETL-Final', default_args=default_args, schedule_interval='*/5 * * * * *')



#Defining the sqoop jobs



sqoop_command_categories='''sqoop job --exec sqoop_job_Categories'''

sqoop_command_cust_hist='''sqoop job --exec sqoop_job_Cust_hist'''

sqoop_command_customers='''sqoop job --exec sqoop_job_Customers '''

sqoop_command_inventories='''sqoop job --exec sqoop_job_Inventories '''

sqoop_command_orderlines='''sqoop job --exec sqoop_job_Orderlines'''

sqoop_command_orders='''sqoop job --exec sqoop_job_Orders '''

sqoop_command_products='''sqoop job --exec sqoop_job_Products '''







#Defining the Tasks



sqoop_import_1 = SSHOperator(

        task_id='sqoop_import_categories',

        ssh_conn_id='ssh_default',

        command=sqoop_command_categories,

        dag=dag

    )



sqoop_import_2 = SSHOperator(

        task_id='sqoop_import_cust_hist',

        ssh_conn_id='ssh_default',

        command=sqoop_command_cust_hist,

        dag=dag

    )





sqoop_import_3 = SSHOperator(

        task_id='sqoop_import_customers',

        ssh_conn_id='ssh_default',

        command=sqoop_command_customers,

        dag=dag

    )

sqoop_import_4 = SSHOperator(

        task_id='sqoop_import_inventories',

        ssh_conn_id='ssh_default',

        command=sqoop_command_inventories,

        dag=dag

    )

sqoop_import_5 = SSHOperator(

        task_id='sqoop_import_orderlines',

        ssh_conn_id='ssh_default',

        command=sqoop_command_orderlines,

        dag=dag

    )

sqoop_import_6 = SSHOperator(

        task_id='sqoop_import_orders',

        ssh_conn_id='ssh_default',

        command=sqoop_command_orders,

        dag=dag

    )

sqoop_import_7 = SSHOperator(

        task_id='sqoop_import_products',

        ssh_conn_id='ssh_default',

        command=sqoop_command_products,

        dag=dag

    )





sqoop_import_1 >> sqoop_import_2 >> sqoop_import_3 >> sqoop_import_4 >> sqoop_import_5 >> sqoop_import_6 >> sqoop_import_7 
