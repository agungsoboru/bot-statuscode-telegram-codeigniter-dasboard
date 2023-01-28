<?php
$user_ip = $_SERVER['REMOTE_ADDR'];
$curl = curl_init();
curl_setopt_array($curl, array(
    CURLOPT_URL => "https://api.telegram.org/bottoken-telegram-bot/sendMessage?chat_id=chat-id-kamu?disable_notification=true&text={$user_ip}",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => "",
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "GET",
));
$response = curl_exec($curl);
$err = curl_error($curl);
curl_close($curl);
if ($err) {
    echo "cURL Error #:" . $err;
} else {
    echo "";
}
