# healthcare-provider-fraud-detection-new
Healthcare Provider Fraud Detection By Data science methods
 

 
 


A Project Report on 
Healthcare Provider Fraud Detection
Submitted in partial fulfilment for award of degree of 

Program Name
In Business Analytics

Submitted by  

Brajesh Kumar
SRN

Under the Guidance of 
Name of the Guide
Designation

REVA Academy for Corporate Excellence 
REVA University
Rukmini Knowledge Park, Kattigenahalli, 
Yelahanka, Bangalore – 560064

July, 2022

 
 
 


Candidate’s Declaration


I, Brajesh Kumar hereby declare that I have completed the project work towards the first year of Master of Business Administration in Business Analytics at, REVA University on the topic entitled Healthcare Provider Fraud Detection under the supervision of JB Sinha. This report embodies the original work done by me in partial fulfilment of the requirements for the award of degree for the academic year 2022.


Place: Bengaluru 		                                            Name of the Student: Brajesh Kumar
Date:								Signature of Student
















 


Certificate

This is to Certify that the Project work entitled Healthcare Provider Fraud Detection carried out by Brajesh Kumar with <SRN>, is a bona fide student of REVA University, is submitting the first-year project report in fulfilment for the award of PGDM in Business Analytics during the academic year 2022.The Project report has been tested for plagiarism, and has passed the plagiarism test with the similarity score less than 15%. The project report has been approved as it satisfies the academic requirements in respect of the project work prescribed for the said Degree.


Signature of the Guide                                                         Signature of the Director
Name of the Guide        	                                              Name of the Director
					


External Viva
Names of the Examiners
1.	
2.	


Place: Bengaluru 		                                            
Date:								




 


Acknowledgement


I would like to thank the following people, without whom I would neither have been able to complete this research, nor would I have made it through my MBA degree:

Dr. P Shayma Raju, Chancellor REVA University 
Dr. S.Y Kulkarni, Ex- Vice Chancellor REVA University 
Dr. K. Mallikharjuna Babu, Vice Chancellor REVA University 
Dr. M. Dhanamjaya, Registrar REVA University 
I would also like to extend my special thanks to Dr. Shinu Abhi, Director REVA Academy of Corporate Excellence for believing in me and for providing all the guidance throughout my MBA degree and for guiding me through all the publications. 
I want to thank my guide JB Sinha for all the help in guiding me through the project and for showing me the path I could walk for this research project. 
I would also thank all the mentors at REVA Academy of Corporate Excellence for teaching us awesome methodologies throughout the academic year. 
Finally, I want to thank my family for patiently supporting me while I was busy working on this research paper, and for believing in me.

Place: Bengaluru 		                                            
Date:	10/July/2022	
 
				
 

Similarity Index Report

Title of the Thesis: Healthcare Provider Fraud Detection
Total No. of Pages: 12
Name of the Student: Brajesh Kumar
Name of the Guide(s): Ravi
This is to certify that this project report titled Monitoring and Alerting Setup for Healthcare Revenue Realization was scanned for similarity detection. Process and outcome are given below.

Software Used: 
Date of Report Generation: 
Similarity Index in %:  
Total word count: 
Name of the Guide: 



Place: Bengaluru 		                                                Name of the Student:
Date:								Signature of Student

Verified by: 

Signature
Dr. Shinu Abhi, 
Director, Corporate Training

 

List of Abbreviations

Sl. No	Abbreviation	Long Form
1	LSTM 	Long short-term Memory
2	GRU	Gated Recurrent Unit
3	CNN	CNN Convolutional Neural Network
4	Yolo	You Only Look Once
5	OpenCV 	Open-Source Computer Vision
6	SVC 	Support Vector Classifier
7	ML 	Machine Learning

List of Figures

No.	Name	Page No. 
Figure No.	Data Architecture for LSTM	12
Figure No.	CRISP-DM Methodology	17

List of Tables

No.	Name	Page No. 
Table No.	Precision and Recall of the Model	9
Table No.	Matrix Predictive Parameters	10
 

Abstract 
How does Healthcare Fraud affect the Healthcare Industry?
According to the definition of fraud, any deliberate and dishonest act committed with knowledge that it could result in an unauthorized benefit to the person committing the act or someone else not entitled to the benefit. Amongst many frauds in insurance claims, healthcare fraud is one of them.  In this article, I have analyzed and worked to detect "Healthcare Provider Fraud" where the provider makes a claim on behalf of the patient/insured/beneficiary. Medicare is currently facing a major problem due to provider fraud. Healthcare fraud is an organized crime that involves peers of providers, physicians, and beneficiaries making false claims. Under U.S. law, insurance companies must pay legitimate healthcare claims within 30 days. As a result, there is very little time to properly investigate this matter. These bad practices have the greatest impact on insurance companies. The Government reports that Medicare spending has increased exponentially as a result of fraud in Medicare claims.

