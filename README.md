# drupal-multi-cron
Run Drupal multisite cron using Python and Drush

# Usage
1. Copy `drupal-multi-cron.py` to home directory.
2. Setup cron task.
    Example: 
    `0 1 * * * python /path/to/scripts/drupal-multi-cron.py /var/www > /dev/null 2>&1`
3. Be happy :)
