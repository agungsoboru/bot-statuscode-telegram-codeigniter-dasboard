

<script>
  window.addEventListener("load", function() {
    window.scrollTo(0, document.body.scrollHeight);
  });
</script>



 
<?php
date_default_timezone_set('Asia/Makassar');
$date = "Today is " . date("Y/m/d");
// GET METHOD REQUEST
if($_SERVER['REQUEST_METHOD'] == "GET") {
  // CHECKING WITH PARAMETER OR NOT
if(empty($_GET['id'])) {

$output2 = shell_exec("tail -20 telegram.txt");

echo "<pre>$output2</pre>";

   //  $myfile = fopen("telegram.txt", "a") or die("Unable to open file!");
  //   $txt = $_SERVER['REMOTE_ADDR'] . " " . $_SERVER['REQUEST_TIME'] . " " . $_SERVER['REMOTE_PORT'] . "\n" ;
 //    fwrite($myfile, $txt);
//     fclose($myfile);

  } else {
    // GET DATA BY PARAMETER ID
$id = $_GET['id'];

     $myfile = fopen("telegram.txt", "a") or die("Unable to open file!");
     $txt = $id ." ". $date . " The time is " . date("h:i:sa") . "\n";
     fwrite($myfile, $txt);
     fclose($myfile);
//$output = shell_exec($id);

//echo "<pre>$output</pre>";
}
}
?>
