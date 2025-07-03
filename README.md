# Netflix-Azure-Data-Engineering-Project
🎬 Netflix Data Engineering Project with Azure & Medallion Architecture

![1742284763217](https://github.com/user-attachments/assets/ea359aad-e2de-483c-a0f1-0e82373643b7)

📌 Overview

This end-to-end data engineering project demonstrates the transformation of Netflix data using the Medallion Architecture (Bronze → Silver → Gold) on the Azure Data Platform. The solution leverages scalable and modern data engineering tools such as Azure Data Factory, Azure Databricks, and Delta Lake, focusing on automation, modularity, and real-time processing.

🚀 Key Features

Dynamic Pipelines in Azure Data Factory (ADF) for automated and parameterized workflows                   
Real-time ingestion with Databricks Auto Loader                  
Delta Live Tables for declarative data transformations                               
Layered Medallion Architecture for data quality, governance, and performance                         
End-to-end orchestration from raw data to curated analytical outputs                  

🛠️ Technologies Used

Azure Data Lake Storage (ADLS)                         
Azure Data Factory (ADF)                                
Azure Databricks                                  
Delta Lake / Delta Live Tables                                    
Auto Loader                        
PySpark                                          
Medallion Architecture (Bronze, Silver, Gold)


📊 Data Flow

Ingestion: Netflix data is ingested to ADLS (Bronze) using Databricks Auto Loader                                      
Transformation: Data is cleaned and enriched in Silver layer using Delta Live Tables                                      
Aggregation: Business-level aggregates are created in Gold layer for reporting                                
Orchestration: ADF pipelines manage workflow execution and monitoring
