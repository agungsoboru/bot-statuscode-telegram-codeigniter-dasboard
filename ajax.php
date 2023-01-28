<?php

$array = array("Bot1 is online and running smoothly","Bot1 systems are operational","Bot1 is responding normally","Bot1 is available and healthy","Bot1 connectivity is confirmed","Bot1 is up and running","Bot1 is accessible and performing well","Bot1 is functioning as expected","Bot1 is accessible and responding","Bot1 is reachable and operational");
$random_string = $array[array_rand($array)];
//$output = shell_exec('ps aux');
//if (strpos($output, 'main.py') !== false ) {
    echo $random_string;
    //echo $random_string;
//} else {
    echo "<pre style=' color:white;font-size:20px;'>Bot1 Nonaktif</pre>";
//}
?>