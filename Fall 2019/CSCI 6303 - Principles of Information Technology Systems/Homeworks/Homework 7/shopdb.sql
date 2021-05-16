/* Initial code of homework 7*/

create database shop;
use shop;

create table users(
   id int null auto_increment,
   firstname varchar(255),
   lastname varchar(255) not null,
   primary key (id)
);

create table products(
  id int null auto_increment,
  name varchar(255),
  price float,
  primary key (id)
);

create table orders(
   id_users int not null,
   id_items int not null,
   primary key (id_users,id_items),
   foreign key (id_users) references users(id),
   foreign key (id_items) references items(id)
);

/*Solutions to "write three SQL queries to answer the following questions"*/

/*1.- Products in the shop catalog; product name.*/

select name from products;

/*2.- List of products in stock (not sold); product name, code, price.*/
/*I added where statement to make a comparition between id in products and orders*/

select products.name, products.id, products.price from products, orders
where products.id <> orders.id_items;

/*3.- Products sold in the shop; product name, code, price and full name of buyer.*/

select products.name, products.id, products.price, users.lastname, users.firstname from products, orders, users
where products.id = orders.id_items and users.id = orders.id_users;