CREATE USER 'admin'@'%' IDENTIFIED WITH mysql_native_password BY 'admin123';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;

CREATE DATABASE IF NOT EXISTS `rentdoor` COLLATE 'utf8_general_ci' ;

CREATE TABLE reviews (
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    user_id int not null,
    rating int default 0,
    title varchar(500) not null,
    description TEXT not null,
    house_num varchar(20),
    city varchar(100) not null,
    state varchar(100) not null,
    pin_code varchar(20) not null,
    country varchar(50) not null,
    address_line_1 varchar(255) not null,
    address_line_2 varchar(255) not null
);
ALTER TABLE `reviews` ADD CONSTRAINT `review_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
