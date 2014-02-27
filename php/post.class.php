<?php
class Request {
	//curl
    public static function post($url, $post_data = '', $timeout = 5){
        $ch = curl_init();
        curl_setopt ($ch, CURLOPT_URL, $url);
        curl_setopt ($ch, CURLOPT_POST, 1);
        if($post_data != ''){
            curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
        }
        curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1); 
        curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
        curl_setopt($ch, CURLOPT_HEADER, false);
        $file_contents = curl_exec($ch);
        curl_close($ch);
        return $file_contents;
    }
	
	//file_get_content
    public static function post2($url, $data){
        $postdata = http_build_query($data);
        $opts = array('http' =>
				  array(
					  'method'  => 'POST',
					  'header'  => 'Content-type: application/x-www-form-urlencoded',
					  'content' => $postdata
				  )
        );
        $context = stream_context_create($opts);
        $result = file_get_contents($url, false, $context);
        return $result;
    }
	
	//fsocket
    public static function post3($host,$path,$query,$others=''){
        $post="POST $path HTTP/1.1\r\nHost: $host\r\n";
        $post.="Content-type: application/x-www-form-";
        $post.="urlencoded\r\n${others}";
        $post.="User-Agent: Mozilla 4.0\r\nContent-length: ";
        $post.=strlen($query)."\r\nConnection: close\r\n\r\n$query";
        $h=fsockopen($host,80);
        fwrite($h,$post);
        for($a=0,$r='';!$a;) {
			$b=fread($h,8192);
			$r.=$b;
			$a=(($b=='')?1:0);
        }
        fclose($h);
        return $r;
    }
}

$url = "http://www.baidu.com";
$data = array('test'=>'test');
$req = new Request();
$result = $req->post2($url,$data);
print_r($result);