There are numerous types of healthcare fraud and abuse. The following are some of the most typical types of provider fraud: 
a) Billing for services that were not rendered. 
b) Submitting a claim for the same service more than once. 
c) Falsely portraying the assistance rendered. 
d) Billing for a service that was not actually rendered but was more complicated or expensive. 
e) Charging for a service that was supposed to be covered but wasn't.
Further, the spread of Fraudulent cases is generally caused based on the below facts. Some providers might get into such practices with the help of one or more such doctors/patients. And, based on the success of the same, they are able to increase the number of fraudulent cases in the coming months. I could also observe that if a provider is into fraudulent practices, then the doctors/patients of this hospital might cause this practice to spread into other hospitals which they are visiting. It could also happen that if a provider is into such malpractices, then the nearby hospitals also get an interest/knowledge of the same and could grow into malpractices.
Over here, I am building a data pipeline with the details of beneficiary, inpatient data, outpatient data, and whether the provider is fraudulent or not. Based on this I create some features like average claim value per doctor and then do its sum for each provider, similarly I prepare many such features. Now based on this I do various sampling ratios of 80:20, 75: 25, 65:35, and 50:50.  Further I have checked various models like Logistic Regression, Decision Tree, SVC Gaussian Naïve Bayes. Further, I also checked the number of significant features. Total features in the final dataset come to around 360, out of which features with an impact of more than 0.01 % are 161. On running the program based on these 161 features also, I see the best result coming from Logistic Regression. Logistic Regression vs Random Forest with all the features: Using RF, the F1 score increased from the LR model with little decrease in AUC. Apparently, it can be said the RF model performs better than the LR model. But if I look at the confusion matrix, the False Negative (Predicted Not-Fraud but actually it is Fraud) count is higher in Random Forest, which is not a good result in this scenario. After looking at all the scores, I could say that Logistic Regression is performing better than Random Forest. Even after filtering the important features, there is no such improvement in model performance for both Logistic Regression and Random Forest. For any of these models, the F1 score has increased even though the False-negative also increased. In this case, it is more important to decrease False Negative than to decrease False Positive. So, any of the models are performing better with all features than only using top important features. After considering AUC, F1 Score, and FNR it can be said the Logistic Regression model is the best model for healthcare provider fraud detection problems.

 
Contents
Candidate’s Declaration	2
Certificate	3
List of Abbreviations	4
List of Figures	4
List of Tables	4
Abstract	5
Chapter 1:  Introduction	7
Chapter 2:  Literature Review	8
Chapter 3: Problem Statement	8
Chapter 4: Objectives of the Study	10
Chapter 5: Project Methodology	11
Chapter 6: Business Understanding	12
Chapter 7:  Data Understanding	13
Chapter 8: Data Preparation	14
Chapter 9:  Data Modeling	15
Chapter 9:  Data Evaluation	16
Chapter 10:  Deployment	17
Chapter 11: Analysis and Results	18
Chapter 12: Conclusions and Recommendations for future work	19
Bibliography	20
Appendix	21
Plagiarism Report	21
Publications in a Journal/Conference Presented/White Paper	21
Any Additional Details	21






 
Chapter 1:  Introduction 
 

Fraud is defined as any conscious, intentional, and deceitful act committed with the knowledge that it could result in an unauthorized benefit or payment to the person committing the act or someone else who is similarly not deserving the benefit. Healthcare fraud is one type of fraud. Here I analyzed and detected “Healthcare Provider Fraud” where the provider makes a claim on behalf of the beneficiary in the insurance provider-related application. Currently, Medicare is facing Provider Fraud as one of the biggest challenges. Healthcare fraud is an organized crime that involves peers of providers, physicians, and beneficiaries acting together to make fraud claims. As per U.S. legislation, an insurance company should pay within 30 days for a legitimate healthcare claim. So, there is very little time for insurance companies to investigate such frauds. these bad practices make the Insurance companies as the most vulnerable institutions. As per the Government, the total Medicare spending increased exponentially due to fraud in Medicare claims.
The reason for this study is to understand the Fraud patterns in the Healthcare provider industry. The impact of this study is to identify the fraudulent providers, and by correctly identifying the same, I could help reduce the cost to the insurance providers, this, in turn, reduces the healthcare insurance cost to the patients/beneficiaries. This also helps us reduce the overall cost of the claims. Later this could help us in approving the claims online and in much faster ways, than requiring manual efforts in checking and then approving the claims.
In the current scenario, once a claim has been received from a provider, someone has to check the details for any specifics related to mismatch of details, further to ensure the claims are within limits, and then further manual checking to check for frauds. This whole process takes time and cost. Hence a statistical approach could help approve claims faster, online, and without manual intervention, thus reducing the time and cost of clearing the claims.
Various Types of Healthcare Provider Fraud:
Healthcare fraud and abuse take many forms. Some of the most common types of fraud by providers are:
a) Billing for such services that were not provided.
b) Multiple submission of a claim for the same service.
c) Giving a false or misleading account of the nature of the service provided.
d) Charging for a more complex or costly service than was actually provided.
e) Billing for such a service that is covered when the service actually provided was not covered.

