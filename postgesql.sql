


-- ингформация по таблице (типы данных и проч)
SELECT *
  FROM information_schema.columns
 WHERE table_schema = 'amplitude'
   AND table_name   = 'users'

-- извлечение недели, месяца
, to_char(a.event_date, 'YYYY-WW') as week
, to_char(a.event_date, 'YYYY-MM') as month
, date_trunc('week', a.event_date::date)::date as week_start_date
