drop table if exists payments;
drop table if exists reservations;
drop table if exists clients;
drop table if exists classes;
drop table if exists instructors;


create table instructors (
  id bigint primary key generated always as identity,
  name text not null,
  specialty text
);

create table classes (
  id bigint primary key generated always as identity,
  name text not null,
  schedule timestamp not null,
  instructor_id bigint references instructors (id),
  max_capacity int not null
);

create table clients (
  id bigint primary key generated always as identity,
  name text not null,
  email text unique not null
);

create table reservations (
  id bigint primary key generated always as identity,
  client_id bigint references clients (id),
  class_id bigint references classes (id),
  reservation_date timestamp default now()
);

create table payments (
  id bigint primary key generated always as identity,
  client_id bigint references clients (id),
  amount numeric(10, 2) not null,
  payment_date timestamp default now()
);



-- Insert sample instructors
insert into
  instructors (name, specialty)
values
  ('John Doe', 'Yoga'),
  ('Jane Smith', 'Pilates'),
  ('Emily Johnson', 'Zumba'),
  ('Michael Brown', 'CrossFit'),
  ('Sarah Davis', 'Spinning');

-- Insert sample classes
insert into
  classes (name, schedule, instructor_id, max_capacity)
values
  ('Morning Yoga', '2023-11-01 08:00:00', 1, 20),
  ('Evening Pilates', '2023-11-01 18:00:00', 2, 15),
  ('Zumba Dance', '2023-11-02 17:00:00', 3, 25),
  (
    'CrossFit Challenge',
    '2023-11-03 19:00:00',
    4,
    10
  ),
  ('Spinning Session', '2023-11-04 07:00:00', 5, 30);

-- Insert sample clients
insert into
  clients (name, email)
values
  (
    'Alice Green',
    'alice.green@example.com'
  ),
  (
    'Bob White',
    'bob.white@example.com'
  ),
  (
    'Charlie Black',
    'charlie.black@example.com'
  ),
  (
    'Diana Blue',
    'diana.blue@example.com'
  ),
  (
    'Ethan Red',
    'ethan.red@example.com'
  );

-- Insert sample reservations
insert into
  reservations (client_id, class_id)
values
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
  (5, 5);

-- Insert sample payments
insert into
  payments (client_id, amount)
values
  (1, 50.00),
  (2, 45.00),
  (3, 60.00),
  (4, 55.00),
  (5, 40.00);