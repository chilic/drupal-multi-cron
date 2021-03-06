#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Chilic'

import os
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Please pass second parameter.')
        exit()

    BASE_DIR = sys.argv[1]

    for root, dirs, files in os.walk(BASE_DIR):
        if 'settings.php' in files:
            sites_path, uri = os.path.split(root)
            drupal_root, sites_folder = os.path.split(sites_path)

            if 'sites' == sites_folder:
                if 'default' != uri:
                    params = "--root=%s --uri=http://%s" % (drupal_root, uri)
                else:
                    params = "--root=%s" % drupal_root

                command = "drush %s cron" % params

                os.popen(command)