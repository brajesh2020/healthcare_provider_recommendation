import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
path1='C:/Users/brajesh/Downloads/healthcare-provider-fraud-detection/archive'
for dirname, _, filenames in os.walk(path1):
    for filename in filenames:
        print(filename)
# Function to load the csv  dataset
def read_data(tp  , N  ):
#     path1=path1
    target = pd.read_csv(path1 + "/{}-{}.csv".format(tp.title(), N))
    pt = pd.read_csv(path1 + "/{}_Beneficiarydata-{}.csv".format(tp.title(), N))
    in_pt = pd.read_csv(path1 + "/{}_Inpatientdata-{}.csv".format(tp.title(), N))
    out_pt = pd.read_csv(path1 + "/{}_Outpatientdata-{}.csv".format(tp.title(), N))
    return(in_pt, out_pt, pt, target)
# Function to load the inputs dataset
# def read_data(tp = "Train", N = 1542865627584):
# #     path1=path1
#     target = pd.read_csv(path1 + "/{}-{}.csv".format(tp.title(), N))
#     pt = pd.read_csv(path1 + "/{}_Beneficiarydata-{}.csv".format(tp.title(), N))
#     in_pt = pd.read_csv(path1 + "/{}_Inpatientdata-{}.csv".format(tp.title(), N))
#     out_pt = pd.read_csv(path1 + "/{}_Outpatientdata-{}.csv".format(tp.title(), N))
#     return(in_pt, out_pt, pt, target)

### Load Train data
# train_in_pt, train_out_pt, train_ben, train_target = read_data()
train_in_pt, train_out_pt, train_ben, train_target = read_data(tp = "Train", N = 1542865627584)

Train_Inpatient=train_in_pt
Train_Outpatient=train_out_pt
Train_Beneficiary=train_ben
Train=train_target

### Load Test data
test_in_pt, test_out_pt, test_ben, test_target = read_data(tp = "Test", N = 1542969243754)

Test_Inpatient=test_in_pt
Test_Outpatient=test_out_pt
Test_Beneficiary=test_ben
Test=test_target



# Replacing 2 with 0 for chronic conditions, Zero indicates chronic condition is No

Train_Beneficiary = Train_Beneficiary.replace({'ChronicCond_Alzheimer': 2,
                                               'ChronicCond_Heartfailure': 2,
                                               'ChronicCond_KidneyDisease': 2,
                           'ChronicCond_Cancer': 2,
                                               'ChronicCond_ObstrPulmonary': 2,
                                               'ChronicCond_Depression': 2,
                           'ChronicCond_Diabetes': 2,
                                               'ChronicCond_IschemicHeart': 2,
                                               'ChronicCond_Osteoporasis': 2,
                           'ChronicCond_rheumatoidarthritis': 2,
                                               'ChronicCond_stroke': 2 }, 0)

# For RenalDiseaseIndicator replacing 'Y' with 1
Train_Beneficiary = Train_Beneficiary.replace({'RenalDiseaseIndicator': 'Y'}, 1)

Test_Beneficiary = Test_Beneficiary.replace({'ChronicCond_Alzheimer': 2,
                                             'ChronicCond_Heartfailure': 2,
                                             'ChronicCond_KidneyDisease': 2,
                           'ChronicCond_Cancer': 2,
                                             'ChronicCond_ObstrPulmonary': 2,
                                             'ChronicCond_Depression': 2,
                           'ChronicCond_Diabetes': 2,
                                             'ChronicCond_IschemicHeart': 2,
                                             'ChronicCond_Osteoporasis': 2,
                           'ChronicCond_rheumatoidarthritis': 2,
                                             'ChronicCond_stroke': 2 }, 0)

Test_Beneficiary = Test_Beneficiary.replace({'RenalDiseaseIndicator': 'Y'}, 1)


