create database galenos_dev;
use galenos_dev;
create user dev_admin@localhost identified by "testing321";
grant all on galenos_dev.* to dev_admin@localhost;