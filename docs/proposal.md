---
title: "DSA Professional Practice Proposal"
author: "Tony Silva"
date: "August 31, 2017"
output: pdf_document
---

# Introduction
  The FAA Logistics Center is home to the National Airspace System's supply chain depot. The FAA Logistics Center (FAALC) provides supply chain, MRO, and warehouse support for the FAA air traffic control network. The parts that the FAALC support are components of the overall air traffic systems such as radars, navigation, weather, and communication systems. A call center exists at the FAALC to support customers (FAA Technicians at airports and FAA facilities) in the field. The Customer Care Center (CCC) supports customers from 6am to 9pm, taking thousands of calls per month. Customers may call to order parts, ask about an existing order, or request a warranty. It is important to answer all customer calls in order to have great customer service and support the customers completely.

  In this project, the Customer Care Center's call center data will be analyzed. The supervisor for this project is the branch manager of the CCC, Tammy Loberg. Her email is Tammy.Loberg@faa.gov, her phone number is (405)-954-4935. Since I work for the FAALC this project is a paid through FAALC funding. The Professional Practice will be worth 4 credit hours.

# Objectives
  The objective for this project is to generate a predictive model for the CCC that can identify when the call center is susceptible to abandon calls. An abandon call occurs when a customer calls the CCC and hangs up before getting to talk with an Agent. Abandon Call rates are an important measure of call center performance. By identifying when the CCC is most susceptible to an abandoned call, we can increase the opportunity at eliminating potential un-happy customers by allocating appropriate resources to a call. This way customers can have their calls answered and their experience with the FAALC be a pleasant one. The CCC's duty is to take care of the FAALC's customers. Through the use of data science, the CCC's job and overall goal can be executed much easier.

  The data the is generated from the Customer Care Center are records of each individual call made to the CCC's call management system. Each call is an observation in the overall data set. Some features already in the data set include: date/time of call, phone number of who called, number of seconds it took to drop/answer call, whether the call was dropped or not, etc.

# Plan
  The project will encompass utilizing the Customer Care Center's call data to analyze, measure, and generate a predictive model to determine when a call is at risk of being abandoned by a customer. In a previous project I performed, I created an Access Database that would store all the Customer Care Center's call data. In that project, I created queries for the CCC's branch manager to extract month outputs from the data. In this Professional Practice, I will expand on those queries and pull together the data into one overall data set. This will include data wrangling, and data cleansing to generate a usable data set. The usable data set will then have machine learning methods applied to it, in order to generate a predictive model. The Machine Learning methods that will be followed are Exploratory Data Analysis, Model Performance Criteria, Feature Engineering, Feature Extraction, Feature Selection, Sampling Approach, Model Training, Model Tuning, and Iteration to find the best model.

  Through this project, I will build skills in Machine Learning/Predictive Modeling. This project will use and expand on skills gained through course work from Engineering Statistics, Intelligent Data Analytics, Data Mining, and Introduction to Text Analytics. 

# Deliverables
  There a couple of deliverables for this project. Please see the table below for a list of the deliverables.

|Deliverables|
|---|
|Cleaned Data Set|
|Code Created in Project|
|Predictive Model|
|Recommendations on Scheduling|

  The cleaned data set will provide the Customer Care Center the complete data used in the project. With the data and the code that was generated in the project, the FAALC will have a means of reproducing the results from the project. These are important deliverables since the Call Center generates new data on a daily basis, the data set for the call center is growing and reassessment of the predictive model may need to be addressed as more data is generated.

The Predictive Model deliverable will be the model created from the Machine Learning activities in this project. This model will allow the Customer Care Center to identify areas of opportunity. The predictive model will not necessarily be production ready, however, requirements around deploying the predictive model into a production environment will be given. From the predictive modeling and exploratory data analysis, recommendations on scheduling call center agents will be given to the Tammy Loberg, the CCC branch manager.

Through these deliverables the project will be executed completely.

# Schedule
The schedule of completion of steps in the project are as follows:

|Task|Date|
|----|----|
|Data Wrangling/Cleaning|09/15/2017|
|Feature Engineering/Extraction|10/01/2017|
|Feature Selection|10/14/2017|
|Sampling Approach|10/17/2017|
|Model Creation|10/27/2017|
|Model Tuning|11/03/2017|
|Final Model|11/15/2017
|Finish Paper|11/21/2017|
|Finish Presentation|11/25/2017|
|Presentation|12/01/2017|

Please note that many of these tasks are iterable. Meaning, I can always go back and edit one of these tasks to help with a future task. (i.e. Create new features to enhance model predictive power.)

