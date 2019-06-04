# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import datetime
from datetime import timedelta 
from django.http import HttpResponse

INP_1 = [
    [ # Monday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "06:30", "end_time": "07:00"},
        {"start_time": "07:00", "end_time": "07:30"},
        {"start_time": "07:30", "end_time": "08:00"}
    ], [ # Tuesday
    ], [ # Wednesday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "06:30", "end_time": "07:00"},
        {"start_time": "07:00", "end_time": "07:30"},
        {"start_time": "07:30", "end_time": "08:00"}
    ], [ # Thursday
        {"start_time": "09:00", "end_time": "09:30"},
        {"start_time": "09:30", "end_time": "10:00"},
        {"start_time": "10:00", "end_time": "10:30"},
        {"start_time": "10:30", "end_time": "11:00"}
    ], [ # Friday
    ], [ # Saturday
    ], [ # Sunday
    ]
]
OUT_1 = [
    {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
    {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
    {"start_time": "2017-01-02 07:00:00", "end_time": "2017-01-02 07:30:00"},
    {"start_time": "2017-01-02 07:30:00", "end_time": "2017-01-02 08:00:00"},
    {"start_time": "2017-01-04 06:00:00", "end_time": "2017-01-04 06:30:00"},
    {"start_time": "2017-01-04 06:30:00", "end_time": "2017-01-04 07:00:00"},
    {"start_time": "2017-01-04 07:00:00", "end_time": "2017-01-04 07:30:00"},
    {"start_time": "2017-01-04 07:30:00", "end_time": "2017-01-04 08:00:00"},
    {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 09:30:00"},
    {"start_time": "2017-01-05 09:30:00", "end_time": "2017-01-05 10:00:00"}
]

INP_2 = [[],[],[],[],[],[],[]]
OUT_2 = []

INP_3 = [
    [ # Monday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "06:30", "end_time": "07:00"},
    ], 
    [ # Tuesday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "07:00", "end_time": "07:30"},
        {"start_time": "07:30", "end_time": "07:45"}
    ], [ # Wednesday
    ], [ # Thursday
        {"start_time": "09:00", "end_time": "10:00"}
    ], [ # Friday
    ], [ # Saturday
    ], [ # Sunday
    ]
]
OUT_3 = [
    {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
    {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
    {"start_time": "2017-01-03 06:00:00", "end_time": "2017-01-03 06:30:00"},
    {"start_time": "2017-01-03 07:00:00", "end_time": "2017-01-03 07:30:00"},
    {"start_time": "2017-01-03 07:30:00", "end_time": "2017-01-03 07:45:00"},
    {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 10:00:00"},
    {"start_time": "2017-01-09 06:00:00", "end_time": "2017-01-09 06:30:00"},
    {"start_time": "2017-01-09 06:30:00", "end_time": "2017-01-09 07:00:00"},
    {"start_time": "2017-01-10 06:00:00", "end_time": "2017-01-10 06:30:00"},
    {"start_time": "2017-01-10 07:00:00", "end_time": "2017-01-10 07:30:00"}
]
INP_4 = [
    [ # Monday
        {"start_time": "06:00", "end_time": "06:30"}
    ], 
    [ # Tuesday
        {"start_time": "06:00", "end_time": "06:30"}
    ], [ # Wednesday
        {"start_time": "09:00", "end_time": "10:00"}
    ], [ # Thursday
        {"start_time": "09:00", "end_time": "10:00"}
    ], [ # Friday
        {"start_time": "09:00", "end_time": "10:00"}
    ], [ # Saturday
        {"start_time": "09:00", "end_time": "10:00"}
    ], [ # Sunday
        {"start_time": "09:00", "end_time": "10:00"}
    ]
]
OUT_4 = [
    {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
    {"start_time": "2017-01-03 06:00:00", "end_time": "2017-01-03 06:30:00"},
    {"start_time": "2017-01-04 09:00:00", "end_time": "2017-01-04 10:00:00"},
    {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 10:00:00"},
    {"start_time": "2017-01-06 09:00:00", "end_time": "2017-01-06 10:00:00"},
    {"start_time": "2017-01-07 09:00:00", "end_time": "2017-01-07 10:00:00"},
    {"start_time": "2017-01-08 09:00:00", "end_time": "2017-01-08 10:00:00"},
    {"start_time": "2017-01-09 06:00:00", "end_time": "2017-01-09 06:30:00"},
    {"start_time": "2017-01-10 06:00:00", "end_time": "2017-01-10 06:30:00"},
    {"start_time": "2017-01-11 09:00:00", "end_time": "2017-01-11 10:00:00"}
]
SAMPLE_INPUT_OUTPUTS = [ (INP_1, OUT_1),(INP_2, OUT_2),(INP_3, OUT_3),(INP_4, OUT_4)]

"""Test cases are designed to run at 8:30 PM.
3 test cases are provided. All cases are not covered. Make sure you
handle the cases that are not covered in the list of test cases.
Expecting more test cases to be written.
"""
def get_next_n_slots(week_config, current_time, n=10):
    next_n_slots = []
    empty_week_config = filter(None, week_config)
    slot_len=0
    if empty_week_config == []:
        return next_n_slots
    else:
        for idx,week in enumerate(week_config):
            slot_len=slot_len+len(week)
            if week:
                for slot_pair in week:
                    temp_dict={}
                    temp_date = (current_time + datetime.timedelta(days=idx+1)).strftime("%Y-%m-%d")
                    start_datetime_str = str(temp_date)+' '+slot_pair["start_time"]+':00'
                    end_datetime_str = str(temp_date)+' '+slot_pair["end_time"]+':00'
                    temp_dict["start_time"] = start_datetime_str
                    temp_dict["end_time"] = end_datetime_str
                    next_n_slots.append(temp_dict)
                    if len(next_n_slots) == n:
                        return next_n_slots
    if slot_len < n and slot_len != 0:
        date_str=next_n_slots[-1]["end_time"]
        new_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        new_time = new_date + timedelta(days=(6 - new_date.weekday()))
        diff_n = abs(n - slot_len)
        next_n_slots.extend(get_next_n_slots(week_config, new_time,n=diff_n))
        if len(next_n_slots) == n:
            return next_n_slots

def home(request):
    time_of_run = datetime.datetime(2017, 1, 1, 20, 30) # Sunday
    results=[]
    for ip, expected_output in SAMPLE_INPUT_OUTPUTS:
        output = get_next_n_slots(ip, time_of_run)
        assert output == expected_output
        results.append(output)
    return HttpResponse(results)