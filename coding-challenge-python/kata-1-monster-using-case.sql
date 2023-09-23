
CREATE DATABASE monsters;
-- TABLE top_left
CREATE TABLE top_half (
    id INTEGER PRIMARY KEY,
    heads INTEGER,
    arms INTEGER
);

INSERT INTO top_half (id, heads, arms)
VALUES (1, 2, 4),
       (2, 3, 6),
       (3, 1, 2);

-- TABLE bottom_left
CREATE TABLE bottom_half (
    id INTEGER PRIMARY KEY,
    legs INTEGER,
    tails INTEGER
);

INSERT INTO bottom_half (id, legs, tails)
VALUES (1, 2, 1),
       (2, 4, 2),
       (3, 6, 3);



-- TABLE output
CREATE TABLE output(
    id INTEGER PRIMARY KEY ,
    heads INTEGER,
     legs INTEGER,
     arms INTEGER,
     tails INTEGER,
     species VARCHAR(10)
);

--* remplir la table output avec les données des tables top_half et bottom_half. 

SELECT t.id, t.heads, b.legs, t.arms, b.tails,
    CASE
        WHEN t.heads > t.arms AND b.tails > b.legs THEN 'BEAST'
        ELSE 'WEIRDO'
    END AS species
FROM top_half t
INNER JOIN bottom_half b 
ON t.id = b.id
ORDER BY species;

--remplir la table output avec les données des tables top_half et bottom_half. 

INSERT INTO output( id, heads, legs, arms, tails) SELECT t.id, t.heads, b.legs, t.arms, b.tails FROM top_half t JOIN bottom_half b ON t.id = b.id;

-- mettre à jour la colonne species de la table output avec la valeur ‘BEAST’ ou ‘WEIRDO’ selon les règles énoncées. 

UPDATE output SET species = CASE WHEN heads > arms AND tails > legs THEN 'BEAST' WHEN heads > arms OR tails > legs THEN 'BEAST' ELSE 'WEIRDO' END;

--vérifier ton résultat
SELECT * FROM output ORDER BY species;