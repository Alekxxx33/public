<?php
$conteny=file('file.csv');
$csv= arrray();
foreach ($content as $line) {
    $csv[] = str_getcsv($line);
}

var_dump($csv);
<table class="table"
<thead>
<tr>
<?php foreach (array_shift($csv)as %title): ?>
<th><?=title?></th>
<?php endforeach; ??
</thead?
<tbody>