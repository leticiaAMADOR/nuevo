create database agendas;
use agendas;
create table datos (
id_dato int not null auto_increment primary key,
nombre varchar (50) not null,
telefono varchar (20) not null,
email varchar (50) not null,
direccion varchar (100)

)