<?php
date_default_timezone_set('Asia/Jakarta');
$verifyToken = '24071997';
$accessToken = 'EAALuikmyCEUBOxTwAerZBdocLKHqxT6OOpKKqeffdBjvZByAufGLfZCOGMbF6WZBKjXofjR5YZA9isDZBsy3iPOGCH0qVP8FuZAKZAnACkGFq8NkQxxraxjbJJjCzrXvklJZB3Q5YsFDw0hyxRRemIAZARtUgsaUW9wU4Yduekz4QcigJofCv2YlgrSLTU4W0m26Dd6vfApEZAayB3wVFqo';

// Handle verification request
if (isset($_GET['hub_mode']) && $_GET['hub_mode'] === 'subscribe') {
    if ($_GET['hub_verify_token'] === $verifyToken) {
        echo $_GET['hub_challenge'];
    }
}else{
  echo "I am ready";
}

function send_reply($access_token='',$reply_message=''){
	$url = "https://graph.facebook.com/v18.0/me/messages?access_token=".$access_token;
	$ch = curl_init();
	$header = array("Content-type: application/json");
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $reply_message);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  
	$st = curl_exec($ch);
	$result = json_decode($st,TRUE);
	save_data('Response Data',json_encode($ch));
	return $result;
}

function save_data($category="",$data=""){
  $servername = "localhost";
  $username = "dev1";
  $password = "12345qwerty";
  $dbname = "bot_handler";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);
  // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  $datetime = date('Y-m-d H:i:s');
  $sql = "INSERT INTO log_access (datetime,category,data)
  VALUES ('$datetime','$category','$data')";

  if ($conn->query($sql) === TRUE) {
    //echo "New record created successfully";
  } else {
    //echo "Error: " . $sql . "<br>" . $conn->error;
  }

  $conn->close();
}
// Validate the integrity and payload and it's origin
$payload = file_get_contents('php://input');
save_data('Incoming Data',$payload);
$data = json_decode($payload, true);
$message = $data['entry'][0]['messaging'][0]['message']['text'];
$id = $data['entry'][0]['messaging'][0]["sender"]['id'];
$replyMessage = '{"messaging_type": "RESPONSE","recipient": {"id": "'.$id.'"},"message": {"text": "Hello, I am Zur\'s assistant. What I can help you ?"}}';
send_reply($accessToken, $replyMessage);
exit;
