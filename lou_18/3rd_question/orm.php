<?php

class Orm extends Model
{
	protected function find()
	{
	    return $this;    
	}

	public function select($select)
	{
        if (is_array($select)) {
            $select = implode(',',$select);
        }
		$this->_select = trim($select);
	    return $this;
	}

	public function one() 
	{
		$this->_limit = ' LIMIT 1';
	    return current($this->get());
	}


	public function all() 
	{
		return $this->get();
	}
	public function or($condition)
	{
		if(empty($this->_where))
		{
			return $this;

		}
        $addString='';
        $conditionString=$this->getWhereString($condition);
		if($conditionString) {
            $addString = ' or (' . $this->getWhereString($condition) . ')';
        }
        $this->_where.=$addString;
        return $this;
	}
	public function and($condition)
	{
		if(empty($this->_where))
		{
			return $this;
		}
        $addString='';
		$conditionString=$this->getWhereString($condition);
		if($conditionString){

            $addString= ' and ('.$conditionString.')';
        }
		$this->_where.=$addString;
		return $this;
	}
	public function where($condition)
	{
        $conditionSting=$this->getWhereString($condition);
	    $this->_where="( $conditionSting )";
        return $this;
	}
	private function getWhereString($condition){
        $whereString="";
        if(is_array($condition)){
            switch ($condition[0]){
                case 'in':
                    $whereString.=($condition[1].' in ('.implode(',',$condition[2]).')');
                    break;
                case 'between':
                    $whereString.=($condition[1].' between '.$condition[2][0] .' and '.$condition[2][1]);
                    break;
                default:
                    $whereString.=($condition[1].' '.$condition[0].' '.$condition[2]);
                    break;
            }
        }else{
            $whereString=$condition;
        }
        if(!$whereString){
            $whereString='';
        }
        return $whereString;
    }

}
