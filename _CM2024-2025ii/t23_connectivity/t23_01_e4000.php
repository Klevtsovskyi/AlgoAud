<?php

function dfs($graph, $n, $start) {
    $count = 0;

    $visited = array_fill(0, $n, 0);
    $visited[$start] = 1;

    $stack = [];
    array_push($stack, $start);

    while (count($stack) > 0) {
        $i = array_pop($stack);
        $count++;
        for ($j = 0; $j < $n; $j++) {
            if ($graph[$i][$j] && !$visited[$j]) {
                array_push($stack, $j);
                $visited[$j] = 1;
            }
        }
    }
    return $count;
}


$lines = file('input.txt');

$data = explode(' ', $lines[0]);
$n = intval($data[0]);
$s = intval($data[1]);

$matrix = [];
for ($i = 1; $i < count($lines); $i++) {
    $row = explode(' ', $lines[$i]);
    for ($j = 0; $j < count($row); $j++) {
        $row[$j] = intval($row[$j]);
    }
    array_push($matrix, $row);
}

echo dfs($matrix, $n, $s - 1);

?>