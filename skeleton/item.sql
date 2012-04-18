-- item.sql
CREATE TABLE items (
    id int auto_increment primary key,
    author_id int,
    body text,
    created timestamp 
);