# convert all these columns datatypes to numeric
Train_Beneficiary[["ChronicCond_Alzheimer", "ChronicCond_Heartfailure", "ChronicCond_KidneyDisease", "ChronicCond_Cancer",
                   "ChronicCond_ObstrPulmonary", "ChronicCond_Depression", "ChronicCond_Diabetes", "ChronicCond_IschemicHeart",
                   "ChronicCond_Osteoporasis", "ChronicCond_rheumatoidarthritis", "ChronicCond_stroke", "RenalDiseaseIndicator"]] = Train_Beneficiary[["ChronicCond_Alzheimer", "ChronicCond_Heartfailure", "ChronicCond_KidneyDisease", "ChronicCond_Cancer", "ChronicCond_ObstrPulmonary", "ChronicCond_Depression", "ChronicCond_Diabetes", "ChronicCond_IschemicHeart", "ChronicCond_Osteoporasis", "ChronicCond_rheumatoidarthritis", "ChronicCond_stroke", "RenalDiseaseIndicator"]].apply(pd.to_numeric)

Test_Beneficiary[["ChronicCond_Alzheimer", "ChronicCond_Heartfailure", "ChronicCond_KidneyDisease", "ChronicCond_Cancer",
                  "ChronicCond_ObstrPulmonary", "ChronicCond_Depression", "ChronicCond_Diabetes", "ChronicCond_IschemicHeart",
                  "ChronicCond_Osteoporasis", "ChronicCond_rheumatoidarthritis", "ChronicCond_stroke", "RenalDiseaseIndicator"]] = Test_Beneficiary[["ChronicCond_Alzheimer", "ChronicCond_Heartfailure", "ChronicCond_KidneyDisease", "ChronicCond_Cancer", "ChronicCond_ObstrPulmonary", "ChronicCond_Depression", "ChronicCond_Diabetes", "ChronicCond_IschemicHeart", "ChronicCond_Osteoporasis", "ChronicCond_rheumatoidarthritis", "ChronicCond_stroke", "RenalDiseaseIndicator"]].apply(pd.to_numeric)


# calculate patient risk score by summing up all the chronic conditions.
# The higher risk score indicates the health of the patient is not good

Train_Beneficiary['Patient_Risk_Score'] = Train_Beneficiary['ChronicCond_Alzheimer'] + Train_Beneficiary['ChronicCond_Heartfailure'] + \
                                        Train_Beneficiary['ChronicCond_KidneyDisease'] + Train_Beneficiary['ChronicCond_Cancer'] +\
                                        Train_Beneficiary['ChronicCond_ObstrPulmonary'] + Train_Beneficiary['ChronicCond_Depression'] +\
                                    Train_Beneficiary['ChronicCond_Diabetes'] + Train_Beneficiary['ChronicCond_IschemicHeart'] +\
                                    Train_Beneficiary['ChronicCond_Osteoporasis'] + Train_Beneficiary['ChronicCond_rheumatoidarthritis'] +\
                                    Train_Beneficiary['ChronicCond_stroke'] + Train_Beneficiary['RenalDiseaseIndicator']

# calculate patient risk score by summing up all risk scores
Test_Beneficiary['Patient_Risk_Score'] = Test_Beneficiary['ChronicCond_Alzheimer'] + Test_Beneficiary['ChronicCond_Heartfailure'] + \
                                        Test_Beneficiary['ChronicCond_KidneyDisease'] + Test_Beneficiary['ChronicCond_Cancer'] +\
                                        Test_Beneficiary['ChronicCond_ObstrPulmonary'] + Test_Beneficiary['ChronicCond_Depression'] +\
                                    Test_Beneficiary['ChronicCond_Diabetes'] + Test_Beneficiary['ChronicCond_IschemicHeart'] +\
                                    Test_Beneficiary['ChronicCond_Osteoporasis'] + Test_Beneficiary['ChronicCond_rheumatoidarthritis'] +\
                                    Test_Beneficiary['ChronicCond_stroke'] + Test_Beneficiary['RenalDiseaseIndicator']


