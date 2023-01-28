<?php
defined('BASEPATH') or exit('No direct script access allowed');
?>


<!-- Main content -->
<div class="content">
  <div class="container-fluid">
    <div style="background-color: #2c2f33;">
      <div class="row">
        <div class="col-md-12 col-xs-12">

          <div class="card" style="background-color: #424648;">

            <div class="card-header card-header-rose card-header-icon">
              <div class="card-icon">
                <i class="material-icons">language</i>
              </div>
              <h4 class="card-title">Domain lists</h4>

              <div class="card-tools">
                <div class="row">
                  <div class="col-lg-2">
                    <!-- <a href="<?php echo base_url('users/setting'); ?>" class="btn btn-block btn-primary">Edit Profile</a> -->
                  </div>
                </div>
              </div>

            </div>

            <html>

            <head>

            </head>

            <body style="background-color: #2c2f33;">
              <!--Your HTML content here-->

              <form action="" method="post">
                <label for="domain">Enter domain name to add:</label>
                <input type="text" id="domain" name="domain">
                <input type="submit" value="Add" name="submit">
              </form>
            </body>
            <?php
            if (isset($_POST['submit'])) {
              $domain = $_POST['domain'];
              //$myfile = fopen("tes.txt", "a") or die("Unable to open file!");
              //$domain = $_POST['domain'];
              //$txt = $id ." ". $date . " The time is " . date("h:i:sa") . "\n";
              //fwrite($myfile, $domain);
              //fclose($myfile);
              $file = '/opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/domain.txt';
              // $domain = $_POST['domain'];
              file_put_contents($file, $domain . PHP_EOL, FILE_APPEND);
              echo 'Domain ' . $domain . ' has been added to the file.';
            }
            ?>
            <br>
            <br>


            <br>
            <?php
            $output2 = shell_exec("cat /opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/domain.txt");
            $output3 = shell_exec("cat /opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/domain2.txt");
            echo "<pre style='color:white;font-size:20px;'>$output2</pre>";
            echo "<pre style='color:white;font-size:20px;'>$output3</pre>";
            //echo "<pre style='color:white;font-size:20px;'>$output2</pre>";
            //echo "<pre>$output2</pre>";
            ?>