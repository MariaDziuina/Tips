 -- Округление времени вниз до секунд:
to_char(bg.event_time, 'YYYY-MM-DD HH24:MI:SS".000"') event_time_round


-- ингформация по таблице (типы данных и проч)
SELECT *
  FROM information_schema.columns
 WHERE table_schema = 'amplitude'
   AND table_name   = 'users'

-- извлечение недели, месяца
, to_char(a.event_date, 'YYYY-WW') as week
, to_char(a.event_date, 'YYYY-MM') as month
, date_trunc('week', a.event_date::date)::date as week_start_date


-- проверка статусов запущенных запросов
SELECT * FROM pg_stat_activity
