<?
$fp = fopen('dane.txt',r');

?>

<?
$fp = fopen("test.txt","r");
$tekst = fread($fp,10);
?>
<?php
$dane= fread(fopen('nazwa_pliku','r'),filesize('nazwa pliku'))

?>
<?

$dane = implode("/n",file('nazwa_pliku'));
?>
<? // wczytanie starych danych
//otwarcie pliku do odczytu
$fp= fopen('plik.txt','r');

//odczytanie danych
$stareDane = fread($fp,filesize('plik.txt'));
//zamkniecie pliku
fclose($fp);
//stworzenie nowych danych
$noweDane= "oto linijka z poczatku\n";
$noweDane.=$stareDane;
//zapisanie nowych danych
// otwarcie pliku do zapisu
$fp = fopen('plik.txt','w');
// zapisanie danych
fputs($fp,$noweDane);
//zamkniecie pliku
fclose($fp);
?>
<?
rename('aaa','bbb'); //zmiana nazwy pliku aaa na bbb
rename('bbb','test/'); //przeniesienie pliku bbb do katalogu o nazwie test
rename('aaa''.');//przeniesienie pliku "aaa"do katologu"
rename('aaa','test/bbb');//"test" ze  zmiana nazwy na "bbb"
?>
<?
$path ="moja/strona/index.html";

echo dirname($path); //wyswietl "/moja /strona"
echo basenname($path);//wyswietlki "index.html'
$arr = pathinfo($path);
echo $arr["dirname"]; //wyswietli "moja/strona"
echo $arr["basename"]; //wyswietli :index.html"
echo $arr["extension"]; //wyswetli "html"
?>
<?
if($dir =@opendir("/tmp")) {
    while($fle = readir($dir)) {
        echo "$file/n";
    }
close($dir);
}
?>
,?$d = dir('/etc');
echo'handle:'$d->handle."
/n";
while($entry =$d->read()){
    echo $entry."
    /n";
    $d0>close();
    ?>
