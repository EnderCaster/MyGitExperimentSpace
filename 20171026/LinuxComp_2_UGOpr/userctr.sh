#!/bin/bash
operationMode=$1
teacherName=$2
studentNamePrefix=$3
studentCount=$4
parameterHasNullValue=($operationMode != "" || $teacherName != "" || $studentNamePrefix != "" || $studentCount != "")
echo $parameterHasNullValue
#parameterHasInvaluedInput=
