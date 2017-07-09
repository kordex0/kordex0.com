<!DOCTYPE html>
<html lang="en">
<head>
    <title>Home</title>
    <link rel="stylesheet"
          href="${request.static_url('kordex0:static/base.css')}"/>
</head>
<body style="">
    <h1>Home</h1>
    <p>Go to <a href="${request.route_url('hello', name='hana')}">HANA</a></p>
</body>
</html>