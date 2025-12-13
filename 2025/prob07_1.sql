CREATE TABLE "lines" (v TEXT, n INTEGER PRIMARY KEY);
.import data07.txt lines
SELECT * FROM lines;


CREATE TABLE vars (name TEXT, value INTEGER);
insert into vars values ('rows', (select count(*) from lines));
insert into vars values ('cols', (select length(v) from lines where n=1));

WITH RECURSIVE data(x, y, v) as (
     select 1, 1, (select substring(v, 1, 1) from lines where n=1)
     union all
     select
        x % (select value from vars where name='cols') + 1,
        y + (x = (select value from vars where name='cols')),
        (select substring(
                v,
                x % (select value from vars where name='cols') + 1,
                1
        ) from lines where n = y + (x = (select value from vars where name='cols'))
        )
        from data
     limit (select value from vars where name='cols')*(select value from vars where name='rows')
)
select * from data;