# Replacing '2' with '0' for Gender Type
Train_Beneficiary = Train_Beneficiary.replace({'Gender': 2}, 0)

Test_Beneficiary = Test_Beneficiary.replace({'Gender': 2}, 0)

# Convert Date of Birth and Date of Death from String to Datetime format
Train_Beneficiary['DOB'] = pd.to_datetime(Train_Beneficiary['DOB'] , format = '%d/%m/%Y')
Train_Beneficiary['DOD'] = pd.to_datetime(Train_Beneficiary['DOD'],format ='%d/%m/%Y')

Test_Beneficiary['DOB'] = pd.to_datetime(Test_Beneficiary['DOB'] , format = '%d/%m/%Y')
Test_Beneficiary['DOD'] = pd.to_datetime(Test_Beneficiary['DOD'],format ='%d/%m/%Y')

# https://stackoverflow.com/questions/25146121/extracting-just-month-and-year-separately-from-pandas-datetime-column
# Get the birth month and Birth year for DOB and DOD
Train_Beneficiary['Birth_Year'] = Train_Beneficiary['DOB'].dt.year
Train_Beneficiary['Birth_Month'] = Train_Beneficiary['DOB'].dt.month

Test_Beneficiary['Birth_Year'] = Test_Beneficiary['DOB'].dt.year
Test_Beneficiary['Birth_Month'] = Test_Beneficiary['DOB'].dt.month


# #### Calculate patient's age based on DOD, if DOD is not available calculate age based on the maximum date available in the data

# In[46]:


# https://stackoverflow.com/questions/46508895/calculating-age-from-date-time-format-in-python-pandas?noredirect=1&lq=1
Train_Beneficiary['Patient_Age'] = round(((Train_Beneficiary['DOD'] - Train_Beneficiary['DOB']).dt.days)/365)
Train_Beneficiary.Patient_Age.fillna(round(((pd.to_datetime('2009-12-01',format ='%Y-%m-%d')-Train_Beneficiary['DOB']).dt.days)/365),inplace=True)

Test_Beneficiary['Patient_Age'] = round(((Test_Beneficiary['DOD'] - Test_Beneficiary['DOB']).dt.days)/365)
Test_Beneficiary.Patient_Age.fillna(round(((pd.to_datetime('2009-12-01',format ='%Y-%m-%d')-Test_Beneficiary['DOB']).dt.days)/365),inplace=True)


# Set value=1 if the patient is dead i.e DOD value is not null
Train_Beneficiary['isDead'] = 0
Train_Beneficiary.loc[Train_Beneficiary.DOD.notna(), 'isDead'] = 1
Test_Beneficiary['isDead'] = 0
Test_Beneficiary.loc[Test_Beneficiary.DOD.notna(), 'isDead'] = 1

# convert ClaimStartDt, ClaimEndDt from string to datetime format
Train_Inpatient['ClaimStartDt'] = pd.to_datetime(Train_Inpatient['ClaimStartDt'] , format = '%Y-%m-%d')
Train_Inpatient['ClaimEndDt'] = pd.to_datetime(Train_Inpatient['ClaimEndDt'],format = '%Y-%m-%d')

Test_Inpatient['ClaimStartDt'] = pd.to_datetime(Test_Inpatient['ClaimStartDt'] , format = '%Y-%m-%d')
Test_Inpatient['ClaimEndDt'] = pd.to_datetime(Test_Inpatient['ClaimEndDt'],format = '%Y-%m-%d')

# convert AdmissionDt, DischargeDt from string to datetime format
Train_Inpatient['AdmissionDt'] = pd.to_datetime(Train_Inpatient['AdmissionDt'] , format = '%Y-%m-%d')
Train_Inpatient['DischargeDt'] = pd.to_datetime(Train_Inpatient['DischargeDt'],format = '%Y-%m-%d')

