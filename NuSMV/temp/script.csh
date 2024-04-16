read_model -i NuSMV/temp/verif.smv 
go
check_ltlspec -P "spec1" -o NuSMV/temp/spec1_result.txt 
check_ltlspec -P "spec3" -o NuSMV/temp/spec3_result.txt 
quit