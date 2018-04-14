<?php

class Practice {
    private $answer = [];
    private $output;
    private $seg = '@@';

    public function __construct()
    {
        echo <<<EOT
根据下列选项，选出正确答案，所有题目均为单选

回车开始做题
EOT;
        if ('' != $this->getStdin()) {
            $this->stop();
        }

        $this->items();
    }

    public function seperate($text = '') 
    {
        return  "\n.................$text..................\n";
    }

    private function getStdin()
    {
        return trim(fgets(STDIN));
    }

    private function items()
    {
        //check answers
        $res = 2;
        $count = 0;

        $msg = '';
        if (file_exists('answer.txt') && 
            !empty($ctt = file('answer.txt'))) {
            $count = count($ctt);
            echo $this->seperate();
            echo <<<EOT

上次做到第 $count 题

重做：1 | 继续：2

选择：
EOT;
            $res = $this->getStdin();
            switch ($res) {
                case 1:
                    exec("rm answer.txt");
                break;
                //判断是否做完
                case 2:

                break;
                default:
                    $this->stop();
            }
        }
        $str = trim(file_get_contents('exercise.txt'))."\n\n";
        $items = explode($this->seg,$str);
        $i = 0;
        $msg = '所有题目完成';
        foreach($items as $key => $item) {
            $item = trim($item);
            if (empty($item)) continue;
            $i++;
            if ($res == 2 && $i-1 < $count) continue;
            echo $this->seperate(),"\n".$item."\n";
            $mes = '';
            echo <<<EOT

回答：
EOT;
            file_put_contents('answer.txt',$this->getStdin()."\n",FILE_APPEND);

        }
        
        echo $this->seperate($msg);
        echo <<<EOT

交卷：1 | 重做：2 

选择：
EOT;
        $this->output = $this->getStdin();
        switch($this->output) {
            case 1:break;
            case 2:
                exec("rm answer.txt");
                $this->items();
            break;
        }
    }

    public function stop($msg = null)
    {
        exit($msg ?? 'Invalid input, exit');
    }

    public function __destruct()
    {
    
    }
}
new Practice();