Over here in the introduction section, I have tried to show why this study is required, what things have been done in the existing solutions and why this new solution/approach is needed.

Chapter 2:  Literature Review 
Over here, I have gone through a few literature reviews and found their benefits or losses with respect to the methods they have used and how it could help in improving my approach or its result. 
Statistical-Methods-for-Health-Care-Fraud-Detection
How this paper is useful in my case study:
I can apply a similar approach in my case study.
1. Filling missing values: I can use the model-based imputation technique to fill the null values of the numerical columns if any. Such as Annual deductible amount, Annual reimbursement amount, Insurance claim amount reimbursed, and deductible amount paid.
2. Get a global view: I need to merge the 4-dataset given for my case study after preprocessing to get a global view of patients and providers.
3. Data Transformation/ Feature Engineering: From the overall merged dataset, I can find out the average claim amount reimbursed per provider, the total number of claims per provider, etc.
4. Removing Redundant features: First I can do a correlation check on the extracted features, then remove the correlated features followed by forwarding feature selection if required.
5. Model Selection: As I have labeled data, I have adopted supervised learning using Decision trees and AUC score, FPR, and FNR as performance metrics. To improve the performance, I have used ensemble models.

Medicare Fraud Detection Using Machine Learning Methods
How this paper useful in my case study:
Here the model is not distinct per specialty, I could apply the same approach to my problem as a specialty is not explicitly mentioned in the data provided. I can do random under-sampling with 4 different ratios and then 5-fold cross-validation with 10 times repetition. For each distribution use decision trees, logistic regression, and SVM as models with AUC as performance metrics. Compare the performance across each distribution and model then pick the best one.

Healthcare Fraud Detection
Because Medicare utilization and payment data are relatively new, there are limited studies using or referencing this particular dataset in fraud detection research. Three earlier studies look for patterns in the Medicare utilization and payment data employing descriptive statistics and correlations but do not apply machine learning techniques. Feldman et al. [1] use 2012 Medicare data to attempt to find correlations between a physician's educational background and practices performed to detect possible misuse or insurance inefficiencies. In doing this, the authors analyzed medical-related variables, such as charges, number of procedures, and payments, to find anomalous behaviors by comparing results with the national distribution of payments and charges. A study by Ko et al. [32] also uses the 2012 Medicare data with a focus on the Urology specialty only. They calculated the variability among Urologists and determined a possible savings of 9% from high utilization variability. Additionally, the authors found that the number of patient visits was strongly correlated with the reimbursements made by Medicare. Pande et al. [37] take older Medicare data and exclusions from the LEIE database to assess who the Medicare fraud perpetrators are and what happens to them after they get caught. The authors only use descriptive statistics to find patterns and make recommendations on Medicare fraud. One of the recommendations made is to use predictive models to detect claims fraud.
The use of descriptive statistics, correlations, etc., are extremely useful, but they tend to rely heavily on humans extracting patterns from the data. Machine learning methods can be employed to lessen this dependence by automatically extracting patterns to produce meaningful results, such as the detection of possibly fraudulent behaviors. One such study that uses machine learning is by Thornton et al. [44]. The authors explore several outlier-based detection techniques using Medicaid claims data for dental providers. Medicaid is another, distinct U.S. healthcare program that provides health coverage to low-income people [5]. They employ three univariate methods which include linear regression, box plots, and time series plots, as well as one multivariate method via clustering. The authors provide a case study of 500 dentists for which they claim the successful identification of 17 possibly fraudulent activities detected out of 360 records. A general coverage paper by Chandola et al. [21] explores several methods to detect healthcare fraud. They do not specify the use of Medicare data, but they do use a provider exclusion list, from the Texas Office of Inspector General's exclusion database, for fraudulent provider labels. The authors use several techniques including social network analysis, text mining, and temporal analysis in order to translate the problem of healthcare data analysis into some well-known data mining methods. The authors discussed the use of normal treatment profiles in order to compare providers and detect possible issues. A recent paper, by Branting et al. [18] creates a graph of providers, drug prescriptions, and procedures. The authors use two algorithms where one calculates the similarity to known fraudulent and non-fraudulent providers, and the other estimates fraud risk via shared practice locations or addresses. Medicare data from 2012 to 2014 was used, as was the LEIE database for fraud labels. They used 11 graph-based features, such as the similarity to the closest k members and the number of co located excluded providers, and 4 additional features and the J48 decision tree implemented in the Weka framework. This resulted in an F-measure of 0.919 and ROC area of 0.960.
Additional research by Bauder et al. explores Medicare fraud detection through several different studies. In one study [11], the authors use multivariate regression to establish a baseline for expected Medicare payments, per provider type. This baseline is then used as the normative case in which to compare the actual payment amounts, with deviations flagged as outliers. Another study [13] incorporates a two-step approach in detecting Medicare fraud, per provider type. The first step involves a multivariate regression model returning model residuals. These residuals are passed into a Bayesian probability model that produces the final probabilities indicating how likely it is that a particular value is fraudulent. They compared their method versus other common outlier detection methods, and found their method performed favorably. Additionally, works [10], [12] continue to explore the use of Bayesian models to detect Medicare fraud. The final studies [14], [29] are exploratory studies that look to predict fraudulent providers by using only the number of procedures performed. The authors employ Multinomial Naive Bayes to predict the provider type. If the predicted provider type does not match what is expected, then this provider is performing outside of normal practice patterns and should be investigated.
Our exploratory, comparative study takes into account many of the methods and data sources found in the related works. I apply these methods in a comprehensive experiment to assess the efficacy of different learners in predicting Medicare fraud. In addition to the learners and data, I incorporate the very real issue of class imbalance and assess detection using four performance metrics.
References: 
1>	Does Medical School Training Relate to Practice? Evidence from Big Data 
a.	https://www.liebertpub.com/doi/full/10.1089/big.2014.0060
2>	Health Services Research Variability in Medicare Utilization and Payment Among Urologists 
a.	https://doi.org/10.1016/j.urology.2014.11.054
3>	Healthcare Provider Fraud Detection And Analysis — Machine learning | by Rohan kumar soni | Medium
4>	A survey on statistical methods for health care fraud detection
a.	https://cpb-us-w2.wpmucdn.com/sites.gatech.edu/dist/4/216/files/2015/09/p70-Statistical-Methods-for-Health-Care-Fraud-Detection.pdf
5>	The Detection of Medicare Fraud Using Machine Learning Methods with Excluded Provider Labels
a.	https://www.aaai.org/ocs/index.php/FLAIRS/FLAIRS18/paper/download/17617/16814
6>	Machine Intelligence & Data Mining in Healthcare Fraud Detection
a.	https://www.roselladb.com/healthcare-fraud-detection.htm#:~:text=Healthcare%20fraud%20detection%20involves%20account,feasible%20by%20any%20practical%20means.
7>	Predicting Healthcare Fraud in Medicaid: A Multidimensional Data Model and Analysis Techniques for Fraud Detection
a.	https://www.sciencedirect.com/science/article/pii/S2212017313002946
8>	HEALTHCARE PROVIDER FRAUD DETECTION ANALYSIS
a.	https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis
9>	Healthcare Provider Fraud Detection Analysis using Machine Learning
a.	https://medium.com/analytics-vidhya/healthcare-provider-fraud-detection-analysis-using-machine-learning-81ebf09ed955
10>	healthcare-provider-fraud-detection
a.	https://github.com/anikmanik04/healthcare-provider-fraud-detection








