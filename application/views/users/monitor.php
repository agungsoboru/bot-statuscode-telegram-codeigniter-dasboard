<?php

defined('BASEPATH') or exit('No direct script access allowed');
?>


<!-- Main content -->
<div class="content">
    <div class="container-fluid">
        <div style="background-color: #2c2f33;">
            <div class="row">
                <div class="col-md-12 col-xs-12">

                    <div class="card">

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
                            <?php
                            //$output2 = shell_exec("cat monitor.json");
                            //echo " <pre style='font-size:20px;'>$output2</pre>";

                            $json = file_get_contents('/opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/monitor.json');
                            $json = json_decode($json);
                            $json = json_encode($json, JSON_PRETTY_PRINT);

                            $json1 = file_get_contents('/opt/lampp/htdocs/bot-telegram-codeigniter-dasboard/bot-telegram/monitor2.json');
                            $json1 = json_decode($json1);
                            $json1 = json_encode($json1, JSON_PRETTY_PRINT);
                            echo $json;
                            echo $json1;
                            ?>