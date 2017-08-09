#!/bin/bash

curl --data-binary @test2.csv -H "Content-Type:text/csv; charset=utf-8" http://localhost/table/api/v1.0/identify_subject_column
