DROP TABLE IF EXISTS statepopulation;
CREATE TABLE statepopulation (
  code text,
  statename text,
  pop real
);

DROP TABLE IF EXISTS topcities;
CREATE TABLE topcities (
  city text,
  statename text,
  citypop real,
  lat real,
  lon real
);