Chapter 3: Problem Statement 
According to a recent study, the cost of Medicare fraud is in excess of $11 billion per year. Of the total $11.3 billion in losses, $7 billion of the total expense is due to fraudulent claims by healthcare provider companies. Fraudulent claims against Medicare account for 15% of total Medicare expenditures. Healthcare payments are the most vulnerable sector to this fraud, and the risk of payment fraud is a contributing factor to premium costs. Our goal is to determine whether an organization is fraudulent or the probability of fraud for that organization and also to find the root causes of the fraud so companies can avoid avoidable financial expenses. Features that determine whether claims are fraudulent are the medical condition and the cost of the treatment. Claims that are high for a low-risk patient are unrealistic and suspicious. Not only the financial loss is a great concern but also protecting the healthcare system so that they can provide quality and safe care to legitimate patients. 
In order to prevent financial loss, our goal is to determine whether a provider is likely to engage in fraud or to provide a likelihood score for that provider's possibly fraudulent behavior.
Using the Healthcare data of beneficiaries, and their data related to inpatient and outpatient claims, further grouped by the provider and also mapped to the existing knowledge of those providers which are found to be fraudulent or not. The insurance company may accept or refuse the claim or launch an investigation into that provider depending on the probability score and any fraudulent justifications.
In this study, I am working to discover the key characteristics that drive the potentially fraudulent providers. For instance, if a patient's risk score is high yet the claim amount is low.
















 
Chapter 4: Objectives of the Study 
1>	To predict whether a provider is potentially fraudulent or the probability score of that provider’s fraudulent activity and also find the reasons behind it as well to prevent financial loss.
2>	To find out the important features which are the reasons behind the potentially fraudulent providers. Such as if the claim amount is high for a patient whose risk score is low, then it is suspicious.
3>	To discover the key characteristics that drive the potentially fraudulent providers.
4>	To identify high risk / low risk patients, diagnosis, and procedures.
5>	To identify patterns in diseases and procedures specific to healthcare providers and further to identify if these patterns are caused by some specific doctors.
6>	To identify if some doctors are using first, second, third visit of some kind of patients to create fraudulent claims.



































Chapter 5: Project Methodology
  
