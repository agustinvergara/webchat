DROP DATABASE IF EXISTS webchat_db;

CREATE DATABASE webchat_db;

USE webchat_db;

CREATE TABLE message(
    message_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    username VARCHAR(100),
    content VARCHAR(600),
    sent_time TIMESTAMP(NOW())
);