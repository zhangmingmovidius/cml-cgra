#!/bin/bash
echo $1
cfile="$1"
name=${cfile%.c}
llfile="$name.ll"
dfgfile="$name.dfg"
schfile="$name.sch"

toolchain="$HOME/CGRA/toolchain"

regiver="REGIMap_2.8"
regimap="$toolchain/REGIMap/$regiver/Release"
nodefile="$HOME/CGRA/cgratoolchain"

LIST1="$(ls *edge*)"
edge=${LIST1[0]}
LIST2="$(ls *node*)"
node=${LIST2[0]}

echo $edge
echo $node
echo $llfile
echo $name

$regimap/REGIMap_2.2 -EDGE $edge -NODE $node -X 4 -Y 4 -R 8 -REGI > $schfile
#$regimap/REGIMap_2.2 -EDGE $edge -X 4 -Y 4 -R 8 -REGI

$nodefile/nodefile $node REGIDUMP_node.txt > final_node.txt
mkdir graphs
for i in $(ls *.dot);
do
  src=$i
  fname=${src%.*}

  dest="graphs/$fname.ps"
  dot -Tps $src -o $dest 
 echo $i
 #echo $fname
 #echo $dest
done

exit