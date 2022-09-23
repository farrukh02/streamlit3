###############################
# This program lets you       #
# - enter values in Streamlit #
# - get prediction            #  
###############################
#import pickle
#from turtle import st

import pandas as pd
import streamlit as st

# loading the model
#path = ''
#modelname = path + '/toymodel.pkl'
#loaded_model = pickle.load(open(modelname, 'rb'))

#############
# Main page #
#############                
st.write("The model prediction")

#LIVINGAPARTMENTS_AVG_MIN = 0.0
#LIVINGAPARTMENTS_AVG_MAX = 1.0
#APARTMENTS_AVG_MIN = 0.0
#APARTMENTS_AVG_MAX = 0.11697126743049956

# Get input values - numeric variables
#LIVINGAPARTMENTS_AVG = st.slider('Please enter the living apartments:',
#                                 min_value=LIVINGAPARTMENTS_AVG_MIN,
#                                 max_value=LIVINGAPARTMENTS_AVG_MAX
#                                 )
#APARTMENTS_AVG = st.slider('Please enter the apartment average:',
#                           min_value=APARTMENTS_AVG_MIN,
  #                         max_value=APARTMENTS_AVG_MAX
#                           )

# Set dummy variables to zero    
cat_list = ['nom_q_9103b', 'nom_q_9103c', 'nom_q_9103d', 'nom_q_9103e',
       'nom_q_9103f', 'nom_q_9103g', 'nom_q_9103h', 'nom_q_9103i',
       'nom_q_9103j', 'nom_q_9103k', 'nom_q_9103l', 'nom_q_9103m',
       'nom_q_9103n', 'nom_q_9103o', 'nom_q_9103p', 'nom_q_9103q',
       'nom_q_9103r', 'nom_q_9103s', 'nom_q_9204']
for i in cat_list:
    exec("%s = %d" % (i, 0))  # The exec() command makes a value as the variable name

# Enter data for prediction
Occupation_b = st.selectbox('касбро интихоб намоед (nom_q_9103_b)',
                          ( 'Electronics',
                            'Chemistry')
                            )
Occupation_c = st.selectbox('(nom_q_9103_c)',
                            ('Photography',
                            'Botany')
                                )
Occupation_d = st.selectbox('(nom_q_9103d)',
                           ('Owning a store',
                            'Advice on work')
                           )
Occupation_e = st.selectbox('(nom_q_9103e)',
                           ('Company management',
                            'Helping families in need')
                           )
Occupation_f = st.selectbox('(nom_q_9103f)',
                           ('Physical training',
                            'Doktor')
                           )
Occupation_g = st.selectbox('(nom_q_9103g)',
                            ('Music',
                             'Working with wood')
                            )
Occupation_h = st.selectbox('(nom_q_9103h)',
                            ('Physics',
                             'Economic sciences')
                            )
Occupation_i = st.selectbox('(nom_q_9103i)',
                            ('Education',
                             'Art')
                            )
Occupation_j = st.selectbox('(nom_q_9103j)',
                            ('Law',
                             'Artist / Folk Crafts' )
                            )
Occupation_k = st.selectbox('(nom_q_9103k)',
                            ('Child care',
                             'Stand electronics')
                            )
if Occupation_k == 'Child care':
    Child_care = 1
elif Occupation_k == 'Stand electronics':
    Stand_electronics = 1
Occupation_l = st.selectbox('(nom_q_9103l)',
                            ('Landscaping',
                             'Playing in a group, being a member of a music team')
                            )
Occupation_m = st.selectbox('(nom_q_9103m)',
                            ('Travel agent',
                             'Mechanic')
                            )
Occupation_n = st.selectbox('(nom_q_9103n)',
                            ('Work in the office',
                             'Picture description')
                            )
Occupation_o = st.selectbox('(nom_q_9103o)',
                            ('Forest',
                             'The nurse of mercy')
                            )
Occupation_p = st.selectbox('(nom_q_9103p)',
                            ('Electric','Economist'))

