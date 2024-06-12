drop database if exists hosteria_byteados;
create database hosteria_byteados;
use hosteria_byteados;

/* utilizar desde acá si se carga en sqlite */
create table Cabanias(
    cabania_id varchar(7) not null,
    nombre varchar(30) not null,
    descripcion varchar(500),
    cap_max int not null,
    precio_dia float not null,
    constraint pk_Cabanias primary key (cabania_id)
);

create table Reservas(
    reserva_codigo integer, /*si una PK es int, auto-increment se implementa automaticamente en sqlite*/
    cabania_id varchar(7) not null,
    fecha_ent date not null,
    fecha_sal date not null,
    id_cliente varchar(9) not null, /* DNI o Pasaporte */
    nombre_completo_cliente varchar(100) not null,
    telefono_cliente int not null,
    mail_cliente varchar(100) not null,
    precio_total float not null,
    primary key (reserva_codigo),
    constraint fk_cabania_id FOREIGN KEY (cabania_id) REFERENCES Cabanias(cabania_id)
);

create table Imagenes(
    imagen_link varchar(2048) not null,
    cabania_id varchar(7),
    descripcion varchar(100),
    constraint pk_Imagenes primary key (imagen_link),
    constraint fk_cabania_id foreign key (cabania_id) references Cabanias(cabania_id)
);