Test_Inpatient['AdmissionDt'] = pd.to_datetime(Test_Inpatient['AdmissionDt'] , format = '%Y-%m-%d')
Test_Inpatient['DischargeDt'] = pd.to_datetime(Test_Inpatient['DischargeDt'],format = '%Y-%m-%d')


# Calculate Hospitalization_Duration = DischargeDt - AdmissionDt
Train_Inpatient['Hospitalization_Duration'] = ((Train_Inpatient['DischargeDt'] - Train_Inpatient['AdmissionDt']).dt.days)+1
# Calculate Claim_Period = ClaimEndDt - ClaimStartDt
Train_Inpatient['Claim_Period'] = ((Train_Inpatient['ClaimEndDt'] - Train_Inpatient['ClaimStartDt']).dt.days)+1

Test_Inpatient['Hospitalization_Duration'] = ((Test_Inpatient['DischargeDt'] - Test_Inpatient['AdmissionDt']).dt.days)+1
Test_Inpatient['Claim_Period'] = ((Test_Inpatient['ClaimEndDt'] - Test_Inpatient['ClaimStartDt']).dt.days)+1

# #### If the number of days claimed for Inpatient treatment is more than no of days hospitalized is suscicious. So, I am adding this feature column.

# ExtraClaimDays = Claim_Period - Hospitalization_Duration
Train_Inpatient['ExtraClaimDays'] = np.where(Train_Inpatient['Claim_Period']>Train_Inpatient['Hospitalization_Duration'], Train_Inpatient['Claim_Period'] - Train_Inpatient['Hospitalization_Duration'], 0)
Test_Inpatient['ExtraClaimDays'] = np.where(Test_Inpatient['Claim_Period']>Test_Inpatient['Hospitalization_Duration'], Test_Inpatient['Claim_Period'] - Test_Inpatient['Hospitalization_Duration'], 0)


# https://stackoverflow.com/questions/25146121/extracting-just-month-and-year-separately-from-pandas-datetime-column
# Get the months and year of claim start and claim end
Train_Inpatient['ClaimStart_Year'] = Train_Inpatient['ClaimStartDt'].dt.year
Train_Inpatient['ClaimStart_Month'] = Train_Inpatient['ClaimStartDt'].dt.month
Test_Inpatient['ClaimStart_Year'] = Test_Inpatient['ClaimStartDt'].dt.year
Test_Inpatient['ClaimStart_Month'] = Test_Inpatient['ClaimStartDt'].dt.month

Train_Inpatient['ClaimEnd_Year'] = Train_Inpatient['ClaimEndDt'].dt.year
Train_Inpatient['ClaimEnd_Month'] = Train_Inpatient['ClaimEndDt'].dt.month
Test_Inpatient['ClaimEnd_Year'] = Test_Inpatient['ClaimEndDt'].dt.year
Test_Inpatient['ClaimEnd_Month'] = Test_Inpatient['ClaimEndDt'].dt.month


# In[65]:


# Get the month and year of Admission_Year and Admission_Month
Train_Inpatient['Admission_Year'] = Train_Inpatient['AdmissionDt'].dt.year
Train_Inpatient['Admission_Month'] = Train_Inpatient['AdmissionDt'].dt.month
Test_Inpatient['Admission_Year'] = Test_Inpatient['AdmissionDt'].dt.year
Test_Inpatient['Admission_Month'] = Test_Inpatient['AdmissionDt'].dt.month

Train_Inpatient['Discharge_Year'] = Train_Inpatient['DischargeDt'].dt.year
Train_Inpatient['Discharge_Month'] = Train_Inpatient['DischargeDt'].dt.month
Test_Inpatient['Discharge_Year'] = Test_Inpatient['DischargeDt'].dt.year
Test_Inpatient['Discharge_Month'] = Test_Inpatient['DischargeDt'].dt.month

