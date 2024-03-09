ALL_QUERIES = """

BEGIN;

-- Remove Foreign Keys
ALTER TABLE "weights"
    DROP CONSTRAINT IF EXISTS weights_to_node_id_fkey;

ALTER TABLE "weights"
    DROP CONSTRAINT IF EXISTS weights_from_node_id_fkey;

ALTER TABLE "edges"
    DROP CONSTRAINT IF EXISTS edges_node_id_fkey;

-- Drop indexes
DROP INDEX IF EXISTS ix_weights_to_node_id;
DROP INDEX IF EXISTS ix_weights_from_node_id;
DROP INDEX IF EXISTS ix_edges_node_id;
DROP INDEX IF EXISTS ix_nodes_point_geom;
DROP INDEX IF EXISTS ix_nodes_id;

-- Drop tables
DROP TABLE IF EXISTS "weights";
DROP TABLE IF EXISTS "edges";
DROP TABLE IF EXISTS "nodes";



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
    "neighbors"   jsonb -- '["A", "B", "C"]'
);

CREATE TABLE "weights"
(
    "id"           bigserial NOT NULL,
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

-- Drop tables if they exist (in reverse order due to dependencies)
DROP TABLE IF EXISTS weights CASCADE;
DROP TABLE IF EXISTS edges CASCADE;
DROP TABLE IF EXISTS nodes CASCADE;

-- Create tables
CREATE TABLE nodes
(
    id         bigserial PRIMARY KEY,
    name       varchar UNIQUE NOT NULL,
    point_geom geometry(Point, 3857) NOT NULL
);

CREATE TABLE edges
(
    id      bigserial PRIMARY KEY,
    node_id bigint NOT NULL,
    neighbors   jsonb -- '["A", "B", "C"]'
);

CREATE TABLE weights
(
    from_node_id bigint NOT NULL,
    to_node_id   bigint NOT NULL,
    distance     double precision NOT NULL,
    PRIMARY KEY (from_node_id, to_node_id)
);

-- Create indexes
CREATE INDEX ix_nodes_id ON nodes (id);
CREATE INDEX ix_nodes_point_geom ON nodes USING gist (point_geom);
CREATE INDEX ix_edges_node_id ON edges (node_id);
CREATE INDEX ix_weights_from_node_id ON weights (from_node_id);
CREATE INDEX ix_weights_to_node_id ON weights (to_node_id);

-- Add foreign keys
ALTER TABLE edges
    ADD FOREIGN KEY (node_id) REFERENCES nodes (id)
    ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE weights
    ADD FOREIGN KEY (from_node_id) REFERENCES nodes (id)
    ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE weights
    ADD FOREIGN KEY (to_node_id) REFERENCES nodes (id)
    ON UPDATE CASCADE ON DELETE CASCADE;

COMMIT;

"""
