<?php
class Model
{
	private static $instance;
	private $db;

    protected $_prepare = true;
	protected $table;

    protected $_sql = '';
	protected $_where = '';
	protected $_select = '*';
	protected $_limit = '';
	
	/**
	 * 实例话对象静态调用
	 *
	 *
	 */
	public static function __callStatic($method,$args) 
	{	
		if (empty(self::$instance) || !self::$instance instanceof self) 
		{
			self::$instance = self::getIns();
		}

        if (empty(self::$instance->table)) {
            self::$instance->table = strtolower(get_called_class()).'s';
        }

        if (method_exists(self::$instance,'init')) {
            self::$instance->init();
        }
		return call_user_func_array(array(self::$instance, $method), $args);
	}

	/**
	 * 获取实例对象
	 *
	 *
	 */
	private static function getIns() 
	{
		return new Static;
	}

	/**
	 * 构造函数数据库初始化连连接接
	 *
	 *
	 */
	private function __construct()
	{
		$this->db = new mysqli('127.0.0.1','root','','shiyanlou');
		$this->db->set_charset('utf8');
		if (mysqli_connect_errno())
		{
          die('Unable to connect!'). mysqli_connect_error();
        }

	}
    /**
     * 返回结果集
     *
     */
    protected function fetchAssoc($sql) 
	{
        $res = $this->db->query($sql);    	
		if (false === $res) {
		    return $this->db->error;
		}
		$data = [];
        while ($row = mysqli_fetch_assoc($res))	{
		    $data[] = $row;    
		}
		return $data;
	}

    /**
     * 结果查询
     *
     */
	protected function get()
	{
		$sql = "SELECT $this->_select FROM `$this->table` where $this->_where $this->_limit";
		echo $sql;
		return $this->fetchAssoc($sql);
	}
}
