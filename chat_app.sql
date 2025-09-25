use chat_app;

create table user(
    id char(36) primary key,
    username varchar(256) not null unique,
    name varchar(256) not null,
    email varchar(256) not null unique,
    password varchar(256) not null,
    profile_picture varchar(128),
    date_of_birth date not null,
    gender enum('male', 'female', 'other') not null,
    created_at datetime not null default now(),
    updated_at datetime
);