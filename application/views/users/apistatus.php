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
                        <?php
                        $curl = curl_init();

                        curl_setopt_array($curl, array(
                            CURLOPT_URL => "http://api.domainanda:11119/api/",
                            CURLOPT_RETURNTRANSFER => true,
                            CURLOPT_TIMEOUT => 10,
                            CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
                            CURLOPT_CUSTOMREQUEST => "GET",
                            CURLOPT_HTTPHEADER => array(
                                "cache-control: no-cache"
                            ),
                        ));

                        $start = microtime(true);
                        $response = curl_exec($curl);
                        $end = microtime(true);
                        $time = number_format($end - $start, 4);

                        curl_close($curl);
                        echo "<p style=color:white;'font-size:20px;'>Response time: " . $time . " seconds</span><br>\n";
                        //echo "Response time: " . $time . " seconds  ";
                        $response = curl_exec($curl);
                        $err = curl_error($curl);

                        curl_close($curl);

                        if ($err) {
                            echo "cURL Error #:" . $err;
                        } else {
                            echo "<p style=color:white;'font-size:20px;'>api.domainanda" . $response . "</p><br>\n";
                            //echo "<pre style='font-size:20px;'>$output2</pre>";
                            //echo "<span class='large-font'>api.domainanda is UP</span><br>\n";
                            //echo "api.domainanda" . "  is UP" . "<br>\n";
                        }



                        $curl1 = curl_init();

                        curl_setopt_array($curl1, array(
                            CURLOPT_URL => "http://172.16.19.40:7000/api/",
                            CURLOPT_RETURNTRANSFER => true,
                            CURLOPT_TIMEOUT => 10,
                            CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
                            CURLOPT_CUSTOMREQUEST => "GET",
                            CURLOPT_HTTPHEADER => array(
                                "cache-control: no-cache"
                            ),
                        ));

                        $start1 = microtime(true);
                        $response1 = curl_exec($curl1);
                        $end1 = microtime(true);
                        $time1 = number_format($end1 - $start1, 4);

                        curl_close($curl1);
                        echo "<p style=color:white;'font-size:20px;'>Response time: " . $time1 . " seconds</span><br>\n";
                        //echo "Response time: " . $time1 . " seconds  ";

                        $response1 = curl_exec($curl1);
                        $err1 = curl_error($curl1);

                        curl_close($curl1);

                        if ($err1) {
                            echo "cURL Error #:" . $err1;
                        } else {
                            echo "<p style=color:white;'font-size:20px;'>172.16.19.40:7000" . $response1 . "</p><br>\n";
                        }
