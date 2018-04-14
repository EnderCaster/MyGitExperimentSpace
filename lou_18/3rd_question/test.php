<?php

spl_autoload_register(function ($class) {
    $class = strtolower($class);
    include "$class.php";
});

$res1 = User::find()
    ->where(['<','age',16])
    ->and(['in','height',[165,170]])
    ->all();

print_r($res1);

$res2 = User::find()
    ->where(['=','gender',1])
    ->or(['like','name','wang'])
    ->all();

print_r($res2);

$res3 = User::find()
    ->where(['between','weight',[40,50]])
    ->and(['>','id',4])
    ->all();

print_r($res3);
