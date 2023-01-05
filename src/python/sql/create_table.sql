CREATE TABLE IF NOT EXISTS {table_name} (
id int not null auto_increment primary key,
title varchar(100),
author varchar(50),
link varchar(200),
created_at datetime not null default current_timestamp)
