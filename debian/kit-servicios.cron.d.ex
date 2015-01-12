#
# Regular cron jobs for the kit-servicios package
#
0 4	* * *	root	[ -x /usr/bin/kit-servicios_maintenance ] && /usr/bin/kit-servicios_maintenance
