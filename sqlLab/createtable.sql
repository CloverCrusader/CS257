DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quatetime timestamp with time zone,
  latitude real,
  longitude real,
  depth real,
  mag real,
  magtype text,
  id text,
  updated timestamp with time zone,
  place text,
  hzlerror real,
  deperror real,
  magerror real
);