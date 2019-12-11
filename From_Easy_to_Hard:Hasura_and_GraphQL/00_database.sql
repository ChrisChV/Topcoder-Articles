CREATE TABLE public.product(
    id SERIAL PRIMARY KEY,
    name text NOT NULL,
    bar_code text
);
 
CREATE TABLE public.store(
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);
 
CREATE TABLE public.price(
    id SERIAL PRIMARY KEY,
    id_product integer NOT NULL REFERENCES public.product(id),
    id_store integer NOT NULL REFERENCES public.store(id),
    price float NOT NULL
);
 
CREATE TABLE public.receipt(
    id SERIAL PRIMARY KEY,
    id_store integer NOT NULL REFERENCES public.store(id)
);
 
CREATE TABLE public.receipt_price(
    id_receipt integer NOT NULL REFERENCES public.receipt(id),
    id_price integer NOT NULL REFERENCES public.price(id)
);
