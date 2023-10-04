# Тестовое задание  

## Эндпоинты:  
1. Write_data (запись и обновление данных)  
2. Check_data (получение данных)
   
# Установка  
1. **Клонируем репозиторий:**  
     `git clone https://github.com/gecsagen/phone.git`  
2. **Запускаем проект с помощью docker:**   
     `make up`  
# Использование  
1. **Переходим в браузер по адресу:**  
     `http://127.0.0.1:8004/docs`
# Ответ на вторую часть  
1. **Вариант 1:**  
```
UPDATE full_names AS fn
SET status = sn.status
FROM short_names AS sn
WHERE fn.name ~ ('^' || sn.name || '\..*$');
```

2. **Вариант 2**
```
sql
-- Устанавливаем размер батча (например, 1000 записей на батч)
DECLARE batch_size INT := 1000;

-- Начинаем цикл
DO $$ 
DECLARE start_offset INT := 0;
DECLARE end_offset INT;
BEGIN
  -- Вычисляем конечное значение для текущего батча
  end_offset := start_offset + batch_size;
  
  -- Пока есть записи в таблице full_names для обновления
  WHILE EXISTS (SELECT 1 FROM full_names WHERE name LIKE '%' OFFSET start_offset LIMIT batch_size) 
  LOOP
    -- Обновляем статус для текущего батча
    UPDATE full_names AS fn
    SET status = sn.status
    FROM short_names AS sn
    WHERE fn.name LIKE sn.name || '.%'
    OFFSET start_offset
    LIMIT batch_size;
    
    -- Увеличиваем смещение для следующего батча
    start_offset := end_offset;
    end_offset := start_offset + batch_size;
  END LOOP;
END $$;
```


