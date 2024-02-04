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
    address_line_2 varchar(255) not null,
    is_active tinyint(1) NOT NULL DEFAULT '1',
    is_deleted tinyint(1) NOT NULL DEFAULT '0',
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
);
ALTER TABLE `reviews` ADD CONSTRAINT `review_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);


CREATE TABLE supporting_docs (
    id int AUTO_INCREMENT not null primary key,
    review_id int not null,
    name varchar(100),
    doc_data longtext not null,
    doc_link varchar(500)
);
ALTER TABLE `supporting_docs` ADD CONSTRAINT `doc_review_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`);
