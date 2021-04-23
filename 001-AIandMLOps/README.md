# 001 - AI and MLOps

## Introduction
Welcome to the Hackathon of AI and MLOps! We will focus on hands-on activities that develop proficiency in AI-oriented services such as AutoML Vision, AI Platform, and MLOps pipeline. These challenges assume an introductory to intermediate knowledge of these services, and if this is not the case, please spend time working through related resources.

## Use Case
Smart Solutions Inc. plans to implement a face recognition solution to be used as an alternative to authenticate users into its internal online systems. The solution needs to be automated as much as possible to reduce human errors and costs. 

## Learning Objectives
Most challenges observed by customers in these realms are in stitching multiple services together. As such, we have tried to place key concepts in the context of a broader solution.

Once all hackathon challenges are completed, you should be able to:
- Configure your apps to call GCP APIs with API Key or Access Token
- Build a Web application that calls various GCP APIs, specifically Vision API and Cloud Storage API  
- Effectively leverage the AutoML Vision to create image classification model that can then be leveraged by the Web application
- Implement ML pipeline to manage dataset, model training and model deployment
- Deploy the Web application and trained model to Kubernetes 
- Automate the infrastructure and service provisioning with Cloud Build, Terraform, etc.

## Background Knowledge
This workshop is meant for an AI Developer on Azure. Since our time today is limited, there are certain things you will need to read or setup after you arrive. If you do not have this background knowledge, please work closely with your team to learn from others or use the links below.
- GCP Console
    - You should have experience with the [GCP Console](https://console.cloud.google.com) and understand how to create resources and configure individual services. 
- GCP Cloud Shell
    - You should have some experience to execute gcloud commands using [Cloud Shell](https://cloud.google.com/shell)
- Visual Studio Code
    - Previous exposure to an IDE tool will be helpful. You should be familiar with how to use [Visual Studio Code](https://code.visualstudio.com) to develop Python applications. We assume each team will have some familiarity with Python (intermediate level - you can learn here).
- AI and ML
    - Basic understanding and knowledge about data engineering and model training with [AutoML Vision](https://cloud.google.com/vision/automl).

## Prerequisites
This is a list of pre-requisites needed to successfully complete the challenges.  Some of these are items to deploy to your development machine.  Some are decisions you should discuss and define as a team, like the framework to use for developing a python Web application.

1. GCP Project
    - You must have a GCP project to use for the hackathon. Either use your existing project or setup a free trial to complete today’s challenges.
2. Vision API, Cloud Storage API and AI Platform
    - Please enable these APIs by using either GCP Console or gcloud commands.
3. Service Account
    - Please create a service account and grant proper roles and permissions.

## Challenges
Your team’s mission is to learn more about AI Platform through hands-on practice by completing challenges in two key areas: AutoML and ML Pipeline.

Your team starts by building a simple Python Web application that allows you to take photos from your face using your Web camera, then upload the photos to Cloud Storage. You will use AutoML to train an image classification model for recognizing the face photos. Once you have this face model tested and deployed, you will integrate it with the Web application to implement a simple face recognition system.

- Challenge 1: **[Implement a Web app to take photos and upload them to Cloud Storage]()**
- Challenge 2: **[Deploy the Web app to App Engine]()**
- Challenge 3: **[Use AutoML Vision to train a model to recognize faces]()**
- Challenge 4: **[Integrate the Web app with the deployed face model]()**
- Challenge 5: **[Deploy the Web app to GKE]()**
- Challenge 6: **[Create a ML Pipeline to manage dataset, model training and deployment]()**
- Challenge 7: **[Automate environment provisioning, app build and deployment]()**

## Resources & Helpful Links
- GCP Project
    - <https://cloud.google.com/resource-manager/docs/creating-managing-projects>
- Cloud Shell
    - <https://cloud.google.com/shell>
- Service Account
    - <https://cloud.google.com/iam/docs/service-accounts>
- AutoML Vision
    - <https://cloud.google.com/vision/automl>
- App Engine
    - <https://cloud.google.com/appengine>
- Visual Studio Code
    - <https://code.visualstudio.com>
- Python Flask
    - <https://flask.palletsprojects.com/en/1.1.x/>   
