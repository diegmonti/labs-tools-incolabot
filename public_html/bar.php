<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>IncolaBot - bar.txt</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="//tools-static.wmflabs.org/static/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
    <style>
        html {
            height: 100%
        }
        body {
            position: relative;
            margin: 0;
            padding-bottom: 4rem;
            min-height: 100%;
            padding-top: 50px;
        }
        .container {
            width: 75% !important;
        }
    </style>

    <script src="//tools-static.wmflabs.org/static/jquery/2.1.0/jquery.min.js"></script>
    <script src="//tools-static.wmflabs.org/static/bootstrap/3.2.0/js/bootstrap.min.js"></script>
</head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="https://tools.wmflabs.org/incolabot">IncolaBot</a>
		  </div>
          <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
              <li><a href="https://tools.wmflabs.org/incolabot">This project</a></li>
              <li><a href="https://it.wikipedia.org/wiki/Utente:Incola">My userpage</a></li>
              <li><a href="https://it.wikipedia.org/wiki/Utente:IncolaBot">My bot</a></li>
			  <li><a href="https://it.wikipedia.org/w/index.php?title=Discussioni_utente:Incola&amp;action=edit&amp;section=new">Contact me</a></li>
            </ul>
          </div>
      </div>
    </div>

    <div class="container">

    <h3>Log of bar.py</h3>

    <pre class="txt" style="font-family:monospace;"><?php echo utf8_encode(file_get_contents( "../log/bar.txt" )); ?></pre>

    </div>

  </body>
</html>
