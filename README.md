# GovTech DataEng test solutions
## Section 1: Data Pipelines
###### Following are the steps for setting up this data pipeline:

Step 1: Place data_pipeline.py python script to the desired source folder.

Step 2: Chnage the path variable in above script to the file's source folder and respective output file to be saved.

Step 3: Make sure the env path of Python2.7 or Python 3 and edit crontab, put the scheduler into it.

## Section 2: Database
###### Following are the contents:

1. ERD file showing entity relationships.
2. cars_db.sql contains query to create the necessary tables.
3. Dockerfile contains set of instructions for cars database.

## Section 3: System Design
###### It's divided as per following parts:
- Image ingesting web application is sitting on two servers to avoid breakpoint in the worst cases, load balancer is used to distribute the load using round robin algorithm.
- The above data is fed to Kafka streams using desired number of brokers.
- These streams are accumulated by Kinesis Firehose to publish it to S3.
- S3 is the heart of raw and processed data storage.
- Raw data is fed to AWS EMR which can use Spark to process the data or AWS Lambda can be used where already developed script      can be deployed.
- This processed data is sent back to S3 to store it till whenever wanted(ideally minimun of 7 days).
- This structured-processed data is pumped to Redshift to put in sophisticated and low cost data warehouse to be used for BI usecases,Quicksights or Tableau.
