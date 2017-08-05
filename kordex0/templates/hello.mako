<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hello ${name}</title>
    <link rel="stylesheet" href="${request.static_url('kordex0:static/css/base.css')}"/>
    <link rel="stylesheet" href="${request.static_url('kordex0:static/css/hello.css')}"/>
</head>
<body style="">
    <h1>Hi ${name}</h1>
    <img src="${request.static_url('kordex0:static/images/flower.jpg')}"/>
</body>
</html>
