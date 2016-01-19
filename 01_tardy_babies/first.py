import survey

pregnancies = survey.Pregnancies()
pregnancies.ReadRecords()
print 'Number of pregnancies', len(pregnancies.records)

live_births = 0
live_births_firsts = 0
total_preg_len_firsts = 0
total_preg_len_others = 0
for preg in pregnancies.records:
    if preg.birthord == 1 and preg.outcome == 1:
        live_births_firsts += 1
        total_preg_len_firsts += preg.prglength
    elif preg.outcome == 1:
        total_preg_len_others += preg.prglength
        live_births += 1 

print 'Number of live births for firsts', live_births_firsts
print 'Number of live births', live_births

ave_preg_len_firsts = float(total_preg_len_firsts) / live_births_firsts
ave_preg_len_others = float(total_preg_len_others) / live_births

print 'Average preg length for firsts', ave_preg_len_firsts 
print 'Average preg length for others', ave_preg_len_others
print 'Difference in days', (ave_preg_len_firsts - ave_preg_len_others ) * 7 
