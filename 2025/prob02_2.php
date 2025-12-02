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

        foreach(range(2, 20) as $repeats) {
            if($len % $repeats) continue; # skip odd length - avoid bug where "1" == "01"!!
            $len2 = $len/$repeats;

            $first_part = substr($id_s, 0, $len2);

            $found_problem = false;
            foreach(range(2, $repeats) as $i) {
                if($first_part != substr($id_s, $len2*($i-1), $len2)) {
                    $found_problem = true;
                    break;
                }
            }
            if($found_problem) continue;

            printf("%d\n", $id);
            $sum += $id;
            break; # done checking this id
        }
    }
}
fclose($file);

printf("%d\n", $sum);
?>
