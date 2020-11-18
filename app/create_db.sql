CREATE DATABASE `python_mysql` CHARACTER SET latin1;

USE `python_mysql`;

CREATE TABLE `commits` (
  `commit_id` tinytext NOT NULL,
  `commit_time` datetime NOT NULL,
  `commit_message` longtext NOT NULL,
  `commit_user` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;