-- create the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- create the table states
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa.states` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
);