# convert ClaimStartDt, ClaimEndDt from string to datetime format
Train_Outpatient['ClaimStartDt'] = pd.to_datetime(Train_Outpatient['ClaimStartDt'] , format = '%Y-%m-%d')
Train_Outpatient['ClaimEndDt'] = pd.to_datetime(Train_Outpatient['ClaimEndDt'],format = '%Y-%m-%d')

Test_Outpatient['ClaimStartDt'] = pd.to_datetime(Test_Outpatient['ClaimStartDt'] , format = '%Y-%m-%d')
Test_Outpatient['ClaimEndDt'] = pd.to_datetime(Test_Outpatient['ClaimEndDt'],format = '%Y-%m-%d')


# https://stackoverflow.com/questions/25146121/extracting-just-month-and-year-separately-from-pandas-datetime-column
# Get the months and year of claim start and claim end
Train_Outpatient['ClaimStart_Year'] = Train_Outpatient['ClaimStartDt'].dt.year
Train_Outpatient['ClaimStart_Month'] = Train_Outpatient['ClaimStartDt'].dt.month
Test_Outpatient['ClaimStart_Year'] = Test_Outpatient['ClaimStartDt'].dt.year
Test_Outpatient['ClaimStart_Month'] = Test_Outpatient['ClaimStartDt'].dt.month

Train_Outpatient['ClaimEnd_Year'] = Train_Outpatient['ClaimEndDt'].dt.year
Train_Outpatient['ClaimEnd_Month'] = Train_Outpatient['ClaimEndDt'].dt.month
Test_Outpatient['ClaimEnd_Year'] = Test_Outpatient['ClaimEndDt'].dt.year
Test_Outpatient['ClaimEnd_Month'] = Test_Outpatient['ClaimEndDt'].dt.month


# Calculate Claim_Period = ClaimEndDt - ClaimStartDt
Train_Outpatient['Claim_Period'] = ((Train_Outpatient['ClaimEndDt'] - Train_Outpatient['ClaimStartDt']).dt.days)+1

Test_Outpatient['Claim_Period'] = ((Test_Outpatient['ClaimEndDt'] - Test_Outpatient['ClaimStartDt']).dt.days)+1

# Create a new column Inpatient_or_Outpatient where Inpatient =1 and Outpatient = 0
Train_Inpatient['Inpatient_or_Outpatient'] = 1
Train_Outpatient['Inpatient_or_Outpatient'] = 0
Test_Inpatient['Inpatient_or_Outpatient'] = 1
Test_Outpatient['Inpatient_or_Outpatient'] = 0


# ## Merge Inpatient and Outpatient Data

# In[96]:


# Merge inpatient and outpatient dataframes based on common columns
common_columns = [ idx for idx in Train_Outpatient.columns if idx in Train_Inpatient.columns]
print(common_columns)
Inpatient_Outpatient_Merge = pd.merge(Train_Inpatient, Train_Outpatient, left_on = common_columns, right_on = common_columns,how = 'outer')


# In[97]:


# Merge beneficiary details with inpatient and outpatient data
Inpatient_Outpatient_Beneficiary_Merge = pd.merge(Inpatient_Outpatient_Merge, Train_Beneficiary,
                                                  left_on='BeneID',right_on='BeneID',how='inner')

# Merge provider details
Final_Dataset_Train = pd.merge(Inpatient_Outpatient_Beneficiary_Merge, Train , how = 'inner', on = 'Provider' )


# In[98]:


# Merge inpatient and outpatient dataframes based on common columns

common_columns_test = [ idx for idx in Test_Outpatient.columns if idx in Test_Inpatient.columns]
Inpatient_Outpatient_Merge_Te = pd.merge(Test_Inpatient, Test_Outpatient, left_on = common_columns_test, right_on = common_columns_test,how = 'outer')

# Merge beneficiary details with inpatient and outpatient data
Inpatient_Outpatient_Beneficiary_Merge_Te = pd.merge(Inpatient_Outpatient_Merge_Te, Test_Beneficiary,
                                                  left_on='BeneID',right_on='BeneID',how='inner')

