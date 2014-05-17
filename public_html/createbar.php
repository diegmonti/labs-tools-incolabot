<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>IncolaBot - createbar.txt</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px;
      }
    </style>
    <link href="css/bootstrap-responsive.css" rel="stylesheet">

    <!--[if lt IE 9]>
      <script src="js/html5shiv.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="index.html">IncolaBot</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="index.html">This project</a></li>
              <li><a href="http://it.wikipedia.org/wiki/Utente:Incola">My userpage</a></li>
              <li><a href="http://it.wikipedia.org/wiki/Utente:IncolaBot">My bot</a></li>
        <li><a href="http://it.wikipedia.org/w/index.php?title=Discussioni_utente:Incola&action=edit&section=new">Contact me</a></li>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="container">

    <h2>Log of createbar.py</h2>

    <pre class="txt" style="font-family:monospace;"><?php echo file_get_contents( "../log/createbar.txt" ); ?></pre>

    </div>

  <script src="js/bootstrap.min.js"></script>

  </body>
</html>
