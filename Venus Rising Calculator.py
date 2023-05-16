#!/usr/bin/env python
# coding: utf-8

###########
# Imports #
###########

import pandas as pd
from os.path import exists
pd.set_option('display.max_rows', 500)

####################
# Set up dataframe #
####################

num_charts = 7
df_cols = ['Base Calc'] + ['Chart '+str(x+1) for x in range(7)] + ['Final Calc']
venus_rising_df = pd.DataFrame(columns=df_cols).fillna(0)


venus_rising_data_dict =[[1,1,10],
                          [2,3,16],
                          [3,1,16],
                          [4,1,8],
                          [5,1,12], #row 8 to 9 is 6st, row 9 to 10 is 2 st, ctnd
                          [6,1,10], #we're back to 2 and 4 again
                          [7,1,21]] #weird, let's just make some manual row_adds for chart 5&7
special_increases = {5:[14,2,4,2,4,2,4,2,6,2,6,2],
                     7:[14,2,4,4,4,2,4,6,4,4,6,2,4,2,4,2,4,2,4,2,2]}

###############################
# Create that functional loop #
###############################

def venus_pattern_loop(chart_num, reps, rows):
    curr_chart = f'Chart {chart_num}'
    prev_chart = f'Chart {chart_num-1}' if chart_num != 1 else 'Base Calc'
    for rep in range(reps):
        for row_val in range(rows):
            row_num = row_val+(rep*rows)
            if chart_num in [5,7]:
                row_add = special_increases[chart_num][row_val]
            elif row_num % 2 == 0:
                row_add = 4
            else:
                row_add = 2
#             print(rep, row_val, row_num, row_add)
            if row_num == 0:
                last_row_num = venus_rising_df[prev_chart].last_valid_index()
                last_row_st = venus_rising_df.loc[last_row_num,prev_chart]
            else:
                last_row_st = venus_rising_df.loc[row_num-1,curr_chart]

            num_row_st = last_row_st + row_add
            venus_rising_df.loc[row_num,curr_chart] = int(num_row_st)
    ret_msg = f"{curr_chart}: {venus_rising_df[curr_chart].last_valid_index()+1} rows."
    print(ret_msg)

############################
##### Set up dataframe #####
############################

curr_chart = 'Chart 1'
# Before automating the calculations, gotta manually set up the proj!
cast_on_st = 3
garter_rows = 12

# this will be added
garter_tab_st = cast_on_st * garter_rows

c1_setup_row = 13

# add prev values to Base Calc
venus_rising_df.loc[0,'Base Calc'] = garter_tab_st
venus_rising_df.loc[1,'Base Calc'] = c1_setup_row

#####################################
# Populate dataframe with st values #
#####################################

if pd.notnull(venus_rising_df.loc[0,'Final Calc']):
    print('Already done!')
else:
    for sheet_num, rows, reps in venus_rising_data_dict:
        venus_pattern_loop(sheet_num, rows, reps)

    last_df_row_num = venus_rising_df[f"Chart {num_charts}"].last_valid_index()
    last_df_row_st = venus_rising_df.loc[last_df_row_num,f"Chart {num_charts}"]
    venus_rising_df.loc[0,'Final Calc'] = last_df_row_st
    print('Done!')

    venus_rising_df = venus_rising_df.fillna(0)

#####################
# Set up dictionary #
#####################
venus_rising_data_dict =[[1,1,10],
                          [2,3,16],
                          [3,1,16],
                          [4,1,8],
                          [5,1,12], #row 8 to 9 is 6st, row 9 to 10 is 2 st, ctnd
                          [6,1,10], #we're back to 2 and 4 again
                          [7,1,21]] #weird, let's just make some manual row_adds for chart 5&7
special_increases = {5:[4,2,4,2,4,2,4,2,6,2,6,2],
                     7:[4,2,4,4,4,2,4,6,4,4,6,2,4,2,4,2,4,2,4,2,2]}

##############################
# Create that functional loop #
##############################

def venus_pattern_loop(chart_num, reps, rows):
    curr_chart = f'Chart {chart_num}'
    prev_chart = f'Chart {chart_num-1}' if chart_num != 1 else 'Base Calc'
    for rep in range(reps):
        for row_val in range(rows):
            row_num = row_val+(rep*rows)
            if chart_num in [5,7]:
                row_add = special_increases[chart_num][row_val]
            elif row_num % 2 == 0:
                row_add = 4
            else:
                row_add = 2
