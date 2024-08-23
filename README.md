# ML Workflow for Scones Unlimited

This project involves building a complete machine learning workflow for Scones Unlimited using Amazon SageMaker. It includes setting up the environment, training and deploying a model, and integrating various AWS services.

## Project Overview

The objective of this project is to create a robust machine learning pipeline using Amazon SageMaker and other AWS services to process and classify images. The workflow encompasses data preparation, model training, API deployment, and monitoring.

## Key Components

1. *SageMaker Studio Setup*
   - Configured SageMaker Studio workspace.
   - Set up a kernel for project development.

2. *Data Preparation*
   - Completed the ETL (Extract, Transform, Load) process for preparing data.

3. *Model Training & Deployment*
   - Trained an image classification model.
   - Deployed the trained model with a unique API endpoint for making predictions.

4. *Lambda Functions*
   - *Image Data Lambda:* Returns image data to the Step Function.
   - *Image Classification Lambda:* Classifies images using the trained model.
   - *Filtering Lambda:* Filters out low-confidence inferences.

5. *Step Functions*
   - Integrated Lambda functions into a Step Function.
   - Provided a JSON export defining the Step Function and included screenshots of the working process.

6. *Model Monitoring*
   - Extracted and visualized monitoring data from S3 to evaluate model performance.

## Learning Outcomes

- Gained proficiency in navigating AWS services.
- Developed skills in managing costs effectively through cost management practices.
- Achieved a full understanding of integrating and utilizing AWS components such as SageMaker, Lambda, and Step Functions.

## Installation and Setup

1. *SageMaker Studio*
   - Set up a SageMaker Studio workspace.
   - Launch a new kernel to begin development.

2. *Data Preparation*
   - Implement ETL processes to prepare your dataset.

3. *Model Training*
   - Follow the steps to train and deploy an image classification model in SageMaker.

4. *Lambda Functions*
   - Write and deploy three Lambda functions for different stages of the workflow.

5. *Step Functions*
   - Author and configure a Step Function that integrates the Lambda functions.

6. *Monitoring*
   - Extract and visualize model monitoring data from S3.
