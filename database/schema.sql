CREATE TABLE "nodes"
(
    "id"         bigserial PRIMARY KEY,
    "name"       varchar UNIQUE        NOT NULL,
    "point_geom" geometry(point, 3857) NOT NULL
);

CREATE TABLE "edges"
(
    "id"      bigserial PRIMARY KEY,
    "node_id" bigint UNIQUE NOT NULL,
<<<<<<< HEAD
    "neighbors"   jsonb -- '["A", "B", "C"]'
=======
    "edges"   jsonb -- '["A", "B", "C"]'
>>>>>>> 4032d35bb5f47b7cc285a62da9f5bd4f1d327633
);

CREATE TABLE "weights"
(
<<<<<<< HEAD
    "id"           bigserial NOT NULL,
=======
>>>>>>> 4032d35bb5f47b7cc285a62da9f5bd4f1d327633
    "from_node_id" bigint NOT NULL,
    "to_node_id"   bigint NOT NULL,
    "distance"     double precision NOT NULL,
    PRIMARY KEY ("from_node_id", "to_node_id")
);

-- indexes
CREATE INDEX ix_nodes_id
    ON "nodes" ("id");

CREATE INDEX ix_nodes_point_geom
    ON "nodes" using gist ("point_geom");

CREATE INDEX ix_edges_node_id
    ON "edges" ("node_id");

CREATE INDEX ix_weights_from_node_id
    ON "weights" ("from_node_id");

CREATE INDEX ix_weights_to_node_id
    ON "weights" ("to_node_id");


-- Foreign Keys
ALTER TABLE "edges"
    ADD FOREIGN KEY ("node_id")
        REFERENCES "nodes" ("id")
        ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE "weights"
    ADD FOREIGN KEY ("from_node_id") REFERENCES "nodes" ("id")
        ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE "weights"
    ADD FOREIGN KEY ("to_node_id") REFERENCES "nodes" ("id")
        ON UPDATE CASCADE ON DELETE CASCADE;

