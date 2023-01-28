<?php
  date_default_timezone_set('Asia/Makassar');
  $datetime = new DateTime();
  echo $datetime->format('Y-m-d H:i:s');
?>