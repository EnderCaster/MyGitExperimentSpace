<?php
return [
	'db_host'=>'localhost',
	'db_user'=>'root',
	'db_password'=>'nothing',
	'db_name'=>'frame_test',
	'db_table_prefix'=>'ec_',
	'db_charset'=>'utf8',
	'default_module'=>'home',
	'default_controller'=>'Index',
	'default_action'=>'index',
	'url_type'=> CONFIG_URL_PATHINFO,//TODO add consts normal-1 pathinfo-2
	'cache_path'=>RUNTIME_PATH.'cache'.DS,
	'cache_prefix'=>'cache_',
	'cache_type'=>'file',// This course just implements this type, we can do more
	'compile_path'=>RUNTIME_PATH.'compile'.DS,
	'view_path'=>APP_PATH.'home'.DS.'view'.DS,
	'view_suffix'=>'.php',//template suffix
	'auto_cache'=>true,
	'url_html_suffix'=>'html'//I think there could make thing interesting
];