# -*- coding: utf8 -*-
import os
def main_handler(event, context):
    print(os.popen("/usr/bin/dd if=/dev/zero of=/mnt/test bs=1M count=128 2>&1").read())
