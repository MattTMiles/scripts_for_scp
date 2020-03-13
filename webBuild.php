<?PHP

?>
<html>
<body>

<?

$pulsars = array();
if ($handle = opendir("pulsars"))
{
  while (false !== ($entry = readdir($handle)))
  {
    if ($entry != "." && $entry != "..")
    {
       array_push($pulsars, $entry);
    }
  }
}
//print_r($pulsars);


foreach ($pulsars as $pulsar)
{
  if ($handle = opendir("pulsars/".$pulsar))
  {
    while (false !== ($entry = readdir($handle)))
    {
      if ($entry != "." && $entry != "..")
      {
        echo "<img src='pulsars/".$pulsar."/".$entry."'/><br>\n";
      }
    }
  }

  echo "file=$file<BR>\n";
}

?>
</body>
</html>