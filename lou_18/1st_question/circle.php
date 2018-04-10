<?php
/**
* print wall circle until the last param is center
*/
$count=count($argv)-1;
if($count<2){
	echo "Parameter Error";
	return 1;
}
$length=2*$count-1;
for ($i=0;$i<$length;$i++){
	for($j=0;$j<$length;$j++){	
		$top=$i;
		$left=$j;
		$right=$length-$i-1;
		$bottom=$length-$j-1;
		$location=$top<$bottom?$top:$bottom;
		$location=$location<$left?$location:$left;
		$location=$location<$right?$location:$right;
		echo $argv[$location+1];
	}
	echo "\n";
}
