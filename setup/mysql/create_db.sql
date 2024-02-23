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
    country varchar(50) not null default "India",
    address_line_1 varchar(255) not null,
    address_line_2 varchar(255) not null,
    is_active tinyint(1) NOT NULL DEFAULT 1,
    is_deleted tinyint(1) NOT NULL DEFAULT 0,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
ALTER TABLE `reviews` ADD CONSTRAINT `review_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER table reviews add COLUMN locality text not null;
ALTER table reviews drop COLUMN house_num;
CREATE INDEX pincode_idx
ON reviews (pin_code);
CREATE FULLTEXT INDEX locality_idx ON reviews(locality);


CREATE TABLE supporting_docs (
    id int AUTO_INCREMENT not null primary key,
    review_id int not null,
    name varchar(100),
    doc_data longtext not null,
    doc_link varchar(500)
);
ALTER TABLE `supporting_docs` ADD CONSTRAINT `doc_review_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`);
ALTER TABLE `supporting_docs` ADD COLUMN `type` varchar(15);
ALTER TABLE `supporting_docs` CHANGE `doc_data` `doc_data` LONGTEXT CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL;

CREATE TABLE `profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profile_pic` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci,
  `profile_pic_link` varchar(512) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `user_id` int NOT NULL,
  `job_title` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `profile_user_id_2aeb6f6b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
