<?php
$file = fopen('data02.txt', 'r');
$line = fgets($file);
$sum = 0;

foreach(explode(',', $line) as $s) {
    list($start, $end) = sscanf($s, '%D-%D');
    $range = range($start, $end);

    foreach($range as $id) {
        $id_s = (string)$id;
        $len = strlen($id_s);
        if($len % 2) continue; # skip odd length - avoid bug where "1" == "01"!!

        if(substr($id_s, 0, $len/2) == substr($id_s, $len/2)) {
            #printf("%d\n", $id);
            $sum += $id;
        }
    }
}
fclose($file);

printf("%d\n", $sum);
?>
