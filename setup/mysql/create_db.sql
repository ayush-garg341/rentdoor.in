CREATE USER 'admin'@'%' IDENTIFIED WITH mysql_native_password BY 'admin123';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;

CREATE DATABASE IF NOT EXISTS `rentdoor` COLLATE 'utf8_general_ci' ;
