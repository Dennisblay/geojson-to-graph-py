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
    "edges"   jsonb -- '["A", "B", "C"]'
);

CREATE TABLE "weights"
(
    "from_node_id" bigint NOT NULL,
    "to_node_id"   bigint NOT NULL,
    "distance"     double NOT NULL,
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

