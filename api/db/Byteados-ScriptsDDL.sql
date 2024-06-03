drop database if exists hosteria_byteados;
create database hosteria_byteados;
use hosteria_byteados;

create table habitaciones(
    habitacion_id varchar(15) not null,
    habitacion_nombre varchar(30),
    habitacion_descripcion varchar(500),
    habitacion_precio_dia float,
    constraint pk_habitacion_id primary key (habitacion_id)
);

create table reservas(
    reserva_codigo int not null,
    habitacion_id int not null,
    reserva_fecha_ent date not null,
    reserva_fecha_sal date not null,
    reserva_dni_cliente char not null,
    reserva_teleono_cliente int not null,
    reserva_mail_cliente int not null,
    reserva_precio_total float not null,
    constraint pk_reserva_codigo primary key (reserva_codigo),
    constraint fk_habitacion_id FOREIGN KEY (habitacion_id) REFERENCES habitaciones(habitacion_id)
);

create table imagenes(
    imagen_link varchar(2048) not null,
    habitacion_id int not null,
    imagen_descripcion varchar(100),
    constraint pk_imagen_link primary key (imagen_link),
    constraint fk_habitacion_id foreing key (habitacion_id) references habitaciones(habitacion_id)
);


