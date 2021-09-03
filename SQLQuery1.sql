create database forensic;
SELECT USER_NAME(); 

drop table police;

DROP DATABASE fore;
DROP TABLE admin_;

use forensic;

create table admin_ (
admin_id varchar(80),
admin_name varchar(80), 
admin_email varchar(80),
admin_password_ varchar(80),
PRIMARY KEY (admin_id)
);


create table police_station (
pst_id varchar(80),
pst_name varchar(80), 
pst_area varchar(80),
pst_place varchar(80),
pst_email varchar(80),
pst_password varchar(80),
PRIMARY KEY (pst_id)
);

select * from police_station;

create table hospital (
h_id varchar(80),
h_name varchar(80), 
h_area varchar(80),
h_place varchar(80),
h_email varchar(80),
h_password varchar(80),
PRIMARY KEY (h_id)
);

create table police(
p_id varchar(80),
p_name varchar(80), 
p_age varchar(80),
p_exp varchar(80),
p_place varchar(80),
p_phone varchar(80),
p_email varchar(80),
p_password varchar(80),
PRIMARY KEY (p_id),
pst_id varchar(80),
FOREIGN KEY (pst_id) references police_station(pst_id) on delete cascade
);
drop table police;

create table doctor (
d_id varchar(80),
d_name varchar(80), 
d_age varchar(80),
d_exp varchar(80),
d_place varchar(80),
d_phone varchar(80),
d_email varchar(80),
d_password varchar(80),
PRIMARY KEY (d_id),
h_id varchar(80),
FOREIGN KEY (h_id) references hospital(h_id) on delete cascade
);

create table case_ (
c_id varchar(80),
c_name varchar(80), 
c_typr varchar(80),
c_date varchar(80),
c_time varchar(80),
c_location varchar(80),
p_id varchar(80),
h_id varchar(80),
PRIMARY KEY (c_id),
FOREIGN KEY (p_id) references police(p_id) on delete cascade,
FOREIGN KEY (h_id) references hospital(h_id) on delete cascade
);

drop table case_;

create table evidence_ (
e_id varchar(80),
c_id varchar(80),
body varchar(80),
body_analysis varchar(80),
weapon varchar(80),
weapon_analysis varchar(80),
fluid_type varchar(80),
fluid_analysis varchar(80),
personal_belongings varchar(80),
personal_belong_analy varchar(80),
PRIMARY KEY (e_id),
FOREIGN KEY (c_id) references case_ (c_id) on delete cascade
);

drop table evidence_;

SET IDENTITY_INSERT ad OFF;

insert into admin_ values ('1','aa','aa','aa');
select * from admin_;
insert into case_ values ('1','aa','aa','25-mar-1998','04:05:44','uu','oo','90');
commit;


CREATE TABLE books (
  id              INT           NOT NULL    IDENTITY    PRIMARY KEY,
  title           VARCHAR(100)  NOT NULL,
  primary_author  VARCHAR(100),
);



SET IDENTITY_INSERT books ON;
INSERT INTO books (title, primary_author)
VALUES ('25','9876543210');
SET IDENTITY_INSERT books OFF;

insert into admin_ (admin_id, admin_name, admin_email, admin_password_) values('ad1', 'admin-1', 'ad1', 'ad1')

insert into admin_ values('aa','ss','sd','qq');

insert into police (p_id,p_name,p_age,p_exp,p_place,p_phone,p_email,p_password) values ('k','kk','kk','kkk','lll','lll','aaa','asdf');
use forensic;

select * from police;
select * from hospital;
select * from admin_;
select * from police_station;
select * from doctor;
select * from case_;

insert into admin_(admin_id) values('hello');

-- DELETE FROM police WHERE p_id=;

select * from admin_;