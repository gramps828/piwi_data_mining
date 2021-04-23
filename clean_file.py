#DEPENDINCIES

import re
import numpy as np
import pandas as pd

#Step 1: Load/read file

raw_db = open('piwi_seqs.txt')
dirty_db = raw_db.read()

#Step 2: remove \t and \n

def remove_tab_line():
    tabLine_replace_with = {
        '\t':'',
        '\n':''
    }

    target_tabline = [
        '\t',
        '\n'
    ]

    for special_char, no_space in tabLine_replace_with.items():
        for targets in target_tabline:
            if targets in dirty_db:
                dirty_interm_01 = dirty_db.replace(special_char, no_space)
                return(dirty_interm_01)
dirty_interm_01 = (remove_tab_line())


# Step 3: a. locate all unique pir_names and enter into pd.Series
#  b. search file for all pir_names, save span in empty list called head_tail
#    c. save pir_name.span as pd.Series and concatonate w/ df_common_name

common_name = re.findall('piR-hsa-\d+', dirty_interm_01)
df_common_name = pd.Series(data=common_name)

re.compile(dirty_interm_01)

head = []
tail = []
for name in common_name:
    find_pir = re.search(name, dirty_interm_01)
    pir_loc_start = find_pir.start()
    pir_loc_end = find_pir.end()
    head.append(pir_loc_start)
    tail.append(pir_loc_end)

df_head = pd.Series(head,dtype=int)
df_tail = pd.Series(tail,dtype=int)
df_head_tail = pd.concat([df_head, df_tail],axis=1)

df_pir_loc = pd.concat([df_common_name, df_head_tail],axis = 1).reindex(df_head_tail.index)
df_pir_loc.columns = ['name','start','end']

# Step 4: section data using start points of rna_name, put into tuple where key is rna_name

pir_data_grouped = []
current_index = 0
z = len(df_pir_loc) - 1

while current_index <= len(df_pir_loc):
    if current_index < z:
        current_pir_end = df_pir_loc.at[current_index,'end']
        next_pir_start = df_pir_loc.at[current_index+1,'start']
        pir_data_grouped.append([dirty_interm_01[current_pir_end:next_pir_start-1]])
        current_index += 1
        continue

    elif current_index == z:
        pir_data_grouped.append([dirty_interm_01[df_pir_loc.at[z,'end']:-1]])
        break

#find_alias
hanky = []
for list in pir_data_grouped:
    for list_2 in list:
        find_alias = re.findall('PIR\d+', list_2)
        hanky.append(find_alias)

#find_species
for list in pir_data_grouped:
    for list_2 in list:
        if 'human' in list_2.lower():
            continue
        else:
            print('There\'s an imposter amoung us')

#find_sequence
doodle = []
for list in pir_data_grouped:
    for list_2 in list:
        find_sequence = re.findall('[ATGC]+', list_2)
        doodle.append(find_sequence)

#find_pub_id
dandy = []
for list in pir_data_grouped:
    for list_2 in list:
        find_pub_id = list_2.find(':')
        dandy.append(list_2[find_pub_id+1:].strip())

#creates pir dictonary
pir_key_value = dict(zip(common_name, zip(hanky,doodle,dandy)))

#Creates df with name and sequence
df_doodle = pd.Series(data=doodle)
df_name_sequence = pd.concat([df_common_name, df_doodle],axis = 1).reindex(df_doodle.index)
df_name_sequence.columns = ['name','sequence']