#             print(rep, row_val, row_num, row_add)
            if row_num == 0:
                last_row_num = venus_rising_df[prev_chart].last_valid_index()
                last_row_st = venus_rising_df.loc[last_row_num,prev_chart]
            else:
                last_row_st = venus_rising_df.loc[row_num-1,curr_chart]

            num_row_st = last_row_st + row_add
            venus_rising_df.loc[row_num,curr_chart] = int(num_row_st)
    ret_msg = f"{curr_chart}: {venus_rising_df[curr_chart].last_valid_index()+1} rows."
    print(ret_msg)

####################
# Set up dataframe #
####################

curr_chart = 'Chart 1'
# Before automating the calculations, gotta manually set up the proj!
cast_on_st = 3
garter_rows = 12

# this will be added
garter_tab_st = cast_on_st * garter_rows

c1_setup_row = 13

# add prev values to Base Calc
venus_rising_df.loc[0,'Base Calc'] = garter_tab_st
venus_rising_df.loc[1,'Base Calc'] = c1_setup_row

#####################################
# Populate dataframe with st values #
#####################################


if pd.notnull(venus_rising_df.loc[0,'Final Calc']):
    print('Already done!')
else:
    for sheet_num, rows, reps in venus_rising_data_dict:
        venus_pattern_loop(sheet_num, rows, reps)

    last_df_row_num = venus_rising_df[f"Chart {num_charts}"].last_valid_index()
    last_df_row_st = venus_rising_df.loc[last_df_row_num,f"Chart {num_charts}"]
    venus_rising_df.loc[0,'Final Calc'] = last_df_row_st
    print('Done!')

    venus_rising_df = venus_rising_df.fillna(0)

########################
# Calculator Prep Work #
########################

total_pattern_st = sum(venus_rising_df.sum())

def get_time_stats(knit_data, st_per_min):
    for k,v in knit_data.items():
        total_min = v['st'] / st_per_min
        total_hr = round(total_min/60,2)
        knit_data[k]['hr'] = int(total_hr)
    return knit_data

def get_perc_stats(knit_data):
    completed_perc = round(100*knit_data['completed']['st']/knit_data['pattern']['st'],2)
    remaining_perc = round(100*knit_data['remaining']['st']/knit_data['pattern']['st'],2)
    knit_data['completed']['perc'] = completed_perc
    knit_data['remaining']['perc'] = remaining_perc
    return knit_data

def calculate_progress(which_date, which_chart, which_rep, which_row, st_per_min):
    # this will hold total stitches, but i'm pre-adding our set up row sts.
    total_completed_st = sum(venus_rising_df.loc[:,'Base Calc'])

    for chart_num in range(1,which_chart):
        st_done_in_prev_chart = sum(venus_rising_df.loc[:,f"Chart {chart_num}"])
        total_completed_st += st_done_in_prev_chart

    # Since chart #2 is the only one with reps, I'm only accounting for that.
    # (that is, which_rep-1 will equal zero for all other charts with 1 rep)
    curr_chart_last_row = which_row + (16*(which_rep-1))
    st_done_in_curr_chart = sum(venus_rising_df.loc[:curr_chart_last_row,f"Chart {which_chart}"])

    total_completed_st += st_done_in_curr_chart
    #---------------

    knit_data = {'pattern':{'st':int(total_pattern_st)},
                 'completed':{'st':int(total_completed_st)},
                 'remaining':{'st':int(total_pattern_st - total_completed_st)}}

    knit_data = get_time_stats(knit_data, st_per_min)
    knit_data = get_perc_stats(knit_data)

    vals =   {'Date': which_date,
             'Chart': which_chart,
               'Rep': which_rep,
               'Row': which_row,
            'St/Min': st_per_min,
      'Pattern (st)': knit_data['pattern']['st'],
     'Pattern (hrs)': knit_data['pattern']['hr'],
    'Completed (st)': knit_data['completed']['st'],
   'Completed (hrs)': knit_data['completed']['hr'],
  'Completed (perc)': knit_data['completed']['perc'],
    'Remaining (st)': knit_data['remaining']['st'],
   'Remaining (hrs)': knit_data['remaining']['hr'],
  'Remaining (perc)': knit_data['remaining']['perc'],
  'timestamp': pd.Timestamp.now()}

    return vals

def give_me_info_on(which_chart, which_rep, which_row, st_per_min):
    curr_row = which_row+((which_rep-1)*16)
    num_st_in_row = venus_rising_df.loc[curr_row,f"Chart {which_chart}"]
    msg = f"For row {which_row}, rep {which_rep}, in Chart {which_chart}:\nNum stitches: {num_st_in_row}, num minutes: {round(num_st_in_row/st_per_min,2)}"
    print(msg)