The Approach
In this approach, I have consolidated the data of inpatient data, outpatient data, beneficiary data, and whether the provider is fraudulent or not. After that, I have done the EDA on the consolidated data. Then I added features based on a business understanding of the data. Then based on these I have tested a few models like Logistic Regression, Decision tree, random forest, and naïve Bayes.
Data Cleaning and EDA
First, I checked each and every dataset provided and try to extract information from it.
Provider Dataset:
I have checked the distribution of Fraudulent and Non-Fraudulent claims. I have already checked it and I can see there are 506 fraudulent providers (10%) and 4904 nonfraudulent providers (90%), which is a highly imbalanced dataset. To mitigate that imbalance, I can use either under-sampling or oversampling. In a paper discussed above, random under-sampling was used because of the very big size of the input data. But here the data size is not big so, I have used the random oversampling technique for my case study. (I have tried to use random under-sampling as well to check which one is performing best.)
Beneficiary Data:
1. From the KYC details of the beneficiaries I have calculated the age of the patients. For those, whose DOD is not available I have considered the last date available from another dataset.
2. I have further checked the other columns if there are any missing values. I need to impute the missing values based on domain knowledge or a model-based approach. If any of the chronic disease fields is missing, I have applied domain knowledge to impute it with yes or no. If the annual reimbursement or annual deductible amount field is missing, I can create a regression model to predict these values.
3. From the chronic disease fields of the patient, I can calculate the risk score. If the patient has a particular chronic disease it has to be filled with 1 else 0. I can sum up all the columns of chronic disease for a patient to calculate the risk score. A risk score is an important feature in fraud detection. If a patient with a low-risk score is claiming a high amount this is suspicious.
4. I have plotted the count plot of Gender, State, and Country to check which are the most occurring in the dataset.
5. I have plotted a graph of the Annual Deductible amount and Annual Reimbursed amount to check the distribution and also to find the outliers.
Inpatient/Outpatient Data:
1. From the claim start date and claim end date I have calculated the total number of days of the claim. If any of the fields are missing, I have tried to impute that by applying domain knowledge. It may be an average number of claim dates from the other patients or depending on the claim type. 
2. For all the Inpatients I need to calculate the total number of admitted days in the hospital in a similar way. 
3. Need to check Claim Reimbursed amount column. If there are any missing values, I have to impute that using domain knowledge or a model-based approach. 
4. I have plotted the count plot of attending physician, and operating physician for inpatient as well as an outpatient to check which all doctors are treating the patients most. 
5. I have plotted the PDF of the reimbursed amount to check the distribution for inpatient as well as outpatient. 
6. Add another column called "Total No of Physicians Attended". That is equal to Attending + Operating + Other physicians. 
7. I have added another column called "Hospitalization Status" in both the datasets, for Inpatients I have filled it with 1 and for outpatients with 0. So that after merging these claims can be distinguished.
Merge Datasets:
I have further merged all these datasets to get a global view of the data. First, merge Inpatient and Outpatient data based on Claim ID then merge it with Beneficiary data on Beneficiary ID and then merge the Provider dataset on Provider ID. Now all the data is combined in a single data frame.
Feature Engineering and EDA after Merging the Datasets:
EDA:
1.	I have plotted the count plot of Fraudulent and Legitimate claims to check the distribution in the claim data.
2.	Now I have plotted the count plots separately for Fraudulent and Legitimate claims on the state, race, and gender to check the top types associated with fraudulent claims.
3.	Further, I have Counted plots of Attending and Operating physicians separately for Fraudulent and Legitimate claims and checked the top attending physicians.
Feature Engineering:
1.	Calculate the average reimbursement received by the patient. Average reimbursement = Total reimbursement received/no of claims.
2.	Total number of claims per patient.
3.	 Average number of claim days per patient. Average no of claim days = Total claim days/ Total no of claims.
4.	Average no of days hospitalized which is the Total No of days hospitalized/No of times hospitalized.
Now, I have grouped the data based on Provider ID as our objective is to predict potentially fraudulent providers and take the sum of all the features applicable (Total amount deducted, the total amount reimbursed, a risk score of patients, chronic conditions, the total number of days admitted, the total number of days claimed, number of unique claims, number of inpatients, total claims for the patient, avg no of days patient was admitted, avg no of hospitalization days, etc.)
Now I have done feature selection using Random Forest to pick the important features. So, I have got 2 separate data frames one with all the features and another with only important features. I used both and pick the best one depending on the performance.
Performance Metric:
1.	AUC score
2.	F1 Score
3.	Confusion Matrix
4.	Check FPR and FNR separately
Train-Test Split and Oversampling:
As our dataset is imbalanced Legitimate: Fraudulent = 90:10, I have done oversampling. First, I split the data into Train and Test (Because if oversampling is done first, cross-validation may contain train data) then I used oversampling to make 4 sets of data with ratios of 80:20, 75:25, 65:35, and 50:50.
Model Selection and Approach to be followed:
I have used Logistic Regression, Decision Trees, Naive Bayes, and SVM for this classification task. For each model, I have used a 5-fold cross-validation 10 times then I have taken the average. I have compared the scores and picked the best model.



 
Chapter 6: Business Understanding
For the healthcare insurance provider companies, they have to try to keep the insurance cost at a minimum, cover all possible, more in-demand diseases or procedures, so that more people take this insurance, and also try to earn a profit, despite providing a decent service to the end customers, which is the patient / the beneficiary. As per the market demand factors, those who tend to take more time in clearing the claims lose their customer base, and the ones who take lesser time in clearing the claims, get more customers. Furthermore, there are some checks and investigations that need to be performed on not all but pattern-based claims to check for frauds. The manual work in identifying the fraudulent claims could be reduced manyfold with the help of machine learning models.





 
Chapter 7:  Data Understanding 
Outpatient Data (Train and Test):
It consists of the claim details for the patients who were not admitted to the hospital, and who only visited there. Important fields are explained below.
BeneID: It is the unique id of each beneficiary i.e patients.
ClaimID: It is the unique id of the claim submitted by the provider.
ClaimStartDt: It is the date when the claim started in yyyy-mm-dd format.
ClaimEndDt: It is the date when the claim ended in yyyy-mm-dd format.
Provider: It is the unique id of the provider.
InscClaimAmtReimbursed: It is the amount reimbursed for that particular claim.
AttendingPhysician: It is the id of the Physician who attended the patient.
OperatingPhysician: It is the id of the Physician who operated on the patient.
OtherPhysician: It is the id of the Physician other than the Attending Physician and Operating Physician who treated the patient.
ClmDiagnosisCode: It is code of the diagnosis performed by the provider on the patient for that claim.
ClmProcedureCode: It is the code of the procedures of the patient for treatment for that particular claim.
DeductibleAmtPaid: It is of the amount by the patient. That is equal to Total_claim_amount - Reimbursed_amount.