Final_Dataset_Test = pd.merge(Inpatient_Outpatient_Beneficiary_Merge_Te, Test , how = 'inner', on = 'Provider' )
# Final_Dataset_Train.head(100).to_csv('01Final_Train_after_merge.csv')
# Final_Dataset_Test.head(100).to_csv('01Final_Test_after_merge.csv')

# create new feature total reimbursement amount for inpatient and outpatient
Final_Dataset_Train['IP_OP_TotalReimbursementAmt'] = Final_Dataset_Train['IPAnnualReimbursementAmt'] + Final_Dataset_Train['OPAnnualReimbursementAmt']
# create new feature total deductible amount for inpatient and outpatient
Final_Dataset_Train['IP_OP_AnnualDeductibleAmt'] = Final_Dataset_Train['IPAnnualDeductibleAmt'] + Final_Dataset_Train['OPAnnualDeductibleAmt']

Final_Dataset_Test['IP_OP_TotalReimbursementAmt'] = Final_Dataset_Test['IPAnnualReimbursementAmt'] + Final_Dataset_Test['OPAnnualReimbursementAmt']
Final_Dataset_Test['IP_OP_AnnualDeductibleAmt'] = Final_Dataset_Test['IPAnnualDeductibleAmt'] + Final_Dataset_Test['OPAnnualDeductibleAmt']

# Final_Dataset_Train.head(100).to_csv('02Final_Train_IP_OP_TotalReimbursementAmt.csv')
# Final_Dataset_Test.head(100).to_csv('02Final_Test_IP_OP_TotalReimbursementAmt.csv')

## Fill missing results using 0
Final_Dataset_Train = Final_Dataset_Train.fillna(0).copy()
Final_Dataset_Test = Final_Dataset_Test.fillna(0).copy()

# Final_Dataset_Train.head(100).to_csv('03Final_Train_fillna.csv')
# Final_Dataset_Test.head(100).to_csv('03Final_Test_fillna.csv')


def create_feature_using_groupby(Train_df, Test_df, gruopby_col, operation_col, operation):
    '''
    This function groupby the 'Train_df' and 'Test_df' dataframe by 'gruopby_col' and performs 'operation' on 'operation_col'
    '''

    for col in operation_col:
        # create new column name for the dataframe
        new_col_name = 'Per' + ''.join(gruopby_col) + '_' + operation + '_' + col
        print(new_col_name)
        Train_df[new_col_name] = Train_df.groupby(gruopby_col)[col].transform(operation)
        Test_df[new_col_name] = Test_df.groupby(gruopby_col)[col].transform(operation)
    return Train_df, Test_df


columns = ['InscClaimAmtReimbursed', 'DeductibleAmtPaid', 'IPAnnualReimbursementAmt',
           'IPAnnualDeductibleAmt', 'OPAnnualReimbursementAmt', 'OPAnnualDeductibleAmt',
           'Patient_Age', 'NoOfMonths_PartACov', 'NoOfMonths_PartBCov',
           'Hospitalization_Duration', 'Claim_Period', 'Patient_Risk_Score']

columns_for_grouping = ['Provider'
    , 'BeneID'
    , 'AttendingPhysician'
    , 'OperatingPhysician'
    , 'OtherPhysician'
    , 'DiagnosisGroupCode'
    , 'ClmAdmitDiagnosisCode'
    , 'ClmProcedureCode_1'
    , 'ClmProcedureCode_2'
    , 'ClmProcedureCode_3'
    , 'ClmProcedureCode_4'
    , 'ClmProcedureCode_5'
    , 'ClmProcedureCode_6'
    , 'ClmDiagnosisCode_1'
    , 'ClmDiagnosisCode_2'
    , 'ClmDiagnosisCode_3'
    , 'ClmDiagnosisCode_4'
    , 'ClmDiagnosisCode_5'
    , 'ClmDiagnosisCode_6'
    , 'ClmDiagnosisCode_7'
    , 'ClmDiagnosisCode_8',
                        'ClmDiagnosisCode_9'
    , 'ClmDiagnosisCode_10']

