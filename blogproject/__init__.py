import pymysql

# define a bigger version 1.4.6 here
pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()