Inpatient Data (Train and Test):
It consists of the claim details for the patients who were admitted to the hospital. So, it consists of 3 extra fields Admission date, Discharge date, and Diagnosis Group code.
AdmissionDt: It is the date on which the patient was admitted into the hospital in yyyy-mm-dd format.
DischargeDt: It is the date on which the patient was discharged from the hospital in yyyy-mm-dd format.
DiagnosisGroupCode: It is a group code for the diagnosis done on the patient.
Beneficiary Data (Train and Test): This data contains beneficiary KYC details like DOB, DOD, Gender, Race, health conditions (Chronic disease if any), State, Country they belong to, etc. fields of this dataset are explained below.
BeneID: It is the unique id of the beneficiary.
DOB: It is the Date of Birth of the beneficiary.
DOD: It is the Date of Death of the beneficiary, if the beneficiary is dead, then the date of death, else null.
Gender, Race, State, Country: It contains the Gender, Race, State, and Country of the beneficiary.
RenalDiseaseIndicator: It is if the patient has existing kidney disease.
ChronicCond_*: The fields started with "ChronicCond_" to indicate if the patient has existed that particular disease. Which also indicates the risk score of that patient.
IPAnnualReimbursementAmt: It is the maximum reimbursement amount for hospitalization annually.
IPAnnualDeductibleAmt: It is a premium paid by the patient for hospitalization annually.
OPAnnualReimbursementAmt: It is the maximum reimbursement amount for outpatient visits annually.
OPAnnualDeductibleAmt: It is a premium paid by the patient for outpatient visits annually.
































 
Chapter 8: Data Preparation 
Over here in this case I was able to identify that the inpatient date is having just a few more fields or information apart from the outpatient details. So, I was able to do outer join and combine both of them. 
Further, I was able to map these claim details with the beneficiary id and the provider information so that I can get to know which particular providers are at prod or not in my training data set. 
This was able to help me create my Master Data further I was able to do one hot categorization for each field of gender and race so that each value of gender or race caused a new column apart from that I also did mean average of Insurance claim amount reimbursed the deductible amount paid and few other search details which need to be grouped a specific to each provider which is kind of become sperm provider average Insurance claim amount reimbursed and that was able to look at it based on per provider per beneficiary id for every attending physician for every operating physician for every other physician for every Diagnostics group for every claim admit diagnosis code. 
Further, I understood that for each of the six procedure codes that are there with a grouping of all the mean insurance claims and mean count of claim id just to get an idea of how far the data could help us determine whether the claim is fraudulent or not. 
Further a similar thing for each of the six Diagnostic claim codes also.
Merging the datasets:
1.	First, I merged Inpatient data with Outpatient data on beneficiary ID.
2.	Then I merged Patient details on Beneficiary Id with Patient data.
3.	Then I merged the class labels on the provider with the previously merged data frame using an inner join.
4.	Now I grouped the data frame based on provider id and extract some new features like total amount reimbursed per provider, average imbursed amount per patient per provider, per patient claims per provider, etc.
5.	Now for each provider ID, I collected the aggregate of other details from the beneficial table and aggregate of details from in-patient and out-patient data to see the volume of impact.


Distribution of Class Labels (Provider Data):
 
Observation: 
This dataset is quite unbalanced. There are 10% fraudulent providers and 90% non-fraudulent providers. 
Distribution of Gender (Beneficiary Data):
 