for i in columns_for_grouping:
    print(i)
    Final_Dataset_Train, Final_Dataset_Test = \
        create_feature_using_groupby(Final_Dataset_Train, Final_Dataset_Test,
                                     [i], columns, 'mean')
    Final_Dataset_Train, Final_Dataset_Test = Final_Dataset_Train.copy(), Final_Dataset_Test.copy()

# Count the claims per provider
Final_Dataset_Train, Final_Dataset_Test = \
    create_feature_using_groupby(Final_Dataset_Train, Final_Dataset_Test, ['Provider'], ['ClaimID'], 'count')

Final_Dataset_Train, Final_Dataset_Test = Final_Dataset_Train.copy(), Final_Dataset_Test.copy()

# Final_Dataset_Train.head(100).to_csv('04Final_Train_feature_groupby.csv')
# Final_Dataset_Test.head(100).to_csv('04Final_Test_feature_groupby.csv')

columns = ['ClaimID']
grp_by_cols = ['BeneID', 'AttendingPhysician', 'OtherPhysician', 'OperatingPhysician', 'ClmAdmitDiagnosisCode',
               'ClmProcedureCode_1',
               'ClmProcedureCode_2', 'ClmProcedureCode_3', 'ClmProcedureCode_4', 'ClmProcedureCode_5','ClmProcedureCode_6',
               'ClmDiagnosisCode_1', 'ClmDiagnosisCode_2',
               'ClmDiagnosisCode_3', 'ClmDiagnosisCode_4', 'ClmDiagnosisCode_5', 'ClmDiagnosisCode_6','ClmDiagnosisCode_7', 'ClmDiagnosisCode_8',
                'ClmDiagnosisCode_9', 'ClmDiagnosisCode_10', 'DiagnosisGroupCode']
for ele in grp_by_cols:
    lst = ['Provider', ele]
    print('ele',ele)
    Final_Dataset_Train,Final_Dataset_Test =\
        create_feature_using_groupby(Final_Dataset_Train, Final_Dataset_Test, lst, columns, 'count')
    Final_Dataset_Train,Final_Dataset_Test=Final_Dataset_Train.copy(),Final_Dataset_Test.copy()

# Final_Dataset_Train.head(100).to_csv('05Final_Train_grp_by_cols.csv')
# Final_Dataset_Test.head(100).to_csv('05Final_Test_grp_by_cols.csv')

# # Function to add percentage based on one hot encoding

def one_hot_encoding_diagnostic(Master_df,Field1):
    admit_diagnosis = Master_df[Field1].value_counts()
    admit_diagnosis_df = admit_diagnosis.to_frame()
    admit_diagnosis_df ['Percentage_' + Field1] = (admit_diagnosis_df[Field1]/admit_diagnosis_df[Field1].sum())*100
    admit_diagnosis_df ['Percentage_' + Field1] = admit_diagnosis_df ['Percentage_' + Field1].cumsum()
    admit_diagnosis_df.loc[admit_diagnosis_df['Percentage_' + Field1] > 80, 'Percentage_' + Field1] = 0
    admit_diagnosis_df.drop([Field1], axis = 1)
    admit_diagnosis_df[Field1 ] = admit_diagnosis_df.index
    Master_df = pd.merge(Master_df, admit_diagnosis_df, how='inner', on=Field1)
    Master_df.loc[Master_df['Percentage_' + Field1] == 0, Field1] = 0
    Master_df.tail(5)
    return Master_df


