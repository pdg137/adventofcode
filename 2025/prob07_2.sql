CREATE TABLE "input" (v TEXT, n INTEGER PRIMARY KEY);
.import data07.txt input
SELECT * FROM input;


CREATE TABLE vars (rows INTEGER, cols INTEGER);
INSERT INTO vars VALUES (
  (select count(*) from input),
  (select length(v) from input where n=1)
  );

CREATE TABLE dirs (dir INTEGER, dirname CHAR);
INSERT INTO dirs values(-1, 'L');
INSERT INTO dirs values(0, 'S');
INSERT INTO dirs values(1, 'R');

WITH RECURSIVE output(path, n, pos) as (
  -- input.v is the current row of the input data
  -- output.path is the path followed, like LRLRR
  -- output.n is the previous column of the tachyon
  -- output.pos is the previous column of the tachyon
  --
  SELECT '', 1, instr(input.v, 'S') FROM input WHERE n=1
  UNION ALL

  SELECT
    if('^' is substr(input.v, pos, 1), concat(output.path, dirname), output.path),
    input.n,
    if('^' is substr(input.v, pos, 1), pos + dir, pos)
    FROM input, output, vars, dirs
    WHERE input.n = output.n+1 AND
      if('^' is substr(input.v, pos, 1), dir <> 0, dir = 0)
)
-- SELECT * FROM output;
SELECT COUNT(*) FROM output where n = (SELECT rows FROM vars);
