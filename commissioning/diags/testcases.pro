spectrum='cat(k93models,50000,0.0,4.0)'
obsmode='galex,fuv'
val='16.0'
unit='abmag'


openw,1,'testt.cases'
printf,1,'rn(bb(5000),band(johnson,v),22.8, abmag)'

printf,1,'rn(' +spectrum+ ',band(' +obsmode+ '),' +val+ ',' +unit+')'

close,1