lst_one_hot_encode=['ClmAdmitDiagnosisCode', 'ClmProcedureCode_1',
               'ClmProcedureCode_2', 'ClmProcedureCode_3',
               'ClmProcedureCode_4', 'ClmProcedureCode_5','ClmProcedureCode_6',
               'ClmDiagnosisCode_1', 'ClmDiagnosisCode_2',
               'ClmDiagnosisCode_3', 'ClmDiagnosisCode_4',
               'ClmDiagnosisCode_5', 'ClmDiagnosisCode_6',
                'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8',
                'ClmDiagnosisCode_9', 'ClmDiagnosisCode_10',
               'DiagnosisGroupCode']
# Final_Dataset_Train  ,Final_Dataset_Test
for i in lst_one_hot_encode:
    print(i)
    Final_Dataset_Train = one_hot_encoding_diagnostic(Final_Dataset_Train, i)
    Final_Dataset_Test = one_hot_encoding_diagnostic(Final_Dataset_Test, i)

# Final_Dataset_Train.head(100).to_csv('06Final_Train_one_hot_encoding.csv')
# Final_Dataset_Test.head(100).to_csv('06Final_Test_one_hot_encoding.csv')


remove_columns=['BeneID', 'ClaimID', 'ClaimStartDt','ClaimEndDt','AttendingPhysician','OperatingPhysician', 'OtherPhysician',
                'ClmDiagnosisCode_1','ClmDiagnosisCode_2', 'ClmDiagnosisCode_3', 'ClmDiagnosisCode_4','ClmDiagnosisCode_5',
                'ClmDiagnosisCode_6', 'ClmDiagnosisCode_7','ClmDiagnosisCode_8', 'ClmDiagnosisCode_9', 'ClmDiagnosisCode_10',
                'ClmProcedureCode_1', 'ClmProcedureCode_2', 'ClmProcedureCode_3','ClmProcedureCode_4', 'ClmProcedureCode_5',
                'ClmProcedureCode_6','ClmAdmitDiagnosisCode', 'AdmissionDt','ClaimStart_Year', 'ClaimStart_Year', 'ClaimStart_Month',
                'ClaimEnd_Year', 'ClaimEnd_Month', 'Admission_Year', 'Admission_Month', 'Discharge_Year', 'Discharge_Month',
                'DischargeDt', 'DiagnosisGroupCode','DOB', 'DOD','Birth_Year', 'Birth_Month','State', 'County']

Final_Dataset_Train_FE=Final_Dataset_Train.drop(columns=remove_columns, axis=1)
Final_Dataset_Test_FE=Final_Dataset_Test.drop(columns=remove_columns, axis=1)

# Final_Dataset_Train_FE.head(100).to_csv('07Final_Train_remove_columns.csv')
# Final_Dataset_Test_FE.head(100).to_csv('07Final_Test_remove_columns.csv')

# Convert type of Gender and Race to categorical
Final_Dataset_Train_FE.Gender=Final_Dataset_Train_FE.Gender.astype('category')
Final_Dataset_Test_FE.Gender=Final_Dataset_Test_FE.Gender.astype('category')

Final_Dataset_Train_FE.Race=Final_Dataset_Train_FE.Race.astype('category')
Final_Dataset_Test_FE.Race=Final_Dataset_Test_FE.Race.astype('category')

# Final_Dataset_Train_FE.head(100).to_csv('08Final_Train_category.csv')
# Final_Dataset_Test_FE.head(100).to_csv('08Final_Test_category.csv')

Final_Dataset_Provider_Train = Final_Dataset_Train_FE.groupby(['Provider','PotentialFraud'],as_index=False).agg('sum')
Final_Dataset_Provider_Test  = Final_Dataset_Test_FE.groupby(['Provider'],as_index=False).agg('sum')

Final_Dataset_Provider_Train.PotentialFraud.replace(['Yes','No'],['1','0'],inplace=True)
Final_Dataset_Provider_Train.PotentialFraud=Final_Dataset_Provider_Train.PotentialFraud.astype('int64')

Final_Dataset_Provider_Train.to_csv('09Final_Train.csv')
Final_Dataset_Provider_Test.to_csv('09Final_Test.csv')

print('Status is completed')