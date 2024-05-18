CREATE SCHEMA images;

CREATE TABLE images.pre_label (
    id SERIAL PRIMARY KEY,
    image_data BYTEA,
    label JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE images.re_label (
    id SERIAL PRIMARY KEY,
    pre_label_id INTEGER REFERENCES images.pre_label(id),
    image_data BYTEA,
    label JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


