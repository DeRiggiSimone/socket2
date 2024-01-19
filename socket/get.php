<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $me=$_SERVER['PHP_SELF'];
    if($_GET)
    {
        echo "marca selezionata :".$_GET['marca']."<BR>";
        echo "modello selezionato :".$_GET['modello']."<BR>";
    }
    else
    {
        echo "<A HREF =".$me."?marca=Fiat&modello=Panda>Panda</A><BR>
        <A HREF =".$me."?marca=AlfaRomeo&modello=Giulietta>Alfa Giulietta</A><BR>
        <A HREF =".$me."?marca=Opel&modello=Panda>Opel Astra</A><BR>
        <A HREF =".$me."?marca=Citroen&modello=DS$>Citoren DS4</A><BR>
        <A HREF =".$me."?marca=Ford&modello=Ka>Ford Ka</A><BR>";
    }
    
    ?>
</body>
</html>