-- Tabla Cabañas
-- ID, nombre, descripcion, cap_max, precio por dia
insert into Cabanias values
("CAB-CLE", "Bestia Clerigo", "Cuenta con dos baños, 1 cama matrimonial, 4 camas individuales -dos cuchetas- y 2 sofá-cama. Ideal para una salida familiar. Su vista es imperdible!!", 8, 200),
("CAB-VIC", "Vicaria Amelia", "Cuenta con dos baños, 6 camas individuales -dos cuchetas y dos camas individuales-. Perfecto para una escapada con amigos!", 6, 150),
("CAB-EMI", "Emisario Celestial", "Esta equipada con 1 cama matrimonial, 2 camas individuales, 2 sofá cama y dos baños. La vista desde esta habitacion es unica.", 6, 90),
("CAB-PRE", "Presencia Lunar", "Se encuentra equipada con 1 Cama matrimonial, 2 camas individuales -cuchetas- y un baño. Esta cabaña dispone de una vista espectacular a la noche.", 4, 80),
("CAB-ADE", "Adela", "Posee una cama matrimonial junto a 2 camas individuales y un baño. Perfecta para dos parejas amigas o una familia pequeña!", 4, 84),
("CAB-ALM", "Almendra", "Cabaña especial para dos personas... veni con tu persona especial! Dispone de 1 cama matrimonial y un baño. Cuenta con todo lo que necesitas para unos dias inolvidables", 2, 100);

-- Tabla Imagenes
insert into Imagenes (descripcion, cabania_id, imagen_link) values
('portada', 'CAB-ADE', 'https://lh3.googleusercontent.com/d/1QloOnCy5hglDf1YIJWAFay5pFm23EzZ2'),
('portada', 'CAB-ALM', 'https://lh3.googleusercontent.com/d/1x0PaThjSKvDgsYr6IKIZ-s7SNtpfeGfF'),
('portada', 'CAB-EMI', 'https://lh3.googleusercontent.com/d/1pWVZQSRyFXoLAUFn0Zeu9lpaBJmt2siO'),
('portada', 'CAB-PRE', 'https://lh3.googleusercontent.com/d/1sXSJ_Nlrm64T2BbO8_8rISRkVuZLN5kY'),
('portada', 'CAB-CLE', 'https://lh3.googleusercontent.com/d/10uNQ4KsZbBDQzzAWQ9p9RjIm2gSJo1Dn'),
('portada', 'CAB-VIC', 'https://lh3.googleusercontent.com/d/10wGokRYw4eFoHNF1H-XC-yEbhWwCSLgZ');

insert into Imagenes (descripcion, imagen_link) values
('cocina1', 'https://lh3.googleusercontent.com/d/1s9gHPAZ3vfpSmhOPU1F5gZqIQ4b6z0fQ'),
('cocina2', 'https://lh3.googleusercontent.com/d/1iBgWraaumdj2R0XZyrLkA9TLmVR2uPF7'),
('arcade1', 'https://lh3.googleusercontent.com/d/1WvH7rO1Zt1MvhB3ZBGDSsxvIt5RX26Zj'),
('arcade2', 'https://lh3.googleusercontent.com/d/1HSNi4PvLBqOQiuNjuO666qdLeubsdozE'),
('juegos', 'https://lh3.googleusercontent.com/d/1NW6J1e_0lQpg_tRo98Dh_BupIdkObdvw'),
('pileta', 'https://lh3.googleusercontent.com/d/1u8g_lklxCPY3VBqDG44t3mMpus_jJoIl'),
('posada', 'https://lh3.googleusercontent.com/d/1tZlru6kU7YWcYAnXWI4Ge8WIk-l4nP27'),
('posadanoche', 'https://lh3.googleusercontent.com/d/1YmZ5-XZtNZY7WVu4yzkm1ymom1dEp4_m'),
('spa', 'https://lh3.googleusercontent.com/d/1_IIpxQbsbPoduTXc70w5h88oPo9XXh-r'),
('tour1', 'https://lh3.googleusercontent.com/d/1--gMgb7clkDxSB4aPFuT8912SwMGfDSq'),
('tour2', 'https://lh3.googleusercontent.com/d/1NR_c0T6FVfTa42qIgoNTErc5Dz0oWZgv');

-- Inserts de base para tabla RESERVAS
-- reserva_codigo, cabania_id, fecha_ent, fecha_sal, id_cliente, telefono_cliente, mail_cliente, precio_total
insert into Reservas(cabania_id, fecha_ent, fecha_sal, id_cliente, nombre_completo_cliente, telefono_cliente, mail_cliente, precio_total) values
("CAB-CLE", "2023-02-14", "2023-02-28", "45011819", "Franz Kafka", 1145891290, "franz_kafka@hotmail.com", 2800),
("CAB-CLE", "2023-02-29", "2023-03-12", "UK1189218", "Edwin Payne", 00441892108, "edw1npaynehere@mail.uk", 2400),
("CAB-ALM", "2023-02-10", "2023-02-20", "JP8918901", "Misato Katsuragi", 8112348918, "katsuragi_misa@live.jp", 1900),
("CAB-ADE", "2023-03-01", "2023-03-20", "JP1191038", "Sampo Koski", 8102901219, "koski_ur_boyfriend@live.jp", 84),
("CAB-PRE", "2023-04-01", "2023-04-8", "20818211", "Gustavo Cerati", 1144894221, "lago_en_el_cielo@gmail.com", 560),
("CAB-EMI", "2023-03-01", "2023-03-11", "US1890331", "Laufey Lín Bing Jónsdóttir", 0911148918, "laufey_lin@mail.com", 990),
("CAB-ADE", "2023-06-01", "2023-07-22", "US9981121", "Daniel Kim", 81149148918, "daniel_w2e@live.com", 4368),
("CAB-ALM", "2023-06-20", "2023-08-27", "HP3891789", "Christopher Bang", 9112367817, "oimate@mail.au", 6700),
("CAB-CLE", "2023-04-02", "2023-04-10", "JP8918901", "Misato Katsuragi", 8112348918, "katsuragi_misa@live.jp", 1299);