def explain(df):
    num_days = len(venus_log_df['Date'].drop_duplicates())
    first_row = venus_log_df.loc[0,:]
    last_row = venus_log_df.loc[venus_log_df.last_valid_index(),:]

    msgs = []
    msgs += [f"You've logged {num_days} days worth of work on the Venus Rising Shawl."]
    msgs += ["-------"]
    msgs += [f"You first logged work up to Chart {first_row['Chart']}, Rep {first_row['Rep']}, Row {first_row['Row']}."]
    msgs += [f"You are currently on Chart {last_row['Chart']}, Rep {last_row['Rep']}, Row {last_row['Row']}."]
    msgs += ["-------"]
    msgs += [f"You've completed {int(last_row['Completed (st)'])} stitches, which comprises {last_row['Completed (perc)']}% of the shawl."]
    msgs += [f"Given your last reported speed of {int(last_row['St/Min'])} st/min, this has taken you a total of roughly {int(last_row['Completed (hrs)'])} hours."]
    msgs += ["-------"]
    msgs += [f"You have {int(last_row['Remaining (st)'])} stitches left, which means {last_row['Remaining (perc)']}% of the shawl remains."]
    msgs += [f"Again, assuming {int(last_row['St/Min'])} st/min, this will take roughly {int(last_row['Remaining (hrs)'])} more hours."]
    msgs += ["-------"]
    full_msg = '\n'.join(msgs)
    print(full_msg)


# ## Venus Rising Calculator
# This will generate information on how many st/min you have completed as well as left in your Venus Rising shawl.
# Notes:
# 1. This calculator assumes that your knitting speed does not change. While this pattern does include stitches of varying complexity, this is just mant to be a rough estimate.
# 2. "which_row" represents the last row you completed. It will be included in the finished portion of the calculations.
# 3. This will not work for any rows *prior to* Chart 1, Row 1.

file_path = 'venus_log.csv'
file_exists = exists(file_path)

if not file_exists:
    print("file doesn't exist")
    cols = ['Date','Chart','Rep','Row','St/Min','Pattern (st)','Pattern (hrs)',
            'Completed (st)','Completed (hrs)','Completed (perc)',
            'Remaining (st)','Remaining (hrs)','Remaining (perc)','timestamp']
    df = pd.DataFrame(columns=['Date','Chart','Rep','Row','timestamp'])
    df.to_csv('venus_log.csv', index=False)

q = input("Do you want to A) save progress or B) ask about your next row? (A or B): ")

# ---------------------
# change this if I want
st_per_min = 14 #int(input('ST/MIN: How many st per min?: ')) #20
# ---------------------

if q == 'A':
    venus_log_df = pd.read_csv('venus_log.csv')
    which_date = input('DATE: What date are you submitting this information for?\n(YYYY-MM-DD format or just hit enter for TODAY): ')
    which_date = which_date if which_date != '' else str(pd.Timestamp.now().date())
    which_chart = int(input('CHART: Which chart are you working on?: '))
    which_rep = int(input('REP: What repetition is this?: '))
    which_row = int(input('ROW: What row did you last finish?: '))

    print("----------\n")
    stats = calculate_progress(which_date, which_chart, which_rep, which_row, st_per_min)

    venus_log_df = venus_log_df.append(stats, ignore_index = True).drop_duplicates()
    venus_log_df.to_csv('venus_log.csv',index=False)
    explain(venus_log_df)

elif q == 'B':
    which_chart = int(input('CHART: Which chart are you curious about?: '))
    which_rep = int(input('REP: What repetition are you curious about?: '))
    which_row = int(input('ROW: What row are you curious about?: '))

    print("----------\n")
    give_me_info_on(which_chart, which_rep, which_row, st_per_min)

####################
# Final Dataframes #
####################
all_rows_df = venus_rising_df.reset_index().melt(id_vars='index', value_vars=venus_rising_df.columns)

all_rows_df = all_rows_df.rename(columns={'index':'Row',
                                         'variable':'Chart',
                                            'value':'Sts'})
non_zero_rows_df = all_rows_df[all_rows_df['Sts'] != 0].reset_index(drop=True)[['Chart','Row','Sts']]

non_zero_rows_df['Running Total'] = non_zero_rows_df['Sts'].cumsum()

non_zero_rows_df['Running Percentage'] = non_zero_rows_df['Running Total'].apply(lambda x: str(round(100*x/max(non_zero_rows_df['Running Total']),2))+"%")
