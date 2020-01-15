CREATE TABLE tbl_user (
	user_id int NOT NULL PRIMARY KEY,
	user_full_name varchar(255
);

CREATE TABLE tbl_role (
	role_id int NOT NULL PRIMARY KEY,
	role_name varchar(255)
);

CREATE TABLE tbl_user_role (
	user_id int,
	role_id int
);


SELECT user_full_name
FROM tbl_user AS u
INNER JOIN tbl_user_role as ur ON u.user_id = ur.user_id
INNER JOIN tbl_role AS r ON ur.role_id = r.role_id
WHERE r.role_name = "IT"; 

SELECT user_full_name
FROM tbl_user AS u
LEFT JOIN tbl_user_role as ur ON u.user_id = ur.user_id
WHERE ur.role_id IS NULL; 