DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quatetime datetime,
  latitude real,
  longitude real,
  depth real,
  mag real,
  magtype text,
  id text,
  updated datetime,
  place text,
  hzlerror real,
  deperror real,
  magerror real
);