Observation:
The ratio of genders in beneficiary data is Gender_0: Gender_1 = 57%: 43%.
Distribution of State (Beneficiary Data):
 
Observation:
1.	The top 20 states in terms of the beneficiary count are shown in the above picture.
2.	States with codes 5, 10, 45, 33, and 39 are the top 5 states.
3.	8.7% of the beneficiaries belong to the state 5.
Distribution of Country (Beneficiary Data):
 
Observation:
1.	The top 20 countries in terms of the beneficiary count are shown in the above picture.
2.	Countries with codes 200, 10, 20, 60, and 0 are the top 5 states.
3.	2.85% of the beneficiaries belong to country code 200.
Distribution of Race (Beneficiary Data):
 
Observation:
1.	Race 1 is the most in terms of beneficiary count.
2.	85% of the beneficiaries belong to race 1.
3.	There is no race 4 in the dataset.
Distribution of Patient Risk Score (Beneficiary Data):
 
Observation:
1.	The distribution of patient risk scores is right-tailed.
2.	Most of the patients with risk scores 2, 3, 4, 5.
3.	Very few patients are there with risk scores 9, 10, 11, 12
Annual Reimbursement Amount (Inpatient and Outpatient):
 
 
Annual Reimbursement Amount — Inpatient(Left) and Outpatient(Right)
Observation:
1.	The total annual reimbursement amount for inpatient is 507162970 and outpatient is 179876080. The inpatient reimbursement amount is 2.81 times the outpatient amount.
2.	There are some outliers in both inpatient and outpatient as the tail of both the distributions is flat with a high value.
Annual Deductible Amount (Inpatient and Outpatient):
 
 
Annual Deductible Amount — Inpatient (Left) and Outpatient (Right)
Observation:
1.	The total annual deductible amount for inpatient is 55401242 and outpatient is 52335131.
2.	In both of the datasets there exists some outliers with high value.
Attending Physician (Inpatient and Outpatient):
 
 
Attending Physician — Inpatient (Left) and Outpatient (Right)
Observation:
1.	PHY422134, PHY341560, PHY315112, PHY411541, and PHY431177 are the top 5 attending physicians for inpatient, and PHY422134, PHY341560, PHY315112, PHY411541, PHY431177 are the top 5 attending physicians for outpatient in terms of the number of patients visit.
2.	Physician PHY422134 treated 1% of the total inpatients and physician PHY330576 treated 0.5% of the total outpatients.
Operating Physician (Inpatient and Outpatient):
 
 
Operating Physician — Inpatient (Left) and Outpatient (Right)
Observation:
1.	PHY429430, PHY341560, PHY411541, PHY352941, and PHY314410 are the top 5 operating physicians for inpatient and PHY330576, PHY424897, PHY314027, PHY423534, PHY357120 are the top 5 operating physicians for outpatient in terms of the number of patients operated.
2.	Physician PHY429430 operated 0.56% of the total inpatients and physician PHY330576 operated 0.08% of the total outpatients.
Other Physician (Inpatient and Outpatient):
 
 
Other Physician — Inpatient (Left) and Outpatient (Right)
Observation:
1.	PHY416093, PHY333406, PHY429929, PHY423728, and PHY361563 are the top 5 attending physicians for inpatient, and PHY412132, PHY341578, PHY338032, PHY337425, PHY347064 are the top 5 other physicians for outpatient in terms of the number of patients visit.
Procedure Code (Inpatient and Outpatient):
 
 
Procedure Code — Inpatient (Left) and Outpatient (Right)
Observation:
1.	4019, 9904, 2714, 8154, 66 are the top 5 procedures for inpatient, and 9904, 3722, 4516, 2744, and 66 are the top 5 procedures for outpatient in terms of the number of diagnoses done.
2.	Procedure 4019 is done 6.5% of the total procedures for inpatient and procedure 9904 is done 7.35% of total procedures for outpatient.
Diagnosis Code (Inpatient and Outpatient):
 
 
Diagnosis Code — Inpatient (Left) and Outpatient (Right)
Observation:
1.	4019, 2724, 25000, 41401, 4280 are the top 5 diagnosis codes for inpatient, and 44019, 25000, 2724, V5869, 4011 are the top 5 diagnosis codes for outpatient in terms of the number of diagnoses done.
2.	Procedure 4019 test is done 4.3% of the total diagnosis for inpatient and 4.65% for outpatient.
Distribution of Inpatient Outpatient in Final Dataset
 
Observation:
1.	The number of claims is less for inpatient data compared to outpatient data.
2.	Even though the claims are less in inpatient data, the percentage of fraudulent activity is more in inpatient data (57.8%) whereas it is 36.5% in outpatient data. This is because the per claim reimbursement amount for inpatients is much higher (35 times calculated earlier) than the per claim reimbursement amount for outpatients.
Insurance Claim Amount reimbursed in Final Data:
 
 Histogram (Left) and Box-Plot (Right)
