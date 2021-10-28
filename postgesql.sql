


-- ингформация по таблице (типы данных и проч)
SELECT *
  FROM information_schema.columns
 WHERE table_schema = 'amplitude'
   AND table_name   = 'users'
