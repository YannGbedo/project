<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link href="css/style.css" rel="stylesheet">
        <script src="js/script.js"></script>
        <script src="bootstrap/js/jquery.js"></script>
        <script src="bootstrap/js/bootstrap.min.js"></script>
        <link href="bootstrap/css/bootstrap.css" rel="stylesheet">
        <link rel="icon" type="image/png" href="img/logo.png" />
        <title>hids</title>
    </head>
    <body>
        <nav class="navbar navbar-default">
        <div class="container-fluid">
            <div class="navbar-header" id="navbar">
                <a class="navbar-brand" href="index.php">HIDS</a>
            </div>
            <ul class="nav navbar-nav">
                <li><a href="index.php?l=alerte">ALERTE</a></li>
                <li><a href="index.php?l=actual">WEBS</a></li>
            </ul>
        </div>
        </nav>
        <?php
        function actual($name,$ip,$user,$pwd){
            /*$name = "webs1";
            $ip = "192.168.8.103";
            $user = "billy";
            $pwd = "billy";*/
	        $command = escapeshellcmd('sudo -u root nohup /usr/bin/python /var/www/html/hids/python/programme.py '.$name.' '.$ip.' '.$user.' '.$pwd.' &');
	        passthru($command);
	        //$output = exec($command);
	        $output = true;
            if($output!=null){
                //echo $output;
            }else{
                echo "erreur sur l'actualisation des erreurs.";
            }
        }
        if($_GET['l']=="actual"){
            if (($handle = fopen('webs/webs.csv', "r")) !== FALSE) {
                print('<table class="table table-striped"><thead><tr><th>Name</th><th>Ip</th><th>User</th><th>Password</th><th>Actualiser</th></tr></thead><tbody>');
                while (($data = fgetcsv($handle, 0, ";")) !== FALSE) {
                    $num = count($data);
                    echo "<tr>";
                    echo '<td>'.$data[0].'</td>';
                    echo '<td>'.$data[1].'</td>';
                    echo '<td>'.$data[2].'</td>';
                    echo '<td>'.$data[3].'</td>';
                    echo "<td><a href='index.php?webs=".$data[0]."&ip=".$data[1]."&user=".$data[2]."&pwd=".$data[3]."'>X</a></td>";
                    echo "</tr>";
                }
                echo '</tbody></table>';
                fclose($handle);
            }
        }else if($_GET['l']=="alerte"){
            if (($handle = fopen('alert/alert.csv', "r")) !== FALSE) {
                print('<table class="table table-striped"><thead><tr><th>Libelle</th><th>Détails</th><th>Fichier</th><th>Date</th></tr></thead><tbody>');
                while (($data = fgetcsv($handle, 0, ",")) !== FALSE) {
                    $num = count($data);
                    echo "<tr>";
                    echo '<td>'.$data[0].'</td>';
                    echo '<td>'.$data[1].'</td>';
                    echo '<td>'.$data[2].'</td>';
                    echo '<td>'.date("d-m-Y",(int)$data[3]).'</td>';
                    echo "</tr>";
                }
                echo '</tbody></table>';
                fclose($handle);
            }
        }else if($_GET['webs']){
            actual($_GET['webs'],$_GET['ip'],$_GET['user'],$_GET['pwd']);
        }else{
            print('<p>Bienvenue dans l\'assistant de gestion des serveurs commerciaux DayLighter.</p>');
            print('<p>Pour des lendemains meilleurs</p>');	
        }
        ?>
    </body>
</html>
