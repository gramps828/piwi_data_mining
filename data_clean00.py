#
import re
piwi_domain_db = open('piwi_seqs.txt')
#
#clean data by first grouping data containted under piwi protein
# group data between pri-hsa-#### and pri-hsa-####+1
#label that range as protein # 1
#This step will separate each protein with its aliace names, sequence, organism
#... data together


'''first step of cleaining data --> put into array
[Name:PROTEIN 1,
    [UNORGANIZED DATA aliases:____, accession:____, organism:____,
    sequence:____,length:____, dataset:______, pubmed:_____]],'''


read_db = piwi_domain_db.read()
empty2 = []
empty2.append(read_db[:100])

#Prints first 100 character entries for raw .txt file
print('This prints the first 100 character entries')
print(empty2)

###These two lines replace tabs and new lines with a double space
read_db_tab = read_db.replace('\t', ' ')
read_db_tab_line = read_db_tab.replace('\n', ' ')
print('These are the first 100 characters of no tab/newlie: ', read_db_tab_line[:100])
'''#make a for_loop# for x in removal_list:'''


'''for x in read_db_tab_line:
    x = re.findall('p', x)
print(x)'''
#print(read_db_space.index('piR-hsa-32826'))
#print(read_db_space)
#for y in removal_list:
#    read_3 = read_db_space.replace(y,'-****-')
#print(read_3)
'''empty = []
empty.append(read_db_space[:100])
print(empty)'''