Occupation_q = st.selectbox('(nom_q_9103q)',
                            ('Accounting', 'Geology'))

Occupation_r = st.selectbox('(nom_q_9103r)',
                            ('Builder', 'Economist'))

Occupation_s = st.selectbox('(nom_q_9103s)',
                            ('Confirmation of a home loan (mortgage)',
                             'Helping patients in the hospital')
                            )

Occupation_4 = st.selectbox('(nom_q_9204)',
                            ('Public administration',
                             'Private sector',
                             'Intergovernmental organizations (World Bank, OSCE, etc.)',
                             'Non-governmental organization',
                             "I didn't want to work",
                             'Other (show) ________________________')
                            )

if Occupation_b == 'Electronics':
    Electronics = 1
elif Occupation_b == 'Chemistry':
    Chemistry = 1

elif Occupation_c == 'Botany':
    Botany = 1
elif Occupation_c == 'Photography':
    Photography = 1

elif Occupation_d == 'Owning a store':
    Owning_a_store = 1
elif Occupation_d == 'Advice on work':
    Advice_on_work = 1

elif Occupation_e == 'Company management':
    Company_management = 1
elif Occupation_e == 'Helping families in need':
    Helping_families_in_need = 1

elif Occupation_f == 'Physical training':
    Physical_training = 1
elif Occupation_f == 'Doktor':
    Doktor = 1

elif Occupation_g == 'Music':
    Music = 1
elif Occupation_g == 'Working with wood':
    Working_with_wood = 1

elif Occupation_h == 'Physics':
    Physics = 1
elif Occupation_h == 'Economic sciences':
    Economic_sciences = 1

elif Occupation_i == 'Education':
    Education = 1
elif Occupation_i == 'Art':
    Art = 1

if Occupation_j == 'Law':
    Law = 1
elif Occupation_j == 'Artist / Folk Crafts':
    Artist_Folk_Crafts = 1

elif Occupation_k == 'Child care':
    Child_care = 1
elif Occupation_k == 'Stand electronics':
    Stand_electronics = 1


elif Occupation_l == 'Landscaping':
    Landscaping = 1
elif Occupation_l == 'Playing in a group':
    Playing_in_group = 1

elif Occupation_m == 'Travel agent':
    Travel_agent = 1
elif Occupation_m == 'Mechanic':
    Mechanic = 1

elif Occupation_n == 'Work in the office':
    Work_office = 1
elif Occupation_n == 'Picture_description':
    Picture_description = 1

elif Occupation_o == 'The nurse of mercy':
    nurse_mercy = 1
elif Occupation_o == 'Forest':
    Forest = 1

elif Occupation_p == 'Economist':
    Economist = 1
elif Occupation_p == 'Electric':
    Electric = 1

elif Occupation_q == 'Accounting':
    Accounting = 1
elif Occupation_q == 'Geology':
    Geology = 1

elif Occupation_r == 'Economist':
    Economist = 1
elif Occupation_r == 'Builder':
    Builder = 1

elif Occupation_s == 'Helping patients in the hospital':
    helping_hospital = 1
elif Occupation_s == 'Confirmation of a home loan (mortgage)':
    mortgage = 1

else:
    OTHER = 1

# when 'Predict' is clicked, make the prediction and store it 
if st.button("Get Your Prediction"):
    X = pd.DataFrame({'nom_q_9103b', 'nom_q_9103c', 'nom_q_9103d', 'nom_q_9103e',
       'nom_q_9103f', 'nom_q_9103g', 'nom_q_9103h', 'nom_q_9103i',
       'nom_q_9103j', 'nom_q_9103k', 'nom_q_9103l', 'nom_q_9103m',
       'nom_q_9103n', 'nom_q_9103o', 'nom_q_9103p', 'nom_q_9103q',
       'nom_q_9103r', 'nom_q_9103s', 'nom_q_9204'
                      })

    # Making predictions            
   # prediction = loaded_model.predict_proba(X)[:, 1]  # The model produces (p0,p1), we want p1.

    #st.success('Your Target is {}'.format(prediction))
