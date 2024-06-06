-- Tabla Cabañas
-- ID, nombre, descripcion, cap_max, precio por dia
insert into Cabanias values
("CAB-CLE", "Bestia Clerigo", "Cuenta con dos baños, 1 cama matrimonial, 4 camas individuales -dos cuchetas- y 2 sofá-cama. Ideal para una salida familiar. Su vista es imperdible!!", 8, 200),
("CAB-VIC", "Vicaria Amelia", "Cuenta con dos baños, 6 camas individuales -dos cuchetas y dos camas individuales-. Perfecto para una escapada con amigos!", 6, 150),
("CAB-EMI", "Emisario Celestial", "Esta equipada con 1 cama matrimonial, 2 camas individuales, 2 sofá cama y dos baños. La vista desde esta habitacion es unica.", 6, 90),
("CAB-PRE", "Presencia Lunar", "Se encuentra equipada con 1 Cama matrimonial, 2 camas individuales -cuchetas- y un baño. Esta cabaña dispone de una vista espectacular a la noche.", 4, 80),
("CAB-ADE", "Adela", "Posee una cama matrimonial junto a 2 camas individuales y un baño. Perfecta para dos parejas amigas o una familia pequeña!", 4, 84),
("CAB-ALM", "Almendra", "Cabaña especial para dos personas... veni con tu persona especial! Dispone de 1 cama matrimonial y un baño. Cuenta con todo lo que necesitas para unos dias inolvidables", 2, 100);

-- Tabla Imagenes --> Joaco

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
("CAB-ALM", "2023-06-20", "2023-08-27", "HP3891789", "Christopher Bang", 9112367817, "oimate@mail.au", 6700);
