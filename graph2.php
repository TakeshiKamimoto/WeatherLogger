<?php
$today  = 'todaydata';
$csv_dir  = '/home/pi/bme280/data/';
$temp_file = $today.'_temp.csv';
$grapgh_t   = '';
$pres_file = $today.'_pres.csv';
$grapgh_p   = '';
$hum_file = $today.'_humd.csv';
$grapgh_h   = '';
if (($handle = fopen($csv_dir.$temp_file, "r")) !== false) {
    while (($line = fgets($handle)) !== false) {
    $grapgh_t .= '['.rtrim($line).'],'.PHP_EOL;
    }
    fclose($handle);
}else{
    echo 'no data';
}
if (($handle = fopen($csv_dir.$pres_file, "r")) !== false) {
    while (($line = fgets($handle)) !== false) {
    $grapgh_p .= '['.rtrim($line).'],'.PHP_EOL;
    }
    fclose($handle);
}else{
    echo 'no data';
}
if (($handle = fopen($csv_dir.$hum_file, "r")) !== false) {
    while (($line = fgets($handle)) !== false) {
    $grapgh_h .= '['.rtrim($line).'],'.PHP_EOL;
    }
    fclose($handle);
}else{
    echo 'no data';
}
?>
<html>
<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
    google.charts.load('current', {packages:['corechart', 'line']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Time');
        data.addColumn('number', 'Temperature[℃]');
        data.addColumn('number', 'Temperature[℃]');
        data.addRows([
            <?php echo $grapgh_t; ?>
        ]);

    var options = {
        title: 'Temprature',
        legend: 'none',
        colors: ['red','black'],
        vAxis: {title: "deg.C"}
    };

        var chart = new google.visualization.LineChart(document.getElementById('chart1'));
        chart.draw(data,options);
    }

    google.charts.load('current', {packages:['corechart', 'line']});
    google.charts.setOnLoadCallback(drawChart2);

    function drawChart2() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Time');
        data.addColumn('number', 'Pressure[hPa]');
        data.addColumn('number', 'Pressure[hPa]');
        data.addRows([
            <?php echo $grapgh_p; ?>
        ]);

    var options = {
        title: 'Pressure',
        legend: 'none',
        colors: ['blue','black'],
        vAxis: {
			title: "hPa"
		}
    };

        var chart = new google.visualization.LineChart(document.getElementById('chart2'));
        chart.draw(data,options);
    }

    google.charts.load('current', {packages:['corechart', 'line']});
    google.charts.setOnLoadCallback(drawChart3);

    function drawChart3() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Time');
        data.addColumn('number', 'Humid[%]');
        data.addColumn('number', 'Humid[%]');
        data.addRows([
            <?php echo $grapgh_h; ?>
        ]);

    var options = {
        title: 'Humidity',
        legend: 'none',
        colors: ['green','black'],
        vAxis: {
			title: "%RH"
		}
     };

        var chart = new google.visualization.LineChart(document.getElementById('chart3'));
        chart.draw(data,options);
    }
</script>
</head>
<body>

<div id="chart1"></div>
<div id="chart2"></div>
<div id="chart3"></div>

</body>
</html>
