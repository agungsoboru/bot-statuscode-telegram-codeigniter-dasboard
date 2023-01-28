<?php
defined('BASEPATH') or exit('No direct script access allowed');
?>
<!-- Main content -->
<div class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12 col-xs-12">

                <div class="card" style="background-color: #424648;">
                    <div class="card-header card-header-rose card-header-icon">
                        <div class="card-icon">
                            <i class="material-icons">language</i>
                        </div>
                        <h4 class="card-title">Domain lists Delete</h4>
                        <h1 class="red-text">Domain lists Delete</h1>

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

                    <body>


                        <form action="" method="post">
                            <label for="domain">Enter domain name to delete:</label>
                            <input type="text" id="domain" name="domain">
                            <input type="submit" value="Delete" name="submit">
                        </form>

                        <?php
                        if (isset($_POST['submit'])) {
                            $file = '/opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/domain.txt';
                            
                            $lines = file($file);
                            $domain = $_POST['domain'];
                            $new_lines = [];
                            foreach ($lines as $line) {
                                if (strpos($line, $domain) === false) {
                                    $new_lines[] = $line;
                                }
                            }
                            file_put_contents($file, implode("", $new_lines));
                            echo 'Domain ' . $domain . ' has been deleted from the file.';



                            $file1 = '/opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/domain2.txt';
                            $lines = file($file1);
                           // $domain = $_POST['domain'];
                            $new_lines = [];
                            foreach ($lines as $line) {
                                if (strpos($line, $domain) === false) {
                                    $new_lines[] = $line;
                                }
                            }
                            file_put_contents($file1, implode("", $new_lines));
                        }
                        ?>
                        <br>
                        <br>


                        <br>
                        <?php
                        $output2 = shell_exec("cat /opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/domain.txt");
                        $output3 = shell_exec("cat /opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/domain2.txt");
                        echo "<pre style=' color:white;font-size:20px;'>$output2</pre>";
                        echo "<pre style='color:white;font-size:20px;'>$output3</pre>";
                        //echo "<pre>$output2</pre>";
                        ?>