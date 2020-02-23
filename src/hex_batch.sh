
#!/bin/bash

function ergodic(){  
    for file in ` ls $1 `  
    do  
        if [ -d $1"/"$file ]   
        then  
             ergodic $1"/"$file  
        else  
            temp=$1/$file
            if [ "${temp##*.}"x = "pdb"x  ];then
                echo $temp
            fi
        fi  
    done  
}  


INIT_PATH="/Users/csx/Downloads/bioInfo/pdbs/ACE2"  
ergodic $INIT_PATH


