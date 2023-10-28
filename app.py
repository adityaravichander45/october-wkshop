import numpy as np
import pandas as pd
import streamlit as st
import joblib
import warnings
warnings.filterwarnings('ignore')


model=joblib.load("pipe_mdl.pkl")
df=pd.read_csv('TRAINCREDIT.csv')

#     
           
     
def pred_loanstat(annual_inc,int_rate,loan_amnt,revol_bal,revol_util,total_acc,open_acc,mort_acc,tot_cur_bal,num_actv_bc_tl,pub_rec_bankruptcies,pub_rec,fico_range_high,fico_range_low,addr_state,verification_status,loan_status,grade,sub_grade,home_ownership,initial_list_status,term_months,purpose,emp_length_yrs,application_type,earliest_crline_year,earliest_crline_months):
      
    #dataframe
      col_names = ['annual_inc','int_rate','loan_amnt','revol_bal','revol_util','total_acc','open_acc','mort_acc','tot_cur_bal','num_actv_bc_tl','pub_rec_bankruptcies','pub_rec','fico_range_high','fico_range_low',
       'addr_state','verification_status','loan_status','grade','sub_grade','home_ownership','initial_list_status','term_months','purpose','emp_length_yrs','application_type','earliest_crline_year','earliest_crline_months']

      col_values = [annual_inc,int_rate,loan_amnt,revol_bal,revol_util,total_acc,open_acc,mort_acc,tot_cur_bal,num_actv_bc_tl,pub_rec_bankruptcies,pub_rec,fico_range_high,fico_range_low,
                  addr_state,verification_status,loan_status,grade,sub_grade,home_ownership,initial_list_status,term_months,purpose,emp_length_yrs,application_type,earliest_crline_year,earliest_crline_months]
      test = pd.DataFrame([col_values])
      test.columns = col_names
      predicted=model.predict(test)
      
    # calling the predict model 
      return predicted
      
      
      
def main():
    st.title('Credit_risk fintech')
       
    html_tmp= """
    <div style='background-color:red;'>
    <h2 style='color:white;text-align:center;'>Credit risk_fintech loan status prediction app</h2>
    </div>
    """
    st.markdown(html_tmp, unsafe_allow_html=True)
    
    annual_inc=st.number_input('annual income',max_value=8500500.55)
    int_rate=st.number_input('initial rate',max_value=32.00)
    loan_amnt=st.number_input('loan amount',max_value=45000.0)
    revol_bal=st.number_input('revolve balance',max_value=1579951.3)
    revol_util=st.number_input('revolve utilization rate:',max_value=160.0)
    total_acc=st.number_input('total no of accounts',max_value=190)
    open_acc=st.number_input('no of open accounts',max_value=100)
    mort_acc=st.number_input('the number of mortgage accounts',max_value=40)
    tot_cur_bal=st.number_input('the total balance is:')
    num_actv_bc_tl=st.number_input('the number of active accounts',max_value=40)
    pub_rec_bankruptcies = st.selectbox('Select the public bankruptcies record:',pd.unique(df['pub_rec_bankruptcies']))
    pub_rec=st.selectbox('Enter the public records',pd.unique(df['pub_rec']))
    fico_range_high = st.slider('Choose the highest fico range',600,900)
    fico_range_low = st.slider('Choose the lowest fico range', 600,900)
    addr_state = st.selectbox('Select the State:',pd.unique(df['addr_state']))
    verification_status = st.radio('Select the verification status:',pd.unique(df['verification_status']))
    loan_status = st.selectbox('Select the loan status:',pd.unique(df['loan_status']))
    grade = st.selectbox('Choose the Grade:',pd.unique(df['grade']))
    sub_grade = st.selectbox('Choose the SubGrade:',pd.unique(df['sub_grade']))
    home_ownership = st.selectbox('Select the ownership:',pd.unique(df['home_ownership']))
    initial_list_status = st.radio('Select your initial status:',pd.unique(df['initial_list_status']))
    term_months = st.radio('Choose the loan term in months:',pd.unique(df['term_months']))
    purpose = st.selectbox('Select your purpose for the loan:',pd.unique(df['purpose']))
    emp_length_yrs = st.selectbox('Select the employee length:',pd.unique(df['emp_length_yrs']))
    application_type = st.radio('Select your type of application:',pd.unique(df['application_type']))
    earliest_crline_year = st.slider('Choose the year of credit line', 1900, 2020, 1950)
    earliest_crline_months = st.selectbox('Choose the month of credit line:',pd.unique(df['earliest_crline_months']))
          
        
# creating a button click to call the predict method
    result=""
    if st.button("Predict"):
        result=pred_loanstat(annual_inc,int_rate,loan_amnt,revol_bal,revol_util,total_acc,open_acc,mort_acc,tot_cur_bal,num_actv_bc_tl,pub_rec_bankruptcies,pub_rec,fico_range_high,fico_range_low,addr_state,
        verification_status,loan_status,grade,sub_grade,home_ownership,initial_list_status,term_months,purpose,emp_length_yrs,application_type,earliest_crline_year,earliest_crline_months)
    
    #displaying the results
    if result==1:
	    st.success("Fully paid")
    else:
	    st.success("Charged Off")
	



if __name__=='__main__':
        main()
