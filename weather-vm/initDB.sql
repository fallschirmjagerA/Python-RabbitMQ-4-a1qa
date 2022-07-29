CREATE TABLE IF NOT EXISTS city (
  id serial primary key,
  name varchar(250) NOT NULL
);

CREATE TABLE IF NOT EXISTS weather (
  min_temp decimal not null,
  max_temp decimal not null,
  pressure int not null,
  added_time timestamp not null,
  city_id int not null references city(id),
  PRIMARY KEY(city_id, added_time)
);