<?php
defined('BASEPATH') or exit('No direct script access allowed');
?>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.9/angular.min.js"></script>

<body ng-app="myApp" ng-controller="myCtrl">
  <div class="content">

    <div class="container-fluid">
      <div class="row">


        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="card card-stats" style="background-color: #424648;">

            <div class="card-header card-header-warning card-header-icon">
              <div class="card-icon">
                <i class="material-icons">storage</i>
              </div>
              <p class="card-category">Used Space</p>
              <h3 class="card-title" style="color:white;"><?php echo (rand(1, 10)); ?>
                <small>GB</small>
              </h3>
            </div>
            <div class="card-footer">
              <div class="stats">
                <i class="material-icons text-danger">warning</i>
                <a href="javascript:;">Get More Space...</a>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="card card-stats" style="background-color: #424648;">
            <div class="card-header card-header-success card-header-icon">
              <div class="card-icon">
                <i class="material-icons">dns</i>
              </div>
              <p class="card-category">Domain List</p>
              <?php
              $filePath = "tes.txt";
              $lines = count(file($filePath));
              //echo $lines;
              ?>
              <h3 class="card-title" style="color:white;"><?php echo $lines; ?></h3>
              </h3>
            </div>
            <div class="card-footer">
              <div class="stats">
                <i class="material-icons">date_range</i> Last 24 Hours
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="card card-stats" style="background-color: #424648;">
            <div class="card-header card-header-danger card-header-icon">
              <div class="card-icon">
                <i class="material-icons">info_outline</i>
              </div>
              <?php
              //exec("pgrep -f 'main.py'", $output1);
              //exec("pgrep -f 'main2.py'", $output2);
              //if (!empty($output1) && !empty($output2)) {
              //  echo "Hidup";
              //}
              ?>
              <p class="card-category">Bot Issues</p>
              <h3 class="card-title"></h3>
            </div>
            <div class="card-footer">
              <div class="stats">
                <i class="material-icons">local_offer</i> Tracked from Github
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="card card-stats">
            <div class="card-header card-header-info card-header-icon">



            </div>
          </div>
        </div>
      </div>
    </div>


    <!-- <script>
      var app = angular.module('myApp', []);
      app.controller('myCtrl', function($scope, $http, $interval) {
        var getData = function() {
          $http({
            method: "GET",
            url: "http://api.domainanda/telegram.php"
          }).then(function mySuccess(response) {
            $scope.data = response.data;
          }, function myError(response) {
            $scope.data = response.statusText;
          });
        }
        getData();
        $interval(getData, 10000);
      });
    </script>

    <div>{{data}}</div> -->
    <!-- <html>

    <head>
      <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400&display=swap" rel="stylesheet">
      <style>
        body {
          font-family: 'Open Sans', sans-serif;
          background-color: #f5f5f5;
        }

        .container {
          width: 50%;
          margin: 0 auto;
          text-align: center;
        }

        h1 {
          font-weight: 300;
          margin-bottom: 30px;
        }

        form {
          background-color: #fff;
          padding: 30px;
          border-radius: 10px;
          box-shadow: 0px 0px 20px 0px #ccc;
        }

        input[type="text"] {
          width: 100%;
          padding: 12px 20px;
          margin: 8px 0;
          box-sizing: border-box;
          border: 2px solid #ccc;
          border-radius: 4px;
          font-size: 16px;
        }

        input[type="submit"] {
          width: 100%;
          background-color: #4CAF50;
          color: white;
          padding: 14px 20px;
          margin: 8px 0;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-size: 16px;
        }

        input[type="submit"]:hover {
          background-color: #45a049;
        }
      </style>
    </head>
-->

    <body>
      <!-- <div class="container"> -->
      <!-- <h1>Enter Domain Name</h1> -->
      <!-- <form action="submit_form.php" method="post"> -->
      <!-- <input type="text" name="domain_name" placeholder="Enter domain name here..."> -->
      <!-- <input type="submit" value="Submit"> -->
      <!-- </form> -->
      <br>
      <br>

      <!-- <script>
setInterval(function(){
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://127.0.0.1/bot-telegram-codeigniter-dasboard/ajax.php');
  xhr.onload = function() {
    if (xhr.status === 200) {
      // response received
      document.getElementById("response").innerHTML = xhr.responseText;
    }
  };
  xhr.send();
}, 5000);
</script>

<div id="response"></div> -->

      <?php

      $array = array("Bot1 is online and running smoothly", "Bot1 systems are operational", "Bot1 is responding normally", "Bot1 is available and healthy", "Bot1 connectivity is confirmed", "Bot1 is up and running", "Bot1 is accessible and performing well", "Bot1 is functioning as expected", "Bot1 is accessible and responding", "Bot1 is reachable and operational");
      $random_string = $array[array_rand($array)];
      $output = shell_exec('ps aux');
      if (strpos($output, 'main.py') !== false) {
        echo "<pre style=' color:white;font-size:20px;'>$random_string</pre>";
        //echo $random_string;
      } else {
        echo "<pre style=' color:white;font-size:20px;'>Bot1 Nonaktif</pre>";
      }
      ?>


      <?php
      $output1 = shell_exec('ps aux');
      if (strpos($output1, 'main2.py') !== false) {
        echo "<pre style=' color:white;font-size:20px;'>Bot2 sedang berjalan</pre>";
      } else {
        echo "<pre style=' color:white;font-size:20px;'>Bot2 Nonaktif</pre>";
      }
      ?>
      <br>
      <br>

      <h1>
        <pre style=' color:white;font-size:20px;'>Domain Status selain 200</pre>
      </h1>

      <?php
      //$json1 = file_get_contents('/opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/monitor.json');
      $json1 = file_get_contents('/opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/monitor2.json');
      $data1 = json_decode($json1, true);
      foreach ($data1 as $domain1 => $value1) {
        if ($value1 != 200) {
          $domain1 = str_replace("https://", "", $domain1); //menghapus https://
          echo "<pre style=' color:white;font-size:20px;'>$domain1</pre>";
        }
      }
      ?>


      <?php
      $json = file_get_contents('/opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/monitor.json');
      //$json = file_get_contents('/opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/monitor2.json');
      $data = json_decode($json, true);
      foreach ($data as $domain => $value) {
        if ($value != 200) {
          $domain = str_replace("https://", "", $domain); //menghapus https://
          echo "<pre style=' color:white;font-size:20px;'>$domain</pre>";
        }
      }
      ?>

  </div>
</body>

</html>