Observation:
1.	25th, 50th percentiles are very less for claim amount reimbursed.
2.	75th percentile amount of Insurance Claim Amount reimbursed for fraudulent claims is higher than the legitimate claims.
Bivariate Analysis:
Scatter Plot of Patient Age vs Claim Period:
 
Observation:
1>	From the scatter plot I can see that when a patient’s age is <60 years and the claim duration is more than 20 days, then there is a higher probability that the transaction is fraudulent.
Scatter Plot of Patient Age vs InscClaimAmtReimbursed:
 
Observation:
•	From the Scatter Plot of Patient Age vs Ins Claim Amt Reimbursed, I can observe that if a patient’s claim amount is > 60000 it tends to be a fraudulent transaction. 
•	If the patient’s age is>88 years and the claim amount is>60000 the probability to be fraudulent is high.
Scatter Plot of IP_OP_TotalReimbursementAmt vs InscClaimAmtReimbursed:
 
Observation:
1.	If InscClaimAmtReimbursed is above 10000 and IP_OP_TotalReimbursementAmt is above 120000 then the chance to be a fraudulent transaction is high.
Scatter Plot of IP_OP_AnnualDeductibleAmt vs InscClaimAmtReimbursed:
 
Observation:
1.	If IP_OP_AnnualDeductibleAmt is less than 5000 and InscClaimAmtReimbursed is above 600000 then the chance to be a fraudulent transaction is high.

 



 

Chapter 9:  Data Modeling 
Below steps have been taken to create the data model process.
Oversample the data using SMOTE, I have used below combinations 80:20, 75:25, 65:35, 50:50. Then I have used Use Grid Search CV to find the best parameters for Logistic Regression. Then I checked with other models like Decision Tree Classifier, Support Vector Classifier, and Naïve Bayes. I further checked the number of features that give the best result for Random Forest and came to the conclusion that out of 336 features, 161 features have a FE ratio of 0.01 or above. 
 
AUC and Confusion Matrix for LR with all features
  
Chapter 9:  Model Evaluation 
Models Performance Measures considered here.
 



Precision: Of all the points the model predicted to be positive, what percentage of the points are actually positive?
Recall: Of all the points that actually belong to class A, how many of the points do the model detect to be belonging to class A?
F1 Score: It is the harmonic mean of precision and recall values, calculated by the below equation: 
AUC Score: AUC stands for “Area under the ROC Curve.” That is, AUC measures the entire two-dimensional area within the entire ROC curve.
3.	 
AUC (Area under the ROC Curve)
•	AUC is a scale-invariant measure. It measures how well predictions are ranked, rather than their absolute values, giving us a relative ranking.
•	AUC is a classification-threshold-invariant measure. It measures how good the model’s predictions are, irrespective of what classification threshold is chosen.


















Chapter 10:  Deployment
I tested the above solution to be working with decent quality with offline data. This solution could now be deployed to a system connecting to the online form and connecting to the ERP of various healthcare providers and insurance providers' claims systems. The model would ask for details for filling in the claim, together with asking more specific questions that help the model to determine whether the claim is fraudulent. This will help us approve the claims faster without manual intervention for those claims where the patient, provider, diagnosis, and procedure risk are low. This helps the insurance provider to concentrate and ask more details questions for the ones where the risk shows as high.





































 
Chapter 11: Analysis and Results 
Final Comparison:
1.	Logistic Regression vs Random Forest with all the features: Using RF, F1 score increased from LR model with little decrease in AUC. Apparently, it can be said the RF model performing better than LR model. But if I look at the confusion matrix, False Negative (Predicted Not-Fraud but actually it is Fraud) count is more in RF, which is very dangerous in our case. After looking at all the scores it can be said that LR is performing better than RF.
2.	After filtering the important features there is no such improvement in model performance for both LR and RF. F1 score is increased even though False negative also increased. In our case decreasing False Negative is more important than decreasing False Positive. So, I can say model is performing better with all features than only using top important features.
3.	After considering AUC, F1 Score, FNR it can be said the Logistic Regression model is the best model in healthcare provider fraud detection problem.




















 
Chapter 12: Conclusions and Recommendations for future work 
Based on the info from inpatient and outpatient info, together with beneficiary details, I was able to create a data model and further understood from the results that the logistic regression with all features is the best model. 1.	After considering AUC, F1 Score, FNR it can be said the Logistic Regression model is the best model in healthcare provider fraud detection problem.
 
Bibliography
Prager, J. (2006). Open-domain question-answering. Foundations and Trends in Information Retrieval, 1(2), 91–233. https://doi.org/10.1561/1500000001
Srivastava, A., Singh, V., & Drall, G. S. (2019). Sentiment analysis of twitter data: A hybrid approach. International Journal of Healthcare Information Systems and Informatics, 14(2), 1–16. https://doi.org/10.4018/IJHISI.2019040101
























Appendix
Plagiarism Report 
Publications in a Journal/Conference Presented/White Paper  
Any Additional Details 
Github:
https://github.com/brajesh2020/healthcare-provider-fraud-detection-new/
