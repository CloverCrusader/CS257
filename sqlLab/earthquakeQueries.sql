-- how many quakes where measured in Mfa (Felt-Area Magnitude)?
SELECT * FROM earthquakes WHERE magtype = 'mfa';
-- which quakes have the least reliable magnitude measurement (highest magerror)?
SELECT * FROM earthquakes ORDER BY magerror DESC LIMIT 1;
-- which quake was felt the longest
SELECT * FROM earthquakes WHERE magtype = 'md' ORDER BY mag DESC LIMIT 1;